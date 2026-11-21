---
title: "​​​Amazon RDS for Db2 now supports renaming databases​"
date: "2026-11-21"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-rename-databases"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# ​​​Amazon RDS for Db2 now supports renaming databases​

**날짜:** 2026년 11월 21일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-rds-db2-supports-rename-databases

## 내용

​​Amazon Relational Database Service (Amazon RDS) for Db2 now supports renaming databases in place. You can rename a database on your DB instance by calling the new rdsadmin.rename_database stored procedure. Previously, renaming a database required you to back it up and restore it under a new name. With rename, the database keeps its data in place, so it's faster than backing up and restoring the database.​ 
​​Database rename simplifies workflows such as replacing a database with a restored copy. For example, after you restore a copy of a database from a backup, you can rename the original database, and then give its name to the restored copy, without changing your application connection strings. Database rename runs as a background task that you can monitor with rdsadmin.get_task_status.​&nbsp; 
​​Database rename is available in all AWS Regions where Amazon RDS for Db2 is offered. To get started, see the Amazon RDS User Guide.​​

## 핵심 요약

요약 미지원
