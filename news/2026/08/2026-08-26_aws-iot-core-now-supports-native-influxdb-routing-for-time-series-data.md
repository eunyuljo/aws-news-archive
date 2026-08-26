---
title: "AWS IoT Core now supports native InfluxDB routing for time-series data"
date: "2026-08-26"
service: "Timestream"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iot-core-influxdb/"
tags: ["Timestream", "2026", "price-reduction", "new-region", "performance"]
nav_exclude: true
---

# AWS IoT Core now supports native InfluxDB routing for time-series data

**날짜:** 2026년 08월 26일
**서비스:** Timestream
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/aws-iot-core-influxdb/

## 내용

AWS IoT Core now supports InfluxDB rule action that routes time-series data from your Internet of Things (IoT) devices directly to InfluxDB databases, without writing custom device-side code or using intermediate cloud services. AWS IoT Core is a fully managed service that securely connects billions of IoT devices to the AWS cloud, and routes IoT device data to AWS and third-party services. 
The new InfluxDB rule action automatically converts time-series data from your device to InfluxDB’s line protocol format and writes it to either an Amazon Timestream managed or a self-hosted InfluxDB cluster. The new rule action also supports the following two batching modes to help you optimize cost and throughput: device-side batching, where your devices send pre-batched payloads to AWS IoT Core; and server-side batching, where IoT rules engine aggregates individual messages before writing to InfluxDB. For example, a life sciences company can batch thousands of telemetry readings from scientific instruments at millisecond granularity and write directly to InfluxDB for monitoring, without building a custom data pipeline. 
To get started, connect your IoT devices to AWS IoT Core and define an InfluxDB rule action specifying the destination database, along with authentication and batching parameters. The InfluxDB rule action is available in all AWS Global Regions where Amazon Timestream for InfluxDB is available. To learn more, visit the AWS IoT Core developer guide.

## 핵심 요약

요약 미지원
