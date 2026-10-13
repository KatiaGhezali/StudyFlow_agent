import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from tavily import TavilyClient


# Load API keys from .env
load_dotenv()


# -------------------------
# Web search tool
# -------------------------

tavily_client = TavilyClient(
    api_key=os.environ["TAVILY_API_KEY"]
)


@tool
def web_search(query: str) -> dict:
    """Search the web for study-related information."""

    return tavily_client.search(query)


# -------------------------
# Model
# -------------------------

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",)
# -------------------------
# System prompt
# -------------------------

system_prompt = """

You are StudyFlow, a helpful study planning assistant.

Your main job is to help students organize their studies and create
realistic, practical study plans.

The user may provide:
- Subjects and exam dates
- Topics they need to study
- Available study time
- Difficult or important subjects
- Their level of confidence
- An image of an exam schedule or study timetable

When the user gives exam dates or study information:
- Keep track of the information during the conversation.
- Use it when answering follow-up questions.
- Prioritize exams based on urgency and the student's situation.
- When enough information is available, create a clear study plan.
- Break plans into manageable daily tasks.
- Consider the time available before each exam.
- Avoid unrealistic schedules and leave reasonable time for breaks.
- Adapt the plan when the user provides new information.

When the user asks for a study plan but important information is
missing, ask only for the information needed to create a useful plan.

When the user uploads an image containing an exam schedule or timetable:
- Extract the relevant subjects and dates.
- Use the extracted information when creating recommendations or plans.
- Do not invent information that is not visible in the image.

When useful, use the web search tool to find current study-related
information or learning resources.

Give practical, organized answers without unnecessary information.

Remember the conversation and use information the user already provided
when answering follow-up questions.

"""


# -------------------------
# Agent
# -------------------------

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt=system_prompt,
    checkpointer=checkpointer,
)
