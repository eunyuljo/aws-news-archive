---
title: "AWS Systems Manager now diagnoses more issues that cause EC2 instances to be unmanaged"
date: "2026-09-10"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/systems-manager-diagnoses-ec2-unmanaged/"
tags: ["EC2", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# AWS Systems Manager now diagnoses more issues that cause EC2 instances to be unmanaged

**날짜:** 2026년 09월 10일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/systems-manager-diagnoses-ec2-unmanaged/

## 내용

Today, AWS Systems Manager extends its diagnosis capability to identify six additional categories of issues that can prevent Amazon EC2 instances and hybrid-activated nodes from becoming managed by Systems Manager. An instance must be managed by Systems Manager before you can patch it, run commands, connect with Session Manager, or collect inventory, and when an instance is unmanaged the cause can be difficult to isolate. The diagnosis previously covered network connectivity, and it now also identifies issues with IAM permissions, SSM Agent version, instance status checks, operating system configuration, Default Host Management Configuration, and hybrid activation.
With this broader coverage, more of your instances return a specific, actionable cause instead of an unidentified result, so you can bring your fleet under management faster. You run a diagnosis across your instances in the Systems Manager unified console experience, and Systems Manager reports the specific issues it finds in each category. Every diagnosed issue comes with step-by-step guidance to help you resolve it, and for some issues you can also run an AWS Systems Manager Automation runbook from the console to remediate the issue directly.
AWS Systems Manager diagnosis capability is available in all AWS Regions that are enabled by default. The capability runs as AWS Systems Manager Automation runbooks, so you pay standard Automation usage charges for the runbooks you run; see AWS Systems Manager pricing for details. To learn more, see the AWS Systems Manager User Guide, or visit the AWS Systems Manager product page.

## 핵심 요약

요약 미지원
