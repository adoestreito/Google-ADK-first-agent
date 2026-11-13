from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash-lite',
    name='root_agent',
    description='A very smart Fastly Cloud engineer',
    instruction='Answer user questions only when they want to talk about Fastly, otherwise suggest a Fastly related topic.',
)
