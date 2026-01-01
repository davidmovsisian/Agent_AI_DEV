# Module 6: LLM as the Agent Brain

## Overview

Learn how LLMs serve as the cognitive engine of AI agents, enabling them to perceive, reason, and act autonomously. This module covers the agent architecture and the observe-think-act loop.

**Duration**: 2-3 hours

## Learning Objectives

- Understand agent architecture and components
- Implement the observe-think-act loop
- Design effective agent prompting strategies
- Enable planning and reasoning in agents

## Key Concepts

### Agent Architecture
```
Environment → Observe → Think → Act → Environment
                ↑                    ↓
                └────────────────────┘
```

### The Agent Loop
1. **Observe**: Gather information from environment
2. **Think**: Reason about what to do (LLM role)
3. **Act**: Execute actions via tools
4. **Learn**: Update memory and state

### Agent Prompting
Special prompting techniques for agent behavior:
- Role definition for agents
- Goal-oriented instructions
- Action space definition
- Reasoning encouragement

## Code Examples

- `agent_loop.py` - Basic agent loop implementation
- `observe_think_act.py` - Full observe-think-act cycle
- `agent_prompting.py` - Agent-specific prompting
- `planning_reasoning.py` - Planning and reasoning patterns

## Exercises

Build foundational agents including:
- Simple reflex agent
- Goal-based agent
- Planning agent
- Learning agent

## Next Steps

Continue to [Module 7: Tool Use & Function Calling](../Module-07-Tool-Use-Function-Calling/lesson.md)

---

*Full detailed content available in course materials.*
