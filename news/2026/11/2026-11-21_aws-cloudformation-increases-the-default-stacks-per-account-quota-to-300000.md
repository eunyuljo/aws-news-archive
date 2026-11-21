---
title: "AWS CloudFormation increases the default stacks per account quota to 300,000"
date: "2026-11-21"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-stacks-per-account-quota/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# AWS CloudFormation increases the default stacks per account quota to 300,000

**날짜:** 2026년 11월 21일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudformation-stacks-per-account-quota/

## 내용

AWS CloudFormation now supports up to 300,000 stacks in each AWS account and Region by default (previously 2,000), which enables you to add stacks as your workloads grow without requesting a quota increase. CloudFormation manages related AWS resources as a stack that you create, update, and delete as one unit. Teams that deploy a separate stack for each customer, environment, or developer can now scale those patterns within a single account. 
A higher default quota allows you to keep growing workloads in the accounts where they already run. Previously, accounts that needed more than 2,000 stacks in a Region requested a quota increase through Service Quotas. Now, the default quota covers these workloads without a request. For example, a software provider that deploys one stack for each customer can grow from 2,000 to 300,000 customer stacks in one account and Region. Existing stacks work without changes. 
The higher quota applies to stacks you create in the CloudFormation console or with the AWS CLI, AWS SDKs, AWS CDK, or AWS SAM. To view your stacks per account quota, open the Service Quotas console. For more information, see CloudFormation quotas in the AWS CloudFormation User Guide. The increased quota is available at no additional charge in all AWS Regions where AWS CloudFormation is supported. For Region availability, see the AWS Region table.

## 핵심 요약

요약 미지원
