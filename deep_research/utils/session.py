from google.adk.sessions import InMemorySessionService

from deep_research.constants import APP_NAME, SESSION_ID, USER_ID

# Create a NEW session service instance
session_service = InMemorySessionService()
print("✅ New InMemorySessionService created.")

initial_state = {
    "research_subject": "",
    "follow_up_answers": [],
    "sources": [],
    "markdown": [],
    "learnings": [],
    "report": []
}

# Create the session, providing the initial state
session_stateful = session_service.create_session(
    app_name=APP_NAME, # Use the consistent app name
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state # <<< Initialize state during creation
)
print(f"✅ Session '{SESSION_ID}' created for user '{USER_ID}'.")

# Verify the initial state was set correctly
retrieved_session = session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id = SESSION_ID)

print("\n--- Initial Session State ---")
if retrieved_session:
    print(retrieved_session.state)
else:
    print("Error: Could not retrieve session.")
