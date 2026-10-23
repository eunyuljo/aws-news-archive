---
title: "AWS CloudFormation now simplifies stack update rollback operations"
date: "2026-10-23"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-cloudformation-cdk/"
tags: ["CloudFormation", "2026", "price-reduction", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS CloudFormation now simplifies stack update rollback operations

**날짜:** 2026년 10월 23일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-cloudformation-cdk/

## 내용

AWS CloudFormation&nbsp;now makes it simpler to complete an update rollback and get back to deploying. An update rollback returns your stack to a known good state. Starting today, if some resources cannot roll back automatically, force rollback enables you to complete the rollback it in a single operation. It works across every CloudFormation workflow, from the AWS CLI, and SDKs to AWS CDK&nbsp;and AI agents. 
With force rollback, CloudFormation completes the update rollback and returns your stack to a deployable state in a single operation, instead of requiring you to identify, list, and retry the operation for each affected resource. Any resource that still needs attention, such as one affected a change outside CloudFormation, is recorded for you to review and resolve it before your next deployment. 
To get started, run continue update rollback with the force rollback option, then create a drift-aware change set to review any configuration differences before your next deployment. To learn more, see &nbsp;Continue rolling back an update&nbsp; in the AWS CloudFormation User Guide. 
Force rollback is available in all Regions at no additional cost. Refer to the &nbsp;AWS Region table&nbsp; for service availability details.

## 핵심 요약

요약 미지원
