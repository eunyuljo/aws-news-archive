---
title: "Amazon WorkSpaces Applications adds support for smart card redirection"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-applications-smart-card-redirection/"
tags: ["RDS", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon WorkSpaces Applications adds support for smart card redirection

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-applications-smart-card-redirection/

## 내용

Amazon WorkSpaces Applications now supports smart card redirection on single-session and multi-session fleets, so users can access the smart card connected to their local device from applications inside their streaming session. It also extends smart card sign-in, previously limited to single-session fleets, to multi-session fleets. This launch helps public sector, healthcare, and other regulated organizations that use Common Access Card (CAC) or Personal Identity Verification (PIV) cards run those workflows on multi-session fleets. 
Administrators can turn smart card sign-in for Active Directory and smart card redirection on or off independently for each stack. Smart card sign-in lets users sign in to domain-joined streaming instances with their smart card instead of a password, while redirected smart cards support in-session authentication, digital signing, and email encryption. For example, a government agency can move CAC users from single-session to multi-session fleets and keep CAC sign-in. 
These capabilities are available today in all AWS commercial and AWS GovCloud (US) regions that offer WorkSpaces Applications. 
To get started, turn on either setting under User settings for your stack, use a Windows image with the latest WorkSpaces Applications agent, and connect with the WorkSpaces Applications client for Windows. New stacks have both settings turned off by default, and existing stacks that use smart card redirection keep it turned on. To learn more, see Create a stack in the Amazon WorkSpaces Applications Administration Guide, or visit the Amazon WorkSpaces Applications product page.

## 핵심 요약

요약 미지원
