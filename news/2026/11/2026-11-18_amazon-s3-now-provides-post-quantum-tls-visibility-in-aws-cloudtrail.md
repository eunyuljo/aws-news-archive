---
title: "Amazon S3 now provides post-quantum TLS visibility in AWS CloudTrail"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-aws-cloudtrail/"
tags: ["S3", "2026", "price-reduction", "new-region", "security"]
nav_exclude: true
---

# Amazon S3 now provides post-quantum TLS visibility in AWS CloudTrail

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-aws-cloudtrail/

## 내용

Amazon S3 now records the TLS key exchange algorithm in AWS CloudTrail for S3 requests, so you can see which requests and clients use post-quantum TLS (PQ-TLS). With this visibility, you can measure the share of your S3 traffic that is protected with post-quantum cryptography, and identify the applications, SDK versions, and IAM principals that still connect with classical key exchange and need to be upgraded. 
The new keyExchange value in the tlsDetails field of CloudTrail management and data events shows the key exchange negotiated on each TLS connection, such as the hybrid post-quantum algorithm X25519MLKEM768 or a traditional algorithm such as x25519. For example, you can query your CloudTrail logs to find the user agents of S3 requests that did not use ML-KEM, then prioritize those clients for your post-quantum migration. The keyExchange value is recorded for requests to general purpose buckets, directory buckets, table buckets, and vector buckets, including requests made through AWS PrivateLink. 
Key exchange details for S3 requests are available in all AWS Regions at no additional cost. Standard AWS CloudTrail pricing applies for S3 data events. To learn more, visit post-quantum TLS in the Amazon S3 User Guide and the CloudTrail record contents reference.

## 핵심 요약

요약 미지원
