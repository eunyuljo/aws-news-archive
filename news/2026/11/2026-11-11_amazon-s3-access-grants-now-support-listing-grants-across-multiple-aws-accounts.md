---
title: "Amazon S3 Access Grants now support listing grants across multiple AWS accounts"
date: "2026-11-11"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/"
tags: ["S3", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon S3 Access Grants now support listing grants across multiple AWS accounts

**날짜:** 2026년 11월 11일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-access-grants-list-across-regions/

## 내용

Amazon S3 Access Grants can now discover and list all your grants across multiple AWS accounts with a single API call, eliminating the need to query each account separately. A single ListCallerAccessGrants call returns grants from your own S3 Access Grants instance and every instance shared with you, giving you a complete view of the S3 data you can access. 
By setting the new InstanceScope parameter to ALL in your ListCallerAccessGrants request, S3 Access Grants queries every instance shared with you through AWS Resource Access Manager (AWS RAM) and returns all the grants in one combined response, each identifying the account that owns it. Additionally, when you request credentials with GetDataAccess for an S3 path and set InstanceScope to ALL, S3 Access Grants locates the owning account for you, routes the request to its instance, and returns credentials for the matching grant. 
This capability is now available in all AWS Regions where S3 Access Grants is available, at no additional cost. You can use the AWS SDK, API, or CLI to list and access grants across accounts. To learn more, visit the S3 Access Grants overview page and the S3 documentation.

## 핵심 요약

요약 미지원
