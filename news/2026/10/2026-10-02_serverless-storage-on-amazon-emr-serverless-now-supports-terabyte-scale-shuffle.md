---
title: "Serverless Storage on Amazon EMR Serverless now supports terabyte-scale shuffle"
date: "2026-10-02"
service: "EMR"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/emr-serverless-terabyte-scale-shuffle/"
tags: ["EMR", "2026", "new-region"]
nav_exclude: true
---

# Serverless Storage on Amazon EMR Serverless now supports terabyte-scale shuffle

**날짜:** 2026년 10월 02일
**서비스:** EMR
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/emr-serverless-terabyte-scale-shuffle/

## 내용

Amazon EMR Serverless now offers enhanced serverless storage capabilities with support for up to 1TB shuffle operations, raising the previous 200 GB per-job limit. Amazon EMR Serverless makes it simple for data engineers and data scientists to run open-source big data analytics frameworks without configuring, managing, and scaling clusters or servers. This enhancement enables enterprise customers to run production-scale Apache Spark workloads that require processing large volumes of shuffle data during complex operations such as joins, aggregations, and sorting.
Enterprise data teams can now confidently migrate production workloads that routinely process terabyte-scale datasets without worrying about storage constraints. This enhancement is particularly valuable for workloads involving large table joins across multi-terabyte datasets, and complex aggregations on high-cardinality data that require extensive data shuffling. The addition of spill support ensures that jobs can seamlessly handle memory-intensive operations by offloading data to disk when necessary, improving job reliability and success rates for demanding analytical workloads.
This feature is available with Amazon emr-7.14, emr-spark-8.1 and later, in 18 AWS Regions where Amazon EMR Serverless is available. See the Amazon EMR documentation for the full list of supported Regions and their applicable limits.
To learn more about Amazon EMR Serverless and get started with terabyte-scale shuffle support, visit the Amazon EMR Serverless page.

## 핵심 요약

요약 미지원
