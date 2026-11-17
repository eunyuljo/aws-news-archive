---
title: "Set up, connect, and govern AI agents faster with Amazon WorkSpaces"
date: "2026-11-17"
service: "S3"
link: "https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-AI-agents-connect-govern"
tags: ["S3", "2026", "GA", "price-reduction", "performance", "security", "ai-ml"]
nav_exclude: true
---

# Set up, connect, and govern AI agents faster with Amazon WorkSpaces

**날짜:** 2026년 11월 17일
**서비스:** S3
**링크:** https://aws.amazon.com/about-aws/whats-new/2026/11/amazon-workspaces-AI-agents-connect-govern

## 내용

Building AI agents has become essential. Across your organization, teams want agents to handle ERP transactions, work through a claims queue, and operate the same applications your people use every day. But how do you move from experiments to production? Before an agent touches real systems and real data, you need to verify who it acted on behalf of, what it did, and whether it stayed within the limits you set. Without that visibility, the agent stays stuck in testing, and the value is never realized. 
Earlier this year, we launched Amazon WorkSpaces for AI agents, extending the power and security of a cloud work environment to agents, not just people. Today, we're excited to announce new capabilities that make it even easier to operate agents confidently across your enterprise and move them from proof of concept to governed production in fewer steps.&nbsp; You can set up new agents or connect the ones your builders have already built, run them under your own identity providers and policies, and keep a record of everything they do. You don't need to stitch together new tools or build custom monitoring. 
Setup used to mean configuring the machine by hand. Now, you can just describe what your agent needs to your AI coding assistant such as Claude Code, Codex, and Kiro. Guided by AWS MCP skills, the assistant builds the WorkSpace from defaults you can adjust. If your teams build on Amazon Bedrock AgentCore, you can connect an agent directly with your AWS credentials and skip writing any agent code. New tools also reduce agent costs and increase accuracy by letting an agent carry out a series of actions in a single call and use the computer-use actions its model already knows. 
But an agent that can work is not necessarily an agent you can trust with mission-critical work and sensitive data. This release gives you the same oversight over an agent that you have over the employees you manage. First, agents can now sign in through any identity provider (IdP) that supports OIDC, in addition to the existing SAML support. Administrators can send sign-in straight to their IdP, so users authenticate with their usual corporate credentials, and you don't build custom authentication. Second, with on-behalf-of (OBO) sign-in, an agent works as the signed-in user, with that user's existing directory identity, permissions, and Group Policies on the desktop.&nbsp; 
WorkSpaces now offers session replay, giving you a reviewable record of what your agent did. Session replay turns session screenshots into a video and pairs it with a plain-language transcript of the agent's actions. Both are stored in your own Amazon S3 bucket and encrypted with your own keys. Your security team can see what the agent saw, and your compliance team gets evidence to support audits. 
Together, these updates help move agents out of pilots and into real production scale. Your teams can keep working the way they do today, with agents working alongside them in familiar and trusted cloud work environments. And every one of those agents is held to the same identity, policy, and audit standards as the rest of your workforce. With WorkSpaces, you can bring AI agents into your business without rebuilding decades of software or needing a separate environment to govern them. 
To get started operating AI agents on WorkSpaces, visit our documentation page.&nbsp;

## 핵심 요약

요약 미지원
