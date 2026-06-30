---
title: "Amazon MWAA Serverless now supports shared VPC configurations"
date: "2026-06-30"
service: "SageMaker"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/"
tags: ["SageMaker", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon MWAA Serverless now supports shared VPC configurations

**날짜:** 2026년 06월 30일
**서비스:** SageMaker
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-mwaa-serverless-vpc/

## 내용

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) Serverless now supports shared VPC subnets. Previously, customers using subnets shared via AWS Resource Access Manager (AWS RAM) received a validation error when creating MWAA Serverless workflows. With this update, MWAA Serverless correctly validates subnet ownership in shared VPC configurations, consistent with MWAA Provisioned environments. Sharing VPC subnets across accounts using AWS RAM is a common pattern in multi-account landing zone architectures. Organizations that centrally manage networking can now launch MWAA Serverless workflows in member accounts using shared subnets — no workarounds required. Customers using Amazon SageMaker Unified Studio Workflows also benefit from this update when their projects are configured with shared VPC networking. This update is available in all AWS Regions where Amazon MWAA Serverless is supported. To learn more, see the Networking section of the Amazon MWAA Serverless User Guide.

## 핵심 요약

요약 미지원
