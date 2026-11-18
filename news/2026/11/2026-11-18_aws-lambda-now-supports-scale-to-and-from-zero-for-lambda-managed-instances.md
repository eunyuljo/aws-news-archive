---
title: "AWS Lambda now supports scale to and from zero for Lambda Managed Instances"
date: "2026-11-18"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-managed-instances-scale-to-zero/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Lambda now supports scale to and from zero for Lambda Managed Instances

**날짜:** 2026년 11월 18일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-managed-instances-scale-to-zero/

## 내용

AWS Lambda now supports scale to and from zero for Event Functions running on&nbsp;Lambda Managed Instances (LMI). Lambda automatically scales execution environments for your function to zero&nbsp;during idle periods and scales them back up when requests arrive, without requiring you to provision minimum capacity. This makes LMI cost-effective for intermittent workloads such as asynchronous processing, development, and test environments. 
Lambda Managed Instances lets you run Lambda functions on your Amazon EC2 instances while maintaining the operational simplicity of Lambda. With Lambda Managed Instances, you can access specialized compute configurations and drive cost efficiency through EC2 pricing advantages, without managing infrastructure.&nbsp;Previously, customers needed to keep a minimum number of execution environments running even when there was no traffic. With this launch, Lambda scales execution environments for your function to zero after a period with no activity, and provisions them again when requests arrive. This improves cost efficiency for workloads with periods of no traffic. 
This feature is available today in all AWS commercial Regions where Lambda Managed Instances is available. To get started, set&nbsp;MinExecutionEnvironments to zero for your function using the Lambda console, AWS CLI, AWS SDKs, AWS CloudFormation, AWS SAM, or AWS CDK. To learn more, visit the AWS Lambda Developer Guide&nbsp;and AWS Lambda pricing.

## 핵심 요약

요약 미지원
