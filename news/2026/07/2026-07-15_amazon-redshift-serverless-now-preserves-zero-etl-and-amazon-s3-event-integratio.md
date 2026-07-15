---
title: "Amazon Redshift Serverless now preserves zero-ETL and Amazon S3 event integrations during snapshot restores"
date: "2026-07-15"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/redshift-serverless-zetl-autocopy-restore/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon Redshift Serverless now preserves zero-ETL and Amazon S3 event integrations during snapshot restores

**날짜:** 2026년 07월 15일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/redshift-serverless-zetl-autocopy-restore/

## 내용

Amazon Redshift Serverless now automatically preserves zero-ETL and Amazon S3 event integrations when restoring a namespace from a snapshot or recovery point to the same serverless namespace. Previously, restoring a snapshot marked associated integrations as failed, requiring you to manually recreate them after the restore completed. This meant additional time reconfiguring data pipelines and potential data ingestion gaps during the rebuild process.  With this enhancement, integrations are automatically maintained and resume operating after the restore completes, simplifying data ingestion workflows and reducing administrative overhead. This streamlines disaster recovery and testing workflows by reducing manual configuration steps and potential errors. This applies to restores within the same serverless namespace only. Restoring to a different namespace or restoring provisioned clusters does not maintain integrations.  This feature is available in all AWS regions where Amazon Redshift Serverless is available. To learn more about restoring Amazon Redshift Serverless namespaces, please visit our documentation or the Redshift behaviour change page.

## 핵심 요약

요약 미지원
