---
title: "Amazon MSK now supports configuring custom domain names for MSK Provisioned clusters"
date: "2026-08-18"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/17/amazon-msk-custom-domain-names/"
tags: ["Config", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon MSK now supports configuring custom domain names for MSK Provisioned clusters

**날짜:** 2026년 08월 18일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/17/amazon-msk-custom-domain-names/

## 내용

You can now easily configure custom domain names on Amazon MSK Provisioned clusters, on either ZooKeeper or KRaft mode for metadata management. This capability helps client applications maintain the same connection endpoints, simplifying cluster migrations, disaster recovery failovers, and scaling operations without reconfiguration. 
Previously, customers configured custom domain names manually on each broker. Additionally, on KRaft-based clusters, customers could not configure custom domain names. With this launch, you can now easily define a custom domain once at the cluster level, and Amazon MSK automatically applies it to every broker in the cluster, eliminating the need to configure each broker individually. The configuration persists through scaling operations and works identically on both ZooKeeper and KRaft-based clusters. This is particularly useful for customers who route traffic through Network Load Balancers, require persistent endpoints across cluster operations, or must adhere to organizational naming conventions for security and compliance. 
You can configure custom domain names on all new and existing MSK Provisioned clusters, in all AWS Regions where Amazon MSK Provisioned is available, at no additional cost. To learn more, see the Amazon MSK Developer Guide.

## 핵심 요약

요약 미지원
