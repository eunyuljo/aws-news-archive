---
title: "AWS Secrets Manager adds managed external secrets support for Databricks and Twilio"
date: "2026-10-13"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/secrets-manager-managed-external-secrets-databricks-twilio/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Manager adds managed external secrets support for Databricks and Twilio

**날짜:** 2026년 10월 13일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/secrets-manager-managed-external-secrets-databricks-twilio/

## 내용

AWS Secrets Manager now extends its managed external secrets capability to include Databricks and Twilio, enabling you to automatically rotate the credentials that your data pipelines and messaging applications use to call these services. You set up rotation directly from the AWS Management Console or API without writing or maintaining any custom rotation Lambda functions.
Long-lived credentials often stay unrotated because rotation is hard to set up and hard to distribute safely to the applications that use the updated credential. With managed external secrets, you can use Secrets Manager to rotate the Databricks personal access tokens that your jobs and continuous integration and continuous delivery (CI/CD) pipelines use. You can also rotate the service principal OAuth client secrets that your automation workflows use. Each replacement personal access token retains the scopes of the token it replaces, so a narrowly scoped token stays narrowly scoped.
For Twilio, you can use Secrets Manager to rotate the API keys and Auth Tokens that your applications use to send messages and place calls. For both services, you store the credential in Secrets Manager as a managed external secret and set a rotation schedule. Secrets Manager always returns the current credential, so your applications pick up rotated values automatically, with no code changes required.
These integrations join existing managed external secrets support for BigID, Cisco Security Platform, Confluent Cloud, Datadog, GitLab, Jenkins, MongoDB Atlas, Netskope, Paddle, Salesforce, Snowflake, and SonarQube.
Databricks and Twilio managed external secrets are available in all AWS Regions where AWS Secrets Manager managed external secrets is supported. To learn more, visit the &nbsp;AWS Secrets Manager managed external secrets documentation.

## 핵심 요약

요약 미지원
