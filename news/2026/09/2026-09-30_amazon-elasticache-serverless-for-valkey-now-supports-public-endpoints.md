---
title: "Amazon ElastiCache Serverless for Valkey now supports public endpoints"
date: "2026-09-30"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-serverless-public-endpoints/"
tags: ["IAM", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon ElastiCache Serverless for Valkey now supports public endpoints

**날짜:** 2026년 09월 30일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-elasticache-serverless-public-endpoints/

## 내용

Amazon ElastiCache Serverless for Valkey now supports public endpoints, letting you connect to your cache directly from a laptop, a serverless function, or any application running outside AWS, without setting up a VPN, a bastion host, or an SSH tunnel.
With a public endpoint, ElastiCache Serverless gives you a fully managed cache reachable over the internet, with no VPC to configure and no infrastructure to provision, and you can create one in under a minute. Use it to rapidly prototype, connect AI coding tools and agents straight to your cache, or add caching to workloads that can't reach a VPC. Every connection uses IAM authentication over TLS 1.3, so there's no password to store or rotate.&nbsp;Connect using Valkey GLIDE 2.2 or later, which has built-in IAM support, or another Valkey client paired with the Developer Toolkit for ElastiCache, an open-source library that generates and refreshes IAM authentication tokens for you.
Public endpoints for ElastiCache Serverless are available in all commercial AWS Regions and the China Regions. There is no additional charge for using public endpoints beyond standard ElastiCache Serverless pricing.&nbsp;To get started, create a Valkey 9.0 or later serverless cache with a public endpoint using the AWS Management Console, AWS SDK, or AWS CLI. To learn more about public endpoints, see Create a Valkey serverless cache with a public endpoint.

## 핵심 요약

요약 미지원
