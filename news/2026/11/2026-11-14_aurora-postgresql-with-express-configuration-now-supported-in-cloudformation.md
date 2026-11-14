---
title: "Aurora PostgreSQL with express configuration now supported in CloudFormation"
date: "2026-11-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-cloudformation/"
tags: ["RDS", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# Aurora PostgreSQL with express configuration now supported in CloudFormation

**날짜:** 2026년 11월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aurora-postgresql-cloudformation/

## 내용

Aurora PostgreSQL now supports express configuration in AWS CloudFormation for infrastructure as code deployment. This launch enables you to automate the infrastructure deployment of your Aurora clusters through CloudFormation templates while benefiting from the speed of express configuration. 
Aurora PostgreSQL clusters created with express configuration allow you to create and query an Aurora serverless database in seconds. The new withExpressConfiguration createOnly property on the AWS::RDS::DBCluster resource creates both the cluster and its primary database instance from one property declaration. You don't need to model or manage the instance separately in your CloudFormation template. This simplifies your templates and makes it easier to manage Aurora clusters with express configuration through infrastructure as code. 
The CloudFormation support is available in all AWS Regions where Aurora PostgreSQL with express configuration is offered. To learn more, see the Aurora User Guide and the AWS::RDS::DBCluster resource reference in the AWS CloudFormation documentation.

## 핵심 요약

요약 미지원
