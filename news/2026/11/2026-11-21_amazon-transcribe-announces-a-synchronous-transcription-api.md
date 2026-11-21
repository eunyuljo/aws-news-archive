---
title: "Amazon Transcribe announces a synchronous transcription API"
date: "2026-11-21"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-transcribe-sync-api/"
tags: ["S3", "2026", "new-region"]
nav_exclude: true
---

# Amazon Transcribe announces a synchronous transcription API

**날짜:** 2026년 11월 21일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-transcribe-sync-api/

## 내용

Amazon Transcribe now offers a synchronous transcription API, TranscribeAudio. Send a complete audio file in a single request and get the full transcript back in the same response. There is no job to start, no status to poll, no connection to manage.&nbsp;The transcripts are as accurate as Amazon Transcribe batch transcription, so you can add fast, accurate speech-to-text to interactive applications such as voice assistants, agent-assist tools and on-demand "transcribe this clip" features. 
The synchronous API supports the Amazon Transcribe features you already use, including: 
 
 Word-level timestamps and smart formatting for numbers, dates, currency and phone numbers 
 Automatic language identification 
 Speaker diarization, and channel identification for up to two channels 
 Custom vocabulary and vocabulary filtering, which you can provide directly in the request with no setup step 
 PII redaction 
 
Send audio inline (up to 25 MB) or from Amazon S3 (up to 500 MB), 0.5 seconds to 1 hour long, in WAV, MP3, FLAC, M4A, MP4, Ogg, WebM or AMR format. The transcript comes back in the response, or Transcribe can write it to an S3 location you choose. Pricing is $0.0070 per minute of audio, billed per second, with speaker diarization, language identification, custom vocabulary and channel identification included. Two-channel audio is billed once on file duration. PII redaction is available as an add-on. 
Supports English, Spanish, French, Italian, German, Japanese, Portuguese, Korean and Chinese (Simplified, Traditional and Hong Kong).&nbsp;Available in US East (N. Virginia, Ohio), US West (Oregon), Canada (Central), Europe (Ireland, London, Frankfurt), Asia Pacific (Mumbai, Singapore, Sydney, Tokyo, Seoul) and South America (São Paulo), with PII redaction available in all stated Regions except South America (São Paulo). 
To get started, see&nbsp;Amazon Transcribe API Reference and the Amazon Transcribe pricing page.

## 핵심 요약

요약 미지원
