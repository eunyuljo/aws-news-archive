---
title: "Amazon S3 adds annotations to provide AI agents and analytics tools with context for data discovery"
date: "2026-06-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-s3-annotations-business-context"
tags: ["S3", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon S3 adds annotations to provide AI agents and analytics tools with context for data discovery

**날짜:** 2026년 06월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-s3-annotations-business-context

## 내용

Amazon S3 adds annotations, so you can attach custom metadata to your S3 objects at massive scale, giving AI agents and analytics tools the context they need to find and use the right data. Annotations are a new metadata capability purpose-built for attaching business context directly in JSON, XML, or YAML to your objects, with up to 1GB per object. Annotations can be modified or deleted at any time, making it easier to keep context current as your data evolves. This lets applications and AI agents discover and understand your data without building or maintaining separate metadata systems.  S3 already supports several ways to describe your objects: system-defined metadata captures properties like size and storage class, object tags support operational tasks like access control and lifecycle management, and user-defined metadata lets you add small amounts of custom information at upload time. Annotations complement these existing capabilities at a fundamentally different scale and flexibility. Annotations share the same durability and consistency properties as the object, move with the object during copy and replication operations, and are removed when the object is deleted. You can attach and retrieve annotations on any existing or new object. To query annotations at scale, you can optionally surface them in S3 Metadata, the easiest and fastest way to discover and understand your S3 data. S3 Metadata automatically captures object metadata and stores it in read-only, fully managed Apache Iceberg tables that you can query with Amazon Athena and other Iceberg-compatible tools. You can also use natural language to search objects by their annotations using agents in Amazon SageMaker Unified Studio, or any IDE with the S3 Tables MCP server.  Annotations are available in all AWS Regions, including the AWS China Regions. Annotation tables are available in all AWS Regions where S3 Metadata is available. Get started using the AWS CLI, S3 APIs, or AWS SDKs. For pricing information, visit the S3 pricing page. To learn more, read the AWS News Blog,&nbsp;documentation, and&nbsp;S3 Metadata overview page.

## 핵심 요약

요약 미지원
