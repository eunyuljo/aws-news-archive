---
title: "Selectively log network activity events by identity in AWS CloudTrail"
date: "2026-07-21"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/"
tags: ["IAM", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Selectively log network activity events by identity in AWS CloudTrail

**날짜:** 2026년 07월 21일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-cloudtrail-filter-useridentity-advance-selectors/

## 내용

Today, AWS launches enhanced event filtering for network activity events for VPC end points, a CloudTrail event type that captures actions transmitted through a&nbsp;Virtual Private Cloud Endpoint.&nbsp;Customers can now control which network activity events are logged based on the IAM user identity making the API call. For example, you can configure selectors to log only access denied events when the calling user identity is not on a known safe list. This lets you capture unauthorized access attempts while excluding routine traffic from trusted identities, reducing both logging costs and noise. 
With UserIdentity filtering, customers building a data perimeter strategy can focus on network activity event logging for scenarios that matter most in security. You can configure selectors to log only VpceAccessDenied events from identities outside a trusted set of IAM roles. This enables detection of potential data exfiltration attempts through VPC endpoints without the cost of logging every successful API call from approved principals. You can combine UserIdentity conditions with existing fields like eventName or vpcEndpointId for fine-grained control over what gets recorded. 
You can use this feature via the AWS Management Console, AWS Command Line Interface, and AWS SDKs. This feature is available in all AWS Regions where CloudTrail network activity events are supported. To learn more about Network Activity events, visit the AWS CloudTrail user guide or read AWS Blog on how to enable Network Activity Events. 
&nbsp;

## 핵심 요약

요약 미지원
