---
title: "Amazon EventBridge relaunches event buses for enterprise scale"
date: "2026-09-25"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/eventbridge-relaunches-custom-event-buses/"
tags: ["RDS", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon EventBridge relaunches event buses for enterprise scale

**날짜:** 2026년 09월 25일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/eventbridge-relaunches-custom-event-buses/

## 내용

Amazon EventBridge relaunches event buses with a new enhanced Custom event bus that lets you build event-driven applications that decouple teams and can scale with your organization. Create a custom event bus, share it across accounts, and now teams can publish and consume events with strict ordering, open event formats, built-in retention, and support for advanced event transformations.
The EventBridge Custom event bus is a serverless event broker that enables you to create scalable event-driven applications by routing events between your applications, SaaS integrations, and AWS services. It can now be shared with one or more accounts through AWS Resource Access Manager allowing publishers to send events directly to the central event bus. With a new event publishing API, you can now publish events in popular JSON based event formats like CloudEvents and preserve their schema without modification. Custom event buses include 24 hours of built-in retention that can be extended for up to one year allowing you to recover from application errors or hydrate new components from historical data. A new Subscriber resource allows you to filter events and deliver them to over 250 AWS services. Now with native support for strictly ordered use cases, customers can ensure events are processed in the exact order they were received and new event evaluations allow automatic content based deduplication.
To get started, you can create and share the new Custom event bus using the AWS Management Console, AWS CLI, AWS SDKs, Serverless Agent skill, and AWS CloudFormation. To help you separate the existing Custom event bus experience from the new enhanced Custom event bus, we have renamed the existing bus to Custom event bus - classic. All existing APIs remain unchanged.
The enhanced Custom event bus is available at launch in fourteen AWS Regions: United States (N. Virginia, Ohio, Oregon), Europe (Ireland, Frankfurt, Stockholm, Spain), and Asia Pacific (Tokyo, Singapore, Sydney, Malaysia, Thailand, Mumbai, Hong Kong). We have introduced a new pricing model that charges for data transferred rather than events, and rewards you with lower costs as your workloads scale. To learn more, visit Amazon EventBridge.&nbsp;
To learn more, see the AWS News blog, the EventBridge user guide, and the EventBridge product page, or download the agent skills.

## 핵심 요약

요약 미지원
