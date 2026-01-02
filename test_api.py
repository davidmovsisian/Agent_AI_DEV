import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat. completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello, AI Agent Developer!' in a creative way."}
        ],
        max_tokens=50
    )
    print("API Response:")
    print(response.choices[0]. message.content)
    print("\n✓ API connection successful!")
except Exception as e:
    print(f"✗ Error: {e}")