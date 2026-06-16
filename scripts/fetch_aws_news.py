#!/usr/bin/env python3
"""
AWS What's New RSS 피드를 수집하여 서비스별로 분류·저장하는 스크립트.

출력 구조:
  news/YYYY/MM/YYYY-MM-DD_<slug>.md      — 개별 뉴스 파일
  services/<service>/index.md            — 서비스별 인덱스
  services/index.md                      — 전체 서비스 목록
  README.md                              — 루트 요약
"""

import os
import re
import json
import hashlib
import textwrap
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


def write_news_file(item: dict, service: str) -> Path:
    path = news_file_path(item)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        return path  # 이미 존재하면 덮어쓰지 않음

    content = textwrap.dedent(f"""\
        ---
        title: "{item['title'].replace('"', "'")}"
        date: "{item['pub_date'].strftime('%Y-%m-%d')}"
        service: "{service}"
        link: "{item['link']}"
        ---

        # {item['title']}

        **날짜:** {item['pub_date'].strftime('%Y년 %m월 %d일')}
        **서비스:** {service}
        **링크:** {item['link']}

        ## 내용

        {item['description']}
    """)
    path.write_text(content, encoding="utf-8")
    return path


def update_service_index(service: str, items: list[dict]) -> None:
    svc_dir = BASE_DIR / "services" / service
    svc_dir.mkdir(parents=True, exist_ok=True)

    sorted_items = sorted(items, key=lambda x: x["pub_date"], reverse=True)
    lines = [f"# {service} — AWS 뉴스\n"]
    lines.append(f"총 **{len(sorted_items)}건** | 최근 업데이트: {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}\n")
    lines.append("---\n")

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

    lines = ["# AWS 서비스별 뉴스 인덱스\n"]
    lines.append(f"최근 업데이트: {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')}\n")
    lines.append("---\n")
    lines.append("| 서비스 | 뉴스 수 |")
    lines.append("|--------|---------|")
    for service, count in sorted_services:
        lines.append(f"| [{service}](./{service}/index.md) | {count} |")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


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

    for item in items:
        service = detect_service(item["title"], item["description"])
        service_items.setdefault(service, []).append(item)

        if item["link"] not in existing_links:
            write_news_file(item, service)
            new_count += 1

    print(f"신규 뉴스 {new_count}건 저장")

    # 서비스별 인덱스 업데이트
    for service, svc_items in service_items.items():
        update_service_index(service, svc_items)

    # 전체 서비스 인덱스 및 README 업데이트
    service_counts = {svc: len(itms) for svc, itms in service_items.items()}
    update_global_service_index(service_counts)
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
