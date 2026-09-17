---
title: "Amazon Corretto 27 is now generally available"
date: "2026-09-17"
service: "Connect"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-corretto-27-generally-available/"
tags: ["Connect", "2026", "GA", "preview", "price-reduction", "performance"]
nav_exclude: true
---

# Amazon Corretto 27 is now generally available

**날짜:** 2026년 09월 17일
**서비스:** Connect
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/amazon-corretto-27-generally-available/

## 내용

Amazon Corretto 27, a Feature Release (FR) version, is now available for download. Amazon Corretto is a no-cost, multi-platform, production-ready distribution of OpenJDK. You can download Corretto 27 for Linux, Windows, and macOS from our downloads page. Corretto 27 will be supported through April 2027. Noticeable features:&nbsp; 
 
 G1 as the Default Garbage Collector in All Environments - Makes G1 the default garbage collector across all environments, delivering more consistent performance and predictable pause times regardless of where your application runs (JEP 523) 
 Post-Quantum Hybrid Key Exchange for TLS 1.3 - Adds protection against future quantum computing threats by combining classical and post-quantum key exchange algorithms in TLS 1.3 connections (JEP 527) 
 Compact Object Headers by Default - Reduces the memory footprint of Java objects by enabling smaller object headers by default, improving memory efficiency and cache utilization (JEP 534) 
 JFR In-Process Data Redaction - Allows sensitive data to be redacted from Java Flight Recorder recordings before they leave the JVM, helping protect confidential information during profiling and diagnostics (JEP 536) 
 Enhanced Pattern Matching (continued preview) - Extends support for primitive types in patterns, instanceof, and switch, letting developers write cleaner type and value checks including for types like int and boolean (JEP 532) 
 Structured Concurrency (continued preview) - Refines the API for structured concurrency, treating groups of related tasks running in different threads as single units of work, streamlining error handling and cancellation, improving reliability, and enhancing observability (JEP 533) 
 Lazy Constants (continued preview) - Provides an API to defer initialization of immutable data until it is actually needed, combining the performance benefits of final fields with the flexibility of lazy initialization (JEP 531) 
 Vector API (continued incubator) - Improves support for high-performance mathematical operations that can take advantage of modern CPU vector capabilities (JEP 537) 
 
A detailed description of these features can be found on the OpenJDK 27 Project page. Amazon Corretto 27 is distributed by Amazon under an open source license.

## 핵심 요약

요약 미지원
