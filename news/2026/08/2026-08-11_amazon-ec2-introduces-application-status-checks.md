---
title: "Amazon EC2 introduces application status checks"
date: "2026-08-11"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-application-status-checks"
tags: ["EC2", "2026", "new-region"]
nav_exclude: true
---

# Amazon EC2 introduces application status checks

**날짜:** 2026년 08월 11일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ec2-application-status-checks

## 내용

Amazon EC2 introduces application status checks, a new status check that helps customers detect and respond to application-level issues on their EC2 instances. With application status checks, EC2 monitors applications to detect issues such as a web server that has stopped accepting requests, a Docker daemon that is not running, an incorrect networking configuration, or a network interface that is no longer passing traffic. 
Customers rely on EC2 status checks today to receive alerts when an instance or the underlying system is unreachable. However, to monitor application issues, customers had to build and maintain their own monitoring solution. Now, with application status checks customers can monitor the status of their applications running on EC2 instances alongside existing EC2 instance and system status checks. Customers create a check by specifying the protocol, port, and path to monitor, along with the response codes that indicate a healthy application. After customers associate the check with their instances by instance ID or tag, Amazon EC2 sends HTTP or HTTPS requests to that port and path and reports on the application’s status every 60 seconds. Auto Scaling groups act on application status, initiating recovery by replacing instances when their applications report unhealthy. 
Application status checks are available in all commercial AWS Regions and AWS GovCloud (US) Regions. 
To get started with application status checks and review pricing, see the Amazon EC2 User Guide.

## 핵심 요약

요약 미지원
