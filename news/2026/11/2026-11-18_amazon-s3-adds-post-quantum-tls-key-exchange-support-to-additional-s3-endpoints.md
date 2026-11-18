---
title: "Amazon S3 adds post-quantum TLS key exchange support to additional S3 endpoints"
date: "2026-11-18"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-key-exchange-support/"
tags: ["S3", "2026", "price-reduction", "new-region"]
nav_exclude: true
---

# Amazon S3 adds post-quantum TLS key exchange support to additional S3 endpoints

**날짜:** 2026년 11월 18일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-s3-post-quantum-tls-key-exchange-support/

## 내용

Amazon S3 adds post-quantum TLS (PQ-TLS) key exchange support to S3 Vectors and AWS PrivateLink for Amazon S3 interface endpoints. This extends the post-quantum cryptography support already available on regional S3, S3 Tables, and S3 Express One Zone endpoints. 
S3 Vectors endpoints and PrivateLink interface endpoints now support Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), one of the National Institute of Standards and Technology (NIST) standardized post-quantum cryptographic algorithms. PQ-TLS key exchange is available to all clients configured to use the ML-KEM key exchange algorithm. S3 Vectors and PrivateLink endpoints automatically negotiate the strongest key exchange that your client software supports, so clients that support ML-KEM receive the benefits of PQ-TLS key exchange without any changes to your applications or endpoint configuration. 
PQ-TLS key exchange for S3 Vectors and AWS PrivateLink for S3 is supported at no additional cost in all AWS Regions. To learn more about PQ-TLS support in S3, visit the Amazon S3 User Guide.

## 핵심 요약

요약 미지원
