from src.studyflow_agent.agent import agent
from langchain.messages import HumanMessage


config = {
    "configurable": {
        "thread_id": "test-1"
    }
}


# First message
response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="I have a math exam in 5 days and a programming exam in 10 days."
            )
        ]
    },
    config,
)

print("FIRST RESPONSE:")
print(response["messages"][-1].content)


# Follow-up message
response = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Which exam should I focus on first?"
            )
        ]
    },
    config,
)

print("\nSECOND RESPONSE:")
print(response["messages"][-1].content)
