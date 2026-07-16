---
title: "Amazon CloudWatch announces lookup processor for log enrichment"
date: "2026-07-16"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-lookup-processor/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon CloudWatch announces lookup processor for log enrichment

**날짜:** 2026년 07월 16일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cloudwatch-lookup-processor/

## 내용

Amazon CloudWatch now supports lookup processor, enabling you to enrich log events with additional context by matching fields in your logs against a lookup table directly within your&nbsp;CloudWatch Pipeline. 
With the lookup processor, you can upload CSV files containing reference data and configure your pipeline to match incoming log fields against this data to add enriched metadata. For example, you can upload a CSV mapping IP addresses to application teams and automatically tag VPC Flow Logs with team ownership information as logs are ingested. The lookup processor matches fields in your log events against fields in a lookup table and adds specified fields from matching rows to your log events. This enables data enrichment scenarios such as mapping user IDs to user details, product codes to product information, or error codes to human-readable error descriptions, thereby eliminating the need to build and maintain custom enrichment logic outside of CloudWatch. By enriching logs at ingestion time, your queries, dashboards, and alarms immediately benefit from the added context without any post-processing. 
The lookup table processor is available in all AWS commercial regions that support Amazon CloudWatch pipelines. You can add a lookup processor to your pipeline using the AWS Management Console, AWS CLI, or AWS SDKs. To get started, see the Amazon CloudWatch Logs documentation.

## 핵심 요약

요약 미지원
