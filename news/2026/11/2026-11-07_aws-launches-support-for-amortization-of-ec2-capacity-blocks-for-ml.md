---
title: "AWS launches support for amortization of EC2 Capacity Blocks for ML"
date: "2026-11-07"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ec2-capacity-blocks-ml/"
tags: ["EC2", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS launches support for amortization of EC2 Capacity Blocks for ML

**날짜:** 2026년 11월 07일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-ec2-capacity-blocks-ml/

## 내용

AWS Data Exports for Cost and Usage Report (CUR) 2.0 and AWS Cost Explorer now amortize the upfront fee for Amazon EC2 Capacity Blocks for ML across the duration of each reservation. You can see the amortized cost of each instance launched into a Capacity Block and the amortized cost of unused capacity, so you can attribute your upfront fee to the workloads that used it and identify capacity that went unused. 
Previously, a Capacity Block's upfront fee appeared as a single charge on the purchase date, making it difficult to see how that cost was spread across usage over the reservation. Now the amortized cost appears alongside your instance usage, so you can allocate GPU costs to the teams, projects, and applications that ran on the reserved capacity. You can also see what share of your reservation went unused and plan future Capacity Block purchases. In CUR 2.0, the amortized costs appear in the reservation_amortized_upfront_fee_for_billing_period, reservation_effective_cost columns, and reservation_net_effective_cost shows the amortized cost after discounts. In Cost Explorer, select the amortized cost view to see Capacity Block costs allocated for&nbsp;the reservation. 
&nbsp;Amortization for Capacity Blocks is available at no additional charge in all AWS Regions except the AWS GovCloud (US) Regions and the China Regions. To learn more, see the CUR 2.0 data dictionary and exploring your data using Cost Explorer.

## 핵심 요약

요약 미지원
