---
title: "Amazon ECR now replicates image deletions across regions and accounts"
date: "2026-11-17"
service: "EventBridge"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/replication-deletes-amazon-ecr"
tags: ["EventBridge", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon ECR now replicates image deletions across regions and accounts

**날짜:** 2026년 11월 17일
**서비스:** EventBridge
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/replication-deletes-amazon-ecr

## 내용

Amazon Elastic Container Registry (Amazon ECR) now supports replicating image deletions and tag removals to your replication destinations. Previously, ECR replication copied images to destination regions and accounts but did not replicate deletions, requiring you to manage deletions separately in each location. With replication of deletes, your destination repositories stay consistent with the source automatically. 
Teams running multi-region or multi-account architectures no longer need to script or manually track image cleanup across every destination. When you delete an image or remove a tag in your source registry, whether directly or through a lifecycle policy, ECR propagates that deletion to each destination in the replication rule. Replicated deletions emit EventBridge events and are recorded in CloudTrail, so you have the same visibility into deletions as you do for image pushes. 
Replication of deletes is available in all AWS Regions where Amazon ECR is available, at no additional cost. To get started, update your replication configuration in the Amazon ECR console or AWS CLI. For more information, see the Amazon ECR User Guide.

## 핵심 요약

요약 미지원
