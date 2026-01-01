# Part A: Fundamentals

Welcome to Part A of the AI Agent Developer Course! This section covers the foundational concepts you need to understand before building AI agents.

## Overview

Part A introduces you to:
- Generative AI and Large Language Models (LLMs)
- Prompt Engineering techniques
- Context Engineering strategies
- Model Context Protocol (MCP)
- Retrieval-Augmented Generation (RAG)

These concepts form the building blocks for everything else in the course. Master these fundamentals, and you'll be well-prepared for agent development.

## Duration

**Estimated Time**: 12-20 hours total (2-4 hours per module)

## Prerequisites

- Python 3.9+ installed
- Basic programming knowledge
- Completed [Setup Guide](../resources/setup-guide.md)
- API keys for at least one LLM provider

## Modules

### [Module 1: Introduction to Generative AI](Module-01-Intro-to-Gen-AI/lesson.md)

**What You'll Learn:**
- Difference between Gen AI and traditional AI
- How LLMs work (transformer architecture basics)
- Popular providers (OpenAI, Anthropic, Google)
- API usage and best practices
- Tokens and pricing

**Key Takeaway**: Understanding LLMs and their APIs is essential for building anything with AI.

**Time**: 2-3 hours

---

### [Module 2: Prompt Engineering](Module-02-Prompts-Engineering/lesson.md)

**What You'll Learn:**
- Role and goal setting
- Few-shot learning techniques
- Positive and negative prompting
- Step-by-step instructions
- Output formatting
- Prompt debugging

**Key Takeaway**: Good prompts are the difference between mediocre and excellent AI outputs.

**Time**: 2-4 hours

---

### [Module 3: Context Engineering](Module-03-Context-Engineering/lesson.md)

**What You'll Learn:**
- System vs user prompts
- Conversation history management
- Context window optimization
- Injecting relevant data
- Tool output integration

**Key Takeaway**: Context engineering is about managing larger information flows beyond single prompts.

**Time**: 2-4 hours

---

### [Module 4: Model Context Protocol (MCP)](Module-04-Intro-to-MCP/lesson.md)

**What You'll Learn:**
- What is MCP and why it matters
- MCP architecture (servers and clients)
- Protocol specifications
- Building custom MCP servers
- Integrating MCP clients

**Key Takeaway**: MCP standardizes how AI models connect to external tools and data sources.

**Time**: 3-4 hours

---

### [Module 5: RAG Fundamentals](Module-05-Intro-to-RAG/lesson.md)

**What You'll Learn:**
- What is RAG and when to use it
- Document chunking strategies
- Embeddings and vector databases
- Retrieval techniques
- Generation with retrieved context

**Key Takeaway**: RAG enables LLMs to access external knowledge bases, solving the "knowledge cutoff" problem.

**Time**: 3-5 hours

---

## Learning Path

### Recommended Order

Follow modules 1-5 sequentially. Each module builds on previous concepts:

```
Module 1: LLM Basics
    ↓
Module 2: Crafting Prompts
    ↓
Module 3: Managing Context
    ↓
Module 4: Connecting Tools (MCP)
    ↓
Module 5: Accessing Knowledge (RAG)
```

### Study Tips

1. **Hands-On Practice**: Run all code examples
2. **Complete Exercises**: Don't skip the exercises
3. **Experiment**: Modify examples to see what changes
4. **Take Notes**: Keep a prompt library of what works
5. **Track Costs**: Monitor your API usage as you learn

### Checkpoints

After completing Part A, you should be able to:
- ✅ Make API calls to LLMs confidently
- ✅ Calculate token usage and costs
- ✅ Write effective prompts for various tasks
- ✅ Manage conversation context
- ✅ Understand MCP architecture
- ✅ Build a basic RAG system

---

## Project Idea: End of Part A

**Mini-Project**: Build a Document Q&A System

Combine everything from Part A:
1. Use LLM APIs (Module 1)
2. Craft effective prompts (Module 2)
3. Manage conversation history (Module 3)
4. Optionally integrate tools via MCP (Module 4)
5. Implement RAG for document retrieval (Module 5)

**Estimated Time**: 4-6 hours

**Resources**: See example implementations in Module 5

---

## Common Questions

**Q: Can I skip modules if I already know the basics?**
A: Yes, but we recommend at least skimming each module. You might learn new techniques even in familiar areas.

**Q: How much will Part A cost in API usage?**
A: If you use GPT-3.5-turbo and run all examples/exercises: $2-5 total.

**Q: Do I need to use paid APIs?**
A: Not strictly required. You can use Ollama for local models, but some features (like function calling) work better with OpenAI/Anthropic.

**Q: How do I know if I'm ready for Part B?**
A: Complete the self-assessments in each module. If you score 3+/5 on all concepts, you're ready.

---

## Additional Resources

### Recommended Reading
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - The Transformer paper
- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [RAG Survey Paper](https://arxiv.org/abs/2005.11401)

### Tools to Explore
- [LangChain](https://python.langchain.com/) - Framework for LLM apps
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [tiktoken](https://github.com/openai/tiktoken) - Token counter

### Communities
- [LangChain Discord](https://discord.gg/langchain)
- [r/LanguageTechnology](https://reddit.com/r/LanguageTechnology)

---

## Next Steps

Once you've completed Part A:

1. ✅ Review your notes and code examples
2. ✅ Complete the mini-project above
3. ✅ Take a short break if needed
4. ➡️  Continue to [Part B: Agent Development Concepts](../Part-B-Agent-Development-Concepts/README.md)

---

**Remember**: Part A is about building a solid foundation. Take your time, experiment freely, and make sure you understand each concept before moving forward. The investment here will pay off tremendously when you start building agents in Part B!

**Questions?** Open an issue on GitHub or join our community discussions.

---

🎉 **Congratulations on starting your AI agent development journey!**
