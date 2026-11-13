---
title: "AWS Glue announces automatic version upgrades for Apache Spark jobs"
date: "2026-11-13"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/glue-spark-auto-upgrades/"
tags: ["EKS", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS Glue announces automatic version upgrades for Apache Spark jobs

**날짜:** 2026년 11월 13일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/glue-spark-auto-upgrades/

## 내용

AWS Glue introduces automatic version upgrades, a capability that keeps your Apache Spark jobs current on the latest AWS Glue runtime without manual coordination. Staying current on supported runtimes gives your jobs the latest security patches, performance improvements, and support for evolving table formats such as Apache Iceberg. Auto upgrades include multiple levels of validations including assessing jobs for compatibility with the upgraded runtime, obtaining your consent before executing jobs on a newer version, and validating upgraded job runs against each job's established output profile, so your jobs upgrade with the right guardrails in place.
By setting a job's version to "Auto", upgrades that once required weeks of planning and execution now happen automatically. Platform teams can standardize runtime versions across large fleets without chasing individual job owners, and business units without a central upgrade team can keep their jobs current hands-free. Each job is validated against its established output schema, data volume, latency, and format before it upgrades, so you can advance with confidence. Jobs that need code changes keep running safely on their current version, and AWS Glue provides an upgrade analysis with specific fixes you can apply directly or with the Apache Spark upgrade agent.
Auto upgrades for AWS Glue are available in all AWS Commercial Regions.
To get started, select "Auto" as the AWS Glue version when creating or updating an Apache Spark job using the AWS Glue Studio or AWS CLI, API, and SDKs. Alternatively, you can update multiple jobs at once using the AWS Glue skill to manage your jobs. To learn more, visit the AWS Glue documentation.

## 핵심 요약

요약 미지원
