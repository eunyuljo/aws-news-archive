---
title: "AWS Marketplace Metering Service now supports decimal usage quantities"
date: "2026-11-17"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-marketplace-metering-service-decimal-usage-quantities/"
tags: ["General", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Marketplace Metering Service now supports decimal usage quantities

**날짜:** 2026년 11월 17일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-marketplace-metering-service-decimal-usage-quantities/

## 내용

AWS Marketplace Metering Service now supports decimal usage quantities in the MeterUsage and BatchMeterUsage APIs. Previously, AWS Marketplace sellers reported usage to both APIs in whole numbers, and now they can report usage with up to six decimal places. 
Sellers can price and meter in the units that match how customers consume their product, for example reporting 1.5 terabytes (TB) of storage instead of 1 or 2 TB. To report decimal quantities, sellers use the new UsageQuantityAsDecimal parameter in MeterUsage and QuantityAsDecimal parameter in BatchMeterUsage, and existing integrations that report whole numbers continue to work without changes. Usage allocations, which split reported usage into buckets by tags, also support decimal quantities with the new AllocatedUsageQuantityAsDecimal parameter. 
This new feature is available in all AWS Regions where AWS Marketplace Metering Service is available. To learn more, see MeterUsage and BatchMeterUsage in the AWS Marketplace API Reference.

## 핵심 요약

요약 미지원
