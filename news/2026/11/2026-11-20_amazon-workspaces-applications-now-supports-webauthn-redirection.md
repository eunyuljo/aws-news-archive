---
title: "Amazon WorkSpaces Applications now supports WebAuthn redirection"
date: "2026-11-20"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-applications-webauthn-redirection/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon WorkSpaces Applications now supports WebAuthn redirection

**날짜:** 2026년 11월 20일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-applications-webauthn-redirection/

## 내용

Amazon WorkSpaces Applications now supports WebAuthn redirection, so users can sign in to websites and applications in their streaming session with a FIDO2 authenticator on their local device, such as a security key, Windows Hello, or Touch ID. Previously, an authenticator attached to the user's computer was not available inside the streaming session, so organizations that require phishing-resistant multi-factor authentication (MFA) had to use weaker sign-in methods or keep those applications off WorkSpaces Applications. This helps organizations with FIDO2 requirements stream those applications. 
When an application in the session makes a WebAuthn request, WorkSpaces Applications forwards it to the user's device, where the authenticator signs it and returns the response. Private keys never leave the user's device. Administrators turn it on per stack in the console or API, and on Windows fleets can limit it to an allow list of processes. For example, a bank can let employees sign in to Microsoft 365 in their streaming session with the same security key they use on their laptop. 
WebAuthn redirection is available at no additional charge in all AWS commercial Regions and AWS GovCloud (US) Regions where WorkSpaces Applications is available. 
To get started, select Enable WebAuthn redirection under User Settings for your stack, use an image with the WorkSpaces Applications agent released on or after October 20, 2026, and connect with the WorkSpaces Applications client for Windows (1.5.0 or later) or macOS (1.6.0 or later). To learn more, see WebAuthn redirection in the Amazon WorkSpaces Applications Administration Guide, or visit the Amazon WorkSpaces Applications product page.

## 핵심 요약

요약 미지원
