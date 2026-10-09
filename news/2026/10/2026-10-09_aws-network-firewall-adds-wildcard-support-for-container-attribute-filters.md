---
title: "AWS Network Firewall adds wildcard support for container attribute filters"
date: "2026-10-09"
service: "EKS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-network-firewall-container-attributes-wildcard"
tags: ["EKS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Network Firewall adds wildcard support for container attribute filters

**날짜:** 2026년 10월 09일
**서비스:** EKS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-network-firewall-container-attributes-wildcard

## 내용

AWS Network Firewall now supports wildcard matching in container attribute-based inspection filters for Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon Elastic Container Service (Amazon ECS). This enhancement allows you to define attribute filters using wildcard patterns to match multiple container workloads in a single rule, eliminating the need to create individual container associations for each variant.
With wildcard support, you can use patterns like app=payments-* to automatically cover all variants of an application, such as payments-api, payments-worker, and payments-cron. This simplifies firewall rule management for dynamic container environments where new application variants are frequently deployed, reducing operational overhead and ensuring consistent security coverage across your containerized workloads.&nbsp;
Wildcard support for container attribute filters is available in all AWS Regions where AWS Network Firewall container attribute-based inspection is supported. For a full list of supported Regions, see the AWS Region Table.
To get started, visit AWS Network Firewall product page and service documentation.&nbsp;

## 핵심 요약

요약 미지원
