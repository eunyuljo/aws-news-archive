---
title: "AWS Storage Gateway now supports FIPS-compliant private connectivity for Amazon S3 File Gateway"
date: "2026-09-11"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/storage-gateway-fips-privatelink-s3/"
tags: ["S3", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS Storage Gateway now supports FIPS-compliant private connectivity for Amazon S3 File Gateway

**날짜:** 2026년 09월 11일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/storage-gateway-fips-privatelink-s3/

## 내용

AWS Storage Gateway now supports FIPS 140-3 validated endpoints over AWS PrivateLink for Amazon S3 File Gateway. Previously, FIPS endpoints for File Gateway were available only over the public internet. Now you can keep FIPS-compliant traffic on the private AWS network, making it easier to use Storage Gateway for regulated workloads. 
With this launch, your File Gateway can reach the Storage Gateway service endpoints privately through a FIPS interface VPC endpoint in your VPC. You can also create NFS and SMB file shares that reach Amazon S3 through an S3 FIPS interface endpoint, enabling FIPS-compliant private connectivity for your end-to-end file transfer workloads. To get started, create FIPS interface endpoints for Storage Gateway and Amazon S3 in your VPC, then choose the FIPS VPC endpoint option when activating your gateway and configuring your file shares. To activate a gateway with a FIPS PrivateLink endpoint, your gateway must be running software version 2.1.10 or later. 
This launch is available in the eight AWS Regions where Storage Gateway offers FIPS endpoints: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Canada (Central), Canada West (Calgary), AWS GovCloud (US-East), and AWS GovCloud (US-West). To learn more, visit the AWS Storage Gateway User Guide or the product page.

## 핵심 요약

요약 미지원
