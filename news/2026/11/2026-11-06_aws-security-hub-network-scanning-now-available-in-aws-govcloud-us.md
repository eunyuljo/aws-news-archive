---
title: "AWS Security Hub Network Scanning now available in AWS GovCloud (US)"
date: "2026-11-06"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-govcloud/"
tags: ["Config", "2026", "GA", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Security Hub Network Scanning now available in AWS GovCloud (US)

**날짜:** 2026년 11월 06일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-govcloud/

## 내용

AWS Security Hub Network Scanning feature is now supported in AWS GovCloud (US). 
Network Scanning probes your resources from the internet to detect actual reachability, not just what could be reachable based on security group rules and route tables. It discovers public IP addresses, virtual machines, and load balancers across your AWS environments, identifies reachable ports, and determines what services are running behind them. This complements Security Hub's existing network reachability findings, which identify configurations that could make a resource reachable from the internet. Network Scanning confirms that configurations do exist which make a resource reachable from the internet. Each reachable port generates a Security Hub finding with evidence of the port and service discovered. Security Hub Exposures then automatically correlates these findings with other findings and resource configurations to determine broader risk. 
Existing customers can enable Network Scanning in individual accounts and regions, or across an organization via a configuration policy. For new Security Hub customers, Network Scanning is on by default. Network Scanning is included with Security Hub Essentials at no additional cost in all AWS commercial and GovCloud (US) Regions that support Security Hub. To learn more, see the AWS Security Hub User Guide and the AWS Security Hub product page. For the full list of Regions, see the AWS Regional Services List.

## 핵심 요약

요약 미지원
