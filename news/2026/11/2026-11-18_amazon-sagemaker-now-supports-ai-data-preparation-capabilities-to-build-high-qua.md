---
title: "Amazon SageMaker now supports AI data preparation capabilities to build high-quality datasets for model development"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-ai-data-prep-capabilities/"
tags: ["S3", "2026", "new-region", "security", "ai-ml"]
nav_exclude: true
---

# Amazon SageMaker now supports AI data preparation capabilities to build high-quality datasets for model development

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/sagemaker-ai-data-prep-capabilities/

## 내용

Building high-quality training datasets has traditionally required weeks of manual labeling and data cleaning. Amazon SageMaker now offers AI data preparation capabilities that help data scientists and ML engineers build high-quality training and evaluation datasets for both text-based model customization and traditional ML. 
Teams can generate synthetic examples grounded in their own documents, auto-label records at scale with confidence scores, incorporate expert feedback through human review, evaluate data quality, and transform data for their chosen training or evaluation technique. Synthetic data generation creates training, evaluation, and test data from a specification grounded in your documents. Auto-labeling labels data at scale with built-in task types including classification, named entity recognition, extractive question answering, ordinal rating, and summarization, plus custom tasks. Rows below your confidence threshold go to a human review queue in the Label Studio Community Edition in SageMaker AI Studio. Data quality evaluation finds duplicates and surfaces issues such as tone and insufficient diversity with both quality metrics and rules. Data transformation cleans and reshapes data for your training or evaluation technique, using operators such as dedupe, filter, and format conversion. 
Teams can start with just a few examples, production traces, or existing data in Amazon S3, Amazon Athena, or AWS Glue Data Catalog. Developers access these capabilities directly through the SageMaker Python SDK API or in natural language through the latest version of the AWS AI-ML skill in the Agent Toolkit for AWS. Your source data, generated datasets, and labels stay in your own Amazon S3 buckets, controlled by an IAM role you manage. 
These capabilities are available in the US East (N. Virginia) (us-east-1) and US West (Oregon) (us-west-2) regions. 
To learn more, see the AI data preparation documentation.

## 핵심 요약

요약 미지원
