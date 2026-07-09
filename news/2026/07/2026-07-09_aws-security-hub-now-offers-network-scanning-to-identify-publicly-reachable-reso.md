---
title: "AWS Security Hub now offers Network Scanning to identify publicly reachable resources"
date: "2026-07-09"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-network-scanning/"
tags: ["Config", "2026", "security"]
nav_exclude: true
---

# AWS Security Hub now offers Network Scanning to identify publicly reachable resources

**날짜:** 2026년 07월 09일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/aws-security-hub-network-scanning/

## 내용

Today, AWS Security Hub introduces Network Scanning, a capability that identifies resources in your environment that are reachable from the public internet.&nbsp; Network Scanning probes your resources from the internet to detect actual reachability, not just what could be reachable based on security group rules and route tables. It discovers public IP addresses, virtual machines, and load balancers across your AWS and Azure environments, identifies reachable ports, and determines what services are running behind them. This complements Security Hub’s existing network reachability findings, which identify configurations that could make a resource reachable from the internet.&nbsp;&nbsp;Network Scanning confirms actual reachability from the internet. Each reachable port generates a Security Hub finding with evidence of the port and service discovered. Security Hub Exposures then automatically correlates these findings with other findings and resource configurations to determine broader risk.

## 핵심 요약

요약 미지원
