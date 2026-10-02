---
title: "Amazon DynamoDB introduces filtered export to Amazon S3"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-introduces-filtered-export/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon DynamoDB introduces filtered export to Amazon S3

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-dynamodb-introduces-filtered-export/

## 내용

Amazon DynamoDB now supports filtered export for tables. Export to Amazon S3 allows you to export your table data for analytics, data sharing, and other offline uses, as either a full export or an incremental export over a time window. Filtered export enables you to specify exactly which items and attributes to export, producing a dataset that contains only the data relevant to your use case.
 
With filtered export, you use a key condition expression on a key attribute and a filter expression on any attribute to select which items to export, and a projection expression to choose which attributes to include. The export then returns only the items and attributes you want. You can use that subset of data to perform granular data recovery, move a slice of data between accounts, or run analytics while meeting your compliance rules. Filtered export works with both full exports and incremental exports.
Filtered export is available in all AWS Regions, except the AWS GovCloud (US) Regions. To get started, see the following resources:

 DynamoDB data export to Amazon S3&nbsp;in the DynamoDB developer guide


 Filtering a table export&nbsp;in the DynamoDB developer guide


 Introducing filtered export from Amazon DynamoDB to Amazon S3 blog post

## 핵심 요약

요약 미지원
