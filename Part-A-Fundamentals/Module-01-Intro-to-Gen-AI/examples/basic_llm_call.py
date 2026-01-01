"""
Basic LLM API Calls - OpenAI and Anthropic Examples

This module demonstrates how to make basic API calls to OpenAI's GPT models
and Anthropic's Claude models. You'll learn the fundamental structure of
API interactions with different LLM providers.

Requirements:
    - openai>=1.12.0
    - anthropic>=0.18.0
    - python-dotenv>=1.0.0

Setup:
    1. Create a .env file with your API keys:
       OPENAI_API_KEY=your_key_here
       ANTHROPIC_API_KEY=your_key_here
    2. Run: python basic_llm_call.py
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def call_openai(
    prompt: str,
    model: str = "gpt-3.5-turbo",
    temperature: float = 0.7,
    max_tokens: int = 150
) -> dict:
    """
    Make a basic API call to OpenAI's GPT models.
    
    Args:
        prompt: The user's input text
        model: Model identifier (e.g., "gpt-3.5-turbo", "gpt-4")
        temperature: Randomness control (0.0-2.0)
        max_tokens: Maximum tokens in response
        
    Returns:
        dict: Response containing text and usage information
        
    Example output:
        {
            'text': 'Paris is the capital of France...',
            'model': 'gpt-3.5-turbo',
            'input_tokens': 12,
            'output_tokens': 45,
            'total_tokens': 57
        }
    """
    from openai import OpenAI
    
    # Initialize client with API key from environment
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    try:
        # Make API call
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Extract and return relevant information
        return {
            'text': response.choices[0].message.content,
            'model': response.model,
            'input_tokens': response.usage.prompt_tokens,
            'output_tokens': response.usage.completion_tokens,
            'total_tokens': response.usage.total_tokens
        }
        
    except Exception as e:
        return {'error': str(e)}


def call_anthropic(
    prompt: str,
    model: str = "claude-3-haiku-20240307",
    temperature: float = 0.7,
    max_tokens: int = 150
) -> dict:
    """
    Make a basic API call to Anthropic's Claude models.
    
    Args:
        prompt: The user's input text
        model: Model identifier (e.g., "claude-3-haiku-20240307")
        temperature: Randomness control (0.0-1.0)
        max_tokens: Maximum tokens in response
        
    Returns:
        dict: Response containing text and usage information
        
    Example output:
        {
            'text': 'Paris is the capital and largest city of France...',
            'model': 'claude-3-haiku-20240307',
            'input_tokens': 15,
            'output_tokens': 48,
            'total_tokens': 63
        }
    """
    from anthropic import Anthropic
    
    # Initialize client with API key from environment
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    try:
        # Make API call
        response = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # Extract and return relevant information
        return {
            'text': response.content[0].text,
            'model': response.model,
            'input_tokens': response.usage.input_tokens,
            'output_tokens': response.usage.output_tokens,
            'total_tokens': response.usage.input_tokens + response.usage.output_tokens
        }
        
    except Exception as e:
        return {'error': str(e)}


def compare_providers(prompt: str) -> None:
    """
    Compare responses from OpenAI and Anthropic for the same prompt.
    
    Args:
        prompt: The user's input text
    """
    print("=" * 70)
    print(f"PROMPT: {prompt}")
    print("=" * 70)
    
    # Call OpenAI
    print("\n🟢 OPENAI (GPT-3.5-turbo):")
    print("-" * 70)
    openai_result = call_openai(prompt)
    if 'error' not in openai_result:
        print(f"Response: {openai_result['text']}")
        print(f"\nTokens - Input: {openai_result['input_tokens']}, "
              f"Output: {openai_result['output_tokens']}, "
              f"Total: {openai_result['total_tokens']}")
    else:
        print(f"Error: {openai_result['error']}")
    
    # Call Anthropic
    print("\n🔵 ANTHROPIC (Claude 3 Haiku):")
    print("-" * 70)
    anthropic_result = call_anthropic(prompt)
    if 'error' not in anthropic_result:
        print(f"Response: {anthropic_result['text']}")
        print(f"\nTokens - Input: {anthropic_result['input_tokens']}, "
              f"Output: {anthropic_result['output_tokens']}, "
              f"Total: {anthropic_result['total_tokens']}")
    else:
        print(f"Error: {anthropic_result['error']}")


def demonstrate_temperature_effect(prompt: str) -> None:
    """
    Show how temperature affects response consistency.
    
    Args:
        prompt: The user's input text
    """
    print("\n" + "=" * 70)
    print("TEMPERATURE EFFECT DEMONSTRATION")
    print("=" * 70)
    print(f"Prompt: {prompt}\n")
    
    temperatures = [0.0, 0.7, 1.5]
    
    for temp in temperatures:
        print(f"\n🌡️  Temperature: {temp}")
        print("-" * 70)
        
        # Make 2 calls with same temperature to show consistency
        for i in range(2):
            result = call_openai(prompt, temperature=temp, max_tokens=50)
            if 'error' not in result:
                print(f"Call {i+1}: {result['text'][:100]}...")
            else:
                print(f"Error: {result['error']}")


def main():
    """
    Main demonstration function.
    """
    print("\n" + "=" * 70)
    print("BASIC LLM API CALLS - DEMONSTRATION")
    print("=" * 70)
    
    # Example 1: Simple question
    compare_providers("What is the capital of France?")
    
    # Example 2: Creative task
    print("\n\n")
    compare_providers("Write a haiku about artificial intelligence.")
    
    # Example 3: Temperature effect
    demonstrate_temperature_effect(
        "Generate a creative name for a coffee shop."
    )
    
    # Example 4: Different models (OpenAI)
    print("\n\n" + "=" * 70)
    print("COMPARING OPENAI MODELS")
    print("=" * 70)
    
    prompt = "Explain quantum computing in one sentence."
    
    for model in ["gpt-3.5-turbo", "gpt-4"]:
        print(f"\n📊 Model: {model}")
        print("-" * 70)
        result = call_openai(prompt, model=model, max_tokens=100)
        if 'error' not in result:
            print(f"Response: {result['text']}")
            print(f"Tokens: {result['total_tokens']}")
        else:
            print(f"Error: {result['error']}")


if __name__ == "__main__":
    # Check if API keys are set
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Warning: OPENAI_API_KEY not found in environment")
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Warning: ANTHROPIC_API_KEY not found in environment")
    
    if os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY"):
        main()
    else:
        print("\n❌ No API keys found. Please set up your .env file.")
        print("See resources/setup-guide.md for instructions.")
