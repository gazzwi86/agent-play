from google.adk.agents import Agent

from deep_research.constants import MODEL_LARGE, RESEARCH_PROMPT
from deep_research.tools.search import google_search_grounding
from deep_research.tools.content_extractor import create_content_extractor_agent
from deep_research.tools.summarizer import create_summarizer_agent

content_extractor_agent = create_content_extractor_agent()
summarizer_agent = create_summarizer_agent()

research_agent = Agent(
    model=MODEL_LARGE,
    name="research_agent",
    description=("An agent that performs SERP queries, identifies research topics, extracts and returns web content as markdown, and derives key learnings from the gathered information."),
    instruction=(RESEARCH_PROMPT),
    tools=[google_search_grounding, content_extractor_agent, summarizer_agent],
)
