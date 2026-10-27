---
title: "AWS Key Management Service now supports ML-KEM for post-quantum key encapsulation"
date: "2026-10-27"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/10/kms-ml-kem-post-quantum/"
tags: ["RDS", "2026", "new-region", "security"]
nav_exclude: true
---

# AWS Key Management Service now supports ML-KEM for post-quantum key encapsulation

**날짜:** 2026년 10월 27일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/10/kms-ml-kem-post-quantum/

## 내용

AWS Key Management Service (KMS) now supports Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM), a post-quantum cryptography standard under NIST FIPS 203, which&nbsp;enables two parties to establish a shared secret.&nbsp;NIST designed ML-KEM to replace the classical key-establishment schemes, like DH/ECDH key agreement, and RSA-based key transport, in their strategic cryptographic roadmap&nbsp;(see NIST IR 8547).&nbsp;ML-KEM addresses the "harvest now, decrypt later" threat to those classical schemes, where an adversary records the key-establishment exchange today and recovers the shared secret once sufficiently powerful quantum computers become available. 
KMS supports all three ML-KEM key specs defined in NIST FIPS 203: ML-KEM-512, ML-KEM-768, and ML-KEM-1024. The Encapsulate API uses the public key to produce a random 32-byte shared secret and its ciphertext form. The Decapsulate API recovers the shared secret from ciphertext using the corresponding private key. KMS protects the private key of an ML-KEM key pair in FIPS 140-3 Level 3 validated hardware security modules (HSMs). You can use the GetPublicKey API to export the public key and distribute it to partners, client applications, or external systems for performing the encapsulate operation locally using cryptographic libraries like AWS-LC, OpenSSL, or Bouncy Castle. 
ML-KEM is available in all AWS Regions where KMS is available, except the the Middle East (UAE), Middle East (Bahrain), and China Regions. For more information, see Key spec reference in the AWS KMS Developer Guide.

## 핵심 요약

요약 미지원
