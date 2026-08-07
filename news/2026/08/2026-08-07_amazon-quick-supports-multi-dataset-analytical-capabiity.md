---
title: "Amazon Quick supports multi-dataset analytical capabiity"
date: "2026-08-07"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-quick/"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon Quick supports multi-dataset analytical capabiity

**날짜:** 2026년 08월 07일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-quick/

## 내용

Today, Amazon Quick announces supporting multi-dataset topics, enabling users to model relationships across multiple datasets in a single topic and use that model to build dashboards and answer questions in natural language. Previously, answering a question in a Quick Sight visual that spanned datasets required pre-joining the data into a single dataset—adding manual JOIN logic in the data preparation, consuming extra SPICE capacity, and users have to rebuild multiple datasets based on different use cases or when the model changed. With multi-dataset topics, a topic becomes a reusable relational data model: users add multiple datasets, define the relationships once, and Quick performs the joins at runtime. 
The new capability applies for both dashboard building and natural-language Q&amp;A. For dashboard building, the topic acts as the data model, so a single visual can draw fields from multiple datasets and Quick generates the underlying join automatically—users author the semantic model once and reuse it across every visual in the dashboard. For natural-language analytics, users can point a chat agent directly at a topic and ask questions; the agent reads the relationships defined in the topic and performs runtime joins across datasets to answer, with no need to pre-join tables or prepare data first. Because both experiences query toward the same topic, one governed semantic model serves as the single source of truth for people and agents alike. Multi-dataset topics reuse existing dataset permissions and support row-level and column-level security (RLS/CLS), so established governance carries through every cross-dataset visual and every answer. 
Multi-dataset topics are now generally available in all AWS Regions where Amazon Quick is available. To get started, see this blog post.

## 핵심 요약

요약 미지원
