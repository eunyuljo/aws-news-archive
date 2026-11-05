---
title: "Amazon ECS Managed Daemons can now collect json-file logs from application containers on Amazon ECS Managed Instances"
date: "2026-11-05"
service: "ECS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-managed-instances-json-file-log-driver/"
tags: ["ECS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon ECS Managed Daemons can now collect json-file logs from application containers on Amazon ECS Managed Instances

**날짜:** 2026년 11월 05일
**서비스:** ECS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-ecs-managed-instances-json-file-log-driver/

## 내용

Amazon Elastic Container Service (Amazon ECS) introduces json-file log driver support for Amazon ECS Managed Instances and log driver volumes for Amazon ECS Managed Daemons. Together, these features let you collect application logs with the observability agent of your choice and forward them to any destination you choose.  With this launch, your application containers on ECS Managed Instances can write their logs as local files in standard Docker json-file format, which most observability agents read natively. Your managed daemons can directly read these files through a volume mount, without specifying host bind mount paths or requiring root privileges. As a result, one managed daemon on each instance can collect logs from every application container that uses the json-file log driver. Amazon ECS keeps each container's logs in a dedicated directory named with the container ID and retains them until the container is removed, so your managed daemon can use native file-based log collection and trace every log back to the container that produced it.  To get started, set the log driver to json-file in the logConfiguration of your application task definition. Next, register a daemon task definition that specifies a volume with logDriverVolumeConfiguration, and mount the volume into your daemon container using mountPoints. You can configure this using the AWS Management Console, AWS CLI, API, AWS SDKs or AWS CloudFormation. This feature is available in all commercial AWS Regions where Amazon ECS Managed Instances and Managed Daemons are available, at no additional cost. To learn more, refer to our documentation page and visit Amazon ECS Managed Instances.

## 핵심 요약

요약 미지원
