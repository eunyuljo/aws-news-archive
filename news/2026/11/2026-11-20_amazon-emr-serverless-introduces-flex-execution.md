---
title: "Amazon EMR Serverless introduces Flex execution"
date: "2026-11-20"
service: "Glue"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-serverless/"
tags: ["Glue", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EMR Serverless introduces Flex execution

**날짜:** 2026년 11월 20일
**서비스:** Glue
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-emr-serverless/

## 내용

Amazon EMR Serverless now supports Flex execution, a new option that reduces the cost of non-urgent Spark batch jobs by up to 60% by running them on spare compute capacity. With Flex, you enable a single configuration when submitting a job, with no changes to Spark scripts or job definitions. 
Flex execution is designed for workloads that have flexible completion requirements, such as nightly batch ETL, backfill jobs, and development or testing pipelines. Start and execution times of Flex jobs vary because spare compute resources may not always be available immediately and may be reclaimed during execution. To reduce the likelihood and impact of interruptions, EMR Serverless spans availability zones, diversifies across instance types, places the Spark driver on dedicated capacity to protect job state, and retries interrupted tasks through Spark's built-in fault tolerance. You can also use Flex execution with Serverless Storage to offload shuffle data, adding another layer of resilience where retried tasks can resume from stored intermediate results instead of recomputing previous stages. Regardless of the execution option, Spark jobs on EMR Serverless have the same capabilities, including AWS Lake Formation fine-grained access control, AWS Graviton-based workers, and AWS Glue Data Catalog integration. Flex workers are billed at Flex rates for vCPU-hours and memory GB-hours, while the Spark driver and storage are billed at Standard rates. 
Amazon EMR Serverless Flex execution is available on all EMR releases and in all AWS Regions where Amazon EMR Serverless is available, including the AWS GovCloud (US) Regions, except the China Regions. To learn more, see Flex execution in the Amazon EMR Serverless User Guide and the blog post - Introducing Amazon EMR Serverless Flex. For pricing details, visit the Amazon EMR pricing page.

## 핵심 요약

요약 미지원
