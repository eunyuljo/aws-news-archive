---
title: "Amazon Kinesis Video Streams now supports VPC endpoints with AWS PrivateLink"
date: "2026-10-02"
service: "Kinesis"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis-video-streams-vpc-privatelink/"
tags: ["Kinesis", "2026", "new-region", "security"]
nav_exclude: true
---

# Amazon Kinesis Video Streams now supports VPC endpoints with AWS PrivateLink

**날짜:** 2026년 10월 02일
**서비스:** Kinesis
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/kinesis-video-streams-vpc-privatelink/

## 내용

Amazon Kinesis Video Streams now supports interface VPC endpoints powered by AWS PrivateLink, providing private connectivity from your Amazon Virtual Private Cloud (Amazon VPC). Traffic between your VPC and Kinesis Video Streams stays on the AWS network and is not exposed to the public internet, across the control plane and the video ingestion and playback data planes.
Customers with strict security, compliance, or network-isolation requirements can now ingest, store, and play back video without internet gateways, NAT devices, or public IP addresses. For example, connected-camera or IoT video workloads in a private subnet can send media to Kinesis Video Streams and retrieve it for playback and analytics entirely over private connectivity. You create the endpoint from the Amazon VPC console, AWS CLI, or AWS SDKs and can attach a VPC endpoint policy to control access.
VPC endpoints for Amazon Kinesis Video Streams are available in all AWS Regions where Amazon Kinesis Video Streams is available, including the AWS GovCloud (US) Regions and the China (Beijing) Region, operated by Beijing Sinnet Technology Co., Ltd. ("Sinnet").
To learn more, see our Getting Started Guide.

## 핵심 요약

요약 미지원
