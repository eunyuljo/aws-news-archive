---
title: "AWS Certificate Manager supports switching from e-mail to DNS validation"
date: "2026-08-14"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/AWS-Certificate-Manager-Email-DNS-Switch"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Certificate Manager supports switching from e-mail to DNS validation

**날짜:** 2026년 08월 14일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/AWS-Certificate-Manager-Email-DNS-Switch

## 내용

AWS Certificate Manager (ACM) now enables you to change the domain validation method on your existing ACM issued public TLS certificates from e-mail to DNS, without reissuing the certificate or changing its existing Amazon Resource Name (ARN).&nbsp;Due to the&nbsp;Certification Authority/Browser (CA/B) Forum's mandated deprecation of email-based domain validation for publicly trusted certificates, effective March 15, 2028, ACM will phase out its support for email validation throughout 2027. ACM will no longer issue email-validated certificates starting March 31 2027, and stop renewing email-validated certificates on September 30 2027. More details on ACM's deprecation of email validation can be found on the AWS Security Blog. By switching to DNS validation now, you can transition ahead of that deadline and enable fully automated renewals through DNS validated certificates. 
Your certificate ARN remains unchanged after switching from e-mail to DNS validation, so existing ARN references in your CI/CD pipelines, load balancer configurations, and other AWS service integrations continue to work without modification. To switch the validation method, use the ACM console or the&nbsp;&nbsp;UpdateCertificateOptions&nbsp;API. ACM provides a CNAME record for each domain in the certificate (the same mechanism used when provisioning new certificates with DNS validation) and you have up to 72 hours to add the records to your DNS configuration. You can monitor the validation status of each domain via the console or the&nbsp;ListCertificateDomainValidations&nbsp;API. We recommend DNS validation for new certificates, and&nbsp;HTTP validation&nbsp;for Amazon CloudFront distributions.. 
This feature is available in all AWS Regions where ACM certificates are available. To get started, refer to &nbsp;Migrating from email to DNS validation&nbsp;in the AWS Certificate Manager User Guide.

## 핵심 요약

요약 미지원
