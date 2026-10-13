# StudyFlow 📚

StudyFlow is an AI-powered study planning assistant built as a learning project.

It helps students organize their studies, plan for upcoming exams, and find useful learning resources through a conversational interface.

## Features

- **AI study assistant:** Get help organizing subjects and preparing for exams.
- **Study planning:** Create practical study plans based on exam dates and available study time.
- **Image understanding:** Upload an exam schedule or timetable for the assistant to analyze.
- **Web search:** Find relevant study resources using Tavily.
- **Conversation memory:** Ask follow-up questions while retaining context during the current session.
- **New study sessions:** Start a fresh conversation whenever needed.

## Technologies

- Python 3.13
- Streamlit
- LangChain
- LangGraph
- Google Gemini
- Tavily Search

## Prerequisites

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- A Google Gemini API key
- A Tavily API key

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/KatiaGhezali/StudyFlow_agent.git
cd StudyFlow_agent
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root and add your own API keys:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Replace the example values with your actual API keys.

**Never commit your `.env` file or publish your API keys.**

### 4. Run the application

```bash
uv run streamlit run app.py
```

## Project structure

```text
StudyFlow_agent/
├── app.py
├── src/
│   └── studyflow_agent/
│       ├── __init__.py
│       ├── agent.py
│       └── image_utils.py
├── test_images/
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md
```

## Learning objectives

This project explores AI agents, tool integration, multimodal inputs, web search, and conversation memory using LangChain and LangGraph.

## Project status

StudyFlow is a learning project developed to explore AI-powered study assistance and agent-based applications.
