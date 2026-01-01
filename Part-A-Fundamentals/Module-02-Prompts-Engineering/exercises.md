# Module 2 Exercises: Prompt Engineering

## Instructions

Complete these exercises to master prompt engineering techniques. These exercises progress from basic to advanced, focusing on practical skills you'll use daily.

**Estimated Time**: 2-3 hours

---

## Part 1: Knowledge Check

### Question 1: Role Setting
**Q:** You need to generate code documentation. Which role would produce the best results?

a) "You are a software engineer"  
b) "You are a technical writer specializing in API documentation"  
c) "You are helpful"  
d) Role doesn't matter

<details>
<summary>Answer</summary>
b) - Specific roles activate relevant knowledge and behavior patterns
</details>

### Question 2: Few-Shot Learning
**Q:** When should you use few-shot learning instead of zero-shot?

a) Always use few-shot for better results  
b) When the task has a complex or unusual output format  
c) Never, it wastes tokens  
d) Only for classification tasks

<details>
<summary>Answer</summary>
b) - Few-shot is ideal for custom formats and specific patterns
</details>

---

## Part 2: Coding Challenges

### Exercise 1: Role-Based Prompt (Beginner)

**Task**: Create a function that generates prompts with different roles for the same task.

```python
def create_role_prompt(task: str, role: str, audience: str) -> str:
    """
    Generate a prompt with specified role and audience.
    
    Args:
        task: What needs to be done
        role: Who the AI should be
        audience: Who the output is for
    
    Returns:
        str: Formatted prompt
    """
    # TODO: Implement
    pass

# Test:
prompt = create_role_prompt(
    task="Explain neural networks",
    role="university professor",
    audience="undergraduate students"
)
print(prompt)
```

### Exercise 2: Few-Shot Classifier (Intermediate)

**Task**: Build a few-shot sentiment classifier.

```python
def create_few_shot_classifier(
    examples: List[Dict[str, str]], 
    test_input: str
) -> str:
    """
    Create a few-shot classification prompt.
    
    Args:
        examples: List of {"input": ..., "output": ...}
        test_input: New text to classify
    
    Returns:
        str: Complete prompt ready for API
    """
    # TODO: Implement
    pass

# Test with emotion classification
examples = [
    {"input": "I just won the lottery!", "output": "joy"},
    {"input": "My flight was cancelled again.", "output": "frustration"},
    {"input": "That movie made me cry.", "output": "sadness"}
]
prompt = create_few_shot_classifier(examples, "Best day ever!")
```

### Exercise 3: Prompt A/B Testing (Advanced)

**Task**: Create a framework to compare different prompts.

```python
from typing import List, Dict
from openai import OpenAI

def ab_test_prompts(
    prompts: List[str],
    test_inputs: List[str],
    evaluation_criteria: callable
) -> Dict:
    """
    Compare multiple prompts on the same inputs.
    
    Args:
        prompts: Different prompt versions to test
        test_inputs: List of test cases
        evaluation_criteria: Function that scores outputs (0-10)
    
    Returns:
        dict: Results with scores for each prompt
    """
    # TODO: Implement
    pass
```

### Exercise 4: Prompt Optimizer (Advanced)

**Task**: Build a tool that suggests improvements to prompts.

**Requirements**:
- Analyze prompt structure
- Identify missing components (role, goal, format, etc.)
- Suggest specific improvements
- Show before/after example

---

## Part 3: Real-World Scenarios

### Scenario 1: Customer Support

Create a prompt for an AI customer support agent that:
- Has appropriate personality
- Follows company guidelines
- Handles complaints professionally
- Knows when to escalate to humans

### Scenario 2: Code Review

Design a prompt that reviews code for:
- Bugs and edge cases
- Performance issues
- Style and readability
- Security vulnerabilities

Provide before/after examples.

### Scenario 3: Content Moderation

Build a few-shot prompt to classify content as:
- Safe
- Needs review
- Violates policy

Include edge cases in your examples.

---

## Part 4: Prompt Debugging

Fix these broken prompts:

### Broken Prompt 1
```
"Write me something good about AI"
```
**Issues**: Vague goal, no constraints, unclear output
**Your fixed version**: ___

### Broken Prompt 2
```
"Don't be boring. Don't use jargon. Don't be too long. 
Don't make it technical. Explain machine learning."
```
**Issues**: Too many negatives, confusing
**Your fixed version**: ___

---

## Bonus Challenges

1. **Prompt Library**: Create a reusable library of prompts for common tasks
2. **Prompt Versioning**: Build a system to track prompt versions and performance
3. **Dynamic Prompts**: Create prompts that adapt based on user input
4. **Multilingual Prompts**: Design prompts that work across languages

---

## Self-Assessment

Rate your skills (1-5):
- [ ] Role and goal setting: ___/5
- [ ] Few-shot learning: ___/5
- [ ] Prompt structure: ___/5
- [ ] Debugging prompts: ___/5
- [ ] Output formatting: ___/5

**Target**: 3+ on all items before Module 3

---

## Next Steps

1. Review solutions in the examples directory
2. Build your personal prompt library
3. Continue to [Module 3: Context Engineering](../Module-03-Context-Engineering/lesson.md)
