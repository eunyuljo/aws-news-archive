---
title: "AWS Storage Gateway now supports FIPS-compliant private connectivity for Tape and Volume Gateway"
date: "2026-08-20"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/storage-gateway-fips-privatelink/"
tags: ["VPC", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Storage Gateway now supports FIPS-compliant private connectivity for Tape and Volume Gateway

**날짜:** 2026년 08월 20일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/storage-gateway-fips-privatelink/

## 내용

AWS Storage Gateway now supports FIPS 140-3 validated endpoints over AWS PrivateLink for Tape Gateway and Volume Gateway. Previously, FIPS endpoints were available only over the public internet. Now you can keep FIPS-compliant traffic on the private AWS network, making it easier to use Storage Gateway for regulated workloads. 
With this launch, your Tape Gateway and Volume Gateway can reach the Storage Gateway service endpoints privately through an interface VPC endpoint in your VPC, while using FIPS validated encryption. To get started, you can create a FIPS interface endpoint for Storage Gateway in your VPC, then choose the FIPS VPC endpoint option when activating your gateway. Once activated, your gateway connects to the Storage Gateway service over FIPS validated endpoint on the private AWS network. To activate a gateway with a FIPS PrivateLink endpoint, your gateway must be running software version 3.2.7 or later. 
This launch is available in the eight AWS Regions where Storage Gateway offers FIPS endpoints: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), and AWS GovCloud (US-West). To learn more, visit the AWS Storage Gateway User Guide or the product page.

## 핵심 요약

요약 미지원
