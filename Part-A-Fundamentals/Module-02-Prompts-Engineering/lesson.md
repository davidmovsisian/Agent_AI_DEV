# Module 2: Prompt Engineering

## Overview

Prompt engineering is the art and science of crafting effective instructions for Large Language Models. This module teaches you how to write prompts that consistently produce high-quality, relevant outputs. You'll learn proven techniques used by professionals to get the most out of LLMs.

**Duration**: 2-4 hours

## Learning Objectives

By the end of this module, you will be able to:
- Write clear, effective prompts using role and goal framing
- Apply few-shot learning to guide model behavior
- Use positive and negative prompting strategically
- Structure step-by-step instructions for complex tasks
- Format inputs and outputs consistently
- Debug and improve underperforming prompts

## Prerequisites

- Completed [Module 1: Intro to Gen AI](../Module-01-Intro-to-Gen-AI/lesson.md)
- Basic understanding of LLM APIs
- Python environment set up with API keys

## Table of Contents

1. [What is Prompt Engineering?](#what-is-prompt-engineering)
2. [The Anatomy of a Good Prompt](#the-anatomy-of-a-good-prompt)
3. [Role and Goal Setting](#role-and-goal-setting)
4. [Few-Shot Learning](#few-shot-learning)
5. [Positive vs Negative Prompting](#positive-vs-negative-prompting)
6. [Step-by-Step Instructions](#step-by-step-instructions)
7. [Input/Output Formatting](#inputoutput-formatting)
8. [Prompt Debugging](#prompt-debugging)
9. [Best Practices](#best-practices)

---

## What is Prompt Engineering?

### Definition

**Prompt Engineering** is the process of designing, refining, and optimizing text inputs to elicit desired responses from language models. It's both an art (creativity, intuition) and a science (systematic testing, iteration).

### Why It Matters

Even powerful models like GPT-4 need good prompts:
- **Same model, different results**: A well-crafted prompt can transform mediocre output into excellent output
- **Cost efficiency**: Better prompts often need fewer tokens and fewer retries
- **Consistency**: Good prompts produce more reliable, predictable results
- **Safety**: Proper prompting can reduce harmful or incorrect outputs

### The Evolution of Prompting

```
Simple Prompts (2020)          Modern Prompting (2024)
"Summarize this"        →      Role: "As a technical writer..."
                               Goal: "Create a concise summary..."
                               Context: "For an executive audience..."
                               Format: "Use bullet points..."
                               Examples: "Like this: ..."
```

---

## The Anatomy of a Good Prompt

### Core Components

A well-structured prompt typically includes:

```
1. ROLE: Who should the AI be?
2. GOAL: What is the desired outcome?
3. CONTEXT: What background information is relevant?
4. CONSTRAINTS: What limitations or requirements exist?
5. FORMAT: How should the output be structured?
6. EXAMPLES: What does good output look like?
```

### Example Comparison

**❌ Poor Prompt:**
```
Write about AI.
```

**✅ Good Prompt:**
```
Role: You are an experienced tech journalist writing for a general audience.

Goal: Write a 200-word introduction to artificial intelligence that explains 
what it is and why it matters.

Audience: Readers with no technical background.

Format: 
- Start with a hook
- Define AI in simple terms
- Give 2-3 real-world examples
- End with why it's important

Tone: Informative but conversational, avoid jargon.
```

---

## Role and Goal Setting

### Assigning Roles

Giving the AI a specific role activates relevant knowledge and behavior patterns:

**Effective Roles:**
```python
# Professional roles
"You are an experienced Python developer..."
"You are a patient math tutor..."
"You are a creative marketing copywriter..."

# Behavioral roles
"You are a careful code reviewer who catches edge cases..."
"You are a skeptical analyst who questions assumptions..."
"You are an encouraging teacher who explains concepts clearly..."
```

### Setting Clear Goals

Be specific about what you want:

**❌ Vague:**
```
"Help me with this code."
```

**✅ Specific:**
```
"Review this Python function for potential bugs, focusing on:
1. Edge cases (empty inputs, None values)
2. Type safety issues
3. Performance problems
Provide specific line-by-line suggestions."
```

### The Power of Perspective

Different roles produce different outputs:

```python
Prompt: "Explain recursion"

As a computer science professor:
→ Formal, theoretical, with mathematical notation

As a coding bootcamp instructor:
→ Practical, uses real-world analogies, focuses on implementation

As a children's book author:
→ Simple language, creative metaphors, storytelling approach
```

---

## Few-Shot Learning

### What is Few-Shot Learning?

Providing examples of desired input-output pairs to guide the model's behavior.

**Types:**
- **Zero-shot**: No examples (just instructions)
- **One-shot**: One example
- **Few-shot**: Multiple examples (typically 2-5)

### When to Use Few-Shot

✅ Use few-shot when:
- The desired format is complex or unusual
- The task requires specific patterns
- Instructions alone aren't producing consistent results
- You want to show edge case handling

❌ Avoid few-shot when:
- The task is straightforward
- It would consume too many tokens
- The examples might bias the output incorrectly

### Few-Shot Examples

**Example 1: Sentiment Classification**

```
Classify the sentiment as positive, negative, or neutral.

Examples:
Input: "This product exceeded my expectations!"
Output: positive

Input: "Shipping was slower than expected but product is okay."
Output: neutral

Input: "Completely disappointed. Waste of money."
Output: negative

Now classify:
Input: "Great quality, would buy again."
Output:
```

**Example 2: Data Extraction**

```
Extract key information in JSON format.

Example 1:
Input: "John Smith, age 32, lives in Seattle"
Output: {"name": "John Smith", "age": 32, "city": "Seattle"}

Example 2:
Input: "Email me at sarah@email.com, I'm 28"
Output: {"name": null, "age": 28, "city": null, "email": "sarah@email.com"}

Now extract:
Input: "I'm Mike, 45 years old from Boston"
Output:
```

---

## Positive vs Negative Prompting

### Positive Prompting

Tell the model what TO do:

```python
✅ "Write a professional email confirming the meeting for Tuesday at 2 PM."

✅ "Explain this concept using simple language and everyday analogies."

✅ "Focus on the technical specifications and performance metrics."
```

### Negative Prompting

Tell the model what NOT to do:

```python
✅ "Explain this concept. Do not use technical jargon or abbreviations."

✅ "Summarize the article. Do not include your own opinions or analysis."

✅ "Generate ideas. Do not filter for feasibility—be creative and ambitious."
```

### When to Use Each

**Use Positive Prompting:**
- Primary guidance
- When you know exactly what you want
- For constructive direction

**Use Negative Prompting:**
- To prevent common mistakes
- To override default behaviors
- To set boundaries

**Combine Both:**
```python
Prompt = """
Write a product description that:
- DO: Highlights benefits, uses emotional language, includes a call-to-action
- DON'T: Make exaggerated claims, use technical jargon, exceed 100 words
"""
```

### Common Pitfalls

❌ **Too many negatives:**
```
"Don't be boring, don't be too long, don't use jargon, don't be vague..."
```
This confuses the model about what you actually want.

✅ **Balance positive guidance with strategic negatives:**
```
"Write an engaging, concise explanation for a general audience. 
Avoid technical jargon."
```

---

## Step-by-Step Instructions

### Breaking Down Complex Tasks

For complex tasks, provide explicit steps:

**Example: Code Review Prompt**

```
Review this Python code following these steps:

Step 1: Read the code and summarize what it does in one sentence.

Step 2: Check for correctness:
- Does it handle edge cases?
- Are there any logical errors?
- Will it produce the expected output?

Step 3: Check for quality:
- Is the code readable and well-structured?
- Are variable names descriptive?
- Is there adequate error handling?

Step 4: Provide specific improvements with code examples.

Code to review:
[code here]
```

### The Power of Chain-of-Thought

Encourage the model to think step-by-step:

```python
# Simple prompt
"What is 15% of 80?"

# Chain-of-thought prompt
"What is 15% of 80? Think step-by-step:
1. Convert 15% to decimal
2. Multiply by 80
3. Show your work"
```

This produces more accurate results, especially for reasoning tasks.

### Sequential Processing

For multi-stage tasks:

```
Task: Analyze this customer feedback

Step 1: Extract key points (bullet list)
Step 2: Identify sentiment (positive/negative/neutral with confidence)
Step 3: Suggest action items for the product team
Step 4: Draft a response to the customer

Feedback: [text here]
```

---

## Input/Output Formatting

### Structured Output Formats

Specify exactly how you want the output:

**JSON Format:**
```python
prompt = """
Extract information in this exact JSON format:
{
    "name": "person's name",
    "age": numeric_age,
    "occupation": "job title",
    "skills": ["skill1", "skill2"]
}

Text: "Sarah is a 28-year-old data scientist skilled in Python and SQL."
"""
```

**Markdown Format:**
```python
prompt = """
Create a product comparison in markdown format:

# Product Comparison

## Product A
- **Price**: $X
- **Pros**: 
  - Point 1
  - Point 2
- **Cons**:
  - Point 1

## Product B
[same structure]

## Recommendation
[1-2 sentences]
"""
```

**Table Format:**
```python
prompt = """
Create a comparison table:

| Feature | Product A | Product B | Winner |
|---------|-----------|-----------|--------|
| Price   | $X       | $Y        | A/B    |
| Speed   | X        | Y         | A/B    |

Products: [descriptions]
"""
```

### Delimiters and Structure

Use clear delimiters to separate different parts:

```python
prompt = """
Analyze this text between the triple quotes:
\"\"\"
[user input here]
\"\"\"

Provide your analysis in three sections:

=== SUMMARY ===
[concise summary]

=== KEY POINTS ===
1. [point]
2. [point]

=== RECOMMENDATIONS ===
- [recommendation]
"""
```

---

## Prompt Debugging

### Common Problems and Solutions

**Problem 1: Inconsistent Output**

❌ Issue:
```python
"Summarize this article."
# Sometimes long, sometimes short, format varies
```

✅ Solution:
```python
"Summarize this article in exactly 3 bullet points, 
each no more than 20 words."
```

**Problem 2: Off-Topic Responses**

❌ Issue:
```python
"What's the best way to learn Python?"
# Model goes off on tangents about history of programming
```

✅ Solution:
```python
"As a practical coding instructor, recommend 3 specific 
resources for learning Python. For each, provide:
- Resource name
- Why it's effective
- Estimated time to complete

Focus only on beginner-friendly resources. Do not include
general advice or programming history."
```

**Problem 3: Overly Creative or Hallucinated Content**

❌ Issue:
```python
"List the features of Product X"
# Model invents features that don't exist
```

✅ Solution:
```python
"Based ONLY on the information below, list the features.
If a feature is not mentioned, do not include it.
Do not make assumptions or add information.

Product information:
[paste actual info]
"
```

### Iterative Refinement Process

```
1. Start with a simple prompt
2. Test with various inputs
3. Identify failure patterns
4. Add constraints/examples
5. Test again
6. Repeat until consistent
```

**Example Iteration:**

```python
# Version 1 (too vague)
"Extract the main points"

# Version 2 (better, but still inconsistent)
"Extract the 3 main points from this text"

# Version 3 (more specific)
"Extract exactly 3 main points from this text.
Format as numbered list. Each point should be 
one complete sentence."

# Version 4 (with example)
"Extract exactly 3 main points from this text.
Format as numbered list. Each point should be 
one complete sentence.

Example:
1. The company reported 20% revenue growth in Q3.
2. New product launches contributed to increased sales.
3. Management expects continued growth in Q4.

Text to analyze:
[text here]"
```

---

## Best Practices

### 1. Be Specific and Explicit

```python
# Vague
"Make this better"

# Specific
"Improve this email by:
- Making the tone more professional
- Reducing length to under 150 words
- Adding a clear call-to-action"
```

### 2. Provide Context

```python
# Lacking context
"Should we launch this feature?"

# With context
"We're a B2B SaaS company targeting enterprise clients.
Our engineering team estimates 3 months to build Feature X.
Current customer surveys show 60% interest.
Should we prioritize this feature? Consider:
- Market timing
- Resource allocation
- Competitive advantage"
```

### 3. Use Appropriate Temperature

```python
# Factual tasks (low temperature)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.1,  # More deterministic
    messages=[{"role": "user", "content": "Extract data from this invoice..."}]
)

# Creative tasks (higher temperature)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    temperature=0.9,  # More creative
    messages=[{"role": "user", "content": "Brainstorm marketing slogans..."}]
)
```

### 4. Test with Edge Cases

Always test your prompts with:
- Empty inputs
- Very long inputs
- Unusual formats
- Ambiguous cases
- Multiple valid interpretations

### 5. Version Your Prompts

Keep track of what works:

```python
PROMPTS = {
    "summarize_v1": "Summarize this text.",
    "summarize_v2": "Summarize this text in 3 bullet points.",
    "summarize_v3": """Create a concise summary with:
    - Main topic (1 sentence)
    - Key points (3-5 bullets)
    - Conclusion (1 sentence)""",
}
```

### 6. Separate Instructions from Data

Use clear delimiters:

```python
prompt = f"""
Instructions:
{instructions}

Data to process:
\"\"\"
{user_data}
\"\"\"
"""
```

---

## Summary

In this module, you learned:
- ✅ Prompt engineering is crucial for LLM performance
- ✅ Good prompts have clear roles, goals, context, and format
- ✅ Few-shot learning guides behavior with examples
- ✅ Balance positive guidance with strategic negative constraints
- ✅ Break complex tasks into step-by-step instructions
- ✅ Specify exact output formats for consistency
- ✅ Debug prompts iteratively based on failure patterns
- ✅ Test with edge cases and version your prompts

## Next Steps

1. Complete the [exercises](exercises.md) to practice prompt engineering
2. Experiment with the [code examples](examples/) 
3. Continue to [Module 3: Context Engineering](../Module-03-Context-Engineering/lesson.md)

## Additional Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Learn Prompting](https://learnprompting.org/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

**Great work!** You now have the foundational skills to craft effective prompts. In the next module, you'll learn about context engineering—managing larger amounts of information and conversation history. Let's continue! 🚀
