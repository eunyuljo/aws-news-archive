---
title: "AWS CloudFormation Service-Managed StackSets adds custom execution roles with nested stacks support"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/stacksets-custom-execution-roles/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS CloudFormation Service-Managed StackSets adds custom execution roles with nested stacks support

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/stacksets-custom-execution-roles/

## 내용

AWS CloudFormation StackSets now supports custom execution roles for service-managed stack sets, which enables you to scope the permissions StackSets uses in each target AWS account. StackSets deploys the same infrastructure, such as networking and security settings, across thousands of accounts and Regions in one operation. With a custom execution role, you can also use nested stacks, macros, and transforms in service-managed stack sets, which allows you to deploy the reusable templates you use for individual stacks across your organization. 
With a custom execution role, you define what StackSets can do in each account. By default, service-managed stack sets use a role in each account that can provision any resource in a template without additional setup, and that default remains available. Now, you can provide a template that defines an IAM role, called the execution role, and StackSets creates it in each account before deploying. For example, a stack set that creates Amazon S3 buckets can use an execution role limited to CloudFormation and Amazon S3 permissions. When you update the execution role template, StackSets updates the role in every account it deployed to. 
To get started, choose Set execution role when you create a stack set in the CloudFormation console, or use the AWS CLI or AWS SDKs. To learn more, visit the documentation and the AWS DevOps Blog. This feature is available at no additional charge in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the China Regions. Refer to the AWS Region table for details.

## 핵심 요약

요약 미지원
