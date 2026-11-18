---
title: "AWS Security Hub Network Scanning now supports scanning Amazon Relational Database Service (Amazon RDS) database instances"
date: "2026-11-18"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-rds/"
tags: ["RDS", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# AWS Security Hub Network Scanning now supports scanning Amazon Relational Database Service (Amazon RDS) database instances

**날짜:** 2026년 11월 18일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/security-hub-network-scanning-rds/

## 내용

AWS Security Hub Network Scanning now scans Amazon RDS DB instances to identify those that are reachable from the internet. Network Scanning automatically discovers existing and new RDS DB instances in your accounts and scans each instance that has Public Access configured. For each reachable port associated with a DB instance, Security Hub creates a finding with details about the instance and the reachable port.
RDS scanning gives you more visibility into which resources in your environment are reachable from the internet. You can then investigate and update their access settings as needed. RDS scanning is turned on automatically for all customers who already have Network Scanning enabled.
Network Scanning probes your resources from the internet to detect reachability, beyond what security group rules and route tables suggest. Security Hub Exposures then correlates these findings with other findings and resource configurations to assess broader risk.
Existing Security Hub customers can enable Network Scanning in individual accounts and Regions, or across an organization with a configuration policy. For new Security Hub customers, Network Scanning is on by default. Network Scanning is included with Security Hub Essentials at no additional cost in all AWS commercial and AWS GovCloud (US) Regions that support Security Hub. To learn more, see the AWS Security Hub User Guide and the AWS Security Hub product page. For the full list of Regions, see the AWS Regional Services List.

## 핵심 요약

요약 미지원
