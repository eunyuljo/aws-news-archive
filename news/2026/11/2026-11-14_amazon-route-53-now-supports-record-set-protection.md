---
title: "Amazon Route 53 now supports record set protection"
date: "2026-11-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-route-53-record-set-protection/"
tags: ["RDS", "2026", "new-region", "performance", "security"]
nav_exclude: true
---

# Amazon Route 53 now supports record set protection

**날짜:** 2026년 11월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-route-53-record-set-protection/

## 내용

Amazon Route 53 now supports record set protection, which helps DNS administrators prevent accidental changes to critical DNS records in their hosted zones. This feature allows you to protect records such as those at the zone apex, MX records, and production endpoints directly in the hosted zone. Any change to a protected record is blocked until the protection is removed by an authorized user.
Previously, to lock specific records, you had to write record-level conditions into the IAM policies of every user and role that could change your hosted zones. When those policies blocked a change, the caller had no indication of whether the record was protected or why. Now you can protect records by name and type directly in the hosted zone. A single protection covers all records with that name and type, including records with different set identifiers; weighted, latency, and other routing policy records are protected together. You can also create a protection proactively before the record exists, preventing records from being created for that name and type. Each protection can include an optional comment of up to 256 characters, allowing you to indicate the reason for the protection. You can manage protections using the Route 53 console, AWS CLI, or AWS SDKs through the CreateResourceRecordSetProtections, DeleteResourceRecordSetProtections, and ListResourceRecordSetProtections API actions. To control who can remove protections, restrict the DeleteResourceRecordSetProtections permission in IAM policies.
Record set protection is available in all AWS commercial Regions where public and private hosted zones are available today. To learn more, see Protecting records from changes in the Amazon Route 53 Developer Guide.

## 핵심 요약

요약 미지원
