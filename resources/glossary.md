# Glossary

A comprehensive guide to key terms and concepts used throughout the AI Agent Developer Course.

## A

**Agent**: An autonomous system that uses an LLM as its "brain" to perceive its environment, make decisions, and take actions to achieve specific goals. Unlike simple chatbots, agents can use tools, maintain memory, and execute multi-step plans.

**Agent Loop**: The core cycle of an agent: Observe (gather information) → Think (reason and plan) → Act (execute actions) → repeat. Also known as the perception-action loop.

**API (Application Programming Interface)**: A set of rules and protocols that allows different software applications to communicate. In this course, we primarily use REST APIs to interact with LLM providers.

**Anthropic**: Company that created Claude, a family of large language models known for long context windows and safety features.

## B

**Base Model**: An LLM trained on general data without specific fine-tuning for particular tasks. Examples include GPT-4-base, Llama-2-base.

## C

**Chain-of-Thought (CoT)**: A prompting technique where the model is encouraged to show its reasoning process step-by-step, leading to more accurate results on complex tasks.

**Chatbot**: An application designed for conversation with users. Can be simple (rule-based) or advanced (LLM-powered).

**ChromaDB**: An open-source vector database designed for storing and querying embeddings, commonly used in RAG systems.

**Claude**: A family of LLMs developed by Anthropic, including Claude 3 Opus, Sonnet, and Haiku variants.

**Context**: The information provided to an LLM to help it understand and respond to a query. Includes system prompts, conversation history, retrieved documents, and tool outputs.

**Context Engineering**: The practice of strategically organizing and structuring information provided to an LLM to optimize its performance. Goes beyond simple prompting to include system architecture decisions.

**Context Window**: The maximum amount of text (measured in tokens) that an LLM can process at once. For example, GPT-4 has a 8K, 32K, or 128K token context window depending on the version.

**CrewAI**: A framework for orchestrating role-playing autonomous AI agents, designed for collaborative multi-agent systems.

## D

**Deterministic**: Producing the same output every time given the same input. LLMs with temperature=0 are more deterministic (but never 100%).

## E

**Embedding**: A numerical representation (vector) of text that captures semantic meaning. Words or documents with similar meanings have similar embedding vectors. Typically 768-1536 dimensions.

**Embedding Model**: A specialized model that converts text into embeddings. Examples: OpenAI's text-embedding-ada-002, sentence-transformers.

**Episodic Memory**: Memory that stores specific experiences or events, allowing an agent to recall past interactions and learn from them.

## F

**FAISS (Facebook AI Similarity Search)**: A library for efficient similarity search and clustering of dense vectors, often used in RAG systems.

**Few-Shot Learning**: Providing an LLM with a few examples of the desired input-output pattern before asking it to perform a task.

**Fine-Tuning**: The process of further training a pre-trained model on specific data to specialize it for particular tasks or domains.

**Function Calling**: A feature of modern LLMs (GPT-4, Claude 3) that allows them to generate structured calls to external functions/tools based on natural language instructions.

## G

**Generative AI**: AI systems that can create new content (text, images, code, etc.) rather than just analyzing or classifying existing content.

**GPT (Generative Pre-trained Transformer)**: Architecture and model family developed by OpenAI. GPT-3.5 and GPT-4 are the most commonly used versions.

**Guardrails**: Safety mechanisms that constrain agent behavior, preventing harmful, unethical, or off-task actions.

## H

**Hallucination**: When an LLM generates plausible-sounding but factually incorrect or nonsensical information. A major challenge in LLM applications.

**Human-in-the-Loop (HITL)**: Design pattern where humans review and approve agent actions before execution, especially for high-stakes decisions.

**Hyperparameter**: Configuration settings for models (like temperature, max_tokens) that affect behavior but aren't learned during training.

## I

**Instruction Tuning**: Training technique where models are fine-tuned to follow instructions better, used to create models like GPT-3.5-turbo from base models.

## L

**LangChain**: Popular Python framework for building LLM applications, providing abstractions for prompts, chains, agents, and memory.

**LangGraph**: Extension of LangChain that uses graph-based workflows to create more complex, cyclical agent behaviors.

**Large Language Model (LLM)**: Neural networks trained on massive text datasets to understand and generate human-like text. Examples: GPT-4, Claude 3, Llama 2.

**Llama**: Open-source LLM family by Meta, including Llama 2 and Llama 3 versions.

**Long-Term Memory**: Persistent storage of information that agents can access across sessions, typically implemented using vector databases.

## M

**MCP (Model Context Protocol)**: A standardized protocol for connecting AI models with external data sources and tools, enabling consistent context integration.

**Memory**: In agents, the ability to store and retrieve information over time. Can be short-term (within a session) or long-term (across sessions).

**Multi-Agent System**: Architecture where multiple specialized agents work together, each handling specific aspects of a complex task.

## N

**Negative Prompting**: Explicitly telling the model what NOT to do or include, helping to avoid unwanted behaviors or outputs.

## O

**Ollama**: Tool for running LLMs locally on your machine, useful for development and avoiding API costs.

**Orchestration**: Coordinating multiple agents, tools, or steps in a workflow to accomplish complex tasks.

## P

**Planning**: The process by which an agent breaks down complex goals into actionable steps before execution.

**Prompt**: The text input given to an LLM, including instructions, context, and questions.

**Prompt Engineering**: The practice of crafting effective prompts to get desired outputs from LLMs. Includes techniques like few-shot learning, chain-of-thought, and role-playing.

**Prompt Template**: A reusable prompt structure with placeholders that can be filled with specific values.

## R

**RAG (Retrieval-Augmented Generation)**: Architecture that combines document retrieval with text generation, allowing LLMs to access external knowledge bases.

**ReAct (Reasoning and Acting)**: Agent pattern that interleaves reasoning (thinking through problems) with acting (using tools), creating a thought-action-observation loop.

**Reasoning**: The cognitive process of drawing conclusions, making inferences, and solving problems. In agents, this is the "thinking" phase.

**Retrieval**: The process of finding relevant documents or information from a knowledge base, typically using semantic similarity search.

## S

**Semantic Search**: Finding information based on meaning rather than exact keyword matches, typically using embeddings.

**Self-Reflection**: Technique where an agent evaluates its own outputs or actions and corrects mistakes, improving performance iteratively.

**Short-Term Memory**: Temporary storage of information within a single session, typically implemented as conversation history in the context window.

**System Prompt**: Special instructions given to an LLM that define its role, personality, and behavioral constraints. Typically processed differently than user prompts.

## T

**Temperature**: Hyperparameter (0-2) controlling randomness in LLM outputs. Lower values (0-0.3) are more deterministic; higher values (0.7-1.0) are more creative.

**Token**: Basic unit of text for LLMs. Roughly 1 token = 0.75 words. "Hello world" = ~2 tokens. Important for pricing and context limits.

**Tool**: External function or API that an agent can call to perform actions beyond text generation (e.g., web search, database query, file operations).

**Tree-of-Thought (ToT)**: Advanced reasoning technique where the model explores multiple reasoning paths (like a tree) before selecting the best solution.

## V

**Vector**: Numerical array representing text (embedding). Enables mathematical operations like similarity comparison.

**Vector Database**: Specialized database optimized for storing and querying high-dimensional vectors (embeddings). Examples: ChromaDB, Pinecone, Weaviate, FAISS.

## W

**Workflow**: Sequence of steps or decisions that accomplish a task. Can be linear, conditional, or parallel.

## Z

**Zero-Shot Learning**: Asking an LLM to perform a task without providing any examples, relying solely on its pre-trained knowledge.

---

## Common Abbreviations

- **AI**: Artificial Intelligence
- **API**: Application Programming Interface
- **CoT**: Chain-of-Thought
- **HITL**: Human-in-the-Loop
- **LLM**: Large Language Model
- **MCP**: Model Context Protocol
- **NLP**: Natural Language Processing
- **RAG**: Retrieval-Augmented Generation
- **SDK**: Software Development Kit
- **ToT**: Tree-of-Thought

---

## Further Reading

For more detailed explanations of these concepts, refer to the relevant module lessons throughout the course.
