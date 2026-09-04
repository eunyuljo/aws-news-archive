---
title: "Amazon SES now supports S/MIME email signing"
date: "2026-09-04"
service: "Lex"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-supports-smime-signing"
tags: ["Lex", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon SES now supports S/MIME email signing

**날짜:** 2026년 09월 04일
**서비스:** Lex
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-ses-supports-smime-signing

## 내용

Amazon Simple Email Service (SES) now supports Secure/Multipurpose Internet Mail Extensions (S/MIME) signing, giving you a way to help recipients verify your emails are authentic.&nbsp;An S/MIME signature lets recipients confirm that a message was sent by the holder of the From address and that its content was not altered in transit. 
Previously, senders who needed S/MIME had to sign each message themselves before submitting it to SES, adding complexity to their sending.&nbsp;With this feature, you store your signing certificate in AWS Certificate Manager and enable S/MIME signing for your sender identity. SES then signs your messages automatically as you send, so you don't have to sign messages yourself beforehand. Recipients whose email clients don't support S/MIME can still read the message normally. This gives security-conscious senders a simple way to add digital signatures to their email while continuing to use their existing SES setup. 
This feature is available in all AWS Regions where Amazon SES is available.&nbsp;To learn more about S/MIME signing in Amazon SES, visit the Amazon SES console or refer to the documentation.

## 핵심 요약

요약 미지원
