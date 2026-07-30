---
title: "Amazon EC2 Auto Scaling now supports Instance Refresh in CloudFormation"
date: "2026-07-30"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-auto-scaling-instance-refresh-cloudformation"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EC2 Auto Scaling now supports Instance Refresh in CloudFormation

**날짜:** 2026년 07월 30일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-auto-scaling-instance-refresh-cloudformation

## 내용

Amazon EC2 Auto Scaling now supports Instance Refresh as a new AWS CloudFormation update policy. When you configure the new AutoScalingInstanceRefresh update policy and update properties that require instance replacement, CloudFormation automatically triggers an Instance Refresh. 
With this integration, you can now access Instance Refresh capabilities including replace root volume for in-place updates, launch-before-terminate, alarm-based monitoring, and checkpoints with bake time for controlled rollouts. Auto Scaling features such as scaling policies and health checks remain active throughout the update, so your service health is not at risk during deployments. Rollback is handled through CloudFormation stack rollback. 
This feature is available in all AWS Regions at no additional cost. To learn more, see AutoScalingInstanceRefresh update policy in the AWS CloudFormation Template Reference.

## 핵심 요약

요약 미지원
