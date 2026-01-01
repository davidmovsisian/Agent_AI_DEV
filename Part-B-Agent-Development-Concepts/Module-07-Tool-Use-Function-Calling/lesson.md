# Module 7: Tool Use and Function Calling

## Overview

Master function calling APIs and the ReAct pattern to build agents that can use external tools effectively. This is a critical capability for practical agents.

**Duration**: 3-4 hours

## Learning Objectives

- Use OpenAI and Anthropic function calling APIs
- Implement the ReAct (Reasoning + Acting) pattern
- Build custom tools for agents
- Handle errors and edge cases in tool use

## Key Concepts

### Function Calling
Modern LLMs can call functions with structured parameters:
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "parameters": {...}
    }
}]
```

### The ReAct Pattern
**Re**asoning + **Act**ing in a loop:
1. Thought: "I need to find the weather"
2. Action: Call get_weather("Seattle")
3. Observation: "Temperature is 65°F"
4. Thought: "Now I can answer the user"

### Custom Tools
Building domain-specific tools:
- Tool definition and schemas
- Input validation
- Error handling
- Response formatting

## Code Examples

- `function_calling_basics.py` - OpenAI/Anthropic function calling
- `react_pattern.py` - Complete ReAct implementation
- `custom_tools.py` - Building custom tools
- `error_handling.py` - Robust error handling

## Exercises

- Implement weather tool agent
- Build calculator tool set
- Create web search agent
- Add error recovery

## Next Steps

Continue to [Module 8: Memory & State Management](../Module-08-Memory-State-Management/lesson.md)
