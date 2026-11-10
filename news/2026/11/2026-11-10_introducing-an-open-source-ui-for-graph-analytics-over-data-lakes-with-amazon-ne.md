---
title: "Introducing an open-source UI for graph analytics over data lakes with Amazon Neptune Analytics"
date: "2026-11-10"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-graphover-datalakes-generally-available"
tags: ["S3", "2026", "preview", "new-region"]
nav_exclude: true
---

# Introducing an open-source UI for graph analytics over data lakes with Amazon Neptune Analytics

**날짜:** 2026년 11월 10일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-graphover-datalakes-generally-available

## 내용

Today, AWS is introducing an open-source solution with a local web UI that helps customers turn data lake records into graphs for analysis with Amazon Neptune Analytics. By projecting selected records and relationships, customers can investigate connections across tables and run graph algorithms without building their own ETL pipelines. 
For example, a customer could project accounts and transactions into a graph to explore how accounts are connected or identify communities that may warrant investigation. Doing this today often means writing queries to prepare node and relationship data, creating a Neptune Analytics graph, and managing the import. Customers may also need to build a selective projection so they do not load an entire dataset for a narrower question. 
The new UI brings those steps into single workflow. To run graph analytics over iceberg tables, customers select an Athena catalog and database, define a property graph using SQL/PGQ, and preview rows before import. The solution runs the projection queries through Athena, stages the selected data in Amazon S3, and imports it into Neptune Analytics. The UI helps customers manage the resulting graph. They can open the loaded graph in Graph Explorer to query and visualize relationships. [1] 
The UI runs locally and it is available in all regions where Amazon Neptune Analytics is available. To get started, see the setup instructions.

## 핵심 요약

요약 미지원
