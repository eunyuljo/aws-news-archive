---
title: "AWS Transfer Family SFTP Connectors now support continuing file transfers during credential rotation"
date: "2026-09-05"
service: "SecretsManager"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-credential-rotation/"
tags: ["SecretsManager", "2026", "new-region"]
nav_exclude: true
---

# AWS Transfer Family SFTP Connectors now support continuing file transfers during credential rotation

**날짜:** 2026년 09월 05일
**서비스:** SecretsManager
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/transfer-family-sftp-credential-rotation/

## 내용

AWS Transfer Family SFTP Connectors now continue running file transfers while you rotate the credentials used to authenticate with remote SFTP servers. You no longer need to update the connector to point to a new secret version each time a credential rotates, removing a manual step and helping avoid failed transfers during the rotation window. 
Connectors can now retrieve credentials from an ordered list of AWS Secrets Manager version stages, such as the current and previous versions, during authentication. The connector automatically tries each version in the order you specify and proceeds with the first that succeeds, so transfers continue uninterrupted as credentials are rotated on either side. You configure this when you create or update a connector, and the connector's credentials must be stored in AWS Secrets Manager. 
Support for continuing transfers during credential rotation is available in all AWS Regions where AWS Transfer Family SFTP Connectors are supported. To learn more, visit the AWS Transfer Family User Guide. Get started with AWS Transfer Family in the AWS Transfer Family console.

## 핵심 요약

요약 미지원
