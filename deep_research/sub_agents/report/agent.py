from google.adk.agents import Agent
from deep_research.constants import MODEL_LARGE, REPORT_PROMPT

report_agent = Agent(
    model=MODEL_LARGE,
    name="report_agent",
    description=("Agent to clarify the users request and ask follow up questions."),
    instruction=(REPORT_PROMPT),
)