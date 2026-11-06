---
title: "Amazon RDS for Oracle now supports Kerberos authentication with self-managed Active Directory"
date: "2026-11-06"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-kerberos-self-managed-ad/"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon RDS for Oracle now supports Kerberos authentication with self-managed Active Directory

**날짜:** 2026년 11월 06일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/rds-oracle-kerberos-self-managed-ad/

## 내용

Amazon Relational Database Service (Amazon RDS) for Oracle (Amazon Relational Database Service (Amazon RDS) for Oracle) now allows customers to join their RDS for Oracle DB instances directly to their self-managed Microsoft Active Directory (AD) domain. Your self-managed AD can run on premises, on Amazon EC2, or with another cloud provider. Users in your AD domain can authenticate to RDS for Oracle DB instances using Kerberos. 
Previously, in order to use Kerberos authentication with self-managed AD for their RDS for Oracle instances, customers were required to deploy AWS Managed Microsoft AD and establish trust between AWS managed domain and self-managed domain. Now, customers can join their existing self-managed AD directly to authenticate and authorize users without setting up an additional directory or trust relationship. You can set this up using the AWS Management Console, AWS CLI, or AWS SDK. You can use self-managed AD without any additional charge. 
Kerberos authentication with self-managed Active Directory in Amazon RDS for Oracle is available in all commercial AWS Regions where Amazon RDS for Oracle is available. To learn more about Kerberos authentication with self-managed Active Directory, visit Working with self-managed Active Directory with an Amazon RDS for Oracle DB instance in the Amazon RDS User Guide.

## 핵심 요약

요약 미지원
