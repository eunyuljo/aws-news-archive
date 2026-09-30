---
title: "AWS DataSync now supports shared VPCs"
date: "2026-09-30"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-datasync-shared-vpcs/"
tags: ["VPC", "2026", "GA", "new-region"]
nav_exclude: true
---

# AWS DataSync now supports shared VPCs

**날짜:** 2026년 09월 30일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-datasync-shared-vpcs/

## 내용

AWS DataSync now supports shared Virtual Private Clouds (VPCs). You can create DataSync agents and run transfer tasks using subnets shared across AWS accounts with AWS Resource Access Manager (RAM). It allows you to transfer data privately over a shared subnet and VPC endpoint managed in a central account, rather than one per account.
Customers that centralize their networking previously had to create a separate DataSync VPC endpoint in every account that connected privately through AWS PrivateLink. Each endpoint consumed IP addresses and added operational overhead to maintain across accounts. With shared VPC support, a single endpoint in the account that owns the VPC serves every account the subnet is shared with, conserving IP address space and removing the need for a per-account endpoint. This launch also helps within a single account setup. You can now use one VPC endpoint across multiple subnets, removing the earlier requirement for a matching VPC endpoint in each subnet.
Shared VPC is supported for both Enhanced mode and Basic mode agent-based tasks. To get started, create a DataSync agent using the console or the CreateAgent API and specify a subnet shared with your account via AWS RAM. AWS DataSync support for Shared VPCs is available in all AWS Regions, except AWS Secret Regions, where AWS DataSync is offered. To learn more, visit the AWS DataSync feature documentation.

## 핵심 요약

요약 미지원
