---
title: "Amazon EMR Serverless now supports IPv6 and dual-stack connectivity"
date: "2026-10-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-emr-serverless/"
tags: ["RDS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon EMR Serverless now supports IPv6 and dual-stack connectivity

**날짜:** 2026년 10월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-emr-serverless/

## 내용

Amazon EMR Serverless now supports IPv6 and dual-stack connectivity, expanding beyond the IPv4-only connectivity that was previously available. You can now run your Apache Spark and Apache Hive jobs over IPv6 in your Amazon Virtual Private Cloud (VPC) by supplying dual-stack (IPv4 and IPv6) or IPv6-only subnets. This gives you greater flexibility in how your applications connect to data stores and services, while maintaining full backward compatibility with your existing IPv4 workloads.
As Spark and Hive workloads scale to many workers, the IPv4 address space in your VPCs and subnets can become a constraint, and a growing number of organizations face compliance mandates that require IPv6 adoption. With dual-stack connectivity, your EMR Serverless applications accept both IPv4 and IPv6, making it easy to adopt IPv6 gradually while maintaining backward compatibility with your existing IPv4 workloads. With IPv6-only subnets, you can eliminate the need for IPv4 addresses entirely, overcoming IPv4 address exhaustion and meeting the networking standards and compliance requirements that call for IPv6, while your jobs reach IPv6 endpoints and services both inside and outside your VPC.
IPv6 and dual-stack connectivity for Amazon EMR Serverless is available at no additional cost in all AWS Regions where Amazon EMR Serverless is available. IPv6 and dual-stack subnets are supported on all EMR Serverless release versions. To get started, see Configure IPv6 subnets for EMR Serverless applications and Configuring VPC access for EMR Serverless applications.

## 핵심 요약

요약 미지원
