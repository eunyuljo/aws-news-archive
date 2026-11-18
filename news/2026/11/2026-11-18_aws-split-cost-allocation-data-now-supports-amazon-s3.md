---
title: "AWS Split Cost Allocation Data now supports Amazon S3"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/split-cost-allocation-data-s3/"
tags: ["S3", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Split Cost Allocation Data now supports Amazon S3

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/split-cost-allocation-data-s3/

## 내용

Starting today, you can allocate the storage and request costs of a shared Amazon S3 general purpose bucket to the prefixes in that bucket in the AWS Cost and Usage Report (CUR). Organizations often store data for many teams, applications, or tenants in one bucket under different prefixes, such as `marketing/` and `finance/`. Until now, attributing that bucket's bill to each prefix required custom pipelines built on S3 Inventory or Storage Lens reports and your own pricing logic. 
With Split Cost Allocation Data for Amazon S3, Amazon S3 Storage Lens publishes prefix-level storage and request metrics to AWS Billing and Cost Management, which allocates the bucket's storage and Tier 1 and Tier 2 request costs to the deepest matching prefix in the range of prefix levels you choose. Each prefix line item carries its full prefix path as AWS-generated cost allocation tags, so you can total cost by top-level prefix, team, or application, and reconcile it back to the bucket. You can use this data for chargeback, showback, and to see which prefixes drive your S3 spend. 
To get started, enable AWS Billing and Cost Management publishing in an S3 Storage Lens advanced tier dashboard configuration, then enable split cost allocation data for Amazon S3 in the AWS Billing and Cost Management console. Prefix cost data appears in your CUR after the next daily Storage Lens metrics are published. Split Cost Allocation Data for Amazon S3 is available in all AWS commercial Regions where S3 Storage Lens advanced metrics are available, at no additional charge beyond S3 Storage Lens advanced tier pricing. To learn more, visit the AWS Cost and Usage Reports product page, Understanding split cost allocation data, and Estimating Amazon S3 costs by prefix with S3 Storage Lens.

## 핵심 요약

요약 미지원
