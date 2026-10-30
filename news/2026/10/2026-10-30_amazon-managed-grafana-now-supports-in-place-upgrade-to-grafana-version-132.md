---
title: "Amazon Managed Grafana now supports in-place upgrade to Grafana version 13.2"
date: "2026-10-30"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/managed-grafana-upgrade-version-13-2/"
tags: ["RDS", "2026", "GA", "new-region"]
nav_exclude: true
---

# Amazon Managed Grafana now supports in-place upgrade to Grafana version 13.2

**날짜:** 2026년 10월 30일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/managed-grafana-upgrade-version-13-2/

## 내용

Amazon Managed Grafana now supports in-place upgrade from Grafana version 12.4 to 13.2. Upgrading to version 13.2 brings features launched as part of open-source Grafana versions 13.0 to 13.2. These include Git Sync for dashboards, dynamic dashboards, and PromQL query support in the Amazon CloudWatch data source plugin.
With Git Sync, you can treat dashboards as code by linking a workspace to a Git repository. Dashboard modifications can be tracked, reviewed, and reverted through version control. Dynamic dashboards bring a more adaptable approach to layout and paneling. You can construct responsive views driven by conditions that respond to the data and variables in scope. With Amazon CloudWatch data source plugin support for Prometheus Query Language, you can use PromQL to query metrics that CloudWatch takes in via its OpenTelemetry (OTLP) endpoint, in addition to the existing Metric Search and Metrics Insights query types.
In-place upgrade to Grafana 13.2 is supported in all AWS regions where Amazon Managed Grafana is generally available. You can upgrade with just a few clicks from the AWS Console, AWS SDK or AWS CLI. For a complete list of new features, refer to Differences between Grafana versions in the Amazon Managed Grafana User Guide. For upgrade instructions, see Update your workspace version. To learn more about Amazon Managed Grafana features and its pricing, visit the product page and pricing page.

## 핵심 요약

요약 미지원
