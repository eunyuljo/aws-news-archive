---
title: "AWS Secrets Manager adds managed external secrets support for Jenkins and SonarQube"
date: "2026-08-12"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/secrets-manager-integration-jenkins-sonarqube/"
tags: ["SecretsManager", "2026", "new-region"]
nav_exclude: true
---

# AWS Secrets Manager adds managed external secrets support for Jenkins and SonarQube

**날짜:** 2026년 08월 12일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/secrets-manager-integration-jenkins-sonarqube/

## 내용

AWS Secrets Manager now extends its managed external secrets capability to include Jenkins API Tokens and SonarQube Tokens, enabling you to automatically rotate these third-party credentials directly from the AWS console without writing any custom rotation code. 
For Jenkins, Secrets Manager mints a new token and revokes the old one only after the replacement is verified active, so your continuous integration and continuous delivery (CI/CD) jobs transition without interruption. Rotation supports both self-rotation, where the token being rotated authenticates its own replacement, and admin-assisted rotation, where a separate admin token performs the generate and revoke operations. For SonarQube, you can rotate three types of tokens — User Tokens, Global Analysis Tokens, and Project Analysis Tokens — via SonarQube's Web API. User Tokens support self-rotation, while analysis tokens are rotated using an admin token. 
These integrations join existing managed external secrets support for BigID, Confluent Cloud, Datadog, GitLab, MongoDB Atlas, Okta, Paddle, Salesforce, and Snowflake. 
Jenkins and SonarQube managed external secrets are available in all AWS Regions where AWS Secrets Manager managed external secrets is supported. To learn more, visit the &nbsp;AWS Secrets Manager managed external secrets documentation&nbsp;.

## 핵심 요약

요약 미지원
