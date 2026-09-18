---
title: "AWS Transfer Family now supports source IP preservation for SFTP servers behind a Network Load Balancer (NLB)"
date: "2026-09-18"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/"
tags: ["VPC", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Transfer Family now supports source IP preservation for SFTP servers behind a Network Load Balancer (NLB)

**날짜:** 2026년 09월 18일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-source-ip-nlb/

## 내용

AWS Transfer Family now preserves the client's source IP address using Proxy Protocol v2 (PPv2) when you place a Network Load Balancer (NLB) in front of your SFTP server that uses a VPC-hosted endpoint. You can now retain visibility of the client's source IP for IP-based auditing, access controls, and compliance when you use your own NLB. 
Previously, an NLB replaced the client's source IP with its own private IP address, so your Transfer Family logs and events recorded the NLB's address instead of the client's source IP. Because the NLB's private IP was the address presented to your custom identity provider during authentication, you couldn't authorize users based on their true source IP. With this launch, you can enable source IP preservation on your SFTP server so that the client's source IP is preserved. The preserved source IP is recorded in your logs and events and presented to your custom identity provider during authentication. You can enable the feature on each Transfer Family server individually through the console, CLI, or API. 
Source IP preservation for SFTP servers is available in all AWS Regions where AWS Transfer Family is available. To get started, visit the AWS Transfer Family console or use the AWS CLI/SDK. To learn more, visit the Transfer Family User Guide.

## 핵심 요약

요약 미지원
