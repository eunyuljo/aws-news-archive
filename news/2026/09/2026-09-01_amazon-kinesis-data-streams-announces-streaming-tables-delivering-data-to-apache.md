---
title: "Amazon Kinesis Data Streams announces streaming tables, delivering data to Apache Iceberg tables on Amazon S3 Tables"
date: "2026-09-01"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/kinesis/data-delivery-s3-tables"
tags: ["S3", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# Amazon Kinesis Data Streams announces streaming tables, delivering data to Apache Iceberg tables on Amazon S3 Tables

**날짜:** 2026년 09월 01일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/kinesis/data-delivery-s3-tables

## 내용

Amazon Kinesis Data Streams introduces streaming tables, a new fully serverless capability that continuously delivers data from Kinesis streams to Amazon S3 Tables in Apache Iceberg format. Streaming tables eliminate the need to build and operate self-managed Iceberg delivery pipelines, reducing data delivery costs by up to 50%. Intelligent inline compaction eliminates the small file problem and keeps query performance predictable, reducing downstream query costs by up to 30%. 
Amazon Kinesis Data Streams is a serverless streaming data service that makes it easy to capture, process, and store data streams at any scale. Customers increasingly want to deliver streaming data to Apache Iceberg tables to power near real time analytics and AI/ML feature pipelines using the freshest data. To do this today, customers build and manage custom pipelines, handle format conversions, and manage compute infrastructure, adding to their costs. High volume streaming ingestion also creates many small Parquet files that degrade downstream query performance and increase storage costs. With streaming tables, customers simply create a streaming table, a fully serverless capability that continuously delivers data from a Kinesis stream to Amazon S3 Tables. Intelligent inline compaction eliminates the performance impact of small files and keeps query performance predictable without sacrificing data freshness. Kinesis Data Streams automatically handles scaling, retries, compaction, and delivery reliability, and delivers in minutes, no custom applications, no self-managed compute, and no operational overhead. Customers configure streaming tables in a few clicks from the console as an integrated experience or via APIs. 
Streaming tables support On Demand Advantage (ODA) and On Demand Standard (ODS) capacity modes with usage-based pricing, no setup fees or minimum commitments. You are only charged for successfully delivered data. Streaming tables are available in all AWS Regions where Amazon Kinesis Data Streams is available, including AWS GovCloud (US) and China regions. To get started, see the Amazon Kinesis Data Streams User Guide and the pricing page.

## 핵심 요약

요약 미지원
