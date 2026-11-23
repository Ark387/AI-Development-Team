import os
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph_supervisor import create_supervisor
from modules.ai_team.graph import create_chat_model
from langgraph.agents import create_agent

def create_chat_model():
    return ChatOpenAI(
        model=os.eviron("OPENAI_MODEL"),
        base_url=os.getenv("OPENAI_BASE_URL") or None,
        temperaturn =0,
        max_retries=6
    )

def build_team(model=None):

    model = create_chat_model()

    planner = create_agent(
        name = "Planner Sub-Agent",
        model=model,
        tools=[],
        system_prompt=""
    )

    reviewer = create_agent(
        name = "Reviewer Sub-Agent",
        model=model,
        tools=[],
        system_prompt=""
    )

    developer = create_agent(
        name = "Developer Sub-Agent",
        model=model,
        tools=[],
        system_prompt=""
    )

    compiler = create_agent(
        name = "Compiler Sub-Agent",
        model=model,
        tools=[],
        system_prompt=""
    )

