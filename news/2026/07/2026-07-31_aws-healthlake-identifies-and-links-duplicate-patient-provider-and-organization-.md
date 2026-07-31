---
title: "AWS HealthLake identifies and links duplicate patient, provider, and organization records (Preview)"
date: "2026-07-31"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-healthlake/"
tags: ["RDS", "2026", "preview", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS HealthLake identifies and links duplicate patient, provider, and organization records (Preview)

**날짜:** 2026년 07월 31일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-healthlake/

## 내용

Duplicate patient records are one of the costliest problems in healthcare data management, scattering a patient's information, leading to redundant tests, missed diagnoses, billing errors, manual reconciliation, and broken analytics that count one patient as many.  AWS HealthLake now supports resource matching, which automatically identifies and links duplicate records in a datastore. Healthcare organizations can build accurate longitudinal patient records and trustworthy population health datasets without specialized master data management tooling. Resource matching works across seven Fast Healthcare Interoperability Resources (FHIR) resource types: Patient, Practitioner, Organization, Location, Device, RelatedPerson, and PractitionerRole. It matches high-confidence healthcare identifiers such as Social Security, medical record, and national provider numbers, applying each identifier's real-world scope and filtering out placeholder values to avoid false matches.  Once enabled, every record that is created or updated is automatically evaluated and matches are connected through FHIR Linkage resources. Resource matching requires no configuration, matching rules, or third-party tools. Original records are never modified or deleted, preserving full provenance. Linkages are automatically re-evaluated as source records change and removed when records no longer match.  AWS HealthLake resource matching is available in gated preview in the US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai), Europe (London), Europe (Ireland), Asia Pacific SouthEast (Sydney), and Canada (Central) Regions. To turn it on for your datastore during the preview period, request to be added to the allowlist here.  To learn more, see Matching duplicate FHIR resources documentation in the AWS HealthLake developer guide.

## 핵심 요약

요약 미지원
