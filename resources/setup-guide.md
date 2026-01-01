# Setup Guide

This guide will help you set up your development environment for the AI Agent Developer Course.

## Prerequisites

- **Python 3.9 or higher**: Check your version with `python --version` or `python3 --version`
- **Basic programming knowledge**: Familiarity with Python syntax and concepts
- **Text editor or IDE**: VS Code, PyCharm, or any editor of your choice
- **Git**: For cloning the repository
- **API Keys**: You'll need access to at least one LLM provider (OpenAI or Anthropic)

## Step 1: Clone the Repository

```bash
git clone https://github.com/davidmovsisian/Agent_AI_DEV.git
cd Agent_AI_DEV
```

## Step 2: Create a Virtual Environment

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

## Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install all required packages including:
- OpenAI and Anthropic SDKs
- LangChain and LangGraph
- CrewAI
- ChromaDB for vector storage
- And other dependencies

**Note**: Installation may take 5-10 minutes depending on your internet connection.

## Step 4: Set Up API Keys

### 4.1 Get API Keys

You'll need at least one of the following:

**OpenAI (Recommended for beginners):**
1. Visit https://platform.openai.com/signup
2. Create an account or sign in
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key (it will only be shown once!)
6. Add billing information (you'll get some free credits initially)

**Anthropic (Claude):**
1. Visit https://console.anthropic.com/
2. Create an account or sign in
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key

**Note**: Both providers charge for API usage. Start with small models (gpt-3.5-turbo or claude-3-haiku) to minimize costs while learning.

### 4.2 Create Environment File

1. Copy the example environment file:
```bash
cp resources/.env.example .env
```

2. Open `.env` in your text editor and add your API keys:
```
OPENAI_API_KEY=sk-proj-...your-actual-key...
ANTHROPIC_API_KEY=sk-ant-...your-actual-key...
```

3. Save the file

**⚠️ Security Warning**: Never commit your `.env` file to git! It's already in `.gitignore`, but be careful.

## Step 5: Verify Installation

Create a test file `test_setup.py`:

```python
import os
from dotenv import load_dotenv
import openai

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
    print("✓ All required packages imported successfully")
except ImportError as e:
    print(f"✗ Import error: {e}")

print("\n🎉 Setup complete! You're ready to start learning.")
```

Run the test:
```bash
python test_setup.py
```

You should see all checkmarks (✓) indicating successful setup.

## Step 6: Test Your First API Call

Create `test_api.py`:

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello, AI Agent Developer!' in a creative way."}
        ],
        max_tokens=50
    )
    print("API Response:")
    print(response.choices[0].message.content)
    print("\n✓ API connection successful!")
except Exception as e:
    print(f"✗ Error: {e}")
```

Run the test:
```bash
python test_api.py
```

If you see a creative response, your setup is complete!

## Common Issues and Solutions

### Issue 1: "ModuleNotFoundError"
**Solution**: Make sure your virtual environment is activated and you've run `pip install -r requirements.txt`

### Issue 2: "API key not found"
**Solution**: 
- Check that `.env` file exists in the root directory
- Verify API key is correctly copied without extra spaces
- Make sure you're loading environment variables with `load_dotenv()`

### Issue 3: "Rate limit exceeded" or "Insufficient quota"
**Solution**: 
- Check your API usage on the provider's dashboard
- Add billing information if you haven't
- Use smaller models (gpt-3.5-turbo instead of gpt-4)

### Issue 4: "Module 'openai' has no attribute 'ChatCompletion'"
**Solution**: You're using an old version. Update with `pip install --upgrade openai`

### Issue 5: Import errors for sentence-transformers
**Solution**: If you're on Mac M1/M2, you may need to install specific versions:
```bash
pip install sentence-transformers==2.5.0 --no-cache-dir
```

## Cost Management Tips

1. **Start with free credits**: Both OpenAI and Anthropic offer initial credits
2. **Use smaller models**: gpt-3.5-turbo ($0.0005-0.0015 per 1K tokens) vs gpt-4 ($0.03-0.06 per 1K tokens)
3. **Set usage limits**: Configure spending limits in your API dashboard
4. **Monitor usage**: Regularly check your usage on the provider's dashboard
5. **Use caching**: Many examples cache responses to avoid repeated calls

**Estimated Course Cost**: $5-20 depending on which models you use and how much experimentation you do.

## Alternative: Use Local Models

If you want to avoid API costs, you can use local models with Ollama:

```bash
# Install Ollama (macOS/Linux)
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2

# Run locally
ollama run llama2
```

Many course examples can be adapted to work with Ollama, though some features (like function calling) may be limited.

## Next Steps

1. Read through the [Glossary](glossary.md) to familiarize yourself with key terms
2. Check out [Additional Resources](additional-resources.md) for supplementary materials
3. Start with [Module 1: Intro to Gen AI](../Part-A-Fundamentals/Module-01-Intro-to-Gen-AI/lesson.md)

## Need Help?

- Review the course [README](../README.md)
- Check the troubleshooting section above
- Open an issue on GitHub
- Join our community discussions

---

Happy learning! 🚀
