---
title: "Amazon CloudFront now supports Origin Access Control (OAC) for Amazon S3 Multi-Region Access Points"
date: "2026-08-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap"
tags: ["Lambda", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon CloudFront now supports Origin Access Control (OAC) for Amazon S3 Multi-Region Access Points

**날짜:** 2026년 08월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-cloudfront-oac-s3-mrap

## 내용

Starting today, customers can protect their origins using Amazon S3 Multi-Region Access Points (MRAP) by using CloudFront Origin Access Control (OAC) to only allow access from designated CloudFront distributions. 
Customers use Amazon S3 MRAP with CloudFront to serve content from a single global endpoint that automatically routes to the closest available replicated bucket across regions during a cache miss, improving performance and resilience for globally distributed users. Previously, customers had to compute and forward their own Asymmetric Signature Version 4 (SigV4a) Authorization header using a custom Lambda@Edge Function. Now, CloudFront natively signs requests to S3 MRAP origins. Customers get faster cache-miss fills from the nearest region and restricted, OAC-secured MRAP access without&nbsp; custom Authorization header computation. 
CloudFront OAC support for Amazon S3 MRAP origins is available worldwide, except in the CloudFront China region. To get started, use the CloudFront Console, SDK, CLI, or CloudFormation to enable OAC when configuring your Amazon S3 MRAP endpoint with CloudFront. For more information, refer to the CloudFront Developer Guide. There are no additional fees associated with this feature

## 핵심 요약

요약 미지원
