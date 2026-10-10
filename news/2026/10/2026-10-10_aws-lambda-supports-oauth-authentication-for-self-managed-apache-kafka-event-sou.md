---
title: "AWS Lambda supports OAuth authentication for self-managed Apache Kafka event sources"
date: "2026-10-10"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-Lambda-supports-oauth-kafka-esm/"
tags: ["Lambda", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# AWS Lambda supports OAuth authentication for self-managed Apache Kafka event sources

**날짜:** 2026년 10월 10일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-Lambda-supports-oauth-kafka-esm/

## 내용

AWS Lambda now supports OAuth authentication for self-managed Apache Kafka event source mappings (ESM), including&nbsp;Kafka clusters that customers run themselves and managed offerings such as Confluent Cloud, Aiven, and Redpanda. With this launch, customers can authenticate their Lambda Kafka consumers through their enterprise identity provider, helping them meet the security and compliance requirements for their Kafka applications.
Customers building event-driven Kafka workloads for use cases such as payment processing, fraud detection, and real-time data pipelines use Kafka ESM to build serverless Kafka consumers. Kafka ESM provides automatic scaling, error handling, batching, and event filtering. Previously, Kafka ESM supported only SASL/PLAIN, SASL/SCRAM, and mutual TLS (mTLS) as&nbsp;authentication methods,&nbsp;so customers in regulated industries that require OAuth could not use Kafka ESM with their clusters. With OAuth support, customers can use their enterprise identity provider, such as Amazon Cognito or Okta,&nbsp;to authenticate their Kafka ESM and apply the same identity governance and access policies across their Kafka clusters and Lambda consumers.
This capability is available in all&nbsp;AWS commercial Regions&nbsp;where self-managed Kafka ESM is available. To use OAuth authentication, create a new Kafka ESM with your authentication configuration through the AWS Management Console, Lambda API, AWS CLI, AWS CloudFormation, or AWS SAM. To learn more, see the AWS Lambda developer guide and AWS Lambda pricing.&nbsp; &nbsp;&nbsp;

## 핵심 요약

요약 미지원
