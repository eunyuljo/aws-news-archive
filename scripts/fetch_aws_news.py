#!/usr/bin/env python3
"""
AWS What's New RSS 피드를 수집하여 서비스별로 분류·저장하는 스크립트.

출력 구조:
  news/YYYY/MM/YYYY-MM-DD_<slug>.md      — 개별 뉴스 파일
  services/<service>/index.md            — 서비스별 인덱스
  services/index.md                      — 전체 서비스 목록
  tags/<tag>/index.md                    — 태그별 인덱스
  tags/index.md                          — 전체 태그 목록
  README.md                              — 루트 요약
"""

import os
import re
import json
import hashlib
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

RSS_URL = "https://aws.amazon.com/about-aws/whats-new/recent/feed/"
BASE_DIR = Path(__file__).resolve().parent.parent

# AWS 서비스 키워드 → 정규화된 폴더명 매핑
SERVICE_MAP = {
    "lambda": "Lambda",
    "s3": "S3",
    "ec2": "EC2",
    "rds": "RDS",
    "dynamodb": "DynamoDB",
    "eks": "EKS",
    "ecs": "ECS",
    "cloudfront": "CloudFront",
    "cloudwatch": "CloudWatch",
    "cloudformation": "CloudFormation",
    "iam": "IAM",
    "sqs": "SQS",
    "sns": "SNS",
    "kinesis": "Kinesis",
    "glue": "Glue",
    "athena": "Athena",
    "redshift": "Redshift",
    "emr": "EMR",
    "sagemaker": "SageMaker",
    "bedrock": "Bedrock",
    "route 53": "Route53",
    "route53": "Route53",
    "vpc": "VPC",
    "api gateway": "APIGateway",
    "api_gateway": "APIGateway",
    "step functions": "StepFunctions",
    "eventbridge": "EventBridge",
    "codecommit": "CodeCommit",
    "codebuild": "CodeBuild",
    "codedeploy": "CodeDeploy",
    "codepipeline": "CodePipeline",
    "elastic beanstalk": "ElasticBeanstalk",
    "elasticache": "ElastiCache",
    "opensearch": "OpenSearch",
    "elasticsearch": "OpenSearch",
    "secretsmanager": "SecretsManager",
    "secrets manager": "SecretsManager",
    "kms": "KMS",
    "waf": "WAF",
    "shield": "Shield",
    "guardduty": "GuardDuty",
    "inspector": "Inspector",
    "macie": "Macie",
    "config": "Config",
    "cloudtrail": "CloudTrail",
    "systems manager": "SystemsManager",
    "ssm": "SystemsManager",
    "transfer family": "TransferFamily",
    "fsx": "FSx",
    "efs": "EFS",
    "ebs": "EBS",
    "lightsail": "Lightsail",
    "aurora": "Aurora",
    "documentdb": "DocumentDB",
    "neptune": "Neptune",
    "timestream": "Timestream",
    "keyspaces": "Keyspaces",
    "memorydb": "MemoryDB",
    "amplify": "Amplify",
    "appsync": "AppSync",
    "cognito": "Cognito",
    "connect": "Connect",
    "chime": "Chime",
    "ivs": "IVS",
    "mediaconvert": "MediaConvert",
    "rekognition": "Rekognition",
    "textract": "Textract",
    "comprehend": "Comprehend",
    "translate": "Translate",
    "polly": "Polly",
    "transcribe": "Transcribe",
    "lex": "Lex",
    "personalize": "Personalize",
    "forecast": "Forecast",
    "quicksight": "QuickSight",
    "lakeformation": "LakeFormation",
    "lake formation": "LakeFormation",
    "datazone": "DataZone",
    "outposts": "Outposts",
    "wavelength": "Wavelength",
    "local zones": "LocalZones",
    "ground station": "GroundStation",
    "iot": "IoT",
    "greengrass": "Greengrass",
}


def fetch_rss(url: str) -> str:
    req = Request(url, headers={"User-Agent": "aws-news-archive/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def parse_items(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    ns = {"dc": "http://purl.org/dc/elements/1.1/"}
    items = []
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date_str = (item.findtext("pubDate") or "").strip()
        description = (item.findtext("description") or "").strip()
        creator = (item.findtext("dc:creator", namespaces=ns) or "AWS").strip()

        # HTML 태그 제거
        description = re.sub(r"<[^>]+>", "", description).strip()

        try:
            pub_date = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
        except ValueError:
            pub_date = datetime.now(tz=timezone.utc)

        items.append(
            {
                "title": title,
                "link": link,
                "pub_date": pub_date,
                "description": description,
                "creator": creator,
            }
        )
    return items


def detect_service(title: str, description: str) -> str:
    text = (title + " " + description).lower()
    for keyword, service in SERVICE_MAP.items():
        if keyword in text:
            return service
    return "General"


def detect_tags(title: str, description: str, service: str, year: str) -> list[str]:
    tags = [service, year]
    text = (title + " " + description).lower()
    if any(k in text for k in ["generally available", "now available", "launched", "launch"]):
        tags.append("GA")
    if "preview" in text:
        tags.append("preview")
    if any(k in text for k in ["price reduction", "cost", "lower cost", "cheaper", "price"]):
        tags.append("price-reduction")
    if any(k in text for k in ["new region", "additional region", "availability zone", "region"]):
        tags.append("new-region")
    if any(k in text for k in ["performance", "faster", "speed", "latency", "throughput"]):
        tags.append("performance")
    if any(k in text for k in ["security", "encryption", "compliance", "iam", "kms", "vulnerability"]):
        tags.append("security")
    if any(k in text for k in ["machine learning", "artificial intelligence", " ai ", "ml model", "inference", "foundation model", "llm", "generative"]):
        tags.append("ai-ml")
    return list(dict.fromkeys(tags))


def translate_to_korean(text: str) -> str | None:
    """TRANSLATE_TO_KO=true 환경변수 + boto3 + AWS 자격증명이 있을 때만 동작"""
    if os.environ.get("TRANSLATE_TO_KO", "").lower() != "true":
        return None
    try:
        import boto3
        client = boto3.client("translate", region_name="us-east-1")
        result = client.translate_text(
            Text=text[:5000],
            SourceLanguageCode="en",
            TargetLanguageCode="ko"
        )
        return result["TranslatedText"]
    except Exception:
        return None


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_-]+", "-", slug)
    slug = slug.strip("-")
    return slug[:80]


def item_id(item: dict) -> str:
    return hashlib.md5((item["link"] or item["title"]).encode()).hexdigest()[:8]


def news_file_path(item: dict) -> Path:
    d = item["pub_date"]
    slug = slugify(item["title"])
    filename = f"{d.strftime('%Y-%m-%d')}_{slug}.md"
    return BASE_DIR / "news" / d.strftime("%Y") / d.strftime("%m") / filename


def write_news_file(item: dict, service: str, force: bool = False) -> Path:
    path = news_file_path(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return path  # 이미 존재하면 덮어쓰지 않음

    year = item["pub_date"].strftime("%Y")
    tags = detect_tags(item["title"], item["description"], service, year)
    tags_yaml = json.dumps(tags)

    # 한국어 번역 시도
    ko_summary = translate_to_korean(item["description"])
    if ko_summary:
        ko_section = f"## 한국어 요약\n\n{ko_summary}\n"
    else:
        ko_section = "## 한국어 요약\n\n번역 미지원\n"

    lines = [
        "---",
        f'title: "{item["title"].replace(chr(34), chr(39))}"',
        f'date: "{item["pub_date"].strftime("%Y-%m-%d")}"',
        f'service: "{service}"',
        f'link: "{item["link"]}"',
        f"tags: {tags_yaml}",
        "nav_exclude: true",
        "---",
        "",
        f"# {item['title']}",
        "",
        f"**날짜:** {item['pub_date'].strftime('%Y년 %m월 %d일')}",
        f"**서비스:** {service}",
        f"**링크:** {item['link']}",
        "",
        "## 내용",
        "",
        item["description"],
        "",
        ko_section,
    ]
    content = "\n".join(lines)
    path.write_text(content, encoding="utf-8")
    return path


def update_service_index(service: str, items: list[dict]) -> None:
    svc_dir = BASE_DIR / "services" / service
    svc_dir.mkdir(parents=True, exist_ok=True)

    sorted_items = sorted(items, key=lambda x: x["pub_date"], reverse=True)

    lines = [
        "---",
        f'title: "{service}"',
        "parent: Services",
        "---",
        "",
        f"# {service} — AWS 뉴스",
        "",
        f"총 **{len(sorted_items)}건** | 최근 업데이트: {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
    ]

    current_year = None
    for item in sorted_items:
        year = item["pub_date"].strftime("%Y")
        if year != current_year:
            lines.append(f"\n## {year}\n")
            current_year = year
        date_str = item["pub_date"].strftime("%Y-%m-%d")
        rel_path = os.path.relpath(news_file_path(item), svc_dir)
        lines.append(f"- [{item['title']}]({rel_path}) `{date_str}`")

    (svc_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_global_service_index(service_counts: dict[str, int]) -> None:
    path = BASE_DIR / "services" / "index.md"
    sorted_services = sorted(service_counts.items(), key=lambda x: (-x[1], x[0]))

    lines = [
        "---",
        "title: Services",
        "nav_order: 2",
        "has_children: true",
        "---",
        "",
        "# AWS 서비스별 뉴스 인덱스",
        "",
        f"최근 업데이트: {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
        "| 서비스 | 뉴스 수 |",
        "|--------|---------|",
    ]
    for service, count in sorted_services:
        lines.append(f"| [{service}](./{service}/index.md) | {count} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def update_tag_indexes(all_items: list[dict]) -> None:
    """태그별 인덱스 파일 생성."""
    tags_dir = BASE_DIR / "tags"
    tags_dir.mkdir(parents=True, exist_ok=True)

    # 각 item에 태그 계산
    tag_items: dict[str, list[dict]] = {}
    for item in all_items:
        service = item.get("service", "General")
        year = item["pub_date"].strftime("%Y")
        tags = detect_tags(item["title"], item["description"], service, year)
        for tag in tags:
            tag_items.setdefault(tag, []).append(item)

    # 태그별 index.md 생성
    for tag, items in tag_items.items():
        tag_dir = tags_dir / tag
        tag_dir.mkdir(parents=True, exist_ok=True)
        sorted_items = sorted(items, key=lambda x: x["pub_date"], reverse=True)

        lines = [
            "---",
            f'title: "{tag}"',
            "parent: Tags",
            "nav_exclude: false",
            "---",
            "",
            f"# 태그: {tag}",
            "",
            f"총 {len(sorted_items)}건",
            "",
        ]
        for item in sorted_items:
            date_str = item["pub_date"].strftime("%Y-%m-%d")
            news_path = news_file_path(item)
            rel_path = os.path.relpath(news_path, tag_dir)
            item_service = item.get("service", "General")
            item_year = item["pub_date"].strftime("%Y")
            item_tags = detect_tags(item["title"], item["description"], item_service, item_year)
            tag_labels = " ".join(f"[{t}]" for t in item_tags if t not in (item_service, item_year))
            lines.append(f"- [{item['title']}]({rel_path}) `{date_str}` {tag_labels}".rstrip())

        (tag_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # tags/index.md 생성
    sorted_tags = sorted(tag_items.items(), key=lambda x: (-len(x[1]), x[0]))
    index_lines = [
        "---",
        "title: Tags",
        "nav_order: 3",
        "has_children: true",
        "---",
        "",
        "# 태그 목록",
        "",
        "| 태그 | 건수 |",
        "|------|------|",
    ]
    for tag, items in sorted_tags:
        index_lines.append(f"| [{tag}](./{tag}/index.md) | {len(items)} |")

    (tags_dir / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def update_readme(service_counts: dict[str, int], total: int, new_count: int) -> None:
    path = BASE_DIR / "README.md"
    top5 = sorted(service_counts.items(), key=lambda x: -x[1])[:5]

    lines = [
        "# AWS News Archive\n",
        "AWS What's New 피드를 자동으로 수집하여 서비스별로 정리한 아카이브입니다.  ",
        "GitHub Actions가 매일 자동으로 최신 뉴스를 업데이트합니다.\n",
        "## 구조\n",
        "```",
        "aws-news-archive/",
        "├── news/",
        "│   └── YYYY/MM/YYYY-MM-DD_<제목>.md   # 개별 뉴스",
        "├── services/",
        "│   ├── index.md                        # 서비스 목록",
        "│   └── <서비스명>/index.md             # 서비스별 뉴스 목록",
        "├── tags/",
        "│   ├── index.md                        # 태그 목록",
        "│   └── <태그명>/index.md               # 태그별 뉴스 목록",
        "└── scripts/",
        "    └── fetch_aws_news.py               # 수집 스크립트",
        "```\n",
        "## 통계\n",
        f"- **전체 뉴스:** {total}건",
        f"- **수집 서비스:** {len(service_counts)}개",
        f"- **마지막 업데이트:** {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n",
        "## 많이 업데이트된 서비스 TOP 5\n",
        "| 서비스 | 뉴스 수 |",
        "|--------|---------|",
    ]
    for service, count in top5:
        lines.append(f"| [{service}](./services/{service}/index.md) | {count} |")

    lines.append("\n## 전체 서비스 목록\n")
    lines.append("[서비스 인덱스 보기](./services/index.md)\n")
    lines.append("## 태그 목록\n")
    lines.append("[태그 인덱스 보기](./tags/index.md)\n")
    lines.append("## 자동화\n")
    lines.append("GitHub Actions (`.github/workflows/fetch-news.yml`)가 매일 UTC 09:00에 실행됩니다.\n")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_existing_links() -> set[str]:
    """이미 저장된 뉴스의 링크를 수집해서 중복 방지."""
    existing = set()
    for md in (BASE_DIR / "news").rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        m = re.search(r'^link:\s*"(.+)"', text, re.MULTILINE)
        if m:
            existing.add(m.group(1))
    return existing


def main() -> None:
    print(f"[{datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}] AWS 뉴스 수집 시작")

    try:
        xml_text = fetch_rss(RSS_URL)
    except URLError as e:
        print(f"RSS 피드 수집 실패: {e}")
        raise

    items = parse_items(xml_text)
    print(f"피드에서 {len(items)}건 파싱 완료")

    existing_links = load_existing_links()
    print(f"기존 뉴스 {len(existing_links)}건 확인")

    # 서비스별 분류
    service_items: dict[str, list[dict]] = {}
    new_count = 0
    all_items_with_service: list[dict] = []

    for item in items:
        service = detect_service(item["title"], item["description"])
        item_with_service = {**item, "service": service}
        service_items.setdefault(service, []).append(item_with_service)
        all_items_with_service.append(item_with_service)

        if item["link"] not in existing_links:
            write_news_file(item, service)
            new_count += 1

    print(f"신규 뉴스 {new_count}건 저장")

    # 서비스별 인덱스 업데이트
    for service, svc_items in service_items.items():
        update_service_index(service, svc_items)

    # 전체 서비스 인덱스, 태그 인덱스, README 업데이트
    service_counts = {svc: len(itms) for svc, itms in service_items.items()}
    update_global_service_index(service_counts)
    update_tag_indexes(all_items_with_service)
    update_readme(service_counts, len(items), new_count)

    print("인덱스 및 README 업데이트 완료")
    print(f"처리 완료: 전체 {len(items)}건 / 신규 {new_count}건")

    # GitHub Actions summary
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(f"## AWS 뉴스 수집 결과\n\n")
            f.write(f"- 전체 파싱: **{len(items)}건**\n")
            f.write(f"- 신규 저장: **{new_count}건**\n")
            f.write(f"- 수집 서비스: **{len(service_counts)}개**\n\n")
            f.write("### 서비스별 분포\n\n")
            f.write("| 서비스 | 건수 |\n|--------|------|\n")
            for svc, cnt in sorted(service_counts.items(), key=lambda x: -x[1]):
                f.write(f"| {svc} | {cnt} |\n")


if __name__ == "__main__":
    main()
