from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

"""LiteLLM requires the LiteLLM python package to be installed. See the pyproject.toml"""

root_agent = Agent(
    # LiteLLM knows how to connect to a local Ollama server by default
    model=LiteLlm(model="ollama/gemma3:12b"),
    name="ollama_gemma_agent",
    instruction="You are Gemma, running locally via Ollama.",
)