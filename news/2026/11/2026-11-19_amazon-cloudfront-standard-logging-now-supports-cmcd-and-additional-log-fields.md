---
title: "Amazon CloudFront standard logging now supports CMCD and additional log fields"
date: "2026-11-19"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-standard-logging-cmcd-fields"
tags: ["S3", "2026", "performance"]
nav_exclude: true
---

# Amazon CloudFront standard logging now supports CMCD and additional log fields

**날짜:** 2026년 11월 19일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/cloudfront-standard-logging-cmcd-fields

## 내용

Amazon CloudFront standard logging now supports additional access log fields that were previously available only in CloudFront real-time logs. You can now include these fields in your standard logs and deliver them to Amazon S3, Amazon CloudWatch Logs, or Amazon Data Firehose, without setting up an additional data stream for real-time logs. 
The new fields include the IP address of the CloudFront server that handled the request, identifiers that separate traffic on a primary distribution from traffic on a staging distribution, and a media quality confidence score. They also include Common Media Client Data (CMCD) fields, which video players send with each request to report details like bitrate, buffer length, and playback session ID. Streaming teams can use these fields to match playback problems that viewers see with CloudFront delivery data, which makes troubleshooting faster. 
These fields are available in all CloudFront edge locations, and standard logging pricing applies. To learn more, see Standard logging page in the Amazon CloudFront Developer Guide.

## 핵심 요약

요약 미지원
