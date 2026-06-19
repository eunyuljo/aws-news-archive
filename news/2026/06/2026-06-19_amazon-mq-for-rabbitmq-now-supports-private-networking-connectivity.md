---
title: "Amazon MQ for RabbitMQ now supports private networking connectivity"
date: "2026-06-19"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-mq-private-network-connectivity/"
tags: ["VPC", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon MQ for RabbitMQ now supports private networking connectivity

**날짜:** 2026년 06월 19일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/05/amazon-mq-private-network-connectivity/

## 내용

Amazon MQ for RabbitMQ now supports private networking, enabling your brokers to connect to private resources in your VPC without exposing those resources publicly.. This helps you meet your security and compliance requirements when your brokers need to reach private identity providers (such as LDAP and OAuth 2.0), other Amazon MQ for RabbitMQ brokers, or self-hosted RabbitMQ brokers. Previously, this connectivity for RabbitMQ Federation, Shovel, or authentication required&nbsp;Network Load Balancer and NAT Gateway workarounds.  Amazon MQ establishes this connectivity using Amazon VPC Lattice, AWS Resource Access Manager (AWS RAM), and AWS PrivateLink, and manages the underlying infrastructure on your behalf. To get started, create a VPC Lattice resource gateway, package your resource configurations into an AWS RAM resource share, and associate it with your broker.  Private networking is available only for Amazon MQ for RabbitMQ brokers, in all AWS Regions where Amazon VPC Lattice is available. To learn more, see Private networking in the Amazon MQ Developer Guide and the Amazon MQ pricing page.

## 핵심 요약

요약 미지원
