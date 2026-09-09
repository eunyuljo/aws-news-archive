---
title: "Amazon Timestream for InfluxDB 3 now supports custom plugins"
date: "2026-09-09"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/timestream-influxdb-custom-plugins/"
tags: ["SecretsManager", "2026", "new-region"]
nav_exclude: true
---

# Amazon Timestream for InfluxDB 3 now supports custom plugins

**날짜:** 2026년 09월 09일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/timestream-influxdb-custom-plugins/

## 내용

Amazon Timestream for InfluxDB now lets you run your own custom Python plugins on the managed versions of InfluxDB 3 Core and Enterprise editions. You host your plugin code in public or private repositories you control and the engine fetches and runs it in response to triggers, letting you implement logic specific to your workload without standing up separate external infrastructure. 
Plugins run on the trigger types the processing engine already supports and with them, you can build custom data transformations, alerting, aggregation, and integrations with your own services, all running close to your data. Plugins execute in a managed Python environment that includes the standard library and Amazon-vetted packages , so you can move workload-specific processing into the database instead of operating a separate pipeline to do it. 
To get started, set a plugin repository on a DB parameter group, apply that parameter group to your cluster, and create triggers that reference your plugin using the influxdb3 CLI or HTTP API; private repositories are authenticated with a token stored in AWS Secrets Manager.&nbsp; Custom plugins are available in all AWS Regions where Amazon Timestream for InfluxDB is available. To get started with Amazon Timestream for InfluxDB 3, visit the Amazon Timestream for InfluxDB console. For more information, see the Amazon Timestream for InfluxDB documentation and pricing page.&nbsp; 
&nbsp; &nbsp;

## 핵심 요약

요약 미지원
