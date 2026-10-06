---
title: "AWS Client VPN now supports device posture assessment"
date: "2026-10-06"
service: "SystemsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-client-vpn-device-posture/"
tags: ["SystemsManager", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Client VPN now supports device posture assessment

**날짜:** 2026년 10월 06일
**서비스:** SystemsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-client-vpn-device-posture/

## 내용

AWS Client VPN now supports device posture assessment, allowing you to verify that connecting user devices meet your security and compliance requirements before granting network access. This feature integrates with your existing device posture providers, so only trusted, compliant devices can access your AWS resources through Client VPN.
Previously, Client VPN authenticated users through certificates, SAML, or Active Directory. With device posture assessment, you can now also integrate &nbsp;CrowdStrike&nbsp;, &nbsp;Jamf&nbsp;, or &nbsp;JumpCloud&nbsp; with Client VPN to automatically evaluate device security signals such as compliance scores, encryption status, and risk level before allowing a connection. You define these requirements using &nbsp;Cedar policies&nbsp;, giving you fine-grained control over which devices can connect. To help you author and validate these policies, Client VPN provides you a Test Policy tool that guides you through creating Cedar policies for your device posture requirements.
This feature continuously re-evaluates device compliance during active sessions, and automatically disconnects a session if a device falls out of compliance, such as when risk score or security settings change. You can also use this feature in monitoring-only mode, which logs posture evaluation results without disconnecting sessions, so you can assess the impact of your policies before enforcing them. Device posture assessment works alongside your existing authorization rules to provide defense in depth.
This feature is available in all AWS Regions where AWS Client VPN is available, at no additional cost. This feature requires AWS VPN Client version 6.2.0 or later.
To learn more about Client VPN:

 Visit the AWS Client VPN &nbsp;product page


 Download the &nbsp;AWS VPN Client


 Read the AWS Client VPN &nbsp;administrator guide


 Read the AWS Client VPN &nbsp;user guide

## 핵심 요약

요약 미지원
