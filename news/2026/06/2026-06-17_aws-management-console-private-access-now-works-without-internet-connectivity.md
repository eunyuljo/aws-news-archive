---
title: "AWS Management Console Private Access now works without internet connectivity"
date: "2026-06-17"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-management-console-private/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Management Console Private Access now works without internet connectivity

**날짜:** 2026년 06월 17일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-management-console-private/

## 내용

AWS Management Console Private Access now enables customers to access the AWS Console from VPCs without internet connectivity, allowing enterprises to manage their AWS infrastructure through the console while maintaining strict network security controls in air-gapped environments.  Previously, AWS Management Console Private Access allowed customers to restrict console access to authorized AWS accounts and corporate networks but still required internet connectivity. With this launch, AWS Console traffic can flow through VPC endpoints for the supported service consoles, eliminating the need for any internet access.&nbsp;This capability is particularly valuable for customers in regulated industries such as financial services, government and defense, and healthcare, and for enterprises with strict security requirements who need to access sensitive data only from controlled environments and use the console in classified or networks without internet connectivity.  AWS Management Console Private Access uses AWS PrivateLink to establish secure network paths between customer VPCs and the console. Customers can apply VPC endpoint policies to restrict access to specific AWS accounts and organizations, and use IAM, Service Control, and Resource Control policies to require that employees access resources only from authorized networks. 
This capability is available in all AWS commercial regions. You pay only for the underlying AWS PrivateLink VPC endpoint usage and data processing. To get started and learn about the supported services, visit the Management Console Private Access documentation.

## 핵심 요약

요약 미지원
