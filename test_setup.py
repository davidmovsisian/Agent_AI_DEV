import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print("✓ API key loaded successfully")
    print(f"✓ API key starts with: {api_key[:10]}...")
else:
    print("✗ API key not found. Check your .env file")

# Test imports
try: 
    import anthropic
    import langchain
    import chromadb
    import tiktoken
    from openai import OpenAI
    print("✓ All required packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")

print("\n🎉 Setup complete! You're ready to start learning.")