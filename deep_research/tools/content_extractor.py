from crawl4ai import AsyncWebCrawler
from google.adk import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool
from google.adk.tools.tool_context import ToolContext

from deep_research.constants import GEMINI_FLASH, CONTENT_EXTRACTOR_TOOL_PROMPT

async def extract_content_from_url(url: str, include_headers: bool = True, tool_context: ToolContext = None) -> dict:
    """
    Extracts content from a URL using Crawl4AI.

    Args:
        url (str): The URL to extract content from.
        include_headers (bool): Whether to include headings in the extraction.
        tool_context (ToolContext, optional): Tool context for ADK.

    Returns:
        dict: A dictionary containing the extracted content, metadata, and status.
    """
    try:
        # Create an instance of AsyncWebCrawler
        async with AsyncWebCrawler() as crawler:
            # Run the crawler on the URL
            result = await crawler.arun(
                url=url,
                include_headers=include_headers
            )

            # Create a structured response
            # FIX: Get the page title safely from the result
            page_title = getattr(result, 'title', None)
            if page_title is None:
                # Try to extract title from markdown or use URL as fallback
                page_title = url.split('/')[-1] if '/' in url else url

                # Try to find title in markdown if available
                if hasattr(result, 'markdown') and result.markdown:
                    # Look for # headers in markdown
                    lines = result.markdown.split('\n')
                    for line in lines:
                        if line.startswith('# '):
                            page_title = line.replace('# ', '')
                            break

            response = {
                "status": "success",
                "title": page_title,
                "url": url,
                "markdown_content": result.markdown[:10000] if hasattr(result, 'markdown') else "No content extracted",  # Limit content to 10k chars
                "content_length": len(result.markdown) if hasattr(result, 'markdown') else 0,
                "headers": [h.text for h in result.headers] if hasattr(result, 'headers') and include_headers else [],
                "word_count": len(result.markdown.split()) if hasattr(result, 'markdown') else 0,
                "has_truncated_content": len(result.markdown) > 10000 if hasattr(result, 'markdown') else False
            }

            # Optional: Store the full content in session state for the summarizer to use
            if tool_context and hasattr(result, 'markdown'):
                tool_context.state[f"extracted_content_{url}"] = result.markdown

            return response
    except Exception as e:
        return {
            "status": "error",
            "url": url,
            "error_message": str(e)
        }

def create_content_extractor_agent():
    """
    Creates an agent specialized in extracting and analyzing content from URLs.
    """
    # Create the FunctionTool for content extraction
    extract_content_tool = FunctionTool(func=extract_content_from_url)

    # Create and return the content extractor agent
    extractor_agent = Agent(
        name="content_extractor",
        model=GEMINI_FLASH,
        description="A specialized agent that extracts and analyzes content from web pages using Crawl4AI.",
        instruction=CONTENT_EXTRACTOR_TOOL_PROMPT,
        tools=[extract_content_tool]
    )

    return AgentTool(agent=extractor_agent)