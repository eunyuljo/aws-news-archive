---
title: "AWS Secrets Manager adds managed external secrets support for Auth0, Okta, and Palo Alto Networks"
date: "2026-11-17"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-managed-external-secrets-auth0-okta-palo-alto/"
tags: ["Lambda", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Secrets Manager adds managed external secrets support for Auth0, Okta, and Palo Alto Networks

**날짜:** 2026년 11월 17일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/secrets-manager-managed-external-secrets-auth0-okta-palo-alto/

## 내용

AWS Secrets Manager now supports managed external secrets for Auth0, Okta, and Palo Alto Networks. Long-lived credentials that are not rotated increase the risk of unauthorized access if exposed. Rotating a third-party credential requires coordinated updates to the external service and every application that uses it. You set a rotation schedule from the AWS Management Console or API. Secrets Manager rotates the credential and stores the current value without a custom rotation Lambda function. 
Secrets Manager offers self-rotation and administrator-assisted rotation for Auth0 credentials. With self-rotation, the target application replaces its own secret. With administrator-assisted rotation, a separate Auth0 application with Management API permissions replaces the target application's secret. For Okta, Secrets Manager offers administrator-assisted rotation with a separate administrator JSON Web Token (JWT) key and validates the replacement before deactivating the old secret. For Palo Alto Networks, Secrets Manager offers self-rotation, in which the current API key authorizes its replacement. 
Applications that already retrieve credentials from Secrets Manager receive the rotated value without a code change or deployment.  
These integrations join existing managed external secrets support for BigID, Cisco Security Platform, Confluent Cloud, Databricks, Datadog, GitLab, Jenkins, MongoDB Atlas, Netskope, Paddle, Salesforce, Snowflake, SonarQube, and Twilio. 
Auth0, Okta, and Palo Alto Networks managed external secrets are available in all AWS Regions where AWS Secrets Manager managed external secrets is supported. To learn more, visit the &nbsp;AWS Secrets Manager managed external secrets documentation&nbsp;.

## 핵심 요약

요약 미지원
