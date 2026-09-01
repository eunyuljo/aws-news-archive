---
title: "Amazon Redshift now supports Apache Iceberg v3 tables"
date: "2026-09-01"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-apache-iceberg-v3"
tags: ["Redshift", "2026", "GA", "performance", "security"]
nav_exclude: true
---

# Amazon Redshift now supports Apache Iceberg v3 tables

**날짜:** 2026년 09월 01일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-redshift-supports-apache-iceberg-v3

## 내용

Amazon Redshift now supports reading from and writing to Apache Iceberg v3 tables in your data lake. Apache Iceberg is an open table format, and its v3 release adds several new features.&nbsp;With this launch, Amazon Redshift introduces support for default column values, row lineage, and deletion vectors. With default column values, you can define an initial value that Amazon Redshift applies when no value is provided, simplifying schema evolution as you add columns to existing tables. Row lineage exposes pseudo-columns that track each row's identity and last-updated sequence number, so you can build incremental pipelines and CDC (change data capture) workflows that process only modified rows. Deletion vectors replace Iceberg v2's positional delete files with compact compressed bitmaps, delivering faster reads and writes for high-frequency update and delete workloads such as compliance-driven record removal. You can create a v3 table with CREATE TABLE &lt;table&gt; ... USING ICEBERG TABLE PROPERTIES ('format-version' = '3'), or upgrade an existing v2 table in place with ALTER TABLE &lt;table&gt; SET TABLE PROPERTIES ('format-version' = '3'). Amazon Redshift's Graviton based provisioned and serverless clusters support the new v3 format. To learn more, see Apache Iceberg v3 features in the Amazon Redshift Documentation.

## 핵심 요약

요약 미지원
