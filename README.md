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
└── scripts/
    └── fetch_aws_news.py               # 수집 스크립트
```

## 통계

- **전체 뉴스:** 10건
- **수집 서비스:** 8개
- **마지막 업데이트:** 2026-06-16 13:09 UTC

## 많이 업데이트된 서비스 TOP 5

| 서비스 | 뉴스 수 |
|--------|---------|
| [EKS](./services/EKS/index.md) | 2 |
| [RDS](./services/RDS/index.md) | 2 |
| [S3](./services/S3/index.md) | 1 |
| [Lambda](./services/Lambda/index.md) | 1 |
| [Bedrock](./services/Bedrock/index.md) | 1 |

## 전체 서비스 목록

[서비스 인덱스 보기](./services/index.md)

## 자동화

GitHub Actions (`.github/workflows/fetch-news.yml`)가 매일 UTC 09:00에 실행됩니다.

