import tiktoken

def count_tokens(text: str, model: str) -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

# Return a dictionary with: token_count, estimated_cost, model
def estimate_cost(text: str, model: str) -> dict:
    output_tokens = 100
    input_tokens = count_tokens(text, model)

    pricing = {
        'gpt-3.5-turbo': {'input': 0.50, 'output': 1.50},
        'gpt-4': {'input': 30, 'output': 60},
        'gpt-4-turbo': {'input': 10, 'output': 30}
    }

    if(model not in pricing):
        raise ValueError(f"Pricing not defined for model: {model}")
    
    input_cost = input_tokens/1000000 * pricing[model]['input']
    output_cost = output_tokens/1000000 * pricing[model]['output']
    estimate_cost = input_cost + output_cost

    return{
        'tokens': input_tokens,
        'estimate_cost': estimate_cost,
        'model': model
    }

def main():
    text = 'The quick brown fox jumps over the lazy dog.'
    model = 'gpt-3.5-turbo'

    cost = estimate_cost(text, model)
    print(f"tokens count {cost['tokens']}")
    print(f"estimate_cost {cost['estimate_cost']}")
    print(f"model {cost['model']}")

if __name__ == "__main__":
    main()