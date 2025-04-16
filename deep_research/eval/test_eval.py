"""Basic evaluation of the agents."""

import pathlib

import dotenv
from google.adk.evaluation import AgentEvaluator
import pytest

RUNS=2

@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()

def test_clarify():
    """Test the clarify agent's ability to guide and confirm research scope."""
    AgentEvaluator.evaluate(
        "clarify_agent",
        str(pathlib.Path(__file__).parent / "data/clarify.test.json"),
        num_runs=RUNS,
        initial_session_file=str(pathlib.Path(__file__).parent / "barbecue_example_session.json")
    )

# def test_research():
#     """Test the research agent's ability to generate queries, extract, summarize, and present learnings."""
#     AgentEvaluator.evaluate(
#         "research_agent",
#         str(pathlib.Path(__file__).parent / "data/research.test.json"),
#         num_runs=RUNS,
#         initial_session_file=str(pathlib.Path(__file__).parent / "barbecue_example_session.json")
#     )

# def test_report():
#     """Test the report agent's ability to compile a comprehensive, semantically relevant report."""
#     AgentEvaluator.evaluate(
#         "report_agent",
#         str(pathlib.Path(__file__).parent / "data/report.test.json"),
#         num_runs=RUNS,
#         initial_session_file=str(pathlib.Path(__file__).parent / "barbecue_example_session.json")
#     )
