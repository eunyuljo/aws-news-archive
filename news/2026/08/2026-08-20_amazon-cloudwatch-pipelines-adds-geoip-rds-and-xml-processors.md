---
title: "Amazon CloudWatch pipelines adds GeoIP, RDS, and XML processors"
date: "2026-08-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/cloudwatch-geoip-rds-xml/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon CloudWatch pipelines adds GeoIP, RDS, and XML processors

**날짜:** 2026년 08월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/cloudwatch-geoip-rds-xml/

## 내용

Amazon CloudWatch pipelines now includes three new processors that parse and enrich log data as it's ingested: an Amazon RDS log parser, an XML parser and a GeoIP enrichment processor. CloudWatch pipelines is a fully managed service that ingests, transforms, and routes telemetry to CloudWatch without managing infrastructure. 
Log sources often produce data that isn't immediately queryable without reprocessing the data. RDS Aurora logs arrive in their native engine format, application logs carry embedded XML, and IP addresses lack location context. The new processors address each case. The Amazon RDS processor parses Aurora audit and error logs into structured fields, the XML parser converts a field containing an XML string into JSON, and the GeoIP processor enriches any IP address field with geographic context such as city, country, and coordinates. For example, you can parse an Aurora audit log into structured fields for compliance reporting. In a separate pipeline, you can extract the XML payload from a Windows Event Log into JSON and resolve its source IP to a city and country for security analysis. You can use these processors independently or combine them in one pipeline. 
These processors are available at no additional cost in all AWS Regions where CloudWatch pipelines is generally available. CloudWatch logs ingestion and storage rates apply. You can add these processors to your pipelines using the AWS Management Console, AWS CLI, or AWS SDKs. To get started, see the Amazon CloudWatch pipelines documentation.

## 핵심 요약

요약 미지원
