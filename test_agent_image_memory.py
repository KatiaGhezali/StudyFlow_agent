from langchain.messages import HumanMessage

from src.studyflow_agent.agent import agent
from src.studyflow_agent.image_utils import image_to_data_url


image_url = image_to_data_url("test_images/exam_schedule.jpg")

config = {
    "configurable": {
        "thread_id": "image-memory-test-1"
    }
}


# First message: give StudyFlow the exam schedule
first_message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Here is my exam schedule. Remember it for my next question.",
        },
        {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
        },
    ],
)


response = agent.invoke(
    {
        "messages": [first_message]
    },
    config,
)

print("FIRST RESPONSE:")
print(response["messages"][-1].content)


# Second message: ask about the schedule without sending the image again
second_message = HumanMessage(
    content="How should I divide my study time between Mathematics and Programming?",
)


response = agent.invoke(
    {
        "messages": [second_message]
    },
    config,
)

print("\nSECOND RESPONSE:")
print(response["messages"][-1].content)
