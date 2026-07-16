---
title: "Amazon Cognito now supports importing users with password hashes"
date: "2026-07-16"
service: "RDS"
link: "https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/"
tags: ["RDS", "2026", "new-region"]
nav_exclude: true
---

# Amazon Cognito now supports importing users with password hashes

**날짜:** 2026년 07월 16일
**서비스:** RDS
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-cognito-password-hash-import/

## 내용

Amazon Cognito now supports importing users with password hashes in CSV user imports. Previously, users imported from a CSV file had to reset their passwords on first sign-in. Now, you can include password hashes in your CSV file so that imported users can sign in immediately with their existing credentials.  When creating a CSV import, you specify the password hashing algorithm used by your source system. Amazon Cognito imports these users and verifies their password against the imported hash on first sign-in. Supported algorithms include bcrypt, scrypt, Argon2id, and PBKDF2 with SHA-256. All imported hashes receive an additional layer of cryptographic protection before storage.  Password hash import is available in all AWS Regions where Amazon Cognito is available. To get started, create a user import using the AWS Management Console, AWS Command Line Interface (CLI), or AWS Software Development Kits (SDKs). See the developer guide for instructions.

## 핵심 요약

요약 미지원
