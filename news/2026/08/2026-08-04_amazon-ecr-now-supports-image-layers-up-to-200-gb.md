---
title: "Amazon ECR now supports image layers up to 200 GB"
date: "2026-08-04"
service: "Lex"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecr-image-layers/"
tags: ["Lex", "2026", "new-region"]
nav_exclude: true
---

# Amazon ECR now supports image layers up to 200 GB

**날짜:** 2026년 08월 04일
**서비스:** Lex
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ecr-image-layers/

## 내용

Amazon Elastic Container Registry (Amazon ECR) has increased the maximum image layer size limit to 200 GB, for images pushed via Docker push. 
Previously, packaging assets required splitting data across multiple layers or offloading to external storage systems. With this update, customers can store up to 200 GB in a single image layer, eliminating extra complexity for use cases like embedding large language models, bundling genomics datasets, or packaging large binary dependencies directly into your container images. Images pushed using the AWS SDK or CLI; (UploadLayerPartAPI) remain limited to 50 GB. 
This feature is available in all AWS Regions and partitions where Amazon ECR is available except the Middle East (Bahrain) and Middle East (UAE) Regions. To learn more, visit the Amazon ECR product page and refer to the Amazon ECR User Guide. For pricing information, see the Amazon ECR pricing page.

## 핵심 요약

요약 미지원
