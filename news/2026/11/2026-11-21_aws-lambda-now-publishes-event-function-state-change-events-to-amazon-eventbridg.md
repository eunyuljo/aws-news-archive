---
title: "AWS Lambda now publishes Event Function state change events to Amazon EventBridge"
date: "2026-11-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-function-state-events/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Lambda now publishes Event Function state change events to Amazon EventBridge

**날짜:** 2026년 11월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-function-state-events/

## 내용

AWS Lambda&nbsp;now publishes Event Function state change events to Amazon EventBridge. Lambda emits an event each time an Event Function version changes state because of a customer action, such as creating, updating, publishing, or deleting a function. These events help platform and DevOps teams to trigger automation as soon as a function becomes ready to invoke, an update finishes, or an operation fails, without polling the&nbsp;GetFunction API. 
Customers use Lambda Event Functions to build APIs, event processing workloads, multi-step workflows, and data pipelines. As organizations grow to thousands of functions, platform teams need to know when a function changes state so they can take the next step. For example, a deployment pipeline can run integration tests and then shift alias traffic once a new version becomes active.&nbsp;Until now, these tools had to poll the GetFunction&nbsp;API to track state changes. Polling consumed API quota, slowed down pipelines, and required custom retry logic, which added operational overhead. With this launch, you can create EventBridge rules&nbsp;that match on fields such as the function ARN, detail type, or state, and route matched events to targets such as AWS Step Functions, AWS Lambda, Amazon SNS, or Amazon SQS. This helps you build reliable, event-driven deployment pipelines across all of your functions, without writing or maintaining custom polling logic. 
This feature is available in all commercial AWS Regions. You can create rules by using the EventBridge console, AWS Command Line Interface (AWS CLI), AWS SDKs, AWS CloudFormation, AWS Cloud Development Kit (AWS CDK), or AWS Serverless Application Model (AWS SAM). Lambda publishes these events automatically at no additional cost. Standard pricing applies to the targets that your EventBridge rules invoke. To learn more, see the AWS Lambda Developer Guide&nbsp;and the Amazon EventBridge User Guide.

## 핵심 요약

요약 미지원
