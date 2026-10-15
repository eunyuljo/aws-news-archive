---
title: "ARC Region switch adds four new capabilities"
date: "2026-10-15"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/region-switch-target-health-ssm-lambda/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# ARC Region switch adds four new capabilities

**날짜:** 2026년 10월 15일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/region-switch-target-health-ssm-lambda/

## 내용

Amazon Application Recovery Controller (ARC) Region switch helps you orchestrate the failover of multi-Region applications to achieve a bounded recovery time during a Regional impairment. Today, Region switch adds four new capabilities: AWS Systems Manager Run Command execution block, payloads for custom action Lambda execution block, service quota parity checks, and wait for target group health feature for compute scaling actions.
AWS Systems Manager Run Command execution block. During failover, you often need to run commands on managed instances and VMs. This execution block lets you invoke Run Command actions on managed instances during failover, with plan evaluation verifying that command documents target valid instances and that IAM permissions are correctly configured.
Payloads for custom action Lambda execution block. ARC Region switch now lets you pass payloads to your custom action Lambda execution block, allowing reusability of your Lambda functions across recovery plans.
Service quota checks. Service quota limits are a common failure mode during recovery. Region switch now verifies quota parity between your primary and standby Region, and automatically submits quota limit increases, reducing the risk of insufficient service quotas during recovery.
Wait for target group health. Amazon ECS service scaling and Amazon EC2 Auto Scaling group execution blocks help you provision compute capacity during recovery, but provisioned capacity may not be ready to serve traffic. The optional wait for target group health feature verifies that your provisioned capacity is ready to serve traffic.
To get started, see the documentation for AWS Systems Manager Run Command execution block&nbsp;,&nbsp;custom action Lambda execution block&nbsp;, Service quota checks&nbsp; and the Wait for target group health for Amazon ECS service scaling execution block&nbsp; and Amazon EC2 Auto Scaling group execution block&nbsp;.&nbsp;&nbsp;

## 핵심 요약

요약 미지원
