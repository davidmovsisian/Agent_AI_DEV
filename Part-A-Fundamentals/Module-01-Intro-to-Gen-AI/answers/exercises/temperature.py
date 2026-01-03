import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def openAI(
    promt: str, 
    model:str="gpt-4o-mini",
    temperature: float=0.7,
    max_tokens: int = 50
) -> dict:

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    'role':'user',
                    'content': promt
                }
            ],
            temperature=temperature,
            max_tokens= max_tokens
        )

        return {
            'text': response.choices[0].message.content,
            'model': response.model,
            'input_tokens': response.usage.prompt_tokens,
            'output_tokens': response.usage.completion_tokens,
            'total_tokens': response.usage.total_tokens,
        }
    except Exception as e:
        return {'error': e}

def count_differences(s1: str, s2:str) -> int:
    diff = sum(c1 != c2 for c1, c2 in zip(s1,s2))
    diff+= abs(len(s1) - len(s2))

    return diff

def temperature_effect(promt: str) -> None:
    temperatures = [0,1]
    
    for temp in temperatures:
        print(f"\nTemperature = {temp}")

        result = openAI(promt)
        if 'error' in result:
            print("Error:", result['error'])
            continue
        
        prev = result['text']
        print(prev)

        for _ in range(2):
            result = openAI(promt)
            if 'error' in result:
                print("Error:", result['error'])
                continue
            curr = result['text']
            print(curr)
            diff = count_differences(prev, curr)
            ratio = diff/max(len(promt), 1)

            if ratio > 0.7:
                print('High')
            elif ratio > 0.4:
                print('Medium')
            else:
                print('Low')

def main():
    temperature_effect('Generate a creative product name for a coffee shop')

if __name__ == "__main__":
    main()