---
title: "Amazon ECR now supports replication backfill for existing container images"
date: "2026-10-27"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/replication-backfill-amazon-ecr"
tags: ["Config", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon ECR now supports replication backfill for existing container images

**날짜:** 2026년 10월 27일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/replication-backfill-amazon-ecr

## 내용

Amazon Elastic Container Registry (Amazon ECR) now supports replication backfill, enabling you to replicate existing images in your private registry to your configured replication registry destinations. Previously, replication only applied to images pushed after the replication configuration was enabled, requiring customers to manually retag images to trigger replication of preexisting images. With replication backfill, you can now replicate your full image catalog to new or existing destinations with a single API call. 
Replication backfill is useful when expanding to a new AWS Region, validating disaster recovery readiness, updating replication rules, or ensuring complete image catalogs exist across Regions for compliance purposes. You can run up to ten backfill jobs concurrently, monitor progress and per-image results through new APIs, and stop a job at any time without deleting images that have already been replicated. 
Replication backfill is available in all AWS Regions where Amazon ECR is available. To learn more, refer to the Amazon ECR user guide.&nbsp;

## 핵심 요약

요약 미지원
