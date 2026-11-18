---
title: "Amazon ECR now supports global authentication tokens for private registries"
date: "2026-11-18"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/global-authentication-amazon-ecr"
tags: ["Config", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon ECR now supports global authentication tokens for private registries

**날짜:** 2026년 11월 18일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/global-authentication-amazon-ecr

## 내용

Amazon Elastic Container Registry (Amazon ECR) now supports global authentication tokens for private registries. Previously, you needed to request a separate authentication token in each AWS Region where you push or pull container images. Now, you can request a single token from the AWS Sign-In CreateBearerToken API and use it across all ECR private registries in the same AWS partition. 
Teams that run proxy services to route container pulls across Regions, a common pattern for optimizing latency or availability, previously had to request, refresh, and coordinate a separate token for every Region behind the proxy. With global tokens, the proxy manages one token for all Regions in the AWS partition. Global tokens are valid for 12 hours by default, but can be configured to be as low as 5 minutes. These tokens work with the Docker CLI, and the Amazon ECR Docker Credential Helper. Existing regional authentication tokens continue to work as before. 
Global authentication tokens are available in all commercial AWS Regions where Amazon ECR is supported. To learn more, see Private registry authentication in the Amazon ECR User Guide.&nbsp;

## 핵심 요약

요약 미지원
