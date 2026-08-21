---
title: "Amazon Timestream for InfluxDB now supports customer managed keys"
date: "2026-08-21"
service: "KMS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-timestream-influxdb-cmk/"
tags: ["KMS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Timestream for InfluxDB now supports customer managed keys

**날짜:** 2026년 08월 21일
**서비스:** KMS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-timestream-influxdb-cmk/

## 내용

Amazon Timestream for InfluxDB now supports AWS Key Management Service (AWS KMS) customer managed keys for encrypting data at rest in InfluxDB 2 database instances, InfluxDB 2 Read Replicas, and InfluxDB 3 clusters. Customers select a symmetric AWS KMS key when creating a database resource. 
Timestream for InfluxDB uses the selected key to encrypt the underlying database storage for InfluxDB 2 and InfluxDB 3 resources. The key must be in the same AWS account and AWS Region as the database resource. Customers specify the key during resource creation. The key cannot be changed after the resource is created. 
Customer managed key support is available through the AWS Management Console, AWS Command Line Interface (AWS CLI), and Timestream for InfluxDB application programming interface (API). The feature is available in all AWS Regions where Timestream for InfluxDB is available. There is no additional Timestream for InfluxDB charge for using customer managed keys. Standard AWS KMS charges apply.  Support for Customer managed keys is available in all AWS Regions where Amazon Timestream for InfluxDB is available. To get started, open the Amazon Timestream console. For more information, see the Amazon Timestream for InfluxDB documentation and pricing page.

## 핵심 요약

요약 미지원
