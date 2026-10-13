from langchain.messages import HumanMessage
from src.studyflow_agent.agent import model
from src.studyflow_agent.image_utils import image_to_data_url


image_url = image_to_data_url("test_images/exam_schedule.jpg")


message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": (
                "Analyze this exam schedule. "
                "Extract the subjects and exam dates. "
                "Present them clearly."
            ),
        },
        {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
        },
    ]
)


response = model.invoke([message])


print(response.content)
