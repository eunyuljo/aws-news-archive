#!/usr/bin/env python3
"""
개발/테스트용 샘플 뉴스 데이터 생성 스크립트.
실제 운영에서는 fetch_aws_news.py 를 사용합니다.
"""

import textwrap
from datetime import datetime, timezone, timedelta
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from fetch_aws_news import (
    write_news_file, update_service_index,
    update_global_service_index, update_readme,
    update_tag_indexes, detect_service,
)

SAMPLE_ITEMS = [
    {
        "title": "Amazon S3 now supports conditional writes for object creation",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-s3-conditional-writes/",
        "description": (
            "Amazon S3 now supports conditional writes that allow you to prevent objects "
            "from being overwritten. You can now add a precondition to your S3 PUT or "
            "COPY request so that the operation only succeeds if the object doesn't "
            "already exist in the bucket."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 8, 15, 10, 0, tzinfo=timezone.utc),
    },
    {
        "title": "AWS Lambda now supports Python 3.13",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/11/aws-lambda-python-3-13/",
        "description": (
            "AWS Lambda now supports creating and updating functions using Python 3.13. "
            "Python 3.13 includes improvements to the typing module, a new REPL, and "
            "performance improvements."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 11, 22, 14, 0, tzinfo=timezone.utc),
    },
    {
        "title": "Amazon Bedrock announces support for Claude 3.5 Sonnet",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/06/amazon-bedrock-claude-3-5-sonnet/",
        "description": (
            "Amazon Bedrock now supports Anthropic Claude 3.5 Sonnet, the most intelligent "
            "model to date. Claude 3.5 Sonnet raises the bar on intelligence, outperforming "
            "competitor models and previous Claude versions."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 6, 20, 9, 0, tzinfo=timezone.utc),
    },
    {
        "title": "Amazon EKS now supports Kubernetes version 1.31",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-eks-kubernetes-1-31/",
        "description": (
            "Amazon EKS now supports Kubernetes version 1.31. Kubernetes 1.31 includes "
            "several new features and bug fixes. Notable changes include AppArmor support "
            "graduating to stable and pod failure policy for jobs graduating to stable."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 10, 8, 12, 0, tzinfo=timezone.utc),
    },
    {
        "title": "Amazon RDS for PostgreSQL supports pgvector 0.7.0",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/05/amazon-rds-postgresql-pgvector-0-7-0/",
        "description": (
            "Amazon RDS for PostgreSQL now supports the pgvector extension version 0.7.0. "
            "pgvector is an open-source extension for vector similarity search. "
            "The new version includes performance improvements for HNSW indexing."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 5, 14, 8, 0, tzinfo=timezone.utc),
    },
    {
        "title": "AWS CloudFront announces HTTP/3 support in all edge locations",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/07/aws-cloudfront-http3-all-edge-locations/",
        "description": (
            "Amazon CloudFront now supports HTTP/3 with QUIC in all edge locations globally. "
            "HTTP/3 can improve performance by reducing connection establishment time and "
            "eliminating head-of-line blocking."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 7, 2, 11, 0, tzinfo=timezone.utc),
    },
    {
        "title": "Amazon DynamoDB global tables support multi-Region strong consistency",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/09/amazon-dynamodb-global-tables-mrsc/",
        "description": (
            "Amazon DynamoDB global tables now support multi-Region strong consistency (MRSC), "
            "enabling you to perform strongly consistent reads from any of the AWS Regions "
            "where your DynamoDB global table is replicated."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 9, 17, 15, 0, tzinfo=timezone.utc),
    },
    {
        "title": "AWS IAM now supports passkey MFA for root and IAM users",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/06/aws-iam-passkey-mfa/",
        "description": (
            "AWS Identity and Access Management (IAM) now supports passkeys as a "
            "multi-factor authentication (MFA) method for both root and IAM users. "
            "Passkeys are more secure than traditional passwords and resistant to phishing."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 6, 10, 13, 0, tzinfo=timezone.utc),
    },
    {
        "title": "Amazon SageMaker Canvas adds time series forecasting with Foundation Models",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/04/sagemaker-canvas-time-series-foundation-models/",
        "description": (
            "Amazon SageMaker Canvas now supports time series forecasting using Foundation "
            "Models including Amazon Chronos. This enables you to generate accurate forecasts "
            "without requiring any ML expertise."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 4, 23, 16, 0, tzinfo=timezone.utc),
    },
    {
        "title": "AWS CloudWatch Container Insights supports GPU metrics for EKS",
        "link": "https://aws.amazon.com/about-aws/whats-new/2024/03/aws-cloudwatch-container-insights-gpu-metrics-eks/",
        "description": (
            "Amazon CloudWatch Container Insights now supports GPU metrics for Amazon EKS. "
            "You can now monitor GPU utilization, memory usage, and temperature for "
            "GPU-enabled workloads running on Amazon EKS."
        ),
        "creator": "AWS",
        "pub_date": datetime(2024, 3, 11, 9, 0, tzinfo=timezone.utc),
    },
]


def main():
    service_items: dict[str, list[dict]] = {}
    all_items_with_service: list[dict] = []

    for item in SAMPLE_ITEMS:
        service = detect_service(item["title"], item["description"])
        item_with_service = {**item, "service": service}
        service_items.setdefault(service, []).append(item_with_service)
        all_items_with_service.append(item_with_service)
        # force=True で既存ファイルも上書き（frontmatter更新のため）
        write_news_file(item, service, force=True)

    for service, items in service_items.items():
        update_service_index(service, items)

    service_counts = {s: len(i) for s, i in service_items.items()}
    update_global_service_index(service_counts)
    update_tag_indexes(all_items_with_service)
    update_readme(service_counts, len(SAMPLE_ITEMS), len(SAMPLE_ITEMS))
    print(f"샘플 데이터 {len(SAMPLE_ITEMS)}건 생성 완료")


if __name__ == "__main__":
    main()
