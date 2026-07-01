---
title: "AWS CloudFormation and CDK express mode speeds up infrastructure deployments by up to 4x"
date: "2026-07-01"
service: "CloudFront"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/"
tags: ["CloudFront", "2026", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS CloudFormation and CDK express mode speeds up infrastructure deployments by up to 4x

**날짜:** 2026년 07월 01일
**서비스:** CloudFront
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation-cdk/

## 내용

AWS CloudFormation and CDK express mode reduces deployment time by up to 4x for developers and AI agents building infrastructure, based on internal benchmarks. Express mode completes stack operations when CloudFormation confirms resource configuration is applied, rather than waiting for extended stabilization checks such as traffic readiness, region propagation, and resource cleanup. This enables faster iteration cycles for developers and AI agents building infrastructure.  When iterating on infrastructure in development environments, developers and AI agents need faster iteration cycles to build infrastructure incrementally. Previously, every deployment waited for full resource stabilization regardless of whether the workflow required it. For example, creating a CloudFront distribution required waiting 5-10 minutes for propagation to all edge locations before the deployment completed, even when the developer only needed the distribution domain name to continue. With express mode, deployments complete in seconds once configuration is applied, and propagation continues in the background. CloudFormation still processes resources in dependency order and handles dependent resource failures within the same stack. Express mode disables rollback by default, enabling immediate fix-and-retry without waiting for rollback operations.  To get started, set --deployment-config '{"mode": "EXPRESS"}' when creating, updating, and deleting stacks or creating a change set through the AWS CLI, AWS SDKs, or the AWS Management Console. For AWS CDK users, activate express mode with cdk deploy --express. No template changes are required. Express mode works with all existing CloudFormation templates, and nested stacks. Visit the CloudFormation Express mode documentation to learn more.  This feature is available in all AWS Regions where CloudFormation is supported. Refer to the AWS Region table for service availability details.

## 핵심 요약

요약 미지원
