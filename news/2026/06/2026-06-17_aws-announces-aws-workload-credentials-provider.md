---
title: "AWS announces AWS Workload Credentials Provider"
date: "2026-06-17"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/aws-workload-credentials-provider/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS announces AWS Workload Credentials Provider

**날짜:** 2026년 06월 17일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/aws-workload-credentials-provider/

## 내용

AWS announces AWS Workload Credentials Provider, a lightweight client-side provider that automates deployment of exported certificates from AWS Certificate Manager (ACM) and local caching of secrets from AWS Secrets Manager across AWS and non-AWS workloads.  Previously, customers exporting public or private certificates from ACM had to build custom automation using Amazon EventBridge to detect renewals and deploy the updated certificates. With public certificate lifetimes decreasing per the the Certification Authority Browser Forum (CA/B) mandate, this custom automation can become difficult to maintain at scale. AWS Workload Credentials Provider eliminates this complexity by providing a single provider that helps distribute and automate both secrets and certificates to your workloads. You configure it with your certificate ARN and specify options such as file paths and server reload behavior — the provider then handles certificate export and deployment automatically to prevent expiry related failures. It runs on Windows and Linux and supports Apache and NGINX web servers.  For secrets caching, the provider maintains full backwards compatibility with the AWS Secrets Manager Agent, enabling you to securely cache application secrets locally across AWS and non-AWS workloads through the same unified provider.  AWS Workload Credentials Provider is open source and available on GitHub. You can use it with exportable ACM certificates and Secrets Manager in all AWS Regions. To learn more, visit the AWS Certificate Manager documentation or the AWS Secrets Manager documentation.

## 핵심 요약

요약 미지원
