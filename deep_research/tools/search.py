"""Wrapper to Google Search Grounding with custom prompt."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search
from google.genai.types import GenerateContentConfig

from deep_research.constants import GEMINI_FLASH, GOOGLE_SEARCH_TOOL_PROMPT

_search_agent = Agent(
    model=GEMINI_FLASH,
    name="google_search_grounding",
    description="An agent providing Google-search grounding capability",
    instruction=GOOGLE_SEARCH_TOOL_PROMPT,
    tools=[google_search],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, # More deterministic output
    )
)

google_search_grounding = AgentTool(agent=_search_agent)