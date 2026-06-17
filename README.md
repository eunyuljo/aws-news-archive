# AWS News Archive

AWS What's New 피드를 자동으로 수집하여 서비스별로 정리한 아카이브입니다.  
GitHub Actions가 매일 자동으로 최신 뉴스를 업데이트합니다.

## 구조

```
aws-news-archive/
├── news/
│   └── YYYY/MM/YYYY-MM-DD_<제목>.md   # 개별 뉴스
├── services/
│   ├── index.md                        # 서비스 목록
│   └── <서비스명>/index.md             # 서비스별 뉴스 목록
├── tags/
│   ├── index.md                        # 태그 목록
│   └── <태그명>/index.md               # 태그별 뉴스 목록
└── scripts/
    └── fetch_aws_news.py               # 수집 스크립트
```

## 통계

- **전체 뉴스:** 100건
- **수집 서비스:** 23개
- **마지막 업데이트:** 2026-06-17 12:55 UTC

## 많이 업데이트된 서비스 TOP 5

| 서비스 | 뉴스 수 |
|--------|---------|
| [RDS](./services/RDS/index.md) | 17 |
| [EC2](./services/EC2/index.md) | 13 |
| [S3](./services/S3/index.md) | 12 |
| [Config](./services/Config/index.md) | 10 |
| [CloudWatch](./services/CloudWatch/index.md) | 8 |

## 전체 서비스 목록

[서비스 인덱스 보기](./services/index.md)

## 태그 목록

[태그 인덱스 보기](./tags/index.md)

## 자동화

GitHub Actions (`.github/workflows/fetch-news.yml`)가 매일 UTC 09:00에 실행됩니다.

각 뉴스 파일에는 원문과 함께 **핵심 요약**, **주요 포인트**가 포함됩니다.

## AI 요약 활성화 (선택)

기본값은 단순 영→한 기계 번역(또는 미지원)입니다. Amazon Bedrock으로 실제 핵심 요약과 주요 포인트 강조를 받으려면 저장소 Settings → Secrets and variables → Actions에서 아래 항목을 설정하세요.

- `AWS_SUMMARIZE_ENABLED` (secret) = `true`
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` (secret) — `bedrock:InvokeModel` 권한 필요
- `BEDROCK_MODEL_ID` (variable, 선택) — 기본값 `anthropic.claude-3-haiku-20240307-v1:0`
- `AWS_REGION` (variable, 선택) — 기본값 `us-east-1`

