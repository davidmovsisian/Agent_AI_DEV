# Module 3: Context Engineering

## Overview

Context engineering goes beyond single prompts to manage larger information flows. You'll learn how to structure system prompts, maintain conversation history, optimize context windows, and integrate external data effectively.

**Duration**: 2-4 hours

## Learning Objectives

By the end of this module, you will be able to:
- Distinguish between system and user prompts and use each effectively
- Manage multi-turn conversation history
- Optimize context windows to stay within token limits
- Inject relevant external data into context
- Integrate tool outputs seamlessly

## Key Concepts

### System vs User Prompts
- System prompts: Define AI's role and behavior (persistent instructions)
- User prompts: Specific queries or tasks  
- Effective separation of concerns

### Conversation History Management
- Storing and retrieving message history
- Summarization techniques for long conversations
- Context window sliding strategies

### Context Optimization
- Prioritizing important information
- Chunking and summarization
- Token budget management

### Data Injection
- Formatting external data for context
- Temporal awareness (dates, versions)
- Source attribution

## Code Examples

This module includes:
- `system_vs_user_prompts.py` - Comparing prompt types
- `conversation_history.py` - Managing multi-turn conversations
- `context_management.py` - Optimizing context windows
- `tool_output_context.py` - Integrating tool results

## Exercises

Complete hands-on exercises including:
- Building a stateful chatbot
- Implementing context summarization
- Creating a conversation manager class
- Integrating external API data into context

## Next Steps

After mastering context engineering, you'll be ready to learn about MCP in [Module 4](../Module-04-Intro-to-MCP/lesson.md).

---

*Full content for this module includes detailed explanations, working code examples, and comprehensive exercises. See the examples directory for runnable code.*
