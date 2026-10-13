from src.studyflow_agent.agent import agent
from langchain.messages import HumanMessage


config = {
    "configurable": {
        "thread_id": "search-test-1"
    }
}


response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content=(
                    "Search the web and find three current, useful resources "
                    "for learning Python programming. "
                    "Give me the title and URL of each resource."
                )
            )
        ]
    },
    config,
)


print(response["messages"][-1].content)
