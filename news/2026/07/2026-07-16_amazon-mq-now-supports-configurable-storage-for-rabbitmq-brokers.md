---
title: "Amazon MQ now supports configurable storage for RabbitMQ brokers"
date: "2026-07-16"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mq-rabbitmq-configurable-storage/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# Amazon MQ now supports configurable storage for RabbitMQ brokers

**날짜:** 2026년 07월 16일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-mq-rabbitmq-configurable-storage/

## 내용

Amazon MQ now allows you to configure the EBS Disk storage size for RabbitMQ brokers independently of instance type. When creating or updating a broker, you can define a custom storage size, allowing you to right-size storage independently of your instance size to match your specific messaging workload requirements. Configurable storage is available for RabbitMQ M7g brokers on version 4.2 or later using cluster deployments only. 
With configurable storage, you can choose a storage size from the default value on M7g to the maximum allowed value depending on your instance size in increments of 5 GB. You can specify the Storage Size using the using the AWS Console, AWS CloudFormation, AWS Command Line Interface (CLI), or the AWS Cloud Development Kit (CDK). Storage changes are applied during the next broker reboot.&nbsp; 
Standard Amazon MQ storage pricing applies based on the disk size as per Amazon MQ pricing. Configurable storage is available in all commercial AWS Regions where Amazon MQ for RabbitMQ is offered. To learn more, see the Amazon MQ Developer Guide.

## 핵심 요약

요약 미지원
