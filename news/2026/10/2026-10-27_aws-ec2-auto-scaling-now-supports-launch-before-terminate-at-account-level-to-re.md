---
title: "AWS EC2 Auto Scaling now supports Launch Before Terminate at account-level to replace instances"
date: "2026-10-27"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-auto-scaling-launch-before-terminate/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS EC2 Auto Scaling now supports Launch Before Terminate at account-level to replace instances

**날짜:** 2026년 10월 27일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/ec2-auto-scaling-launch-before-terminate/

## 내용

AWS EC2 Auto Scaling now lets you enable Launch Before Terminate as the default replacement behavior across all Auto Scaling groups in your account. When enabled, Auto Scaling launches a replacement instance and waits for it to pass health checks before terminating the instance it replaces, helping your applications maintain full capacity and availability during instance replacement events. This applies to replacement events such as instance refreshes, rebalancing, health checks, and maximum-instance-lifetime replacements. 
You can enable Launch Before Terminate through AWS EC2 Auto Scaling account settings, which let you configure the behavior once at the account level instead of on each Auto Scaling group individually. You can manage the setting with the new `PutAccountSetting` and `DescribeAccountSettings` APIs, available through the AWS Management Console, AWS CLI, or AWS SDKs. 
Launch Before Terminate is available in all AWS Regions at no additional cost. 
To learn more, see Launch Before Terminate in the AWS EC2 Auto Scaling User Guide and AWS EC2 Auto Scaling API Reference Guide.

## 핵심 요약

요약 미지원
