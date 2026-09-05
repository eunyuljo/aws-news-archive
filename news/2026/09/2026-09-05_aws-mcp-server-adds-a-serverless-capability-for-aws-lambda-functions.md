---
title: "AWS MCP Server adds a serverless capability for AWS Lambda functions"
date: "2026-09-05"
service: "Lambda"
link: "https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/"
tags: ["Lambda", "2026", "price-reduction", "new-region", "performance", "ai-ml"]
nav_exclude: true
---

# AWS MCP Server adds a serverless capability for AWS Lambda functions

**날짜:** 2026년 09월 05일
**서비스:** Lambda
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/09/aws-mcp-server-serverless/

## 내용

Today, AWS Model Context Protocol Server (AWS MCP Server) added a serverless capability so that coding agents such as Claude Code and Kiro can efficiently diagnose issues with your Lambda functions. The serverless capability helps you troubleshoot your running Lambda functions and their connected resources. 
The AWS MCP Server, available through the Agent Toolkit for AWS or as a standalone installation, is a managed service that gives AI coding agents secure access to AWS services. With the new serverless capability in the AWS MCP Server, your coding agent inspects your Lambda function and its connected resources across Amazon API Gateway, Amazon EventBridge, Amazon S3, Amazon DynamoDB, Amazon SNS, Amazon SQS, and AWS Step Functions. The agent can correlate error signals against a 7-day baseline to pinpoint what changed, surface recurring errors to identify trends, retrieve the deployed configuration of your function and connected resources, provide a timeline of recent changes to track what happened, and analyze service latency across connected resources. As the agent gets comprehensive data in a single call, it consumes fewer tokens compared to orchestrating multiple API calls. 
To get started, configure the Agent toolkit for AWS by running ‘aws configure agent-toolkit’ from the AWS CLI, or enable the AWS MCP Server directly. 
The AWS MCP Server can access services in all commercial AWS Regions, while the AWS MCP Server itself runs in the US East (N. Virginia) and Europe (Frankfurt) Regions. The serverless diagnostic capabilities in the AWS MCP Server are available at no additional cost. To learn more, see the user guide.&nbsp;&nbsp;&nbsp;

## 핵심 요약

요약 미지원
