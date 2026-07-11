---
title: "Amazon EC2 now supports using an EBS volume for Replace Root Volume"
date: "2026-07-11"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-replace-root-volume-ebs-volume/"
tags: ["EC2", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon EC2 now supports using an EBS volume for Replace Root Volume

**날짜:** 2026년 07월 11일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-ec2-replace-root-volume-ebs-volume/

## 내용

Today, AWS announces Replace Root Volume using an existing EBS volume, a new option for replacing the root volume of a running Amazon EC2 instance. Customers can now use an EBS volume as the target for a root volume replacement, in addition to the existing options of replacing from a snapshot or an AMI. This option supports customers running stateful workloads who need to include specific metadata or software on the root volume before the application boots.  Many customers use Replace Root Volume today to apply operating system patches and configuration changes without stopping the instance. However, customers who needed specific metadata or software on the root volume had to first capture an volume with data as a snapshot or register it as an AMI before they could replace the root volume. These intermediate steps added time and operational overhead. Customers can now configure the volume directly and use it as the new root volume, removing the snapshot and AMI creation steps. This reduces operational overhead and speeds up root volume patching for stateful workloads where downtime is costly.  Using an EBS volume when replacing a root volume of an EC2 instance is available in all commercial AWS Regions and AWS GovCloud (US) regions. To get started, see Replace an EC2 instance root volume&nbsp;in the Amazon EC2 User Guide.

## 핵심 요약

요약 미지원
