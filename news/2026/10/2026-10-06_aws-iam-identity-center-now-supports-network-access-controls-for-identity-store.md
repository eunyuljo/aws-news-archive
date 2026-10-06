---
title: "AWS IAM Identity Center now supports network access controls for Identity Store"
date: "2026-10-06"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-network-controls/"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS IAM Identity Center now supports network access controls for Identity Store

**날짜:** 2026년 10월 06일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-identity-store-network-controls/

## 내용

AWS IAM Identity Center helps you configure the single sign-on experience for your workforce to AWS accounts and applications. IAM Identity Center now supports network access controls for Identity Store, which stores your users and groups. You can restrict access to the Identity Store API and the SCIM API based on the network that requests originate from. Your custom applications and user provisioning workflows use the Identity Store API to manage and look up users and groups, and your external identity provider uses the SCIM API to synchronize users and groups.
For the Identity Store API, you can require that requests arrive only through allowed VPC endpoints in your account or organization, or from specific source VPCs. For both APIs, you can allow requests only from specific IP ranges. Within the same configuration, you can apply different restrictions to each API. For example, you can require that Identity Store API requests arrive only through VPC endpoints, while allowing SCIM requests from your external identity provider's published IP ranges.
Network access controls are optional and turned off by default. Requests that AWS services make on your behalf are exempt. You configure network access controls by using the Identity Store API through the AWS SDKs and AWS CLI. This capability is available in all AWS Regions where IAM Identity Center is offered.
To learn more about IAM Identity Center, visit the product detail page. To get started with network access controls, see the Identity Store API Reference.

## 핵심 요약

요약 미지원
