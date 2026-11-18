---
title: "AWS Control Tower now supports existing Amazon S3 bucket for log delivery"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/control-tower-existing-s3-log-bucket/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# AWS Control Tower now supports existing Amazon S3 bucket for log delivery

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/control-tower-existing-s3-log-bucket/

## 내용

AWS Control Tower now lets you use an existing Amazon S3 bucket in your landing zone to store AWS Config and AWS CloudTrail logs. Previously, AWS Control Tower required you to use the Amazon S3 bucket it creates and manages for log storage. Now, customers who want full control of bucket policies, lifecycle rules, and logging infrastructure can consolidate centralized logs in an Amazon S3 bucket they already manage.
You can use your own Amazon S3 bucket for both AWS Config and AWS CloudTrail, giving you full control of bucket policies, lifecycle rules, and logging infrastructure. You can switch between self-managed and AWS Control Tower managed buckets at any time, and your Amazon S3 buckets are preserved during landing zone updates, resets, and decommissioning. The bucket must be owned by an AWS account in your organization, be located in your AWS Control Tower home Region, and be preconfigured with the bucket policy that AWS Control Tower requires.
This feature is supported in landing zone version 4.0 and later and is available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the AWS European Sovereign Cloud where AWS Control Tower is available.
To learn more about configuring self-managed Amazon S3 bucket for your AWS Control Tower landing zone, visit the AWS Control Tower documentation.

## 핵심 요약

요약 미지원
