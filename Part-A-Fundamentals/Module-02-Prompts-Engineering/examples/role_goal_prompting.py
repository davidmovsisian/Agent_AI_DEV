"""
Role and Goal Prompting - Effective Prompt Structuring

This module demonstrates how to use role-based prompting and clear goal
setting to significantly improve LLM outputs.

Key Concepts:
- Assigning specific roles to guide model behavior
- Setting clear, measurable goals
- Combining role and goal for optimal results
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict, List

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def compare_prompt_approaches(
    base_query: str,
    simple_prompt: str,
    role_goal_prompt: str
) -> None:
    """
    Compare outputs from simple vs role/goal-structured prompts.
    
    Args:
        base_query: The basic question
        simple_prompt: Simple version of the prompt
        role_goal_prompt: Structured version with role and goal
    """
    print(f"\n{'='*80}")
    print(f"BASE QUERY: {base_query}")
    print(f"{'='*80}")
    
    # Simple prompt
    print(f"\n❌ SIMPLE PROMPT:")
    print(f"{'-'*80}")
    print(f"{simple_prompt}")
    print(f"\n💬 Response:")
    
    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": simple_prompt}],
        max_tokens=200,
        temperature=0.7
    )
    print(response1.choices[0].message.content)
    
    # Role + Goal prompt
    print(f"\n\n✅ ROLE + GOAL PROMPT:")
    print(f"{'-'*80}")
    print(f"{role_goal_prompt}")
    print(f"\n💬 Response:")
    
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": role_goal_prompt}],
        max_tokens=200,
        temperature=0.7
    )
    print(response2.choices[0].message.content)


def role_experiment() -> None:
    """
    Show how different roles produce different perspectives.
    """
    print(f"\n{'='*80}")
    print("ROLE EXPERIMENT - Same Question, Different Roles")
    print(f"{'='*80}")
    
    question = "Explain what recursion is in programming."
    
    roles = [
        {
            "title": "Computer Science Professor",
            "prompt": """You are a computer science professor teaching an 
            advanced algorithms course. Explain what recursion is in 
            programming."""
        },
        {
            "title": "Coding Bootcamp Instructor",
            "prompt": """You are a friendly coding bootcamp instructor 
            teaching beginners. Explain what recursion is in programming 
            using simple language and real-world analogies."""
        },
        {
            "title": "Technical Writer",
            "prompt": """You are a technical writer creating documentation. 
            Explain what recursion is in programming. Be clear, concise, 
            and include a simple example."""
        }
    ]
    
    for role in roles:
        print(f"\n🎭 ROLE: {role['title']}")
        print(f"{'-'*80}")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": role['prompt']}],
            max_tokens=150,
            temperature=0.7
        )
        
        print(response.choices[0].message.content)


def goal_specificity_demo() -> None:
    """
    Demonstrate the importance of specific goals.
    """
    print(f"\n{'='*80}")
    print("GOAL SPECIFICITY DEMONSTRATION")
    print(f"{'='*80}")
    
    topic = "Python list comprehensions"
    
    prompts = [
        {
            "label": "Vague Goal",
            "prompt": f"Tell me about {topic}."
        },
        {
            "label": "Moderate Goal",
            "prompt": f"Explain {topic} with an example."
        },
        {
            "label": "Specific Goal",
            "prompt": f"""Explain {topic} following this structure:
            1. What are they? (1 sentence definition)
            2. Basic syntax (show the pattern)
            3. Simple example (convert a for loop to list comprehension)
            4. One benefit (why use them)
            
            Keep total response under 100 words."""
        }
    ]
    
    for p in prompts:
        print(f"\n📋 {p['label']}: \"{p['prompt']}\"")
        print(f"{'-'*80}")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": p['prompt']}],
            max_tokens=200,
            temperature=0.7
        )
        
        print(f"💬 {response.choices[0].message.content}\n")
        print(f"Token count: {response.usage.total_tokens}")


def practical_example_code_review() -> None:
    """
    Real-world example: Code review with role and goal.
    """
    print(f"\n{'='*80}")
    print("PRACTICAL EXAMPLE - Code Review")
    print(f"{'='*80}")
    
    code_to_review = """
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
"""
    
    # Poor prompt
    poor_prompt = f"Review this code:\n{code_to_review}"
    
    # Good prompt with role and goal
    good_prompt = f"""
Role: You are a senior Python developer conducting a code review.

Goal: Review the following code and provide:
1. What the code does (1 sentence)
2. One potential bug or edge case issue
3. One specific improvement with example code

Be concise and actionable.

Code:
{code_to_review}
"""
    
    print("\n❌ POOR PROMPT:")
    print(f"{'-'*80}")
    print(poor_prompt)
    
    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": poor_prompt}],
        max_tokens=200,
        temperature=0.3
    )
    print(f"\n💬 Response:\n{response1.choices[0].message.content}")
    
    print("\n\n✅ GOOD PROMPT (with Role + Goal):")
    print(f"{'-'*80}")
    print(good_prompt)
    
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": good_prompt}],
        max_tokens=200,
        temperature=0.3
    )
    print(f"\n💬 Response:\n{response2.choices[0].message.content}")


def create_reusable_prompt_template() -> Dict[str, str]:
    """
    Create a reusable prompt template structure.
    
    Returns:
        dict: Template with placeholders
    """
    template = {
        "role": "You are a {expertise} with {experience_level} experience.",
        "goal": """Your task is to {action} by:
        1. {step_1}
        2. {step_2}
        3. {step_3}
        
        Output should be {format_requirement}.""",
        "constraints": "Do not {constraint_1}. Do not {constraint_2}.",
        "full_template": """
Role: You are a {expertise} with {experience_level} experience.

Goal: Your task is to {action} by:
1. {step_1}
2. {step_2}
3. {step_3}

Output should be {format_requirement}.

Constraints: Do not {constraint_1}. Do not {constraint_2}.

{task_specific_content}
"""
    }
    
    return template


def demonstrate_template_usage() -> None:
    """
    Show how to use the reusable template.
    """
    print(f"\n{'='*80}")
    print("REUSABLE PROMPT TEMPLATE")
    print(f"{'='*80}")
    
    template = create_reusable_prompt_template()
    
    # Fill in the template
    filled_prompt = template["full_template"].format(
        expertise="customer support specialist",
        experience_level="5 years",
        action="respond to a customer complaint",
        step_1="Acknowledge the customer's frustration",
        step_2="Explain what went wrong clearly",
        step_3="Offer a specific solution and next steps",
        format_requirement="professional, empathetic, and under 150 words",
        constraint_1="make excuses",
        constraint_2="use overly technical language",
        task_specific_content="""
Customer complaint:
"I ordered a product 2 weeks ago and still haven't received it. 
The tracking hasn't updated in days. This is unacceptable!"
"""
    )
    
    print("📝 FILLED TEMPLATE:")
    print(f"{'-'*80}")
    print(filled_prompt)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": filled_prompt}],
        max_tokens=200,
        temperature=0.7
    )
    
    print(f"\n💬 GENERATED RESPONSE:")
    print(f"{'-'*80}")
    print(response.choices[0].message.content)


def main():
    """
    Run all demonstrations.
    """
    print("\n" + "="*80)
    print("ROLE AND GOAL PROMPTING DEMONSTRATION")
    print("="*80)
    
    # Demo 1: Direct comparison
    compare_prompt_approaches(
        base_query="How do I learn Python?",
        simple_prompt="How do I learn Python?",
        role_goal_prompt="""
        Role: You are a career counselor specializing in tech education.
        
        Goal: Recommend a specific learning path for Python, including:
        1. One best resource to start with (name and why)
        2. Estimated time to basic proficiency
        3. One practical first project to build
        
        Keep it actionable and concise (under 100 words).
        """
    )
    
    # Demo 2: Role variations
    role_experiment()
    
    # Demo 3: Goal specificity
    goal_specificity_demo()
    
    # Demo 4: Practical example
    practical_example_code_review()
    
    # Demo 5: Template usage
    demonstrate_template_usage()
    
    # Summary
    print(f"\n{'='*80}")
    print("KEY TAKEAWAYS")
    print(f"{'='*80}")
    print("""
1. Role setting activates relevant knowledge and behavior patterns
2. Specific goals produce more focused, useful outputs
3. Combining role + goal dramatically improves quality
4. Templates make prompt engineering reusable and consistent
5. Always test and iterate on your prompts
    """)


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not found in environment")
        print("Please set up your .env file. See resources/setup-guide.md")
    else:
        main()
