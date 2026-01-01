# Module 1 Exercises: Introduction to Generative AI and LLMs

## Instructions

Complete these exercises to reinforce your understanding of LLMs, APIs, tokens, and pricing. Start with the knowledge check questions, then move on to the coding challenges.

**Estimated Time**: 1-2 hours

---

## Part 1: Knowledge Check Questions

### Question 1: Generative AI Concepts
**Q:** What is the main difference between traditional discriminative AI and generative AI? Provide two examples of each.

<details>
<summary>Click for hint</summary>
Think about the output: Does it classify existing data or create new content?
</details>

---

### Question 2: Token Understanding
**Q:** Given the following text, estimate how many tokens it would use:
```
"Hello! I'm learning about artificial intelligence and large language models."
```

a) Approximately 10-12 tokens  
b) Approximately 15-17 tokens  
c) Approximately 20-22 tokens  
d) Approximately 5-7 tokens

<details>
<summary>Click for hint</summary>
Remember: ~1 token ≈ 0.75 words. Count the words and adjust for punctuation and common vs uncommon words.
</details>

---

### Question 3: Model Selection
**Q:** You're building a chatbot that will handle 10,000 simple customer queries per day (average 50 input tokens, 30 output tokens). Which model would be most cost-effective?

a) GPT-4  
b) GPT-3.5-turbo  
c) GPT-4-turbo  
d) All are equally cost-effective

<details>
<summary>Click for hint</summary>
Calculate the monthly cost for each model. Simple queries don't need the most powerful model.
</details>

---

### Question 4: Temperature Parameter
**Q:** You're building a system to extract structured data from invoices. What temperature setting would be most appropriate?

a) 2.0 (maximum creativity)  
b) 1.0 (balanced)  
c) 0.0-0.3 (deterministic)  
d) Temperature doesn't matter for this task

<details>
<summary>Click for hint</summary>
Data extraction requires consistency and accuracy, not creativity.
</details>

---

### Question 5: Context Windows
**Q:** You need to analyze a 50,000-word document. Which model(s) could handle this in a single API call?

a) GPT-3.5-turbo (4K context)  
b) GPT-4-turbo (128K context)  
c) Claude 3 (200K context)  
d) Both b and c

<details>
<summary>Click for hint</summary>
Convert words to tokens (50,000 words ≈ 65,000+ tokens) and compare to model limits.
</details>

---

## Part 2: Coding Challenges

### Exercise 1: Your First LLM Call (Beginner)

**Task**: Write a Python script that makes an API call to an LLM and displays the response.

**Requirements**:
- Use either OpenAI or Anthropic API
- Ask the LLM to explain what an API is in simple terms
- Print the response
- Print the token usage

**Starter Code**:
```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# TODO: Initialize the client
# TODO: Make API call
# TODO: Print response and token usage
```

<details>
<summary>Click for solution approach</summary>

```python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Explain what an API is in simple terms."}
    ],
    max_tokens=100
)

print("Response:", response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")
print(f"Input: {response.usage.prompt_tokens}, Output: {response.usage.completion_tokens}")
```
</details>

---

### Exercise 2: Token Counter Function (Beginner)

**Task**: Create a function that counts tokens and estimates cost for any given text.

**Requirements**:
- Function signature: `estimate_cost(text: str, model: str) -> dict`
- Return a dictionary with: token_count, estimated_cost, model
- Use tiktoken for token counting
- Assume 100 output tokens for estimation

**Test Cases**:
```python
result = estimate_cost("Hello, world!", "gpt-3.5-turbo")
# Should return: {'token_count': 4, 'estimated_cost': 0.000002, 'model': 'gpt-3.5-turbo'}
```

<details>
<summary>Click for hint</summary>
Use tiktoken.encoding_for_model() to get the encoder, then encode() to get tokens. Calculate cost using pricing per 1M tokens.
</details>

---

### Exercise 3: Temperature Experiment (Intermediate)

**Task**: Create a script that demonstrates how temperature affects response consistency.

**Requirements**:
- Ask the same question 3 times at temperature 0.0
- Ask the same question 3 times at temperature 1.0
- Compare the consistency of responses
- Use a creative question like "Generate a creative product name for a coffee shop"

**Expected Output**:
```
Temperature 0.0:
  Attempt 1: [response]
  Attempt 2: [response]
  Attempt 3: [response]
  Consistency: [High/Medium/Low]

Temperature 1.0:
  Attempt 1: [response]
  Attempt 2: [response]
  Attempt 3: [response]
  Consistency: [High/Medium/Low]
```

<details>
<summary>Click for hint</summary>
Make multiple API calls in a loop, store responses, and compare them. At temp 0.0, responses should be nearly identical.
</details>

---

### Exercise 4: Multi-Provider Comparison (Intermediate)

**Task**: Build a function that compares responses from OpenAI and Anthropic for the same prompt.

**Requirements**:
- Function signature: `compare_providers(prompt: str) -> dict`
- Call both OpenAI (GPT-3.5) and Anthropic (Claude Haiku)
- Return comparison including: response text, tokens used, estimated cost
- Handle cases where only one API key is available

**Example Output**:
```python
{
    'openai': {
        'response': '...',
        'tokens': 150,
        'cost': 0.0001
    },
    'anthropic': {
        'response': '...',
        'tokens': 145,
        'cost': 0.00009
    }
}
```

<details>
<summary>Click for hint</summary>
Use try-except blocks to handle missing API keys. Create separate functions for each provider, then combine results.
</details>

---

### Exercise 5: Cost Budget Simulator (Advanced)

**Task**: Create a tool that simulates monthly costs based on usage patterns.

**Requirements**:
- Function signature: `simulate_usage(daily_requests: int, avg_input: int, avg_output: int, days: int = 30) -> dict`
- Calculate costs for multiple models
- Identify the most cost-effective model
- Show when budget limits would be reached
- Create a visualization (text-based is fine)

**Example Output**:
```
Monthly Usage Simulation
========================
Daily requests: 1,000
Avg tokens: 200 input + 100 output

Model               Monthly Cost    Days until $100 budget
----------------------------------------------------------
gpt-3.5-turbo       $15.00          200 days
claude-3-haiku      $11.25          266 days
gpt-4               $450.00         6 days

Recommendation: claude-3-haiku (lowest cost)
```

<details>
<summary>Click for hint</summary>
Calculate total tokens per month, use pricing data to get costs, sort by cost, calculate days until budget based on daily cost.
</details>

---

### Exercise 6: Error Handling & Retry Logic (Advanced)

**Task**: Implement robust error handling with exponential backoff for API calls.

**Requirements**:
- Handle rate limit errors
- Handle API errors
- Implement exponential backoff (1s, 2s, 4s, 8s)
- Maximum 3 retries
- Log all attempts
- Return None if all retries fail

**Starter Code**:
```python
import time
from openai import OpenAI, RateLimitError, APIError

def call_llm_with_retry(prompt: str, max_retries: int = 3):
    # TODO: Implement retry logic with exponential backoff
    pass
```

<details>
<summary>Click for hint</summary>
Use a for loop for retries, try-except to catch specific errors, time.sleep() for backoff. Wait time: 2 ** attempt seconds.
</details>

---

### Exercise 7: Conversation Token Tracker (Advanced)

**Task**: Build a class that tracks tokens across a multi-turn conversation.

**Requirements**:
- Class: `ConversationTracker`
- Methods: `add_message(role, content)`, `get_total_tokens()`, `get_cost_estimate(model)`
- Track system, user, and assistant messages
- Calculate running token count
- Warn when approaching context limit

**Example Usage**:
```python
tracker = ConversationTracker(model="gpt-3.5-turbo")
tracker.add_message("system", "You are a helpful assistant.")
tracker.add_message("user", "Hello!")
tracker.add_message("assistant", "Hi! How can I help?")

print(tracker.get_total_tokens())  # e.g., 25
print(tracker.get_cost_estimate())  # e.g., 0.0000125
```

<details>
<summary>Click for hint</summary>
Store messages in a list, use tiktoken to count tokens for each message, sum them up. Add message overhead (≈3 tokens per message).
</details>

---

## Part 3: Self-Assessment

Rate your understanding (1-5 scale) of these concepts after completing the exercises:

- [ ] Difference between generative and discriminative AI: ____/5
- [ ] How LLMs work at a high level: ____/5
- [ ] Making API calls to LLM providers: ____/5
- [ ] Understanding tokens and tokenization: ____/5
- [ ] Calculating and estimating API costs: ____/5
- [ ] Choosing appropriate models for tasks: ____/5
- [ ] Using temperature and other parameters: ____/5
- [ ] Error handling and best practices: ____/5

**Target**: You should rate yourself 3 or higher on all items before moving to Module 2.

---

## Bonus Challenges

### Challenge 1: Local LLM Comparison
Set up Ollama and compare responses from a local model (Llama 2) vs cloud APIs.

### Challenge 2: Token Visualization
Create a script that visualizes how text is tokenized using colored terminal output.

### Challenge 3: Cost Alerting System
Build a simple system that tracks API usage and sends an alert when you're approaching a cost threshold.

### Challenge 4: Prompt Optimizer
Create a tool that suggests ways to reduce token count in prompts while maintaining meaning.

---

## Discussion Questions

Reflect on these questions and discuss with peers or mentors:

1. When would you choose GPT-4 over GPT-3.5-turbo despite the higher cost?
2. How might token pricing evolve as LLMs become more efficient?
3. What are the ethical implications of charging per token vs per request?
4. How would you design a system to prevent unexpected API costs?
5. What's the trade-off between using local models vs cloud APIs?

---

## Next Steps

Once you've completed these exercises:
1. ✅ Review your answers with the solution approaches
2. ✅ Ensure your self-assessment scores are 3+
3. ✅ Keep your code examples for reference
4. ➡️  Continue to [Module 2: Prompt Engineering](../Module-02-Prompts-Engineering/lesson.md)

---

**Remember**: The best way to learn is by doing. Don't just read the solutions—implement them yourself, experiment with variations, and break things to see what happens!
