---
title: "IAM Policy Autopilot now supports Terraform plan files"
date: "2026-08-19"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/iam-policy-autopilot-now-supports-terraform-plan-files"
tags: ["RDS", "2026", "GA", "price-reduction", "security"]
nav_exclude: true
---

# IAM Policy Autopilot now supports Terraform plan files

**날짜:** 2026년 08월 19일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/iam-policy-autopilot-now-supports-terraform-plan-files

## 내용

IAM Policy Autopilot can now generate baseline IAM policies directly from a Terraform plan file. IAM Policy Autopilot is an open source tool, launched at re:Invent 2025, that analyzes your code to deterministically create scoped-down IAM policies you can refine as your application evolves, reducing the time you spend writing IAM policies and troubleshooting access issues. Until now the tool analyzed application source code, but it was not possible to generate policies for deploying AWS infrastructure defined via Infrastructure as Code. 
Now you can pass a Terraform plan file as input, and IAM Policy Autopilot applies a deterministic analysis to produce a policy scoped to the CRUD functions of the resources in that plan. The generated policies reference specific resource ARNs rather than wildcards, when possible. Supporting policy generation for deploying AWS infrastructure defined via Terraform has been the most requested capability since IAM Policy Autopilot launched, and it complements the existing Terraform-aware analysis, which cross-references Terraform resource definitions with SDK calls in your application code to resolve ARNs. 
IAM Policy Autopilot is available at no additional cost and runs on your own machine. To get started, visit the IAM Policy Autopilot GitHub repository.

## 핵심 요약

요약 미지원
