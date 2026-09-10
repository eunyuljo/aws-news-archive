---
title: "AWS Entity Resolution adds record-level confidence scores for ML matching"
date: "2026-09-10"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/entity-resolution-record-confidence/"
tags: ["RDS", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# AWS Entity Resolution adds record-level confidence scores for ML matching

**날짜:** 2026년 09월 10일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/entity-resolution-record-confidence/

## 내용

AWS Entity Resolution now provides record-level confidence scores for Machine Learning (ML) based matching workflows, giving you a per-record signal of how confident the model is in each individual identity match. Previously, all records within a match group carried the same group-level confidence score regardless of actual match quality — making it impossible to distinguish a near-certain match from a borderline one. This forced customers to apply a single confidence threshold across all records, limiting the number of resolved identities that could be activated downstream.
With record-level confidence scores, each resolved record now carries its own score reflecting actual match quality. This gives you the precision to qualify more records for activation by applying differentiated thresholds — using higher confidence for automated merges and lower thresholds to include additional records that still meet quality standards. The result is larger addressable audiences and improved lead conversions, while maintaining compliance-grade match transparency with audit-ready evidence for each resolved record. For incremental ML workflows, the existing RecordConfidenceLevel column now reflects the actual per-record score with no schema changes required.
You can start using record-level confidence scores in all AWS Regions where AWS Entity Resolution is available. For more information, see our user guide. For more information about AWS Entity Resolution, visit our product page.

## 핵심 요약

요약 미지원
