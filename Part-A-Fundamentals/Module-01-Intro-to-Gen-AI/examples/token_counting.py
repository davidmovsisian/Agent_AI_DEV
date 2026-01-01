"""
Token Counting - Understanding and Managing Tokens

This module demonstrates how to count tokens for different text inputs,
understand tokenization, and estimate token usage before making API calls.

Tokens are the fundamental units that LLMs process. Understanding token
counts is crucial for:
1. Estimating API costs
2. Staying within context limits
3. Optimizing prompt efficiency

Requirements:
    - tiktoken>=0.6.0
    - openai>=1.12.0
"""

import tiktoken
from typing import List, Dict
import json


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Count the number of tokens in a text string for a specific model.
    
    Args:
        text: Input text to tokenize
        model: Model name (e.g., "gpt-3.5-turbo", "gpt-4")
        
    Returns:
        int: Number of tokens
        
    Example:
        >>> count_tokens("Hello, world!")
        4
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)


def visualize_tokenization(text: str, model: str = "gpt-3.5-turbo") -> None:
    """
    Show how text is broken down into individual tokens.
    
    Args:
        text: Input text to tokenize
        model: Model name
        
    Output example:
        Text: "Hello, world!"
        Tokens: ['Hello', ',', ' world', '!']
        Token IDs: [15496, 11, 1917, 0]
        Total tokens: 4
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    
    # Decode each token to see what it represents
    token_strings = [encoding.decode([token]) for token in tokens]
    
    print(f"\n{'='*70}")
    print(f"Text: '{text}'")
    print(f"{'='*70}")
    print(f"Tokens: {token_strings}")
    print(f"Token IDs: {tokens}")
    print(f"Total tokens: {len(tokens)}")
    print(f"Characters: {len(text)}")
    print(f"Words (approx): {len(text.split())}")
    print(f"Ratio: {len(tokens) / len(text.split()):.2f} tokens per word")


def compare_tokenization_examples() -> None:
    """
    Compare how different types of text are tokenized.
    """
    print("\n" + "="*70)
    print("TOKENIZATION COMPARISON")
    print("="*70)
    
    examples = [
        "Hello world",
        "Hello, world!",
        "artificial intelligence",
        "AI",
        "uncommonword123",
        "I'm learning about LLMs",
        "日本語のテキスト",  # Japanese text
        "def hello_world():",
        "{'key': 'value'}",
        "https://www.example.com/path?query=value"
    ]
    
    for text in examples:
        token_count = count_tokens(text)
        print(f"\n'{text}'")
        print(f"  → {token_count} tokens ({len(text)} characters)")
        
        # Show first 5 tokens if more than 5
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
        tokens = encoding.encode(text)
        if len(tokens) <= 5:
            token_strings = [encoding.decode([t]) for t in tokens]
            print(f"  → Breakdown: {token_strings}")


def estimate_conversation_tokens(
    messages: List[Dict[str, str]],
    model: str = "gpt-3.5-turbo"
) -> Dict[str, int]:
    """
    Estimate token count for a conversation (chat format).
    
    OpenAI's chat models use special tokens for message formatting:
    - Each message has overhead (role, name, formatting)
    - Typically 3-4 tokens per message overhead
    
    Args:
        messages: List of message dicts with 'role' and 'content'
        model: Model name
        
    Returns:
        dict: Token counts breakdown
        
    Example:
        >>> messages = [
        ...     {"role": "system", "content": "You are helpful."},
        ...     {"role": "user", "content": "Hello!"}
        ... ]
        >>> estimate_conversation_tokens(messages)
        {'system': 5, 'user': 3, 'total': 11, 'overhead': 3}
    """
    encoding = tiktoken.encoding_for_model(model)
    
    token_counts = {
        'system': 0,
        'user': 0,
        'assistant': 0,
        'overhead': 0,
        'total': 0
    }
    
    # Each message has approximately 3-4 tokens overhead
    # <|start|>role\n + content + <|end|\n>
    tokens_per_message = 3
    tokens_per_name = 1
    
    for message in messages:
        role = message.get('role', 'user')
        content = message.get('content', '')
        
        # Count content tokens
        content_tokens = len(encoding.encode(content))
        
        # Add to role-specific count
        if role in token_counts:
            token_counts[role] += content_tokens
        
        # Add message overhead
        token_counts['overhead'] += tokens_per_message
        
        # Add name token if present
        if 'name' in message:
            token_counts['overhead'] += tokens_per_name
    
    # Add 3 tokens for assistant reply priming
    token_counts['overhead'] += 3
    
    # Calculate total
    token_counts['total'] = sum(token_counts.values()) - token_counts['overhead'] + token_counts['overhead']
    
    return token_counts


def demonstrate_context_limits() -> None:
    """
    Show how to check if content fits within model context limits.
    """
    print("\n" + "="*70)
    print("CONTEXT LIMIT AWARENESS")
    print("="*70)
    
    # Model context limits
    limits = {
        "gpt-3.5-turbo": 4096,
        "gpt-3.5-turbo-16k": 16384,
        "gpt-4": 8192,
        "gpt-4-32k": 32768,
        "gpt-4-turbo": 128000,
    }
    
    # Sample long text
    long_text = "AI " * 1000  # Repeat to make it long
    token_count = count_tokens(long_text)
    
    print(f"\nSample text token count: {token_count}")
    print(f"\nModel compatibility:")
    
    for model, limit in limits.items():
        fits = token_count < (limit * 0.8)  # Leave 20% for response
        status = "✓" if fits else "✗"
        print(f"  {status} {model}: {limit} tokens "
              f"({'fits' if fits else 'too large'})")


def estimate_cost_breakdown(
    input_text: str,
    expected_output_tokens: int = 100,
    model: str = "gpt-3.5-turbo"
) -> None:
    """
    Estimate the cost of an API call.
    
    Args:
        input_text: The prompt/input text
        expected_output_tokens: Expected response length
        model: Model name
    """
    # Pricing (per 1M tokens) - as of 2024
    pricing = {
        "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
        "gpt-4": {"input": 30.00, "output": 60.00},
        "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    }
    
    if model not in pricing:
        print(f"Pricing not available for {model}")
        return
    
    input_tokens = count_tokens(input_text, model)
    
    # Calculate costs
    input_cost = (input_tokens / 1_000_000) * pricing[model]["input"]
    output_cost = (expected_output_tokens / 1_000_000) * pricing[model]["output"]
    total_cost = input_cost + output_cost
    
    print(f"\n{'='*70}")
    print(f"COST ESTIMATE - {model}")
    print(f"{'='*70}")
    print(f"Input tokens:  {input_tokens:,}")
    print(f"Output tokens: {expected_output_tokens:,} (estimated)")
    print(f"Total tokens:  {input_tokens + expected_output_tokens:,}")
    print(f"\nInput cost:    ${input_cost:.6f}")
    print(f"Output cost:   ${output_cost:.6f}")
    print(f"Total cost:    ${total_cost:.6f}")
    
    # Show cost per 1000 requests
    cost_per_1k = total_cost * 1000
    print(f"\nCost per 1,000 requests: ${cost_per_1k:.2f}")


def analyze_prompt_efficiency(prompt: str) -> None:
    """
    Analyze a prompt for token efficiency.
    
    Args:
        prompt: The prompt to analyze
    """
    token_count = count_tokens(prompt)
    word_count = len(prompt.split())
    char_count = len(prompt)
    
    print(f"\n{'='*70}")
    print(f"PROMPT EFFICIENCY ANALYSIS")
    print(f"{'='*70}")
    print(f"Prompt: '{prompt[:100]}{'...' if len(prompt) > 100 else ''}'")
    print(f"\nMetrics:")
    print(f"  Characters: {char_count}")
    print(f"  Words:      {word_count}")
    print(f"  Tokens:     {token_count}")
    print(f"\nRatios:")
    print(f"  Chars/token:  {char_count/token_count:.2f}")
    print(f"  Tokens/word:  {token_count/word_count:.2f}")
    
    # Efficiency rating
    if token_count / word_count < 1.3:
        rating = "Excellent (common words)"
    elif token_count / word_count < 1.5:
        rating = "Good"
    else:
        rating = "Poor (many uncommon words/characters)"
    
    print(f"\nEfficiency rating: {rating}")


def main():
    """
    Run all demonstrations.
    """
    print("\n" + "="*70)
    print("TOKEN COUNTING DEMONSTRATION")
    print("="*70)
    
    # Example 1: Basic tokenization
    visualize_tokenization("Hello, world!")
    visualize_tokenization("The quick brown fox jumps over the lazy dog.")
    visualize_tokenization("I'm learning about tokenization in LLMs!")
    
    # Example 2: Compare different texts
    compare_tokenization_examples()
    
    # Example 3: Conversation token estimation
    print("\n" + "="*70)
    print("CONVERSATION TOKEN ESTIMATION")
    print("="*70)
    
    messages = [
        {"role": "system", "content": "You are a helpful coding assistant."},
        {"role": "user", "content": "How do I reverse a list in Python?"},
        {"role": "assistant", "content": "You can use list.reverse() or list[::-1]"},
        {"role": "user", "content": "What's the difference between them?"}
    ]
    
    counts = estimate_conversation_tokens(messages)
    print(f"\nMessage breakdown:")
    print(f"  System:    {counts['system']} tokens")
    print(f"  User:      {counts['user']} tokens")
    print(f"  Assistant: {counts['assistant']} tokens")
    print(f"  Overhead:  {counts['overhead']} tokens")
    print(f"  Total:     {counts['total']} tokens")
    
    # Example 4: Context limits
    demonstrate_context_limits()
    
    # Example 5: Cost estimation
    sample_prompt = """
    Analyze the following customer feedback and extract:
    1. Sentiment (positive/negative/neutral)
    2. Key themes
    3. Action items
    
    Feedback: "The product works well but the shipping was delayed."
    """
    
    estimate_cost_breakdown(sample_prompt, expected_output_tokens=150, model="gpt-3.5-turbo")
    estimate_cost_breakdown(sample_prompt, expected_output_tokens=150, model="gpt-4")
    
    # Example 6: Prompt efficiency
    analyze_prompt_efficiency("What is AI?")
    analyze_prompt_efficiency(
        "Please provide a comprehensive, detailed explanation of artificial "
        "intelligence, including its history, current applications, and future prospects."
    )


if __name__ == "__main__":
    main()
