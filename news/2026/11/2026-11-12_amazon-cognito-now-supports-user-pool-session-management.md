---
title: "Amazon Cognito now supports user pool session management"
date: "2026-11-12"
service: "CloudFormation"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-session-management/"
tags: ["CloudFormation", "2026", "new-region"]
nav_exclude: true
---

# Amazon Cognito now supports user pool session management

**날짜:** 2026년 11월 12일
**서비스:** CloudFormation
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-cognito-session-management/

## 내용

Amazon Cognito now supports session management for user pools, giving you visibility into and control over the sessions your users establish when they sign in to your applications. Single sign-on (SSO) sessions are created when a user signs in through managed login and let them access other app clients without re-authenticating. Token sessions are created when a user signs in to an app client and receives tokens. Session management lets you list a user's active SSO and token sessions across all devices and app clients and revoke any of them on demand. You can also now configure how long each app client reuses an SSO session before requiring re-authentication, instead of the previous fixed one-hour duration. 
Each session includes details such as session type, app client ID, device type, last activity time and location, and initial sign-in time, so you can build your own end-user or admin session experiences. You can revoke an individual session, optionally with its linked sessions, or use global sign-out to end all sessions associated with one user. You can also set a maximum number of active token sessions per user. 
Session management is available for user pools in the Essentials or Plus feature plans in all AWS Regions where Amazon Cognito is available. You can manage sessions using the AWS Management Console, API, AWS Command Line Interface, and AWS Software Development Kits, and configure settings with AWS CloudFormation. Visit the Developer Guide and API Reference for details.&nbsp;

## 핵심 요약

요약 미지원
