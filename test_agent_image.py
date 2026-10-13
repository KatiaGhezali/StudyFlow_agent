from langchain.messages import HumanMessage

from src.studyflow_agent.agent import agent
from src.studyflow_agent.image_utils import image_to_data_url


image_url = image_to_data_url("test_images/exam_schedule.jpg")


message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": (
                "Here is my exam schedule. "
                "Analyze it and tell me which exam I should prioritize "
                "first and why."
            ),
        },
        {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
        },
    ],
)


config = {
    "configurable": {
        "thread_id": "image-test-1"
    }
}


response = agent.invoke(
    {
        "messages": [message]
    },
    config,
)


print(response["messages"][-1].content)
