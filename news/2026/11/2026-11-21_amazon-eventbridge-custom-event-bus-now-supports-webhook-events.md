---
title: "Amazon EventBridge Custom event bus now supports Webhook Events"
date: "2026-11-21"
service: "EventBridge"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-webhook-events"
tags: ["EventBridge", "2026", "new-region", "ai-ml"]
nav_exclude: true
---

# Amazon EventBridge Custom event bus now supports Webhook Events

**날짜:** 2026년 11월 21일
**서비스:** EventBridge
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-eventbridge-webhook-events

## 내용

Amazon EventBridge now supports Webhook Events for the enhanced Custom event bus, so SaaS applications, AI agents, and custom integrations can send events to a bus over HTTPS. You no longer need to deploy and operate your own API endpoint and compute to receive webhooks and publish them to your bus. 
The EventBridge Custom event bus is a serverless event broker that enables you to create scalable event-driven applications by routing events between your applications, SaaS integrations, and AWS services. When you create a webhook event source on your bus, EventBridge provides a managed HTTPS URL and verifies each request using an HMAC signature, a static token, or basic authentication. EventBridge then publishes accepted events to the bus, where Subscribers filter and deliver them like any other event. For example, shipment status updates from a logistics partner can reach your order tracking and customer notification Subscribers as soon as the partner sends them. 
Webhook Events are available in all AWS Regions where the enhanced Custom event bus is available. Events received through a webhook are billed as standard Custom event bus ingress, with no additional charge for the webhook. 
To learn more, see Webhook Events in the Amazon EventBridge User Guide and the Amazon EventBridge product page. Install the Agent Toolkit for AWS to start building with your AI coding agent.

## 핵심 요약

요약 미지원
