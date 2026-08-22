---
title: "Amazon SES now supports open and click tracking override parameters"
date: "2026-08-22"
service: "Config"
link: "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-adds-open-click-tracking-override/"
tags: ["Config", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon SES now supports open and click tracking override parameters

**날짜:** 2026년 08월 22일
**서비스:** Config
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-ses-adds-open-click-tracking-override/

## 내용

Amazon Simple Email Service (SES) now supports open and click tracking override parameters in the SendEmail and SendBulkEmail APIs. Senders can enable or disable open tracking and click tracking on an individual API call, rather than managing tracking preferences through separate configuration sets.  Previously, controlling tracking behavior required maintaining a distinct configuration set for each combination of open- and click-tracking settings. With this new capability, you specify the tracking preference directly in the send request, reducing configuration overhead and simplifying how you honor recipient-level tracking consent. This is useful for senders that must respect per-recipient consent choices to meet data protection requirements such as GDPR and CNIL guidance.  The tracking overrides apply per request and take precedence over the tracking behavior defined in the associated configuration set, giving you fine-grained control without changing your existing configuration set structure. There is no additional cost to use this feature.  This capability is available in all AWS Regions where Amazon SES is available. 
To learn more, see the documentation on open and click tracking in the Amazon SES Developer Guide.&nbsp;

## 핵심 요약

요약 미지원
