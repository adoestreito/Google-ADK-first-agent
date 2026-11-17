"""
Test script to see state access directly.
Run with: python test_state.py
"""

from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

# Setup session and runner
session_service = InMemorySessionService()

# Create the session initially
app_name = "name_extractor_app"
user_id = "test_user"
session_id = "test_session"

session_service.create_session(
    app_name=app_name,
    user_id=user_id,
    session_id=session_id
)

runner = Runner(
    agent=root_agent,
    app_name=app_name,
    session_service=session_service
)

# Test: Extract name
user_message = Content(parts=[Part(text="Hi, my name is Alex Johnson")])

print("=== Running agent ===")
result = runner.run(
    user_id=user_id,
    session_id=session_id,
    new_message=user_message
)

# Show final response
for event in result:
    if event.is_final_response():
        print(f"\nAgent response: {event.content.parts[0].text}")

# Access state programmatically by fetching the current session from the service
current_session = session_service.get_session(
    app_name=app_name, 
    user_id=user_id, 
    session_id=session_id
)

print(f"\n=== State after execution ===")
print(f"Full state: {current_session.state}")
extracted_name = current_session.state.get('user_name') if current_session.state else None
print(f"Extracted name: {extracted_name}")

if extracted_name:
    print("Name was successfully extracted and stored!")
else:
    print("Name extraction failed")

# Test accessing in subsequent turns
print("\n=== Simulating second turn ===")
result2 = runner.run(
    user_id=user_id,
    session_id=session_id,
    new_message=Content(parts=[Part(text="What's my name?")])
)

for event in result2:
    if event.is_final_response():
        print(f"Agent response: {event.content.parts[0].text}")

# Re-fetch session to verify persistence across turns
updated_session = session_service.get_session(
    app_name=app_name, 
    user_id=user_id, 
    session_id=session_id
)
print(f"\nState still contains: {updated_session.state.get('user_name')}")
print("State persists across turns!")