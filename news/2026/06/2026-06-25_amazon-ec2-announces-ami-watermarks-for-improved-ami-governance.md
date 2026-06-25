---
title: "Amazon EC2 announces AMI Watermarks for improved AMI governance"
date: "2026-06-25"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-image-watermarks-allowed-images"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EC2 announces AMI Watermarks for improved AMI governance

**날짜:** 2026년 06월 25일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/ec2-image-watermarks-allowed-images

## 내용

Amazon EC2 introduces AMI watermarks, letting you embed custom identifiers in your private AMIs. Once applied, a watermark automatically carries forward to every AMI derived from the original, whether you copy it across regions or create a new AMI from a running instance. Watermarks also remain visible when you share an AMI with other accounts. This helps you identify trusted AMIs, track provenance, and enforce governance policies across your organization.  Each watermark includes metadata such as the AMI ID, owner ID, region, and creation timestamps, providing reliable provenance that persists regardless of how many times an AMI is copied or new AMIs are created from it. AMI Watermarks improve AMI tracking by enabling you to filter and find related AMIs across your accounts. For governance, you can combine watermarks with Allowed AMIs&nbsp;to restrict instance launches to only AMIs carrying approved watermarks and enforce the setting at scale across your organization through Declarative Policies.  You can start adding AMI watermarks to your private AMIs by using the AWS Management Console, AWS CLI, or SDKs. To learn more, please visit the documentation.&nbsp;You can also attach watermarks through EC2 Image Builder, a service used to create and manage AMIs, as part of your AMI build pipeline.  AMI watermarks are available to all customers at no additional cost in all AWS regions including AWS China (Beijing) Region, operated by Sinnet, and AWS China (Ningxia) Region, operated by NWCD, and AWS GovCloud (US) Regions.&nbsp;

## 핵심 요약

요약 미지원
