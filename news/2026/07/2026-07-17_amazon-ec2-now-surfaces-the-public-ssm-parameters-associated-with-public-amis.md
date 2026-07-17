---
title: "Amazon EC2 now surfaces the public SSM parameters associated with public AMIs"
date: "2026-07-17"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-public-images-ssm-parameters"
tags: ["EC2", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EC2 now surfaces the public SSM parameters associated with public AMIs

**날짜:** 2026년 07월 17일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/ec2-public-images-ssm-parameters

## 내용

Amazon EC2 now surfaces the AWS Systems Manager (SSM) Parameter Store parameters associated with public AMIs directly in the AMI metadata. When you describe a public AMI, the response includes the associated public SSM parameter,&nbsp;making it easy to discover and reference in your configurations. 
Previously, finding the SSM parameter associated with a public AMI required searching through SSM parameter namespaces manually. Now, when you describe a public AMI, the response includes the public SSM parameter it is associated with. This allows you to discover the SSM parameter for a public AMI easily and use it as an alias that always resolves to the latest version, simplifying AMI updates across your infrastructure.  This capability is available to all customers at no additional cost in all AWS regions including AWS China (Beijing) Region, operated by Sinnet, and AWS China (Ningxia) Region, operated by NWCD, and AWS GovCloud (US) Regions. To learn more, please visit the documentation.

## 핵심 요약

요약 미지원
