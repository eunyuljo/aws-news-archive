---
title: "Amazon MWAA now supports fine-grained access control with IAM Identity Center and multi-team environments"
date: "2026-11-13"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-fine-grained-access-control/"
tags: ["S3", "2026", "preview", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon MWAA now supports fine-grained access control with IAM Identity Center and multi-team environments

**날짜:** 2026년 11월 13일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-fine-grained-access-control/

## 내용

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) now supports fine-grained access control, giving administrators precise control over who can access which workflows and resources in an Apache Airflow environment. Fine-grained access control is delivered through two new capabilities: IAM Identity Center integration and multi-team environments.
With IAM Identity Center integration, users sign in to the Apache Airflow UI with their corporate identity provider. Authorization is evaluated per request using IAM policies attached to IAM Identity Center Permission Sets, with condition keys that scope access by resource type (DAGs, connections, variables, pools, and more), action, and specific resource ID.
With multi-team environments, several teams can share a single MWAA environment. Each team gets its own DAG folder in Amazon S3, and users see only shared DAGs plus their own teams' DAGs based on IAM Identity Center group membership. Teams reduce cost through shared infrastructure and simplify management by configuring environment settings once. Multi-team environments are based on the Apache Airflow multi-team feature, which is currently in preview.
These features are available in all AWS Regions where Amazon MWAA is available.
To learn more, visit the IAM Identity Center integration documentation and the multi-team environments documentation.

## 핵심 요약

요약 미지원
