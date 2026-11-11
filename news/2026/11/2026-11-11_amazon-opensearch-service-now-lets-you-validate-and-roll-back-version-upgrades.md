---
title: "Amazon OpenSearch Service now lets you validate and roll back version upgrades"
date: "2026-11-11"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service/upgrades/"
tags: ["CloudWatch", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon OpenSearch Service now lets you validate and roll back version upgrades

**날짜:** 2026년 11월 11일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service/upgrades/

## 내용

Amazon OpenSearch Service now supports clone-based upgrades, which let you validate a new OpenSearch version alongside your current one and cut over to it only when you're satisfied. If you find a problem, you can cancel before you cut over or roll back afterward. With clone-based upgrades, you can move to new versions with more confidence. 
When you start a clone-based upgrade, OpenSearch Service copies the data from your existing cluster (the primary cluster) to a second cluster running the new version (the cloned cluster). While the primary cluster keeps serving your workload, you can run the same search queries on both clusters and compare their performance using Amazon CloudWatch metrics. After you finish validating, you can cut over to the cloned cluster. If you keep the previous version for a retention period you choose, you can roll back to it at any time during that period. You can start and manage a clone-based upgrade from the AWS Management Console, the AWS CLI, or the OpenSearch Service APIs. 
Clone-based upgrades are available for domains running OpenSearch 1.1 or later, or Elasticsearch 7.10,&nbsp;in AWS Commercial Regions where Amazon OpenSearch Service is offered, except Asia Pacific (New Zealand), Asia Pacific (Taipei), Asia Pacific (Thailand), and Mexico (Central). For a complete list of Regions, see the AWS Region Table. 
To learn more, see Upgrading Amazon OpenSearch Service domains in the Amazon OpenSearch Service Developer Guide. To get started, visit the Amazon OpenSearch Service product page.

## 핵심 요약

요약 미지원
