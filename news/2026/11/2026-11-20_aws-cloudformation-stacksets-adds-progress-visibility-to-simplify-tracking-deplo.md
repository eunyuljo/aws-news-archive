---
title: "AWS CloudFormation StackSets adds progress visibility to simplify tracking deployments at scale"
date: "2026-11-20"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-stacksets-progress/"
tags: ["CloudFormation", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS CloudFormation StackSets adds progress visibility to simplify tracking deployments at scale

**날짜:** 2026년 11월 20일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-stacksets-progress/

## 내용

AWS CloudFormation StackSets now shows stage-by-stage progress for deployments across accounts and AWS Regions, whether you target tens of accounts or thousands. You can follow each deployment as it progresses and take action when needed, without waiting for it to finish. StackSets lets you consistently apply the same infrastructure or application components, such as networking and security settings, across many accounts and Regions in one operation. With this launch, you can see how many stack instances are deployed, how many remain, and which ones need attention. This gives you confidence that a rollout is on track at every stage. 
Stage-level progress gives you a clear, detailed view of where each deployment stands. Previously, a StackSets deployment showed an overall status while it ran. Now, StackSets also reports progress for two stages. The first is role provisioning, which prepares access in each target account of a service-managed stack set. The second is stack deployment, which deploys your template as a stack instance in each account and Region. For example, in a deployment to 2,000 accounts in 3 Regions, you can see that role provisioning is complete and stack deployment has reached 40 percent, with 2,400 stack instances completed and 3,600 pending. Progress for each Region and the result of each stage remain available after the deployment completes. 
To get started, open the Progress view for a stack set operation in the CloudFormation console, or use the AWS CLI or AWS SDKs. Existing integrations continue to work without changes. Visit the StackSets documentation to learn more. 
Deployment progress is available at no additional charge in all AWS Regions where CloudFormation StackSets is supported. Refer to the AWS Region table for service availability details.

## 핵심 요약

요약 미지원
