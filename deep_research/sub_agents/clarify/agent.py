from google.adk.agents import Agent

from deep_research.constants import MODEL_SMALL, CLARIFY_PROMPT

follow_up_questions_agent = Agent(
    model=MODEL_SMALL,
    name="follow_up_questions_agent",
    description="A research agent specilised in clarifying a research request, defining the key considerations and details the users wishes to include in the report.",
    instruction=CLARIFY_PROMPT,
)
