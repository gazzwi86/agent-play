from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.tool_context import ToolContext
from deep_research.constants import GEMINI_FLASH_LITE, CONTENT_SUMMARIZER_TOOL_PROMPT

def summarize_content(content: str, summary_length: str = "medium", tool_context: ToolContext = None) -> dict:
    """
    Tool to save content for the agent to summarize.

    This doesn't actually summarize the content itself - it just saves the content
    to the session state so the LLM can access it directly.

    Args:
        content (str): The text content to summarize.
        summary_length (str): The desired length of the summary ("short", "medium", or "long").
        tool_context (ToolContext, optional): Tool context for ADK.

    Returns:
        dict: A dictionary with status information.
    """
    if tool_context:
        tool_context.state["content_to_summarize"] = content
        tool_context.state["requested_summary_length"] = summary_length

        # Calculate some metrics on the content
        word_count = len(content.split())

        return {
            "status": "success",
            "message": f"Content saved for summarization (word count: {word_count}). Ready to generate a {summary_length} summary.",
            "word_count": word_count
        }
    else:
        return {
            "status": "error",
            "message": "Tool context not available. Cannot store content."
        }

def create_summarizer_agent():
    """
    Creates an agent specialized in summarizing content.
    """
    # Create a simple tool to save content for summarization
    summarize_content_tool = summarize_content

    # Create and return the summarizer agent
    summarizer_agent = Agent(
        name="summarizer",
        model=GEMINI_FLASH_LITE,
        description="A specialized agent that summarizes content at various detail levels.",
        instruction=CONTENT_SUMMARIZER_TOOL_PROMPT,
        tools=[summarize_content_tool]
    )

    return AgentTool(agent=summarizer_agent)