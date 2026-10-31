---
title: "Amazon MSK now supports TLS 1.3 for data in transit"
date: "2026-10-31"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-tls/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon MSK now supports TLS 1.3 for data in transit

**날짜:** 2026년 10월 31일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-msk-tls/

## 내용

Amazon MSK now supports version 1.3 of Transport Layer Security (TLS) protocol for MSK Provisioned clusters through encryption policies. TLS 1.3 delivers faster, more secure encryption for streaming data and is increasingly required by compliance frameworks and enterprise security standards. It is also one of the prerequisites for post-quantum cryptography for protecting data against attacks that collect encrypted traffic now with the intent to decrypt it later. 
Customers can opt in to TLS 1.3 by selecting a named security policy in their MSK cluster configuration, with no change to existing clusters until a policy is applied. A named security policy defines which TLS version and cipher suites a cluster can accept. With this launch, Amazon MSK provides a set of policies customers can select and any connection that does not meet the selected policy requirements is rejected. This allows customers to stay in control of their security and compliance posture. Policies that support both TLS 1.2 and TLS 1.3 allow connections to negotiate the highest version the client supports allowing clients that support TLS 1.3 to connect on it immediately while clients on TLS 1.2 continue to connect on TLS 1.2. This lets customers upgrade their clients at their pace before applying a stricter policy. Customers can also select stricter policies that align closer with their compliance requirements to restrict connections to TLS 1.3 only. 
This capability is available at no additional cost in all AWS Regions where Amazon MSK Provisioned is available. To learn more, see the Amazon MSK documentation.

## 핵심 요약

요약 미지원
