---
title: "Amazon CloudFront Functions now supports logging to CloudFront access logs"
date: "2026-07-15"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/cloudfront-functions-access-logs/"
tags: ["CloudFront", "2026", "GA"]
nav_exclude: true
---

# Amazon CloudFront Functions now supports logging to CloudFront access logs

**날짜:** 2026년 07월 15일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/cloudfront-functions-access-logs/

## 내용

You can now write custom data directly into CloudFront access logs using a new helper method available from within CloudFront Functions. CloudFront Functions run lightweight JavaScript at the edge for tasks like URL rewrites, header manipulation, and request routing. Previously, you could only emit log data to Amazon CloudWatch Logs as a separate log file from your CloudFront access logs. With this launch, you no longer need to correlate function decisions with CloudFront access log data across separate logging systems. 
You can call cf.logCustomData() from viewer request or viewer response functions to log values such as A/B test variant assignments, authentication outcomes, or routing decisions directly into the CloudFront access log record for that request. This works with both CloudFront real time log configurations and standard logging (v2), so you can analyze function behavior and request outcomes in a single query. The existing console.log() functionality remains available and the two methods can be used together in the same function. 
Amazon CloudFront Functions custom log data is available today in all CloudFront edge locations. There is no additional charge for using cf.logCustomData(). Standard CloudFront Functions invocation pricing and access log delivery charges apply. To get started, visit CloudFront Functions helper methods.

## 핵심 요약

요약 미지원
