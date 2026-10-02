---
title: "Amazon Redshift simplifies access to secure logging with federated permissions"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/redshift-secure-logging-permissions/"
tags: ["S3", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Redshift simplifies access to secure logging with federated permissions

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/redshift-secure-logging-permissions/

## 내용

Amazon Redshift now makes it easier to troubleshoot and audit queries on data protected by federated permissions with fine-grained access control (FGAC). Using the new DEBUG permission, data owners can let specific identities see unredacted secure logging records across multiple Redshift data warehouses.
With Amazon Redshift federated permissions, you define data permissions once, and Redshift enforces them automatically across every Redshift warehouse in your AWS account. When a query accesses FGAC-protected data, secure logging redacts sensitive values in system table records, such as rewritten query text, error messages, and object names. This protects the producer's data from consumers. At the same time, authorized auditors and administrators need visibility into these records to troubleshoot queries and meet compliance requirements, without turning off secure logging.
With the new DEBUG permission, a superuser or database owner can choose which identities see these records without redaction. You grant DEBUG with the standard Redshift GRANT command, typically to an IAM user, IAM role, or IAM Identity Center user or group, so that identity can see unredacted records for its own queries. You can also grant DEBUG to the administrators of a consumer account for full log visibility during troubleshooting and audit. Records authorized for account administrators also stay unredacted when you export Redshift system table data to Amazon S3 Tables. You get precise, auditable control over who can see logs, and secure logging stays on.
The feature is available in all AWS Regions where Amazon Redshift is supported. To learn more, see federated permissions,&nbsp;&nbsp;Usage Notes and secure logging in the Amazon Redshift documentation.

## 핵심 요약

요약 미지원
