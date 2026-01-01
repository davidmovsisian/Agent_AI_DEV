"""
Negative and Positive Prompting Examples

This module demonstrates when and how to use positive (what TO do) 
vs negative (what NOT to do) prompting techniques.

Key Concepts:
- Positive prompting provides constructive guidance
- Negative prompting sets boundaries and prevents issues
- Balance both for optimal results
- Too many negatives can confuse the model
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def demonstrate_positive_prompting() -> None:
    """Show effective positive prompting examples."""
    print(f"\n{'='*80}")
    print("POSITIVE PROMPTING - What TO Do")
    print(f"{'='*80}")
    
    examples = [
        {
            "task": "Email Writing",
            "prompt": """Write a professional email to a client about a project delay.
            
            DO:
            - Start with acknowledging the situation
            - Explain the reason briefly (1-2 sentences)
            - Provide a new realistic timeline
            - Offer a solution or compensation
            - End with reassurance
            
            Keep it under 150 words and maintain a professional but warm tone."""
        },
        {
            "task": "Code Explanation",
            "prompt": """Explain this Python function to a beginner programmer:
            
            def fibonacci(n):
                if n <= 1: return n
                return fibonacci(n-1) + fibonacci(n-2)
            
            DO:
            - Use simple, everyday language
            - Provide an analogy or real-world example
            - Walk through one example step-by-step
            - Mention one key takeaway about recursion"""
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{'─'*80}")
        print(f"Example {i}: {example['task']}")
        print(f"{'─'*80}")
        print(f"Prompt:\n{example['prompt']}")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": example['prompt']}],
            max_tokens=200,
            temperature=0.7
        )
        
        print(f"\n💬 Response:\n{response.choices[0].message.content}")


def demonstrate_negative_prompting() -> None:
    """Show when and how to use negative prompting."""
    print(f"\n\n{'='*80}")
    print("NEGATIVE PROMPTING - What NOT to Do")
    print(f"{'='*80}")
    
    examples = [
        {
            "task": "Factual Summary",
            "prompt": """Summarize the following article about climate change.
            
            DON'T:
            - Add your own opinions or interpretations
            - Include information not in the article
            - Use emotional or biased language
            
            Article: [Climate change is affecting global temperatures with 
            scientific data showing a 1.1°C increase since pre-industrial times.]
            
            Provide just the key facts in 2-3 bullet points."""
        },
        {
            "task": "Technical Documentation",
            "prompt": """Document this API endpoint:
            
            POST /api/users - Creates a new user account
            
            DON'T:
            - Use marketing language or sales pitch
            - Assume prior knowledge of the system
            - Omit required parameters
            
            Include: endpoint, method, parameters, example request."""
        }
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{'─'*80}")
        print(f"Example {i}: {example['task']}")
        print(f"{'─'*80}")
        print(f"Prompt:\n{example['prompt']}")
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": example['prompt']}],
            max_tokens=200,
            temperature=0.3
        )
        
        print(f"\n💬 Response:\n{response.choices[0].message.content}")


def demonstrate_balanced_approach() -> None:
    """Show combining positive and negative prompting."""
    print(f"\n\n{'='*80}")
    print("BALANCED APPROACH - Combining Both")
    print(f"{'='*80}")
    
    scenarios = [
        {
            "name": "Product Review Analysis",
            "poor": "Analyze this product review: 'Great product but shipping was slow'",
            "good": """Analyze this product review and extract structured information.
            
            DO:
            - Identify sentiment (positive/negative/mixed)
            - Extract specific praises or complaints
            - Rate sentiment numerically (1-5)
            
            DON'T:
            - Make assumptions beyond what's stated
            - Add general advice
            
            Review: "Great product but shipping was slow"
            
            Format as: Sentiment: [X], Score: [Y], Praises: [list], Issues: [list]"""
        },
        {
            "name": "Creative Writing",
            "poor": "Write a story about AI",
            "good": """Write a 100-word flash fiction story about AI.
            
            DO:
            - Include a clear beginning, middle, and end
            - Focus on one specific moment or event
            - Use vivid, concrete details
            - End with a twist or revelation
            
            DON'T:
            - Explain or preach about AI ethics
            - Use clichéd "robot uprising" tropes
            - Exceed 100 words"""
        }
    ]
    
    for scenario in scenarios:
        print(f"\n{'─'*80}")
        print(f"Scenario: {scenario['name']}")
        print(f"{'─'*80}")
        
        print(f"\n❌ Poor Prompt (Vague):")
        print(scenario['poor'])
        
        print(f"\n✅ Better Prompt (Balanced):")
        print(scenario['good'])
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": scenario['good']}],
            max_tokens=200,
            temperature=0.7
        )
        
        print(f"\n💬 Response:\n{response.choices[0].message.content}")


def demonstrate_common_mistakes() -> None:
    """Show common negative prompting mistakes."""
    print(f"\n\n{'='*80}")
    print("COMMON MISTAKES TO AVOID")
    print(f"{'='*80}")
    
    print("""
1. ❌ TOO MANY NEGATIVES
Bad: "Don't be boring, don't be long, don't use jargon, don't be vague,
     don't assume knowledge, don't be technical..."
     
Better: "Write a clear, engaging 100-word explanation for beginners. 
        Use simple language and concrete examples."

2. ❌ CONFLICTING INSTRUCTIONS
Bad: "Be creative but don't be imaginative. Be brief but thorough."

Better: "Be creative within these constraints: 150 words, focus on 
        practical solutions."

3. ❌ ONLY NEGATIVES, NO POSITIVES
Bad: "Don't use passive voice, don't include opinions, don't be informal..."

Better: "Use active voice, stick to facts, maintain professional tone."

4. ❌ VAGUE NEGATIVES
Bad: "Don't write anything bad."

Better: "Avoid: technical jargon, unverified claims, promotional language."

5. ❌ CONTRADICTING WITH NEGATIVES
Bad: "Write creatively. Don't be creative with facts."

Better: "Use creative language and structure. Base all statements on 
        the provided facts."
    """)


def best_practices_guide() -> None:
    """Print best practices for positive/negative prompting."""
    print(f"\n\n{'='*80}")
    print("BEST PRACTICES")
    print(f"{'='*80}")
    print("""
🎯 WHEN TO USE POSITIVE PROMPTING:
   - Primary guidance and direction
   - Constructive requirements
   - Defining desired outcomes
   - Setting expectations

⛔ WHEN TO USE NEGATIVE PROMPTING:
   - Preventing specific common mistakes
   - Setting clear boundaries
   - Avoiding known pitfalls
   - Overriding default behaviors

🔄 COMBINING BOTH:
   - Start with positive guidance (what you want)
   - Add strategic negatives (what to avoid)
   - Keep negatives to 2-3 key items
   - Balance ratio: 3-4 positive instructions per 1 negative

📋 STRUCTURE TEMPLATE:
   Task: [What to accomplish]
   
   Do:
   - [Positive instruction 1]
   - [Positive instruction 2]
   - [Positive instruction 3]
   
   Don't:
   - [Critical thing to avoid]
   - [Common mistake to prevent]
   
   Format: [Expected output structure]

⚡ QUICK TIPS:
   1. Use positives for "how" (approach, style, format)
   2. Use negatives for "boundaries" (what's off-limits)
   3. Test your prompts—add negatives only if needed
   4. More negatives ≠ better results
   5. Be specific in both positive and negative instructions
    """)


def main():
    """Run all demonstrations."""
    print("\n" + "="*80)
    print("POSITIVE & NEGATIVE PROMPTING DEMONSTRATION")
    print("="*80)
    
    # Demo 1: Positive prompting
    demonstrate_positive_prompting()
    
    # Demo 2: Negative prompting
    demonstrate_negative_prompting()
    
    # Demo 3: Balanced approach
    demonstrate_balanced_approach()
    
    # Demo 4: Common mistakes
    demonstrate_common_mistakes()
    
    # Demo 5: Best practices
    best_practices_guide()


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not found in environment")
        print("Please set up your .env file. See resources/setup-guide.md")
    else:
        main()
