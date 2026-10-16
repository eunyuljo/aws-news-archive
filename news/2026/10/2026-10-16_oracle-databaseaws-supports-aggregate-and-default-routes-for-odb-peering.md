---
title: "Oracle Database@AWS supports aggregate and default routes for ODB peering"
date: "2026-10-16"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-database-aws-aggregate-routes-odb/"
tags: ["VPC", "2026", "GA", "new-region"]
nav_exclude: true
---

# Oracle Database@AWS supports aggregate and default routes for ODB peering

**날짜:** 2026년 10월 16일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/oracle-database-aws-aggregate-routes-odb/

## 내용

Oracle Database@AWS (ODB) now supports advertising aggregate routes and a default route (0.0.0.0/0) when configuring ODB peering between applications in an Amazon VPC and databases in an ODB network. This simplifies network operations as customers extend new VPCs or on-premises networks to reach their databases, without updating the advertised CIDRs for each network that needs connectivity to the ODB network.
Previously, customers had to advertise each network reaching the ODB network as a separate CIDR, and could not advertise a broad aggregate range or a default route. With this launch, customers can advertise any CIDR range, so a single aggregate or default route can cover all networks reachable through the peered VPC, such as those connected through an AWS Transit Gateway, without a separate entry for each one.
This capability is available on ODB networks that support multiple ODB peering connections, in all AWS Regions where Oracle Database@AWS is available. To learn more, visit Oracle Database@AWS and the Oracle Database@AWS User Guide. To get started, subscribe through AWS Marketplace.

## 핵심 요약

요약 미지원
