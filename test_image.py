import base64

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
)


with open("test_images/exam_schedule.jpg", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")


message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": """
Look at this exam schedule.

Extract:
1. The subjects
2. The exam dates
3. Any other useful information you can read

Present the information in a clear table.
""",
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{image_data}"
            },
        },
    ]
)


response = model.invoke([message])

print(response.content)
