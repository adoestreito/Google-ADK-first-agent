Google-ADK-first-agent
The simplest agent you can create using the Agent Development Kit (ADK). This agent is a Fastly Cloud Engineer who really wants to talk about Fastly.

🚀 Quick Start
Run the agent directly from your terminal using one of the following commands:

Web UI: adk web .

CLI Run: adk run my_first_agent

API Server: adk api_server (Exposes interactive OpenAPI docs at http://localhost:8000/docs)

🐍 Running in Code
Python Script (agent-script.py)
Python
import asyncio

asyncio.run(run_agent())
Jupyter Notebook / Google Colab
Python
await run_agent()
📄 YAML Configuration
You can also define and run your agent using a YAML configuration file.

Create a YAML agent:

Bash
adk create --type=config my_config_agent
(An example can be found in the YAML_agent folder).

Why use YAML? YAML configuration is ideal for straightforward agents where you want to keep things simple. Non-programmers can easily edit a YAML file to adjust agent behavior without touching code—making it great for cross-functional team collaboration.

📚 Primary References
ADK Documentation – Official ADK reference (update link as needed)

ADK Python Quickstart – Getting started guide

Agent Config Documentation – YAML configuration reference

Gemini Platform – Gemini platform overview