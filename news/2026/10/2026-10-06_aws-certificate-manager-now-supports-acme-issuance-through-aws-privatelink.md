---
title: "AWS Certificate Manager now supports ACME issuance through AWS PrivateLink"
date: "2026-10-06"
service: "CloudWatch"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/AWS-Certificate-Manager-ACME-Privatelink"
tags: ["CloudWatch", "2026", "new-region"]
nav_exclude: true
---

# AWS Certificate Manager now supports ACME issuance through AWS PrivateLink

**날짜:** 2026년 10월 06일
**서비스:** CloudWatch
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/AWS-Certificate-Manager-ACME-Privatelink

## 내용

AWS Certificate Manager (ACM) now supports AWS PrivateLink for ACME public certificate issuance, allowing you to request and renew public TLS certificates over a private network path that stays within the AWS network. You can now create a VPC interface endpoint to the ACM ACME service and route issuance traffic from any ACMEv2-compatible client through your VPC.
If you're already using ACME with ACM, setup requires no changes to your ACME clients. After you create your managed ACME endpoint in ACM, you create a standard VPC interface endpoint using the VPC console, AWS CLI, or AWS CloudFormation. Private DNS resolves your existing ACME directory URL to the interface endpoint inside your VPC automatically, so the same client configuration and directory URL continue to work with no reconfiguration. Issuance operations—account creation, order creation, domain validation, finalization, and certificate retrieval—then flow over PrivateLink. All activity remains visible in the ACM console with AWS CloudTrail logging and Amazon CloudWatch metrics for auditability.
AWS PrivateLink support for ACME certificate issuance is available in all commercial AWS Regions. Standard AWS PrivateLink charges apply for interface endpoints; see the AWS PrivateLink pricing page. For ACM pricing details, see the &nbsp;ACM pricing page. To get started with ACME and PrivateLink, visit the &nbsp;AWS News blog post&nbsp;&nbsp;or read the&nbsp;documentation.

## 핵심 요약

요약 미지원
