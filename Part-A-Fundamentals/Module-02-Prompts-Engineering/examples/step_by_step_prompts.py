"""
Step-by-Step Prompting - Breaking Down Complex Tasks

This module demonstrates how to structure prompts that guide LLMs
through multi-step processes, improving accuracy and completeness.

Key Concepts:
- Sequential instructions for complex tasks
- Chain-of-thought encouragement
- Explicit step numbering
- Verification at each stage
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def simple_vs_stepwise(task: str, simple: str, stepwise: str) -> None:
    """Compare simple prompt vs step-by-step approach."""
    print(f"\n{'='*80}")
    print(f"TASK: {task}")
    print(f"{'='*80}")
    
    # Simple approach
    print(f"\n❌ SIMPLE PROMPT:")
    print(f"{'-'*80}")
    print(simple)
    
    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": simple}],
        max_tokens=250,
        temperature=0.7
    )
    print(f"\n💬 Response:\n{response1.choices[0].message.content}")
    
    # Step-by-step approach
    print(f"\n\n✅ STEP-BY-STEP PROMPT:")
    print(f"{'-'*80}")
    print(stepwise)
    
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": stepwise}],
        max_tokens=250,
        temperature=0.7
    )
    print(f"\n💬 Response:\n{response2.choices[0].message.content}")


def math_problem_solving() -> None:
    """Demonstrate step-by-step for math problems."""
    print(f"\n{'='*80}")
    print("EXAMPLE 1: Math Problem Solving")
    print(f"{'='*80}")
    
    problem = "A store has 45 apples. They sell 60% in the morning. Then they receive a shipment of 30 more apples. How many apples do they have now?"
    
    simple = f"Solve: {problem}"
    
    stepwise = f"""Solve this problem step by step:

{problem}

Step 1: Calculate how many apples were sold (60% of 45)
Step 2: Calculate remaining apples after morning sales
Step 3: Add the new shipment
Step 4: State the final answer

Show your work for each step."""
    
    simple_vs_stepwise("Math Problem", simple, stepwise)


def code_review_example() -> None:
    """Step-by-step code review."""
    print(f"\n{'='*80}")
    print("EXAMPLE 2: Code Review Process")
    print(f"{'='*80}")
    
    code = """
def process_data(items):
    result = []
    for item in items:
        if item > 0:
            result.append(item * 2)
    return result
"""
    
    simple = f"Review this code:\n{code}"
    
    stepwise = f"""Review this Python code following these steps:

{code}

Step 1: Describe what the code does in one sentence.

Step 2: Identify potential issues:
- Edge cases (empty list, None values, etc.)
- Type safety
- Performance concerns

Step 3: Suggest one specific improvement with example code.

Step 4: Rate the code quality (1-5) and explain why."""
    
    simple_vs_stepwise("Code Review", simple, stepwise)


def data_analysis_example() -> None:
    """Step-by-step data analysis."""
    print(f"\n{'='*80}")
    print("EXAMPLE 3: Data Analysis")
    print(f"{'='*80}")
    
    data = """
Sales Data:
Q1: $100,000
Q2: $120,000
Q3: $110,000
Q4: $150,000
"""
    
    simple = f"Analyze this sales data:\n{data}"
    
    stepwise = f"""Analyze this sales data following these steps:

{data}

Step 1: Calculate total annual sales.

Step 2: Calculate average quarterly sales.

Step 3: Identify the best and worst performing quarters.

Step 4: Calculate the growth rate from Q1 to Q4.

Step 5: Provide one insight or recommendation based on the data.

Show calculations for each step."""
    
    simple_vs_stepwise("Data Analysis", simple, stepwise)


def chain_of_thought_reasoning() -> None:
    """Demonstrate explicit chain-of-thought prompting."""
    print(f"\n{'='*80}")
    print("CHAIN-OF-THOUGHT REASONING")
    print(f"{'='*80}")
    
    prompt = """Question: If a train travels 240 miles in 3 hours, and then 
160 miles in 2 hours, what is its average speed for the entire journey?

Let's think through this step by step:

1. First, calculate total distance: [your calculation]
2. Then, calculate total time: [your calculation]
3. Finally, calculate average speed: [your calculation]
4. State the answer with units

Please show your reasoning for each step."""
    
    print(f"\nPrompt:\n{'-'*80}")
    print(prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3
    )
    
    print(f"\n💬 Response:\n{'-'*80}")
    print(response.choices[0].message.content)


def complex_task_decomposition() -> None:
    """Show how to decompose complex tasks."""
    print(f"\n{'='*80}")
    print("COMPLEX TASK DECOMPOSITION")
    print(f"{'='*80}")
    
    task = """Create a launch plan for a new mobile app."""
    
    prompt = f"""Task: {task}

Break this down and complete each step:

STEP 1: Pre-Launch (2-3 bullet points)
- What needs to be done before launch?

STEP 2: Launch Day (2-3 bullet points)
- What happens on launch day?

STEP 3: Post-Launch (2-3 bullet points)
- What follow-up actions are needed?

STEP 4: Success Metrics (2-3 items)
- How do we measure success?

Keep each section concise and actionable."""
    
    print(f"\nPrompt:\n{'-'*80}")
    print(prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.7
    )
    
    print(f"\n💬 Response:\n{'-'*80}")
    print(response.choices[0].message.content)


def verification_steps() -> None:
    """Add verification to step-by-step process."""
    print(f"\n{'='*80}")
    print("STEP-BY-STEP WITH VERIFICATION")
    print(f"{'='*80}")
    
    prompt = """Solve this logic puzzle using a systematic approach:

Puzzle: Alice, Bob, and Carol are in a race. Alice finishes before Bob. 
Carol finishes before Alice. Who won the race?

Step 1: List what we know as facts.

Step 2: Represent this information in order (first → last).

Step 3: Verify your ordering against each statement.

Step 4: State who won and explain your reasoning.

Follow each step carefully and check your work."""
    
    print(f"\nPrompt:\n{'-'*80}")
    print(prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.3
    )
    
    print(f"\n💬 Response:\n{'-'*80}")
    print(response.choices[0].message.content)


def best_practices() -> None:
    """Print best practices for step-by-step prompting."""
    print(f"\n\n{'='*80}")
    print("BEST PRACTICES FOR STEP-BY-STEP PROMPTING")
    print(f"{'='*80}")
    print("""
✅ WHEN TO USE STEP-BY-STEP:
   - Complex calculations or reasoning
   - Multi-stage processes
   - Tasks requiring verification
   - Analytical or systematic work
   - Reducing errors in critical tasks

📋 HOW TO STRUCTURE:
   1. State the overall task clearly
   2. Number each step explicitly
   3. Make steps atomic (one action per step)
   4. Include verification steps
   5. Ask to show work/reasoning

🎯 EFFECTIVE STEP PATTERNS:

   Pattern 1: Sequential Process
   Step 1: [First action]
   Step 2: [Second action]
   Step 3: [Verification]
   Step 4: [Final result]

   Pattern 2: Analysis Framework
   Step 1: Observe (what do we see?)
   Step 2: Interpret (what does it mean?)
   Step 3: Evaluate (is it good/bad?)
   Step 4: Recommend (what to do?)

   Pattern 3: Problem Solving
   Step 1: Understand (restate the problem)
   Step 2: Plan (outline approach)
   Step 3: Execute (implement plan)
   Step 4: Verify (check solution)

⚡ PRO TIPS:
   - Use "Let's think step by step" for automatic CoT
   - Include "Show your work" for transparency
   - Add verification steps for accuracy
   - Keep steps simple and clear
   - Use consistent formatting (numbers, bullets, etc.)

❌ AVOID:
   - Too many steps (diminishing returns after 5-7)
   - Vague step descriptions
   - Steps that depend on unclear previous steps
   - Skipping the verification step
   - Making steps too complex

🔬 WHEN NOT TO USE:
   - Simple, straightforward tasks
   - Creative tasks that need free flow
   - When brevity is more important than accuracy
   - Tasks already well-defined
    """)


def main():
    """Run all demonstrations."""
    print("\n" + "="*80)
    print("STEP-BY-STEP PROMPTING DEMONSTRATION")
    print("="*80)
    
    # Example 1: Math
    math_problem_solving()
    
    # Example 2: Code Review
    code_review_example()
    
    # Example 3: Data Analysis
    data_analysis_example()
    
    # Example 4: Chain of Thought
    chain_of_thought_reasoning()
    
    # Example 5: Task Decomposition
    complex_task_decomposition()
    
    # Example 6: With Verification
    verification_steps()
    
    # Best Practices
    best_practices()


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not found in environment")
        print("Please set up your .env file. See resources/setup-guide.md")
    else:
        main()
