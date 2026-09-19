---
title: "AWS PrivateLink announces Tunnel Endpoints to access network segments"
date: "2026-09-19"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint/"
tags: ["VPC", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS PrivateLink announces Tunnel Endpoints to access network segments

**날짜:** 2026년 09월 19일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/9/privatelink-tunnel-endpoint/

## 내용

AWS PrivateLink customers can now use VPC endpoint to privately and securely access network segments in another VPC/account. They can use a ‘tunnel’ endpoint, a new type of VPC endpoint, to tunnel into the network segment and access resources located within it. 
AWS PrivateLink is a highly available and scalable technology that enables private access across VPC and account boundaries to load balanced services, appliances, and resources such as databases and domains. Prior to this launch, customers who wanted to share their resources with another party such as an external vendor had to do it one at a time by creating a Resource Configuration for every resource. Now, customers can create a Resource Configuration to represent a CIDR range in their network, and share it with a vendor via AWS Resource Access Manager (RAM). The vendor can then create a tunnel endpoint and use GENEVE encapsulation to tunnel through it into the customer’s VPC to access resources located in CIDR range specified by the customer. There is an hourly charge for the tunnel endpoint and a per-GB charge for data processed through it. Please refer to the pricing page for AWS PrivateLink. &nbsp;  The capability is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Jakarta), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Asia Pacific (Mumbai), Asia Pacific (Osaka), Asia Pacific (Seoul), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Canada West (Calgary), Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm), Europe (Zurich), Mexico (Central), South America (São Paulo). 
To learn more about this capability and get started, please refer to the AWS PrivateLink documentation.

## 핵심 요약

요약 미지원
