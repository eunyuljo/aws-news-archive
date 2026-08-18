---
title: "Amazon OpenSearch Service now supports automatic semantic enrichment for VPC domains"
date: "2026-08-18"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-opensearch-service-vpc/"
tags: ["VPC", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon OpenSearch Service now supports automatic semantic enrichment for VPC domains

**날짜:** 2026년 08월 18일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-opensearch-service-vpc/

## 내용

Amazon OpenSearch Service now extends automatic semantic enrichment to VPC-enabled domains, allowing customers with private network configurations to leverage AI-powered semantic search without exposing their domains to the public internet. 
&nbsp; Automatic semantic enrichment transforms traditional keyword-only search into context-aware retrieval by understanding the meaning behind queries. For example, a search for "lightweight laptop for travel" returns results about "ultrabooks" and "portable notebooks under 3 lbs" even when these exact terms aren't in the query. The feature handles all semantic processing automatically, eliminating the need to self-manage machine learning models and integration overhead. Previously, automatic semantic enrichment was available only on domains that are not VPC-enabled. This capability is now supported within VPCs (Virtual Private Clouds), enabling customers with stricter network security requirements to improve search relevance while maintaining their existing security posture. No changes to existing VPC configurations are required. To learn more about automatic semantic enrichment, see our documentation. 
&nbsp; Automatic semantic enrichment for VPC domains is available across 11 Regions globally: US East (N. Virginia, Ohio), US West (Oregon), Asia Pacific (Mumbai, Singapore, Sydney, Tokyo), and Europe (Frankfurt, Ireland, Spain, Stockholm). To get started, on your VPC-enabled OpenSearch Service domain running OpenSearch version 2.19 or later, create an index with automatic semantic enrichment fields configured. Note that you may need to update your domain to the latest service software version, see updating service software for more information.

## 핵심 요약

요약 미지원
