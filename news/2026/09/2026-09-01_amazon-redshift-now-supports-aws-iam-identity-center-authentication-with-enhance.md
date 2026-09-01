---
title: "Amazon Redshift now supports AWS IAM Identity Center authentication with enhanced VPC routing"
date: "2026-09-01"
service: "IAM"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr"
tags: ["IAM", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon Redshift now supports AWS IAM Identity Center authentication with enhanced VPC routing

**날짜:** 2026년 09월 01일
**서비스:** IAM
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-idc-evr

## 내용

Amazon Redshift now supports AWS IAM Identity Center authentication for provisioned clusters and serverless workgroups configured with enhanced VPC routing (EVR). You can access Amazon Redshift with single sign-on with your corporate credentials, and the traffic traverses Amazon Virtual Private Cloud (Amazon VPC) and stays on the AWS network. This is valuable for customers with data residency, regulatory, or network-isolation requirements that mandate no public internet egress for analytics. 
With Redshift EVR, all traffic between your Redshift warehouse and other AWS services goes through your VPC, where you can govern it with security groups, network ACLs, and endpoint policies, and observe it in VPC Flow Logs. With this launch, Redshift validates and exchanges IAM Identity Center tokens over AWS PrivateLink interface VPC endpoints from inside your VPC, so authentication and authorization follows the same governed network path as the rest of your Redshift traffic. This feature also supports IAM Identity Center multi-Region replication for customers running Redshift in a different Region than their primary Identity Center instance. 
Read the Amazon Redshift enhanced VPC routing documentation and the blog post&nbsp;to get started. This capability is available in all AWS Regions where both Amazon Redshift and IAM Identity Center are available.&nbsp;

## 핵심 요약

요약 미지원
