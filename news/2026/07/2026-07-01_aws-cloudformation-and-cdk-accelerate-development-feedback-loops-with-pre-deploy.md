---
title: "AWS CloudFormation and CDK accelerate development feedback loops with pre-deployment validation on all stack operations"
date: "2026-07-01"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation/"
tags: ["S3", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# AWS CloudFormation and CDK accelerate development feedback loops with pre-deployment validation on all stack operations

**날짜:** 2026년 07월 01일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-cloudformation/

## 내용

AWS CloudFormation customers can now get immediate feedback on deployment errors in seconds, eliminating the need to wait through a full provision-and-rollback cycle to discover preventable failures. CloudFormation now runs pre-deployment validation on Create Stack and Update Stack operations, catching common deployment errors before resource provisioning begins. This accelerates development velocity across all deployment workflows, from manual iteration to CI/CD pipelines to AI agents provisioning infrastructure.  Previously, pre-deployment validation was available during change set creation, covering property syntax errors, resource name conflicts, and S3 bucket emptiness constraints. With this release, the same validations now run automatically on Create Stack and Update Stack operations. Additionally, three new validation checks are now available as warnings during change set creation. Service quota limits validation warns when creating resources would exceed your account's service quotas. AWS Config Recorder conflict detection warns when your template adds Config rules to an account that does not have Config recording enabled, or defines a Config Recorder in an account where one is already active. ECR repository delete readiness validation warns when an ECR repository targeted for deletion still contains images. When validation detects an issue, you can view errors using the DescribeEvents API with the operation ID, or in the CloudFormation console by navigating to your stack's Events tab and clicking the operation ID (or the link in the banner or status reason column) to open the Operation view page, which opens directly on the Deployment validations tab. Each error includes the logical resource ID and property path, so you can pinpoint and fix the problem before any resources are provisioned. In CDK, both cdk deploy and cdk validate surface validation results with construct-level tracing in a unified report, so AI agents and automation tools can parse structured responses and self-correct immediately.  Pre-deployment validation is enabled by default on all stack operations with no configuration required. If you need to skip validation for a specific operation, use the new DisableValidation parameter on CreateStack, UpdateStack and CreateChangeSet API calls, or the --disable-validation flag in the CLI. Visit the Validate stack deployments User Guide to learn more.  This feature is available in all AWS Regions where CloudFormation is supported, excluding China. Refer to the AWS Region table for service availability details.

## 핵심 요약

요약 미지원
