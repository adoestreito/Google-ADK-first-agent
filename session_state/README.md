[ADK documentation - State: The Session's Scratchpad](https://adk.dev/sessions/state/)

Session state is a Python dictionary accessible through the 'session.state' attribute on Gemini platform. Think of it as variables your agent stores and your code can check

**When to use state:**

When your code needs to check exact values (if state.get("name"):).

When making routing decisions programmatically.

When tracking conversation progress or user information.

DON’T use for only providing context to LLM (conversation history already does that).

[Accessing state](https://adk.dev/sessions/state/#how-state-is-updated-recommended-methods)

-State is accessed as a dictionary: session.state.
-Use .get(key, default) for safe reading (returns default if key doesn't exist).
-State persists across all turns in the same session.
-Your code can check state values to make programmatic decisions.

[Saving responses with output_key](https://adk.dev/agents/llm-agents/#data-handling)

-You want to save the agent’s response for later use.
-You need programmatic access to what the agent said.
-When building applications that need to track extracted information.
-DON’T use for: Responses you don’t need to reference later.

```
from google.adk.agents import LlmAgent

agent = LlmAgent(
    name="topic_extractor",
    model="gemini-flash-latest",
    instruction="Extract the main topic. Return ONLY the topic.",
    output_key="topic"  # Automatically saves response to state["topic"]
)

# After agent runs, state["topic"] contains the response text
# No manual code needed!
```