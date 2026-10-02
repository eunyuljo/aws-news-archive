---
title: "Amazon Redshift now supports cross-Region queries for your data lake"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-cross-Region-queries-for-data-lake"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Redshift now supports cross-Region queries for your data lake

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/redshift-cross-Region-queries-for-data-lake

## 내용

Amazon Redshift now supports querying Amazon S3 data lake tables located in a different AWS Region. With enhanced VPC routing, data lake query traffic between Amazon S3 and Amazon Redshift stays within your own VPC.&nbsp;Both capabilities are powered by the integrated data lake query engine that runs directly on the compute of RG provisioned and Serverless clusters. These features are aimed at enterprises with globally distributed data and at security-sensitive customers who need tight control over how their data travels.
With cross-Region support, you can use Amazon Redshift to query S3 data in another Region directly, without first copying or replicating it. This makes it easier to run global analytics, consolidate reporting across Regions, and query data that must remain in a specific Region for residency requirements. Cross-Region queries incur standard data transfer charges. Because the query engine runs on your cluster's compute, data moving between Amazon S3 and Amazon Redshift flows entirely over your VPC when you use enhanced VPC routing, never over public networks. Regulated industries such as financial services, healthcare, and government benefit from this feature as it keeps data lake queries within the network boundaries their compliance requirements demand.&nbsp;&nbsp;Both capabilities work with the integrated data lake query engine, which is available in all regions where RG provisioned and Serverless clusters are available. To learn more, see Querying your data lake&nbsp;tables with enhanced VPC routing&nbsp;in the Amazon Redshift documentation.

## 핵심 요약

요약 미지원
