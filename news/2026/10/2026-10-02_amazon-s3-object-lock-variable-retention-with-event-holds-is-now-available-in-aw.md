---
title: "Amazon S3 Object Lock variable retention with event holds is now available in AWS GovCloud (US) Regions"
date: "2026-10-02"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/s3-object-lock-variable-retention-event-holds-aws-govcloud/"
tags: ["S3", "2026", "GA", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 Object Lock variable retention with event holds is now available in AWS GovCloud (US) Regions

**날짜:** 2026년 10월 02일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/s3-object-lock-variable-retention-event-holds-aws-govcloud/

## 내용

Amazon S3 Object Lock support for variable retention with event holds is now available in AWS GovCloud (US-East) and AWS GovCloud (US-West).
Amazon S3 Object Lock variable retention allows you to apply write-once-read-many (WORM) protection to objects whose required retention period starts with a future event, such as a contract closing or an audit completing. You place an event hold with a retention duration on an object and S3 protects the object while the hold is in place. When you release the hold, S3 retains the object for the duration you specified. Unlike legal holds, which end protection immediately upon removal, event holds provide WORM compliance for the required retention period after the triggering event, so you can meet event-based retention requirements without retaining data longer than your policy requires.
 
 
 To learn more, read the AWS Storage Blog post, the S3 Object Lock overview page, and the S3 documentation. This capability has been assessed by Cohasset Associates for use in environments subject to SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC Regulation 1.31.

## 핵심 요약

요약 미지원
