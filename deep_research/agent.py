from google.adk.agents import Agent
from google.adk.runners import Runner

from deep_research.constants import MODEL_SMALL, APP_NAME, ROOT_PROMPT
from deep_research.utils.session import session_service
from deep_research.sub_agents.clarify.agent import follow_up_questions_agent
from deep_research.sub_agents.research.agent import research_agent
from deep_research.sub_agents.report.agent import report_agent

root_agent = None
runner_root = None

if 'follow_up_questions_agent' and 'research_agent' and 'report_agent' in globals():
    orchestrator_agent = Agent(
        model=MODEL_SMALL,
        name="deep_research_orchestrator_agent",
        description=("The main coordinator agent. Handles research requests and delegates to specialist agents."),
        instruction=(ROOT_PROMPT),
        sub_agents=[
            follow_up_questions_agent,
            research_agent,
            report_agent
        ],
    )
    
    root_agent = orchestrator_agent
    runner_root = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service # Use the NEW stateful session service
    )

    print(f"✅ Root Agent '{orchestrator_agent.name}' created using model '{MODEL_SMALL}' with sub-agents: {[sa.name for sa in orchestrator_agent.sub_agents]}")

else:
    print("❌ Cannot create root agent because one or more sub-agents failed to initialize or 'get_weather' tool is missing.")
    if 'clarify_root_agent' not in globals(): print(" - clarify_root_agent is missing.")
    if 'research_agent' not in globals(): print(" - research_agent is missing.")
    if 'report_agent' not in globals(): print(" - report_agent is missing.")
    if 'google_search_grounding' not in globals(): print(" - google_search_grounding function is missing.")


