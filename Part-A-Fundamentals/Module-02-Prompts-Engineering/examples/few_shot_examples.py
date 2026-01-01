"""
Few-Shot Learning Examples - Teaching LLMs by Example

This module demonstrates how to use few-shot learning to guide LLM behavior
through examples rather than lengthy instructions.

Few-shot learning is particularly effective for:
- Custom output formats
- Specific classification tasks  
- Consistent style/tone
- Pattern recognition
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List, Dict

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def zero_shot_vs_few_shot(task: str, examples: List[Dict[str, str]], test_input: str) -> None:
    """
    Compare zero-shot (no examples) vs few-shot (with examples) performance.
    
    Args:
        task: Description of the task
        examples: List of input-output example pairs
        test_input: New input to test
    """
    print(f"\n{'='*80}")
    print(f"TASK: {task}")
    print(f"{'='*80}")
    
    # Zero-shot (no examples)
    zero_shot_prompt = f"{task}\n\nInput: {test_input}\nOutput:"
    
    print(f"\n📝 ZERO-SHOT (No Examples):")
    print(f"{'-'*80}")
    print(zero_shot_prompt)
    
    response1 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": zero_shot_prompt}],
        max_tokens=100,
        temperature=0.3
    )
    print(f"\n💬 Output: {response1.choices[0].message.content}")
    
    # Few-shot (with examples)
    few_shot_prompt = f"{task}\n\n"
    for ex in examples:
        few_shot_prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
    few_shot_prompt += f"Input: {test_input}\nOutput:"
    
    print(f"\n\n📚 FEW-SHOT (With {len(examples)} Examples):")
    print(f"{'-'*80}")
    print(few_shot_prompt)
    
    response2 = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": few_shot_prompt}],
        max_tokens=100,
        temperature=0.3
    )
    print(f"\n💬 Output: {response2.choices[0].message.content}")


def sentiment_classification_demo() -> None:
    """
    Demonstrate few-shot learning for sentiment classification.
    """
    print(f"\n{'='*80}")
    print("EXAMPLE 1: Sentiment Classification")
    print(f"{'='*80}")
    
    examples = [
        {"input": "This product exceeded my expectations! Love it.", "output": "positive"},
        {"input": "Terrible quality. Broke after one use.", "output": "negative"},
        {"input": "It's okay, nothing special but does the job.", "output": "neutral"},
        {"input": "Best purchase I've made this year!", "output": "positive"},
        {"input": "Disappointed with the slow shipping.", "output": "negative"},
    ]
    
    test_cases = [
        "Great value for money, highly recommend!",
        "Not sure if it's worth the price.",
        "Absolute waste of money, very unhappy."
    ]
    
    for test in test_cases:
        zero_shot_vs_few_shot(
            task="Classify the sentiment as positive, negative, or neutral.",
            examples=examples[:3],  # Use 3 examples
            test_input=test
        )


def data_extraction_demo() -> None:
    """
    Demonstrate few-shot for structured data extraction.
    """
    print(f"\n{'='*80}")
    print("EXAMPLE 2: Structured Data Extraction")
    print(f"{'='*80}")
    
    examples = [
        {
            "input": "John Smith, 32 years old, lives in Seattle, works as a Software Engineer",
            "output": '{"name": "John Smith", "age": 32, "city": "Seattle", "occupation": "Software Engineer"}'
        },
        {
            "input": "Sarah is 28 and from Boston",
            "output": '{"name": "Sarah", "age": 28, "city": "Boston", "occupation": null}'
        },
        {
            "input": "Mike Johnson, data analyst",
            "output": '{"name": "Mike Johnson", "age": null, "city": null, "occupation": "data analyst"}'
        }
    ]
    
    test_input = "Emily Chen, age 35, works as a marketing manager in San Francisco"
    
    zero_shot_vs_few_shot(
        task="Extract information into JSON format with fields: name, age, city, occupation.",
        examples=examples,
        test_input=test_input
    )


def custom_format_demo() -> None:
    """
    Demonstrate few-shot for custom output formatting.
    """
    print(f"\n{'='*80}")
    print("EXAMPLE 3: Custom Format Generation")
    print(f"{'='*80}")
    
    examples = [
        {
            "input": "Python programming language",
            "output": """📚 Topic: Python
🎯 Category: Programming Language
⭐ Key Feature: Easy to learn, versatile
🔗 Use Cases: Web dev, data science, automation"""
        },
        {
            "input": "Machine learning",
            "output": """📚 Topic: Machine Learning
🎯 Category: AI Technology
⭐ Key Feature: Learns from data patterns
🔗 Use Cases: Predictions, recommendations, automation"""
        }
    ]
    
    test_input = "React framework"
    
    zero_shot_vs_few_shot(
        task="Format the topic information with emojis and structure.",
        examples=examples,
        test_input=test_input
    )


def style_matching_demo() -> None:
    """
    Demonstrate few-shot for matching writing style.
    """
    print(f"\n{'='*80}")
    print("EXAMPLE 4: Style Matching")
    print(f"{'='*80}")
    
    task_desc = "Rewrite the sentence in a friendly, casual tone suitable for social media."
    
    examples = [
        {
            "input": "Our company has achieved significant growth this quarter.",
            "output": "We're crushing it this quarter! 🚀 Growth is through the roof!"
        },
        {
            "input": "Please submit your application by the deadline.",
            "output": "Hey! Don't forget to send in your application before the deadline! ⏰"
        },
        {
            "input": "This product offers excellent value for money.",
            "output": "This product is an absolute steal! 💰 You're getting so much bang for your buck!"
        }
    ]
    
    test_input = "We are pleased to announce our new product launch."
    
    zero_shot_vs_few_shot(
        task=task_desc,
        examples=examples,
        test_input=test_input
    )


def edge_case_handling() -> None:
    """
    Show how few-shot examples can teach edge case handling.
    """
    print(f"\n{'='*80}")
    print("EXAMPLE 5: Edge Case Handling")
    print(f"{'='*80}")
    
    task = "Extract the email address. If no email is present, return 'N/A'."
    
    examples = [
        {"input": "Contact me at john@email.com", "output": "john@email.com"},
        {"input": "My email is sarah.smith@company.org", "output": "sarah.smith@company.org"},
        {"input": "No email provided", "output": "N/A"},
        {"input": "Call me at 555-1234", "output": "N/A"},
    ]
    
    test_cases = [
        "Reach out via mike.jones@startup.io for more info",
        "Phone only: 555-9876",
        "I don't use email"
    ]
    
    for test in test_cases:
        zero_shot_vs_few_shot(task, examples, test)


def optimal_example_count() -> None:
    """
    Demonstrate how the number of examples affects performance.
    """
    print(f"\n{'='*80}")
    print("OPTIMAL EXAMPLE COUNT ANALYSIS")
    print(f"{'='*80}")
    
    all_examples = [
        {"input": "Great product!", "output": "positive"},
        {"input": "Terrible experience", "output": "negative"},
        {"input": "It's okay", "output": "neutral"},
        {"input": "Absolutely love it!", "output": "positive"},
        {"input": "Very disappointed", "output": "negative"},
    ]
    
    test_input = "Pretty good, would buy again"
    
    for num_examples in [1, 2, 3, 5]:
        print(f"\n{'='*40}")
        print(f"Using {num_examples} example(s):")
        print(f"{'='*40}")
        
        task = "Classify sentiment as positive, negative, or neutral."
        few_shot_prompt = f"{task}\n\n"
        
        for ex in all_examples[:num_examples]:
            few_shot_prompt += f"Input: {ex['input']}\nOutput: {ex['output']}\n\n"
        
        few_shot_prompt += f"Input: {test_input}\nOutput:"
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": few_shot_prompt}],
            max_tokens=10,
            temperature=0.3
        )
        
        print(f"Result: {response.choices[0].message.content}")
        print(f"Tokens used: {response.usage.total_tokens}")


def few_shot_best_practices() -> None:
    """
    Print best practices for few-shot learning.
    """
    print(f"\n{'='*80}")
    print("FEW-SHOT LEARNING BEST PRACTICES")
    print(f"{'='*80}")
    print("""
1. EXAMPLE QUALITY:
   ✅ Use diverse, representative examples
   ✅ Include edge cases in examples
   ✅ Ensure examples are accurate and consistent

2. QUANTITY:
   - 0 examples (zero-shot): Simple, obvious tasks
   - 1-2 examples: Clear pattern, low variability
   - 3-5 examples: Complex patterns, edge cases
   - 5+ examples: Diminishing returns, higher cost

3. ORDER MATTERS:
   ✅ Put most representative examples first
   ✅ Include edge cases toward the end
   ✅ Test different orderings if results vary

4. FORMAT CONSISTENCY:
   ✅ Use identical format for all examples
   ✅ Consistent separators (Input:/Output:)
   ✅ Match the format you want in output

5. WHEN TO USE:
   ✅ Custom or unusual output formats
   ✅ Specific classification schemes
   ✅ Style or tone matching
   ❌ When instructions are simpler/clearer
   ❌ When examples would use too many tokens

6. TESTING:
   ✅ Test with various inputs
   ✅ Verify edge case handling
   ✅ Compare zero-shot vs few-shot
   ✅ Find minimum effective example count
    """)


def main():
    """
    Run all demonstrations.
    """
    print("\n" + "="*80)
    print("FEW-SHOT LEARNING DEMONSTRATION")
    print("="*80)
    
    # Example 1: Sentiment classification
    sentiment_classification_demo()
    
    # Example 2: Data extraction
    data_extraction_demo()
    
    # Example 3: Custom formatting
    custom_format_demo()
    
    # Example 4: Style matching
    style_matching_demo()
    
    # Example 5: Edge cases
    edge_case_handling()
    
    # Analysis: Optimal count
    optimal_example_count()
    
    # Best practices
    few_shot_best_practices()


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Error: OPENAI_API_KEY not found in environment")
        print("Please set up your .env file. See resources/setup-guide.md")
    else:
        main()
