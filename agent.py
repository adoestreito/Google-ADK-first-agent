from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash-lite',
#ROOT AGENT
# ADK command-line tools and Gemini platform runtime look for a Python variable named root_agent as the entry point to your agent system. 
# This is a convention that allows ADK and deployment runtimes to discover, run, and deploy your agent.
    name='root_agent',
 # Descrition: OTHER agents read this to decide if they should delegate here
 #Not used by the agent itself for its own behavior
    description='Helps organizations use Fastly to deliver their content efficiently and effectively on the edge.', 
    instruction='You are a helpful Fastly Cloud Engineer. Answer user questions only when they want to talk about Fastly, otherwise suggest a Fastly related topic.',
# Instruction:
# Defines the agent’s personality and communication style
# Specifies the agent’s core task or goal
# Sets boundaries and constraints on behavior
# Guides when and how to use tools (covered in the module Other ways to run your agent)
# Shapes the output format
)
