---
title: "Amazon Aurora DSQL now supports foreign key constraints"
date: "2026-08-28"
service: "Aurora"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-dsql-foreign-key-constraints/"
tags: ["Aurora", "2026", "new-region"]
nav_exclude: true
---

# Amazon Aurora DSQL now supports foreign key constraints

**날짜:** 2026년 08월 28일
**서비스:** Aurora
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aurora-dsql-foreign-key-constraints/

## 내용

Amazon Aurora DSQL now lets you add foreign key constraints to new and existing tables. Aurora DSQL is a serverless, distributed SQL database with PostgreSQL compatibility and active-active multi-Region availability. 
You can now express your application's rules about how tables reference each other as FOREIGN KEY constraints in your Aurora DSQL cluster. Declare, for example, that a customer's primary address must reference an existing row in your address table. Aurora DSQL then refuses any write that would leave that customer pointing at an address that no longer exists.&nbsp;You choose what happens when a referenced row is deleted or updated, with the options NO ACTION, RESTRICT, CASCADE, SET NULL, and SET DEFAULT. 
This feature is available in all AWS Regions where Aurora DSQL is available. To learn more, see working with foreign key constraints and the CREATE TABLE foreign key syntax in the Aurora DSQL User Guide.

## 핵심 요약

요약 미지원
