---
title: "AWS Transfer Family now supports custom CloudWatch log groups for managed workflows"
date: "2026-10-02"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-custom-cloudwatch-log-groups/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# AWS Transfer Family now supports custom CloudWatch log groups for managed workflows

**날짜:** 2026년 10월 02일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/transfer-family-custom-cloudwatch-log-groups/

## 내용

AWS Transfer Family now lets you choose a custom log group in Amazon CloudWatch Logs for managed workflow execution logs. You can organize workflow logs to monitor individual workflows separately or bring logs from related workflows together.
Previously, every workflow attached to a Transfer Family server sent its execution logs to that server’s CloudWatch log group, so you could not set a separate log destination for each workflow. When creating a workflow through the AWS Transfer Family console or API, you can now select a workflow-level log group that is separate from the server’s log group. Transfer Family delivers workflow logs only to the selected group, so no server logging role is required. Workflow logs retain their existing structured JSON format and remain queryable using Amazon CloudWatch Logs Insights. You can also send logs from multiple workflows to a shared log group to create consolidated metrics and dashboards for tracking workflow execution. If you do not select a structured log destination, workflow logs continue using the server’s role-based logging configuration when configured. Existing workflows continue using their current logging configuration.
This feature is available in all AWS Regions where Transfer Family managed workflows are offered. To learn more, visit the Transfer Family managed workflows User Guide.

## 핵심 요약

요약 미지원
