---
title: "AWS Lambda now publishes logs for Lambda Managed Instances capacity providers"
date: "2026-07-25"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-managed-instances-logs/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Lambda now publishes logs for Lambda Managed Instances capacity providers

**날짜:** 2026년 07월 25일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-lambda-managed-instances-logs/

## 내용

AWS Lambda now publishes logs for Lambda Managed Instances (LMI) capacity providers to Amazon CloudWatch Logs, giving you visibility into scaling activity and instance lifecycle operations. LMI enables you to run Lambda functions on Amazon EC2 instances while maintaining serverless operational simplicity. Capacity providers are resources that let you define compute resources that Lambda provisions on your behalf. With capacity provider logs, you can monitor, troubleshoot, and optimize these managed EC2 instances, helping you quickly diagnose provisioning issues and understand scaling behavior. 
Customers use LMI to operate high-volume, predictable workloads with specialized compute configurations and achieve cost efficiency through EC2 pricing options like Savings Plans and Reserved Instances. With this launch, Lambda automatically generates logs for compute resources managed by capacity providers and delivers them to CloudWatch Logs. Lambda publishes structured JSON logs capturing instance lifecycle events like launches, terminations, and health checks. This structured format lets you identify failed operations and provisioning errors through CloudWatch Logs filtering, helping you resolve issues quickly and shorten debugging cycles. 
The capacity provider logs are&nbsp;available in all AWS Commercial Regions where LMI is available. The logs are enabled by default for all capacity providers. You can view your capacity provider logs by visiting the Lambda console's capacity provider page. You can use the Lambda API, Lambda console, AWS CLI, AWS SAM, or AWS CloudFormation to change&nbsp;capacity provider&nbsp;log configuration. Standard Amazon CloudWatch Logs charges apply.&nbsp;To learn more, visit the AWS Lambda Managed Instances product page and documentation.&nbsp;

## 핵심 요약

요약 미지원
