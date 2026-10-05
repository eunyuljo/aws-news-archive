---
title: "AWS Private CA now provides detailed certificate issuance logs"
date: "2026-10-05"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-private-ca-certificate-issuance-logs/"
tags: ["RDS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Private CA now provides detailed certificate issuance logs

**날짜:** 2026년 10월 05일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-private-ca-certificate-issuance-logs/

## 내용

AWS Private CA announces detailed certificate issuance logs, a new AWS CloudTrail service event that records the complete certificate content, issuing CA information, requester identity, and signing status for every issuance. You can use these events for compliance auditing, certificate inventory, algorithm migration tracking, and failed-issuance monitoring. Previously, the CloudTrail management event for the IssueCertificate API confirmed that the API call succeeded by providing a certificate ARN but did not capture the certificate content, information about the CA that signed it, or issuances that failed before signing.
The new IssueCertificateDetails event captures the complete to-be-signed (TBS) certificate with all X.509 fields and extensions, plus convenience fields for the subject, issuer, serial number, validity period, template, and signing algorithm. Events are emitted for both successful and failed issuance, so pre-signing failures such as name constraints violations now produce a record with a failure explanation. Each event identifies the requester: the account and IAM principal for direct API callers, or the service principal for certificates issued through AWS Private CA connectors or integrated AWS services. In cross-account configurations, the event is delivered to the CA owner account.
The event is delivered automatically as a CloudTrail management event, with no configuration or opt-in required and no additional cost beyond standard AWS CloudTrail pricing. Because it flows through CloudTrail, you can act on it in real time with Amazon EventBridge or query it in batch with Amazon Athena for certificate auditing, inventory, tracking, and monitoring.&nbsp;This feature is available in all AWS Regions where AWS Private CA is offered. To learn more, see the AWS Private CA User Guide.

## 핵심 요약

요약 미지원
