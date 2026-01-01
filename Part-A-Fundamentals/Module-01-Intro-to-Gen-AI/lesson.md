# Module 1: Introduction to Generative AI and LLMs

## Overview

Welcome to the first module of the AI Agent Developer Course! This module introduces you to Generative AI and Large Language Models (LLMs), the foundational technology powering modern AI agents. You'll learn how LLMs work, how to interact with them via APIs, and understand critical concepts like tokens and pricing.

**Duration**: 2-3 hours

## Learning Objectives

By the end of this module, you will be able to:
- Explain the difference between Generative AI and traditional AI
- Understand how Large Language Models (LLMs) work at a high level
- Make API calls to different LLM providers (OpenAI, Anthropic)
- Calculate token usage and estimate API costs
- Choose appropriate models for different use cases
- Apply best practices for working with LLMs

## Prerequisites

- Basic Python programming knowledge
- Completed [Setup Guide](../../resources/setup-guide.md)
- API keys for at least one LLM provider

## Table of Contents

1. [What is Generative AI?](#what-is-generative-ai)
2. [Understanding Large Language Models](#understanding-large-language-models)
3. [Popular LLM Providers](#popular-llm-providers)
4. [Working with LLM APIs](#working-with-llm-apis)
5. [Tokens: The Currency of LLMs](#tokens-the-currency-of-llms)
6. [Understanding Pricing](#understanding-pricing)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)

---

## What is Generative AI?

### Traditional AI vs. Generative AI

**Traditional AI** (Discriminative AI):
- Analyzes and classifies existing data
- Examples: Image classification, spam detection, recommendation systems
- Output: Labels, categories, predictions from fixed set of options
- Limited to what it was explicitly trained to recognize

**Generative AI**:
- Creates new content that didn't exist before
- Examples: Text generation, image creation, code synthesis, music composition
- Output: Novel content (text, images, code, etc.)
- Can generalize to tasks it wasn't explicitly trained for

### Why This Matters

Generative AI, particularly LLMs, enables us to build **agents** - systems that can:
- Understand complex instructions in natural language
- Reason about problems and devise solutions
- Generate human-like responses and content
- Adapt to new situations without retraining
- Use tools and take actions in the real world

This flexibility makes LLMs ideal "brains" for autonomous agents.

---

## Understanding Large Language Models

### What is an LLM?

A **Large Language Model** is a neural network trained on massive amounts of text data (billions to trillions of words) to:
1. Predict the next word/token in a sequence
2. Understand language patterns, grammar, facts, and reasoning
3. Generate coherent, contextually appropriate text

### The Transformer Architecture

Modern LLMs are based on the **Transformer** architecture (2017):

```
Input Text → Tokenization → Embeddings → Transformer Layers → Output Probabilities
                                           ↓
                              [Self-Attention Mechanism]
                              [Feed-Forward Networks]
```

**Key Concepts**:
- **Self-Attention**: Allows the model to weigh the importance of different words in context
- **Parallel Processing**: Unlike RNNs, transformers process all tokens simultaneously
- **Positional Encoding**: Tracks word order in the sequence

### Training Process

LLMs are typically trained in stages:

1. **Pre-training**: Learn language patterns from massive text corpus (unsupervised)
   - Objective: Predict next token
   - Data: Books, websites, code repositories (trillions of tokens)
   - Result: "Base model" with broad knowledge

2. **Fine-tuning**: Adapt to specific tasks (supervised)
   - Instruction tuning: Learn to follow instructions
   - RLHF (Reinforcement Learning from Human Feedback): Align with human preferences
   - Result: Models like GPT-3.5-turbo, GPT-4

### Model Sizes

LLM capability generally scales with:
- **Parameter count**: Number of learnable weights (7B, 13B, 70B, 175B+)
- **Training data**: More diverse data = better generalization
- **Training compute**: More GPU hours = better performance

Common sizes:
- **Small** (7B-13B parameters): Fast, cheap, good for simple tasks (Llama 2 7B)
- **Medium** (30B-70B): Balanced performance (Llama 2 70B)
- **Large** (175B+): Best performance, slower, expensive (GPT-4, Claude 3 Opus)

---

## Popular LLM Providers

### OpenAI (GPT Models)

**Models**:
- **GPT-4-turbo**: Most capable, expensive ($10/M input tokens)
- **GPT-3.5-turbo**: Fast, affordable, good for most tasks ($0.50/M tokens)
- **GPT-4o**: Optimized for speed and cost

**Strengths**:
- Industry leader, most widely used
- Excellent function calling support
- Strong code generation
- Fast response times

**Best for**: Production applications, complex reasoning, code generation

### Anthropic (Claude Models)

**Models**:
- **Claude 3 Opus**: Most capable, rivals GPT-4
- **Claude 3 Sonnet**: Balanced performance and cost
- **Claude 3 Haiku**: Fast and economical

**Strengths**:
- Longer context windows (200K tokens!)
- Strong safety features and alignment
- Excellent at analysis and writing
- Less prone to hallucination

**Best for**: Long document analysis, safety-critical applications, creative writing

### Google (Gemini Models)

**Models**:
- **Gemini Pro**: Competitive with GPT-3.5-turbo
- **Gemini Ultra**: Competes with GPT-4

**Strengths**:
- Multimodal (text, images, audio)
- Integrated with Google services
- Competitive pricing

**Best for**: Multimodal applications, Google ecosystem integration

### Open Source Options

**Meta Llama 2/3**:
- Can run locally with sufficient hardware
- No API costs, full control
- Good for experimentation and learning

**Mistral**:
- High-quality open models
- API available or self-hosted

---

## Working with LLM APIs

### Basic API Structure

All LLM APIs follow similar patterns:

```python
1. Initialize client with API key
2. Create messages (system, user, assistant)
3. Call API with model name and parameters
4. Extract response from result
```

### OpenAI API Example

```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain recursion in simple terms."}
    ],
    temperature=0.7,
    max_tokens=150
)

print(response.choices[0].message.content)
```

### Anthropic API Example

```python
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=150,
    messages=[
        {"role": "user", "content": "Explain recursion in simple terms."}
    ]
)

print(response.content[0].text)
```

### Key Parameters

**temperature** (0.0 - 2.0):
- 0.0-0.3: Deterministic, focused, factual (good for data extraction)
- 0.7-1.0: Balanced creativity (good for general tasks)
- 1.0-2.0: Very creative, random (good for brainstorming)

**max_tokens**: Maximum length of response
- Includes both input and output for some models
- Balance between completeness and cost

**top_p** (0.0 - 1.0): Alternative to temperature
- Controls diversity of word selection
- 0.9-0.95 typical values

**presence_penalty** & **frequency_penalty**: Discourage repetition

---

## Tokens: The Currency of LLMs

### What is a Token?

Tokens are the basic units LLMs process:
- **Roughly** 1 token ≈ 0.75 words (English)
- **Roughly** 1 token ≈ 4 characters

**Examples**:
- "Hello world" = 2 tokens
- "ChatGPT is amazing!" = 5 tokens
- "artificial intelligence" = 2-3 tokens
- "I'm" = 1 token (common contraction)
- "uncommonword" = might be 2-3 tokens

### Why Tokens Matter

1. **API Pricing**: Charged per token (input + output)
2. **Context Limits**: Models have maximum token capacity (4K, 8K, 128K)
3. **Speed**: More tokens = longer processing time
4. **Cost Control**: Understanding tokens helps manage expenses

### Tokenization Process

```
Text → Byte Pair Encoding (BPE) → Token IDs → Model Processing

"Hello world!" → ["Hello", " world", "!"] → [15496, 995, 0] → Processing
```

Common words = 1 token, rare words = multiple tokens

### Counting Tokens

Use `tiktoken` library for OpenAI models:

```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "How many tokens is this sentence?"
tokens = encoding.encode(text)
print(f"Token count: {len(tokens)}")  # Output: 7
```

**Pro Tip**: Always count tokens before sending to API to avoid surprises!

---

## Understanding Pricing

### Cost Structure

LLM APIs typically charge:
1. **Input tokens**: Text you send (prompts, context)
2. **Output tokens**: Text the model generates

**Formula**: `Total Cost = (Input Tokens × Input Price) + (Output Tokens × Output Price)`

### Pricing Examples (2024)

**OpenAI GPT-3.5-turbo**:
- Input: $0.50 per 1M tokens
- Output: $1.50 per 1M tokens
- **Example**: 1000 input tokens + 500 output tokens = $0.00125

**OpenAI GPT-4**:
- Input: $30 per 1M tokens
- Output: $60 per 1M tokens
- **Example**: 1000 input tokens + 500 output tokens = $0.06 (48x more expensive!)

**Anthropic Claude 3 Haiku**:
- Input: $0.25 per 1M tokens
- Output: $1.25 per 1M tokens
- **Example**: 1000 input tokens + 500 output tokens = $0.000875 (cheaper than GPT-3.5!)

### Cost Optimization Strategies

1. **Choose appropriate models**: Don't use GPT-4 when GPT-3.5 suffices
2. **Minimize input tokens**: Send only necessary context
3. **Limit output tokens**: Set `max_tokens` appropriately
4. **Cache responses**: Store and reuse common queries
5. **Batch requests**: Combine multiple queries when possible
6. **Use streaming**: For better UX, not cost savings

### Real-World Cost Examples

**Chatbot (10K users, 10 messages/user/month)**:
- Average: 100 input + 50 output tokens per message
- Total: 1M input + 500K output tokens
- **GPT-3.5 cost**: $1.25/month
- **GPT-4 cost**: $60/month

**Document Analysis (1000 docs/month)**:
- Average: 5000 input + 500 output tokens per doc
- Total: 5M input + 500K output tokens
- **GPT-3.5 cost**: $3.25/month
- **GPT-4 cost**: $180/month

---

## Best Practices

### 1. Start Simple

Begin with basic prompts and iterate:
```python
# Bad: Overly complex first attempt
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Analyze this dataset considering statistical significance, outliers, correlations..."}]
)

# Good: Start simple, add complexity as needed
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Summarize the key trends in this data."}]
)
```

### 2. Handle Errors Gracefully

```python
from openai import OpenAI, APIError, RateLimitError
import time

def call_llm_with_retry(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except RateLimitError:
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
        except APIError as e:
            print(f"API error: {e}")
            raise
```

### 3. Monitor Usage

Track tokens and costs:
```python
total_input_tokens = 0
total_output_tokens = 0

response = client.chat.completions.create(...)

total_input_tokens += response.usage.prompt_tokens
total_output_tokens += response.usage.completion_tokens

print(f"Input: {total_input_tokens}, Output: {total_output_tokens}")
print(f"Estimated cost: ${(total_input_tokens * 0.0000005 + total_output_tokens * 0.0000015):.4f}")
```

### 4. Use Environment Variables

Never hardcode API keys:
```python
# Bad
client = OpenAI(api_key="sk-proj-...")

# Good
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### 5. Set Reasonable Limits

Prevent runaway costs:
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[...],
    max_tokens=500,  # Limit output length
    timeout=30  # Prevent hanging requests
)
```

---

## Common Pitfalls

### 1. Ignoring Token Limits

**Problem**: Sending text that exceeds context window
**Solution**: Check token count before sending, implement chunking if needed

### 2. Using Expensive Models Unnecessarily

**Problem**: Using GPT-4 for simple tasks
**Solution**: Test with GPT-3.5 first, upgrade only if needed

### 3. Not Handling Rate Limits

**Problem**: Rapid requests causing failures
**Solution**: Implement exponential backoff and request queuing

### 4. Expecting Determinism

**Problem**: Assuming same input = same output
**Solution**: Set temperature=0 for consistency, but accept some variability

### 5. Forgetting About Latency

**Problem**: Poor UX from slow responses
**Solution**: Use streaming, show loading states, optimize prompts

---

## Summary

In this module, you learned:
- ✅ Generative AI creates new content, unlike traditional discriminative AI
- ✅ LLMs are trained on massive text data using transformer architecture
- ✅ Popular providers: OpenAI (GPT), Anthropic (Claude), Google (Gemini)
- ✅ APIs follow similar patterns: client → messages → call → response
- ✅ Tokens are the basic units (≈0.75 words), affecting cost and limits
- ✅ Pricing varies widely; GPT-4 is ~50x more expensive than GPT-3.5
- ✅ Best practices: start simple, handle errors, monitor usage, protect API keys

## Next Steps

1. Complete the [exercises](exercises.md) to practice what you learned
2. Experiment with the [code examples](examples/) in this module
3. Move on to [Module 2: Prompt Engineering](../Module-02-Prompts-Engineering/lesson.md)

## Additional Resources

- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer)
- [Anthropic Pricing](https://www.anthropic.com/pricing)
- [Transformers Explained (Visual)](https://jalammar.github.io/illustrated-transformer/)
- [LLM Pricing Comparison](https://artificialanalysis.ai/models)

---

**Congratulations!** You've completed Module 1. You now understand the fundamentals of LLMs and how to interact with them via APIs. Ready to learn how to craft effective prompts? Continue to Module 2! 🚀
