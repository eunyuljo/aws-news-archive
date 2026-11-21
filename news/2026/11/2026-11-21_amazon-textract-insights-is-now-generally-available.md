---
title: "Amazon Textract Insights is now generally available"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/textract-insights-ga/"
tags: ["S3", "2026", "GA", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon Textract Insights is now generally available

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/textract-insights-ga/

## 내용

Amazon Textract Insights brings document understanding to Amazon Textract. It is a new generative AI feature of Amazon Textract, and is now generally available in the US East (N. Virginia) and US West (Oregon) AWS Regions. Amazon Textract Insights splits, classifies, and extracts structured data from documents in a single asynchronous request. Documents like insurance claims, tax packets, and onboarding packages often arrive as one long scan that holds many documents in no fixed order. Processing them has meant assembling and operating separate steps for text detection, splitting, classification, and extraction. Amazon Textract Insights handles that work in one managed request, with no AI models to train.
How it works: You define the fields you need in a blueprint, a JSON schema that describes each field in natural language, or you can start from a library of AWS public blueprints for common document types such as W-2s, invoices, and bank statements. Amazon Textract Insights can split each file into separate sub-documents, classify each one by matching it to the best-fitting blueprint, and extract your fields. It returns a confidence score for every value and grounds each one to its location on the page, so you can automate high-confidence results and route the rest to human review. It can also return Markdown, HTML, and plain text for retrieval-augmented generation (RAG) applications, generate document summaries and figure captions, and detect and redact personally identifiable information. Amazon Textract Insights reads documents from and writes results to your own Amazon S3 buckets.
You can use Amazon Textract Insights through the AWS SDKs and the AWS CLI. To learn more, see the Amazon Textract product page and the Amazon Textract Insights section of the Amazon Textract Developer Guide.
Regional Availability: US East (N. Virginia), US West (Oregon)

## 핵심 요약

요약 미지원
