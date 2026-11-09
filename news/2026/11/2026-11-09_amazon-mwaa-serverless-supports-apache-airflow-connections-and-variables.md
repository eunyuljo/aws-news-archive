---
title: "Amazon MWAA Serverless supports Apache Airflow connections and variables"
date: "2026-11-09"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-serverless-connections-variables/"
tags: ["SecretsManager", "2026", "new-region"]
nav_exclude: true
---

# Amazon MWAA Serverless supports Apache Airflow connections and variables

**날짜:** 2026년 11월 09일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/mwaa-serverless-connections-variables/

## 내용

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) Serverless now supports Apache Airflow connections and variables, so your workflows can reach databases, APIs, and other external systems. You can manage credentials and configuration outside your workflow code.
You store sensitive connections and variables in the secrets backend of your choice, such as AWS Secrets Manager, AWS Systems Manager Parameter Store, or your own custom backend, configure it on your workflow, and grant your workflow execution role access. Tasks retrieve them at run time through standard Apache Airflow methods. You can define non-secret values as environment variables on the workflow.
This feature is available in all AWS Regions where Amazon MWAA Serverless is available. For more information, see Amazon MWAA Serverless Regions.
To learn more, see Managing connections and variables and Using environment variables in Amazon MWAA Serverless workflows in the Amazon MWAA Serverless User Guide.

## 핵심 요약

요약 미지원
