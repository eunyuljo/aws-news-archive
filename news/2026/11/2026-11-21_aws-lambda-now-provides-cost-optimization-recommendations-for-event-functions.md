---
title: "AWS Lambda now provides cost optimization recommendations for Event Functions"
date: "2026-11-21"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-cost-optimization-recommendations/"
tags: ["Lambda", "2026", "GA", "price-reduction", "new-region"]
nav_exclude: true
---

# AWS Lambda now provides cost optimization recommendations for Event Functions

**날짜:** 2026년 11월 21일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/aws-lambda-cost-optimization-recommendations/

## 내용

AWS Lambda now provides cost optimization recommendations for Event Functions in AWS Trusted Advisor.&nbsp;These recommendations identify on-demand functions&nbsp;where moving to Lambda Managed Instances (LMI) is estimated to reduce costs, and provide configuration guidance for running on LMI. With&nbsp;these recommendations, you can lower your Lambda costs by focusing your efforts on the functions with the greatest estimated savings. 
LMI&nbsp;lets you run Lambda functions on Amazon EC2 instances while maintaining the operational simplicity of Lambda. With LMI, you can access specialized compute configurations and drive cost efficiency through EC2 pricing options such as Savings Plans and Reserved Instances, without managing infrastructure. Previously, to determine whether a function was a good fit for LMI, you had to analyze its invocation patterns, estimate LMI costs, and select the right instance type and memory-to-vCPU ratio yourself. This manual process added overhead and delayed savings. With this launch, Lambda automatically analyzes the invocation patterns, duration, and resource utilization of your high-volume Event Functions and recommends those where LMI is estimated to reduce costs. Estimates are based on a simulation of each function's invocation patterns, using public&nbsp;Lambda pricing and Amazon EC2 On-Demand pricing.&nbsp;Each recommendation includes the function ARN,&nbsp;the recommended EC2 instance type and memory-to-vCPU ratio, the estimated current&nbsp;cost, the estimated LMI cost, and the estimated savings. You can use the recommended configuration to run a function on LMI without sizing it yourself and realize cost savings sooner. 
These recommendations are available in the following AWS Regions: US East (N. Virginia), US West (Oregon), Europe (Ireland), and Europe (Milan). Customers with eligible AWS Support plans&nbsp;can access them in the Trusted Advisor console alongside other cost optimization checks. To learn more, visit the AWS Lambda Developer Guide,&nbsp;the AWS Trusted Advisor User Guide, and the AWS Lambda pricing.

## 핵심 요약

요약 미지원
