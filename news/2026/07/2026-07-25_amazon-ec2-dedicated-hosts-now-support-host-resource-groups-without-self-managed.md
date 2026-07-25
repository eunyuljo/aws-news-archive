---
title: "Amazon EC2 Dedicated Hosts now support host resource groups without self-managed licenses"
date: "2026-07-25"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-dedicated-hosts-hrg/"
tags: ["EC2", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon EC2 Dedicated Hosts now support host resource groups without self-managed licenses

**날짜:** 2026년 07월 25일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-dedicated-hosts-hrg/

## 내용

Starting today, customers can create Host Resource Groups (HRGs) for EC2 Dedicated Hosts without the previously required step of creating Self-Managed Licenses (SMLs) and associating AMIs through AWS License Manager. 
This flexibility is particularly valuable for EC2 Mac Instance customers and for customers who need Dedicated Hosts for hardware-level isolation rather than Bring Your Own License (BYOL). Customers with BYOL workloads can continue to create HRGs with SMLs to ensure that only instances from associated AMIs can be launched on the host and track host-level license consumption. 
To create an HRG without SML, uncheck the "Restrict to AMIs associated with self-managed license" option when creating a Host Resource Group in the EC2 Console, or set instance-launch-option to license-configuration-required via the AWS CLI. 
This feature is available in all AWS Regions where Host Resource Groups are supported. To learn more, visit the Host Resource Group User Guide

## 핵심 요약

요약 미지원
