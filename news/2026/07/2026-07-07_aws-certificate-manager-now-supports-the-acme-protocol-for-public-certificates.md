---
title: "AWS Certificate Manager now supports the ACME protocol for public certificates"
date: "2026-07-07"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-certificate-manager-acme/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS Certificate Manager now supports the ACME protocol for public certificates

**날짜:** 2026년 07월 07일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-certificate-manager-acme/

## 내용

AWS Certificate Manager (ACM) now allows you to provision a fully managed ACME server endpoint that issues public TLS certificates with a 45 day validity from Amazon Trust Services using any ACMEv2-compatible client, including Certbot, cert-manager for Kubernetes, and acme.sh. With the CA/Browser Forum mandating 47-day certificate lifetimes by 2029, manual management of public certificates becomes untenable. ACME support in ACM gives developers a standards-based path to fully automate certificate issuance and renewal.  PKI administrators can create managed ACME endpoints with centralized governance controls: define domain scopes to restrict which certificates each client can issue, enforce policies on wildcard usage, and delegate certificate requests to application teams without distributing DNS credentials. Domain validation is performed once at the endpoint level, while application owners use standard ACME clients to request certificates. All activity is visible in the ACM console with AWS CloudTrail logging and Amazon CloudWatch metrics for auditability.  ACME support in ACM is available in all commercial AWS Regions. For pricing details, see the ACM pricing page. To get started, visit the AWS News blog post or read the documentation.

## 핵심 요약

요약 미지원
