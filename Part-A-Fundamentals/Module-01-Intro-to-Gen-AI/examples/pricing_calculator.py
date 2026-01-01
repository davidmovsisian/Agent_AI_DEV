"""
Pricing Calculator - Estimate and Compare LLM API Costs

This module helps you understand and estimate costs for different LLM
providers and models. It includes:
1. Real-time cost calculation based on token usage
2. Cost comparison across providers
3. Budget planning tools
4. Usage scenarios with cost projections

Requirements:
    - tiktoken>=0.6.0
"""

import tiktoken
from typing import Dict, List, Tuple
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ModelPricing:
    """
    Pricing information for an LLM model.
    
    Attributes:
        name: Model name
        provider: Provider name (OpenAI, Anthropic, etc.)
        input_price: Price per 1M input tokens (USD)
        output_price: Price per 1M output tokens (USD)
        context_limit: Maximum context window in tokens
    """
    name: str
    provider: str
    input_price: float
    output_price: float
    context_limit: int


# Pricing data (as of 2024 - check provider websites for current prices)
PRICING_DATA = {
    # OpenAI models
    "gpt-3.5-turbo": ModelPricing("gpt-3.5-turbo", "OpenAI", 0.50, 1.50, 4096),
    "gpt-3.5-turbo-16k": ModelPricing("gpt-3.5-turbo-16k", "OpenAI", 3.00, 4.00, 16384),
    "gpt-4": ModelPricing("gpt-4", "OpenAI", 30.00, 60.00, 8192),
    "gpt-4-32k": ModelPricing("gpt-4-32k", "OpenAI", 60.00, 120.00, 32768),
    "gpt-4-turbo": ModelPricing("gpt-4-turbo", "OpenAI", 10.00, 30.00, 128000),
    
    # Anthropic models
    "claude-3-opus": ModelPricing("claude-3-opus", "Anthropic", 15.00, 75.00, 200000),
    "claude-3-sonnet": ModelPricing("claude-3-sonnet", "Anthropic", 3.00, 15.00, 200000),
    "claude-3-haiku": ModelPricing("claude-3-haiku", "Anthropic", 0.25, 1.25, 200000),
}


def calculate_cost(
    input_tokens: int,
    output_tokens: int,
    model: str
) -> Dict[str, float]:
    """
    Calculate the cost for a given number of tokens.
    
    Args:
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        model: Model identifier
        
    Returns:
        dict: Cost breakdown
        
    Example:
        >>> calculate_cost(1000, 500, "gpt-3.5-turbo")
        {
            'input_cost': 0.0005,
            'output_cost': 0.00075,
            'total_cost': 0.00125,
            'model': 'gpt-3.5-turbo'
        }
    """
    if model not in PRICING_DATA:
        raise ValueError(f"Unknown model: {model}")
    
    pricing = PRICING_DATA[model]
    
    input_cost = (input_tokens / 1_000_000) * pricing.input_price
    output_cost = (output_tokens / 1_000_000) * pricing.output_price
    total_cost = input_cost + output_cost
    
    return {
        'input_cost': input_cost,
        'output_cost': output_cost,
        'total_cost': total_cost,
        'model': model,
        'provider': pricing.provider
    }


def compare_models(
    input_tokens: int,
    output_tokens: int,
    models: List[str] = None
) -> None:
    """
    Compare costs across different models.
    
    Args:
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        models: List of model names to compare (None = all models)
    """
    if models is None:
        models = list(PRICING_DATA.keys())
    
    print(f"\n{'='*80}")
    print(f"COST COMPARISON")
    print(f"{'='*80}")
    print(f"Input tokens: {input_tokens:,}")
    print(f"Output tokens: {output_tokens:,}")
    print(f"Total tokens: {input_tokens + output_tokens:,}")
    print(f"\n{'Model':<25} {'Provider':<12} {'Cost':<12} {'vs Cheapest'}")
    print("-" * 80)
    
    # Calculate costs for all models
    results = []
    for model in models:
        if model in PRICING_DATA:
            cost_data = calculate_cost(input_tokens, output_tokens, model)
            results.append(cost_data)
    
    # Sort by cost
    results.sort(key=lambda x: x['total_cost'])
    cheapest_cost = results[0]['total_cost']
    
    # Display results
    for result in results:
        cost = result['total_cost']
        multiplier = cost / cheapest_cost if cheapest_cost > 0 else 0
        print(f"{result['model']:<25} {result['provider']:<12} "
              f"${cost:>10.6f}  {multiplier:>6.1f}x")


def estimate_monthly_cost(
    requests_per_day: int,
    avg_input_tokens: int,
    avg_output_tokens: int,
    model: str
) -> Dict[str, float]:
    """
    Estimate monthly costs based on usage patterns.
    
    Args:
        requests_per_day: Average requests per day
        avg_input_tokens: Average input tokens per request
        avg_output_tokens: Average output tokens per request
        model: Model identifier
        
    Returns:
        dict: Monthly cost projections
    """
    days_per_month = 30
    monthly_requests = requests_per_day * days_per_month
    
    total_input = monthly_requests * avg_input_tokens
    total_output = monthly_requests * avg_output_tokens
    
    cost = calculate_cost(total_input, total_output, model)
    
    return {
        'daily_requests': requests_per_day,
        'monthly_requests': monthly_requests,
        'monthly_input_tokens': total_input,
        'monthly_output_tokens': total_output,
        'daily_cost': cost['total_cost'] / days_per_month,
        'monthly_cost': cost['total_cost'],
        'yearly_cost': cost['total_cost'] * 12,
        'model': model
    }


def scenario_analysis() -> None:
    """
    Analyze common usage scenarios with cost projections.
    """
    print(f"\n{'='*80}")
    print("SCENARIO ANALYSIS - Monthly Cost Projections")
    print(f"{'='*80}")
    
    scenarios = [
        {
            "name": "Small Chatbot",
            "description": "100 users, 5 messages/day each",
            "requests_per_day": 500,
            "avg_input": 100,
            "avg_output": 75
        },
        {
            "name": "Medium Customer Support",
            "description": "1000 users, 3 messages/day each",
            "requests_per_day": 3000,
            "avg_input": 200,
            "avg_output": 150
        },
        {
            "name": "Document Analyzer",
            "description": "100 documents/day, long context",
            "requests_per_day": 100,
            "avg_input": 3000,
            "avg_output": 500
        },
        {
            "name": "Code Assistant",
            "description": "50 developers, 20 queries/day each",
            "requests_per_day": 1000,
            "avg_input": 150,
            "avg_output": 200
        }
    ]
    
    for scenario in scenarios:
        print(f"\n📊 Scenario: {scenario['name']}")
        print(f"   {scenario['description']}")
        print(f"   {scenario['requests_per_day']} requests/day, "
              f"{scenario['avg_input']} input + {scenario['avg_output']} output tokens")
        print(f"\n{'Model':<20} {'Monthly Cost':<15} {'Yearly Cost'}")
        print("-" * 60)
        
        # Compare top models
        models = ["gpt-3.5-turbo", "gpt-4", "claude-3-haiku", "claude-3-sonnet"]
        costs = []
        
        for model in models:
            est = estimate_monthly_cost(
                scenario['requests_per_day'],
                scenario['avg_input'],
                scenario['avg_output'],
                model
            )
            costs.append((model, est['monthly_cost'], est['yearly_cost']))
        
        # Sort by monthly cost
        costs.sort(key=lambda x: x[1])
        
        for model, monthly, yearly in costs:
            print(f"{model:<20} ${monthly:>12.2f}   ${yearly:>12.2f}")


def budget_planner(budget_usd: float, model: str) -> Dict[str, int]:
    """
    Calculate how many requests you can make within a budget.
    
    Args:
        budget_usd: Your budget in USD
        model: Model identifier
        
    Returns:
        dict: Request estimates
    """
    # Assume typical request: 200 input + 100 output tokens
    typical_input = 200
    typical_output = 100
    
    cost_per_request = calculate_cost(typical_input, typical_output, model)['total_cost']
    
    max_requests = int(budget_usd / cost_per_request) if cost_per_request > 0 else 0
    
    return {
        'budget': budget_usd,
        'model': model,
        'cost_per_request': cost_per_request,
        'max_requests': max_requests,
        'requests_per_day_30days': max_requests // 30,
        'requests_per_day_365days': max_requests // 365
    }


def print_budget_analysis(budget: float) -> None:
    """
    Print a budget analysis for different models.
    
    Args:
        budget: Monthly budget in USD
    """
    print(f"\n{'='*80}")
    print(f"BUDGET ANALYSIS - ${budget}/month")
    print(f"{'='*80}")
    print(f"Assuming typical request: 200 input + 100 output tokens")
    print(f"\n{'Model':<20} {'$/request':<12} {'Requests/day':<15} {'Total/month'}")
    print("-" * 80)
    
    models = ["gpt-3.5-turbo", "gpt-4-turbo", "gpt-4", "claude-3-haiku", "claude-3-sonnet"]
    
    for model in models:
        plan = budget_planner(budget, model)
        print(f"{model:<20} ${plan['cost_per_request']:>10.6f}  "
              f"{plan['requests_per_day_30days']:>13,}  "
              f"{plan['max_requests']:>13,}")


def optimize_model_selection(
    expected_requests: int,
    avg_input_tokens: int,
    avg_output_tokens: int
) -> None:
    """
    Recommend optimal model based on usage and cost.
    
    Args:
        expected_requests: Expected number of requests per month
        avg_input_tokens: Average input tokens
        avg_output_tokens: Average output tokens
    """
    print(f"\n{'='*80}")
    print("MODEL OPTIMIZATION RECOMMENDATION")
    print(f"{'='*80}")
    print(f"Expected usage: {expected_requests:,} requests/month")
    print(f"Average tokens: {avg_input_tokens} input + {avg_output_tokens} output")
    
    # Calculate costs for different models
    models = list(PRICING_DATA.keys())
    costs = []
    
    total_input = expected_requests * avg_input_tokens
    total_output = expected_requests * avg_output_tokens
    
    for model in models:
        cost_data = calculate_cost(total_input, total_output, model)
        costs.append((model, cost_data['total_cost'], PRICING_DATA[model]))
    
    # Sort by cost
    costs.sort(key=lambda x: x[1])
    
    print(f"\n💡 Recommendations:")
    print(f"\n1. Most Economical: {costs[0][0]}")
    print(f"   Monthly cost: ${costs[0][1]:.2f}")
    print(f"   Best for: Simple tasks, high volume")
    
    print(f"\n2. Balanced Option: {costs[len(costs)//2][0]}")
    print(f"   Monthly cost: ${costs[len(costs)//2][1]:.2f}")
    print(f"   Best for: Moderate complexity, reasonable volume")
    
    # Check if high token count might need larger context
    if avg_input_tokens > 2000:
        print(f"\n⚠️  Note: High input token count ({avg_input_tokens})")
        print(f"   Consider models with larger context windows:")
        for model, cost, pricing in costs:
            if pricing.context_limit >= 16000:
                print(f"   - {model}: {pricing.context_limit:,} token limit (${cost:.2f}/month)")


def main():
    """
    Run all demonstrations.
    """
    print("\n" + "="*80)
    print("LLM PRICING CALCULATOR")
    print("="*80)
    
    # Example 1: Single request comparison
    compare_models(1000, 500)
    
    # Example 2: Larger request
    print("\n")
    compare_models(5000, 2000, models=["gpt-3.5-turbo", "gpt-4", "claude-3-haiku", "claude-3-sonnet"])
    
    # Example 3: Scenario analysis
    scenario_analysis()
    
    # Example 4: Budget planning
    print_budget_analysis(50.00)
    print_budget_analysis(200.00)
    
    # Example 5: Optimization
    optimize_model_selection(10000, 250, 150)
    optimize_model_selection(1000, 4000, 500)
    
    # Example 6: Cost tracking tips
    print(f"\n{'='*80}")
    print("💰 COST OPTIMIZATION TIPS")
    print(f"{'='*80}")
    print("""
1. Start with cheaper models (GPT-3.5, Claude Haiku) and upgrade only if needed
2. Set max_tokens to limit output length and prevent runaway costs
3. Cache responses for frequently asked questions
4. Use prompt compression techniques to reduce input tokens
5. Implement rate limiting to control usage
6. Monitor usage regularly via provider dashboards
7. Consider batch processing for non-urgent requests
8. Use streaming only when needed (doesn't reduce cost but improves UX)
9. Set up billing alerts on provider platforms
10. Test thoroughly in development to avoid waste in production
    """)


if __name__ == "__main__":
    main()
