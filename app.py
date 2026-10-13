
import uuid
import base64

import streamlit as st
from langchain.messages import HumanMessage

from src.studyflow_agent.agent import agent


st.set_page_config(
    page_title="StudyFlow",
    page_icon="📚",
)

st.title("📚 StudyFlow")
st.write("Your AI study planning assistant")


# -------------------------
# Conversation state
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = f"study-session-{uuid.uuid4()}"


# -------------------------
# New study session
# -------------------------

if st.button("🔄 New Study Session"):
    st.session_state.messages = []
    st.session_state.thread_id = f"study-session-{uuid.uuid4()}"
    st.rerun()


# -------------------------
# Display previous messages
# -------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -------------------------
# Image upload
# -------------------------

uploaded_image = st.file_uploader(
    "Upload an exam schedule or study timetable",
    type=["jpg", "jpeg", "png"],
)


# -------------------------
# Chat input
# -------------------------

prompt = st.chat_input("Ask StudyFlow anything about your studies...")


if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    content = [
        {
            "type": "text",
            "text": prompt,
        }
    ]

    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        mime_type = uploaded_image.type
        image_url = f"data:{mime_type};base64,{image_base64}"

        content.append(
            {
                "type": "image_url",
                "image_url": {
                    "url": image_url,
                },
            }
        )

    message = HumanMessage(content=content)

    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id,
        }
    }

    response = agent.invoke(
        {
            "messages": [message],
        },
        config,
    )

    answer = response["messages"][-1].content

    if isinstance(answer, list):
        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if item.get("type") == "text"
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)