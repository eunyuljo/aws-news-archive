---
title: "Amazon Redshift expands SUPER data type to store strings up to 16 million bytes"
date: "2026-11-07"
service: "Redshift"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-redshift-expands-super-to-16-million-bytes/"
tags: ["Redshift", "2026", "new-region"]
nav_exclude: true
---

# Amazon Redshift expands SUPER data type to store strings up to 16 million bytes

**날짜:** 2026년 11월 07일
**서비스:** Redshift
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-redshift-expands-super-to-16-million-bytes/

## 내용

Amazon Redshift now supports individual strings up to 16 million bytes within SUPER data types. Once you opt in through a database parameter, this enhancement applies when ingesting structured or semi-structured data from JSON, PARQUET, TEXT, and CSV source files, and when transforming data through extract load and transform (ELT) processes. Previously, individual strings within SUPER data types were limited to 65,535 bytes. 
Storing large individual strings in the SUPER data type helps avoid complex pre-loading transformations needed to store the source data in Amazon Redshift. You can now directly ingest large individual strings greater than 65,535 bytes without extra processing (for example, lengthy documents like terms and conditions and contracts), making them queryable using SQL. Once the data is in Amazon Redshift, you can use the flexibility of PartiQL language to explore and navigate through the data or use string functions to transform the data.&nbsp;Functions such as JSON_PARSE, CONCAT, and LISTAGG can now take input strings and return output strings up to 16 million bytes in length. 
This enhancement is available in all AWS Regions, including the AWS GovCloud (US) Regions, where Amazon Redshift is available. See the AWS Region Table for more details. To learn more, please visit our documentation or blog.&nbsp;&nbsp;

## 핵심 요약

요약 미지원
