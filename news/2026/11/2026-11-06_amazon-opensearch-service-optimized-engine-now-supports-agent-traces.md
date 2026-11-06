---
title: "Amazon OpenSearch Service optimized engine now supports agent traces"
date: "2026-11-06"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-support-traces"
tags: ["RDS", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon OpenSearch Service optimized engine now supports agent traces

**날짜:** 2026년 11월 06일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-opensearch-service-support-traces

## 내용

Today, the Amazon OpenSearch Service optimized engine adds support for agent traces, including OpenTelemetry traces. Your traces and logs now live in the same place. You can follow a request or an agent session from start to finish, find the step that failed or slowed down, and check the related logs without switching tools.&nbsp; 
The optimized engine maps OpenTelemetry logs and traces to object, nested, and flat object fields, with support for multi-valued arrays. Span events, span links, prompts, and tool calls retain their nested structure, allowing field-level queries without flattening data during ingestion. 
On hot-tier data, the engine supports update, delete, and upsert operations by document ID.&nbsp;When data arrives late or with errors, you can correct it in place, so your dashboards and alerts work from accurate data. In OpenSearch UI, you can analyze this data with Discover Traces, application performance monitoring, the service map, and the agent traces and sessions views. 
These features are available on OpenSearch 3.7, at no additional charge in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Canada (Central), Asia Pacific (Mumbai), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), Europe (London), and Europe (Spain).&nbsp;&nbsp;To get started, send OpenTelemetry data to your domain, for example by using Amazon OpenSearch Ingestion. To learn more, see the documentation.

## 핵심 요약

요약 미지원
