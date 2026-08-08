---
title: "Amazon OpenSearch UI now supports Network Access Control"
date: "2026-08-08"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-ui-network-access-control"
tags: ["IAM", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon OpenSearch UI now supports Network Access Control

**날짜:** 2026년 08월 08일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/opensearch-ui-network-access-control

## 내용

Amazon OpenSearch Service now supports network access controls for OpenSearch UI applications. OpenSearch UI is the fully managed web service for search, analytics, and unified observability across multiple AWS data sources. With network access controls, you can restrict access to your OpenSearch UI applications to approved networks using the same IAM condition keys (aws:SourceVpce, aws:SourceVpc, and aws:SourceIp) that you already use elsewhere in AWS, helping you establish a consistent data perimeter across your environment. 
You can enforce network restrictions at three levels: identity-based policies for specific principals, VPC endpoint policies to control which applications users reach through an endpoint, and resource control policies (RCPs) to enforce access uniformly across every account in your AWS organization. With RCPs, you can block off-network users before they authenticate, preventing anyone outside your corporate network or VPC from reaching the login page. 
Network access controls are available in all AWS Regions where OpenSearch UI is available. To learn more, see Restricting network access to OpenSearch UI applications in the Amazon OpenSearch Service Developer Guide. For more information about Amazon OpenSearch Service, see the Amazon OpenSearch Service product page.

## 핵심 요약

요약 미지원
