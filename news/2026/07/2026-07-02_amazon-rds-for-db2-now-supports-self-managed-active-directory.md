---
title: "Amazon RDS for Db2 now supports self-managed Active Directory"
date: "2026-07-02"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-db2-supports-self-managed-active-directory"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon RDS for Db2 now supports self-managed Active Directory

**날짜:** 2026년 07월 02일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-rds-db2-supports-self-managed-active-directory

## 내용

Amazon Relational Database Service (Amazon RDS) for Db2 now allows customers to directly join their RDS for Db2 DB instances to the domains of self-managed Microsoft Active Directory (AD). Self-managed AD can be on-premises, on AWS, or in another cloud. Customers use Kerberos as the authentication protocol to enable single sign-on for their database users.  Previously, to use Kerberos authentication against a self-managed AD with their RDS for Db2 instances, customers were required to deploy AWS Managed Microsoft AD and establish a trust between the AWS managed domain and the self-managed domain. Now, customers can use their existing self-managed AD directly to authenticate and authorize database users without the additional complexity of a managed directory or a directory trust — helping them meet compliance requirements with their existing identity infrastructure. Customers can domain-join their RDS for Db2 instance by either creating a new instance or modifying an existing one, supplying the credentials of a delegated AD service account stored in AWS Secrets Manager and encrypted with AWS KMS. Customers can use self-managed AD free of charge.  Self-managed Active Directory with Amazon RDS for Db2 is now generally available in all AWS Regions where Amazon RDS for Db2 is available, including the AWS GovCloud (US) Regions.  To learn more and get started with self-managed Active Directory, visit the Amazon RDS for Db2 User Guide and the Amazon RDS for Db2 product page.

## 핵심 요약

요약 미지원
