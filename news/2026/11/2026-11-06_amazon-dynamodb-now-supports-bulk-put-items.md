---
title: "Amazon DynamoDB now supports bulk put items"
date: "2026-11-06"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/"
tags: ["S3", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon DynamoDB now supports bulk put items

**날짜:** 2026년 11월 06일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-dynamodb-now-supports-bulk-put-items/

## 내용

Today, AWS announces the general availability of bulk put items for Amazon DynamoDB, a fully managed feature that writes data from Amazon S3 into your existing DynamoDB tables. Many DynamoDB applications use data that other systems produce and store in Amazon S3. Writing this data into existing DynamoDB tables has typically meant building custom pipelines and managing table capacity. With bulk put items, developers and data engineers can write this data without impacting existing workloads or building a custom ingestion pipeline, in a cost-efficient way. 
You point bulk put items at the S3 location of your input files, and DynamoDB handles the rest. Each item supports its own condition expression, so you can enforce insert-only or version-guarded writes. The Standard tier fits most workloads, and the Accelerated tier is for more time-sensitive workloads. Common use cases include daily refreshes, large catalog enrichments, backfills, and migrations. 
Bulk put items with Standard tier is available in all commercial AWS Regions and the AWS GovCloud (US) Regions, to see the list where the Accelerated tier is available see the regional availability. To learn more, visit the Introducing bulk put items for Amazon DynamoDB blog and the Amazon DynamoDB Developer Guide.

## 핵심 요약

요약 미지원
