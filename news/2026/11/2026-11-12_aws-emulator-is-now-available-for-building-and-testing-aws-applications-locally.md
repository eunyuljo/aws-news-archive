---
title: "AWS Emulator is now available for building and testing AWS applications locally"
date: "2026-11-12"
service: "DynamoDB"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-emulator-now-available/"
tags: ["DynamoDB", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Emulator is now available for building and testing AWS applications locally

**날짜:** 2026년 11월 12일
**서비스:** DynamoDB
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-emulator-now-available/

## 내용

AWS Emulator is now available for building and testing AWS applications locally. 
Starting today, you can use AWS Emulator to build and test AWS applications on your computer or in your continuous integration (CI) environment. Your existing AWS SDK and CLI calls go to AWS Emulator and come back in milliseconds, so you and your coding agents can find and fix errors locally, with no deployments or AWS account required. 
You create and manage resources with the same AWS SDK and AWS CLI calls you use with AWS, signed with credentials the emulator provides. For the operations it supports, AWS Emulator returns the same result as AWS for valid calls and the same errors for invalid ones. Operations it doesn’t yet support return 501 Not Implemented.&nbsp;AWS Emulator keeps the state of your resources in memory until you stop it. Each copy you start gets its own port, keys and in-memory state, so agents, test suites, and CI jobs never see each other’s resources. For example, a coding agent can create an Amazon DynamoDB table, test against it offline, and fix its code before it deploys. 
Services in AWS Emulator are generated from the API models AWS publishes, the same models behind the AWS SDKs. When AWS adds a service or API, it shows up in AWS Emulator, and its behavior is filled in and verified release by release. To see how its responses compare to AWS, review the AWS Emulator fidelity report. 
AWS Emulator doesn’t depend on an AWS Region. AWS Emulator has no additional service fee. You pay only for AWS resources when you deploy to AWS. Its source code is published under the CC0 1.0 Universal public domain dedication. To get started, see the AWS Emulator documentation, or view the source in the AWS Emulator GitHub repository.

## 핵심 요약

요약 미지원
