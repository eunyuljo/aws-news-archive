---
title: "AWS Lambda Managed Instances now supports Tag Propagation for Managed Resources"
date: "2026-06-17"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-managed-instances-tag-propagation/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Lambda Managed Instances now supports Tag Propagation for Managed Resources

**날짜:** 2026년 06월 17일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-managed-instances-tag-propagation/

## 내용

AWS Lambda Managed Instances (LMI) now supports tag propagation, enabling you to automatically apply tags to managed resources such as Amazon EC2 instances, Amazon EBS volumes, and Amazon ENIs. This helps you enforce cost allocation, service control policies (SCPs), and compliance requirements across all resources provisioned by your capacity providers. 
LMI lets you run Lambda functions on managed EC2 instances with built-in routing, load balancing, and auto scaling, giving you access to specialized compute configurations including the latest-generation processors and high-bandwidth networking, with no operational overhead. Organizations that use resource tagging for cost tracking, governance, or security previously had no way to propagate tags to the underlying managed resources that LMI provisions on their behalf. This made it difficult to track costs accurately, enforce SCPs, or meet compliance standards that require approved tags on all resources. Now, with tag propagation, you can specify a set of tags on your capacity provider configuration, and LMI automatically applies those tags to all managed resources it creates. This ensures consistent tagging across your EC2 instances, EBS volumes, and ENIs without requiring manual intervention or custom automation. 
This feature is available in all AWS commercial Regions where LMI is generally available. To get started, configure the PropagateTags setting on your capacity provider using the CreateCapacityProvider or UpdateCapacityProvider APIs. Set the mode to Explicit and provide your desired tags as key-value pairs. Tag propagation applies to all new managed resources provisioned after the configuration is applied. You can configure these settings using the AWS Management Console, AWS CLI, AWS CloudFormation, AWS CDK, or AWS SAM. To learn more, visit the AWS Lambda Managed Instances product page and documentation.

## 핵심 요약

요약 미지원
