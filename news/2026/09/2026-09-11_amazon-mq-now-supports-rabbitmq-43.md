---
title: "Amazon MQ now supports RabbitMQ 4.3"
date: "2026-09-11"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-mq-rabbitmq-43/"
tags: ["Config", "2026", "new-region", "performance"]
nav_exclude: true
---

# Amazon MQ now supports RabbitMQ 4.3

**날짜:** 2026년 09월 11일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-mq-rabbitmq-43/

## 내용

Amazon MQ now supports RabbitMQ version 4.3 which adds quorum queue feature enhancements such as compaction, increased priority levels, native delayed retries, and graceful consumer timeouts.&nbsp;RabbitMQ 4.3 also includes various bug fixes and performance improvements for memory management. 
Quorum queues on RabbitMQ 4.3 performs compaction to reduce disk usage for queues and native support for 32 strict priority levels, compared to the relative 2 levels supported in previous RabbitMQ versions. Quorum queues can now automatically set failed messages aside and retry delivery after a set cooldown delay. Consumer timeouts have moved from global protocol channels to quorum queues and can be configured specific to the protocol now.&nbsp;Both consumer timeouts and delayed retries can be configured and managed by RabbitMQ Policies. Transient non-exclusive queues, Global QoS, and Classic queues v1 storage are no longer supported on RabbitMQ 4.3. Consumer timeouts also do not apply to classic queues. 
To start using RabbitMQ 4.3 on Amazon MQ, simply select RabbitMQ 4.3 when creating a new broker using the m7g instance type through the AWS Management console, AWS CLI, or AWS SDKs. Amazon MQ automatically manages patch version upgrades for your RabbitMQ 4.3 brokers, so you need to only specify the major.minor version. To learn more about the changes in RabbitMQ 4.3, see the Amazon MQ release notes and the Amazon MQ developer guide. This version is available in all regions where Amazon MQ m7g type instances are available today.&nbsp;

## 핵심 요약

요약 미지원
