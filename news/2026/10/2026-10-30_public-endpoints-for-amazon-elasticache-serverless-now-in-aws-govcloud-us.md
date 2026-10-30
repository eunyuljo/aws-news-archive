---
title: "Public endpoints for Amazon ElastiCache Serverless now in AWS GovCloud (US)"
date: "2026-10-30"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-serverless-public-endpoints-govcloud/"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Public endpoints for Amazon ElastiCache Serverless now in AWS GovCloud (US)

**날짜:** 2026년 10월 30일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-elasticache-serverless-public-endpoints-govcloud/

## 내용

Amazon ElastiCache Serverless for Valkey now supports public endpoints in the AWS GovCloud (US) Regions. A public endpoint lets you connect to your cache from a serverless function or any application running outside a VPC, without setting up a VPN, a bastion host, or an SSH tunnel. 
With a public endpoint, ElastiCache Serverless gives you a fully managed cache with no VPC to configure and no infrastructure to provision, and you can create one in under a minute. Every connection uses IAM authentication over TLS 1.3, so there's no password to store or rotate. Connect using Valkey GLIDE 2.2 or later, which has built-in IAM support, or another Valkey client paired with the Developer Toolkit for ElastiCache, an open-source library that generates and refreshes IAM authentication tokens for you. 
With this expansion, public endpoints for ElastiCache Serverless are now available in all commercial AWS Regions, the AWS GovCloud (US) Regions, and the China Regions. There is no additional charge for using public endpoints beyond standard ElastiCache Serverless pricing. 
To get started, create a Valkey 9.0 or later serverless cache with a public endpoint using the AWS Management Console, AWS SDK, or AWS CLI. To learn more about public endpoints, see Create a Valkey serverless cache with a public endpoint.&nbsp;

## 핵심 요약

요약 미지원
