---
title: "AWS announces Networking Flexible Cost Allocation for Amazon VPC"
date: "2026-11-17"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/networking-flexible-cost-allocation/"
tags: ["EC2", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS announces Networking Flexible Cost Allocation for Amazon VPC

**날짜:** 2026년 11월 17일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/networking-flexible-cost-allocation/

## 내용

Amazon Virtual Private Cloud (VPC) now supports Networking Flexible Cost Allocation (FCA), which splits shared networking costs by the resources that actually drive them, so you can see what each team or application used. Until now, AWS Cost and Usage Report (CUR), including CUR 2.0 in AWS Data Exports, showed networking usage as a single item, and most customers split it across teams with custom scripts and manual estimates. FCA splits this line item by the resources that generated it. It supports NAT gateway data processing and data transfer, including traffic to the internet, and in-Region Amazon Elastic Compute Cloud (Amazon EC2) and VPC peering data transfer.
Today, when several teams share a resource such as a NAT gateway, the account that owns it pays the full cost and can't see which team or application drove it. To work around this, some customers built custom scripts to analyze VPC Flow Logs, which takes ongoing engineering effort. Others used fixed-percentage splits, which overcharge some teams and undercharge others. FCA breaks down usage based on traffic sources, helping you accurately track financial metrics based on applications and teams. To get started, attach a cost allocation policy to a NAT gateway, VPC peering connection, or Amazon EC2 instance, then select Networking flexible cost allocation under split cost allocation data in the AWS Billing and Cost Management console. Allocated line items appear in your CUR within 24 hours. FCA changes only how costs are shown in your reports. Your bill and total charges stay the same.
FCA is available at no additional charge. It's supported in all AWS commercial Regions except Middle East (Bahrain) and Middle East (UAE). It's also available in the China Regions. It is not available in the AWS GovCloud (US) Regions. To learn more, visit the Networking FCA product page.

## 핵심 요약

요약 미지원
