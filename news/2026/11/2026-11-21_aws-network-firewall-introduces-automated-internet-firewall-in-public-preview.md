---
title: "AWS Network Firewall introduces automated Internet firewall in public preview"
date: "2026-11-21"
service: "VPC"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-automated-internet/"
tags: ["VPC", "2026", "GA", "preview", "new-region", "security"]
nav_exclude: true
---

# AWS Network Firewall introduces automated Internet firewall in public preview

**날짜:** 2026년 11월 21일
**서비스:** VPC
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/network-firewall-automated-internet/

## 내용

AWS Network Firewall announces the public preview of automated Internet firewall, a new centralized control that allows you to configure Network Firewall, with native network address translation (NAT) capability, on the internet gateways of all the Virtual Private Clouds (VPCs) in your environment. Using automated Internet firewall mode, you can centrally define your Network Firewall security rules and enforce them on all inbound and outbound traffic across the internet gateways of your VPCs. You are not required to make routing or architectural changes to deploy automated Internet firewall. You can deploy it across select VPCs or your entire account, organization or organization unit. 
AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your VPC. Customers use it to inspect their traffic and secure AWS resources. Prior to this launch, customers would configure AWS Network Firewalls inside their VPCs in the traffic path of all internet communication to achieve thorough security coverage against the threats on the internet. They deployed Network Firewall endpoints in dedicated subnets and made route updates for every subnet that needed internet access across all their VPCs. In addition, they monitored the environment to ensure that no new internet network paths bypassed these security controls. Automated Internet firewall makes this deployment and management simpler. You just define and maintain filtering rules, and AWS enforces it directly at the internet gateway of every VPC in scope, ensuring that all intended traffic entering or leaving your VPCs via the internet gateway is inspected. Automated Internet firewall comes with built-in NAT functionality for your egress-only internet connectivity needs. You can use it to filter traffic, perform NAT and log all internet activity across all internet gateways. You don't need to make architectural changes inside every VPC or monitor every internet network path. Automated Internet firewall allows you the option to automatically extend your organization's security policy to all future VPCs and subnets at creation. 
To help you get started quickly, automated Internet firewall comes with a default security policy, which uses Amazon managed rule groups including active threat defense that uses AWS unique threat intelligence to protect your workloads against evolving threats on the internet. You can also create your own custom rule groups or use any of the managed rule groups from AWS Marketplace with automated Internet firewall. 
AWS Network Firewall operating in automated Internet firewall mode is available in preview in all AWS Regions except AWS GovCloud and China. To learn more, visit the Network Firewall documentation and see the AWS Network Firewall pricing page. To get started, visit the Amazon VPC or Network Security Manager console.&nbsp;&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
