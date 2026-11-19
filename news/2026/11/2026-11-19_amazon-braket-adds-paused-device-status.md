---
title: "Amazon Braket adds PAUSED device status"
date: "2026-11-19"
service: "General"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/braket-new-device-state/"
tags: ["General", "2026", "new-region"]
nav_exclude: true
---

# Amazon Braket adds PAUSED device status

**날짜:** 2026년 11월 19일
**서비스:** General
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/braket-new-device-state/

## 내용

Amazon Braket now offers a new device status, PAUSED, to give customers clear and actionable information on when they can submit quantum tasks and hybrid jobs and when those tasks and jobs will run. Device status now tells you: 
 
 ONLINE: The device is accepting quantum tasks and hybrid jobs and is actively processing them during its availability window. 
 (New) PAUSED: The device is accepting quantum tasks and hybrid jobs but isn't processing them right now, because it is outside its availability window, in short-term maintenance, or in a reservation. Tasks and jobs you submit stay QUEUED and run once the device is ONLINE. 
 OFFLINE: The device is unavailable and isn't accepting new quantum tasks or hybrid jobs, for example due to scheduled maintenance, upgrades, or operational issues. 
 RETIRED: The device has been permanently decommissioned and is no longer available on Amazon Braket. 
 
When a device is PAUSED, a Status Reason is provided with additional information on why it's paused, when the status began, and an estimated end time if one is available. You can view device status on the Devices page in the Amazon Braket console, or programmatically with the GetDevice and SearchDevices APIs or the Amazon Braket SDK. For example, the GetDevice API will return one of the following status reasons for PAUSED state: OUTSIDE_AVAILABILITY_WINDOW, MAINTENANCE, or RESERVATION. 
Amazon Braket is available in the US East (N. Virginia), US West (N. California), US West (Oregon), Europe (London), and Europe (Stockholm) AWS Regions. To learn more, see the Amazon Braket Developer Guide.

## 핵심 요약

요약 미지원
