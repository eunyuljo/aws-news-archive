---
title: "Amazon Cognito now supports multi-Region replication"
date: "2026-06-17"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cognito-multi-region/"
tags: ["Config", "2026", "new-region"]
nav_exclude: true
---

# Amazon Cognito now supports multi-Region replication

**날짜:** 2026년 06월 17일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-cognito-multi-region/

## 내용

Amazon Cognito now supports multi-Region replication, enabling you to synchronize user and machine identity data — including credentials, user pool configurations, and federation setups — to a secondary user pool in a standby Region you designate in near real-time. This capability helps you improve the resilience of your authentication system by providing a standby replica that can accept traffic in case there is a regional service disruption. In the event of a disruption in the primary Region, you can redirect traffic to the secondary user pool. Signed-in users continue accessing their applications without re-authenticating, and registered users can sign in with their existing credentials. Authentication methods continue to work in the secondary Region, including username/password, federation with social identity and SAML/OIDC providers, and machine-to-machine authorization flows. Multi-Region replication is available as an add-on for user pools in Essentials or Plus feature tiers. You can start using this feature in the following AWS Regions: US East (Ohio, N. Virginia), US West (N. California, Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney, Tokyo), Canada (Central), Europe (Frankfurt, Ireland, London, Paris, Stockholm), and South America (São Paulo). To get started, configure multi-Region replication using the AWS Management Console, AWS Command Line Interface (CLI), or AWS Software Development Kits (SDKs) by adding a replica user pool. Visit the&nbsp;pricing page&nbsp;for pricing details and the&nbsp;developer guide&nbsp;for instructions.

## 핵심 요약

요약 미지원
