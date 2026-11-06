---
title: "AWS Network Load Balancer is now available in the AWS Phoenix Local Zone"
date: "2026-11-06"
service: "EBS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/aws-nlb-available-phx-local-zone/"
tags: ["EBS", "2026", "GA", "new-region", "performance"]
nav_exclude: true
---

# AWS Network Load Balancer is now available in the AWS Phoenix Local Zone

**날짜:** 2026년 11월 06일
**서비스:** EBS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/aws-nlb-available-phx-local-zone/

## 내용

AWS Network Load Balancer is now available in the Phoenix Local Zone (us-west-2-phx-2a). AWS Local Zones is a type of AWS infrastructure deployment that places AWS compute, storage, database, and other select services closer to large population, industry, and IT centers where no AWS Region exists today. 
With this launch, you can create an AWS Network Load Balancer directly in the Phoenix Local Zone. Previously, if your targets ran in the Phoenix Local Zone, you had to place the load balancer in an Availability Zone in the parent Region, so connections and their traffic had to travel to the parent Region and back. This added latency and routed traffic outside the zone where your application runs. Now, connection routing stays local to your targets, delivering lower and more consistent latency to end users in the Phoenix metro area and keeping traffic within the Local Zone. This is especially valuable for latency-sensitive workloads such as real-time gaming, media streaming, and live financial applications serving users in the region. 
To learn more about Network Load Balancer, visit the documentation. For more information on AWS Local Zones, visit the AWS Local Zones website. The Locations webpage lists the available and announced Local Zones. You can enable AWS Local Zones from the Local Zones tab in the AWS Global View console, or the ModifyAvailabilityZoneGroup API.

## 핵심 요약

요약 미지원
