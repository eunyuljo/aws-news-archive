---
title: "EC2 Amazon Machine Images can now be scanned for vulnerabilities through Amazon Inspector"
date: "2026-11-03"
service: "EC2"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-amis-scanned-through-inspector/"
tags: ["EC2", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# EC2 Amazon Machine Images can now be scanned for vulnerabilities through Amazon Inspector

**날짜:** 2026년 11월 03일
**서비스:** EC2
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/ec2-amis-scanned-through-inspector/

## 내용

Amazon Inspector now extends its vulnerability scanning to EC2 Amazon Machine Images (AMIs), enabling you to identify software vulnerabilities in your AMIs without launching instances or installing additional software. This helps you fix issues at the source before AMIs are used to launch instances across your fleet. 
With this capability, you can run continuous evaluations to monitor your AMI catalog for newly discovered vulnerabilities, or perform targeted one-time scans for specific AMIs directly from the EC2 Console. You can enable AMI scanning for an account or across your entire organization in Amazon Inspector. For AWS Security Hub customers, you can enable AMI scanning as an add-on across your organization, and findings are also delivered to Security Hub. Based on the scan results, you can enable the Allowed AMIs setting and specify security criteria that AMIs must meet to be available within your account and enforce this setting across the entire organization using Declarative Policies. Customers building AMIs with EC2 Image Builder can integrate scanning directly into their pipelines and restrict distribution of AMIs that do not meet their security standards. 
AMI Scanning helps you detect and remediate vulnerabilities earlier in your deployment pipeline, reducing the risk of deploying compromised compute resources. Security teams can now establish a consistent vulnerability scanning process across all AMIs improving their security posture before instances are launched. 
This capability is available in all commercial AWS Regions where Amazon Inspector is available. To learn more, see the EC2 User Guide,&nbsp;Amazon Inspector User Guide,&nbsp;the Amazon Inspector pricing page, and the Amazon Inspector product page.

## 핵심 요약

요약 미지원
