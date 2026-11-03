# EON — Personal Artificial Intelligence System

**Beyond Intelligence. Into Possibility.**

EON is a personal AI assistant project focused on building an intelligent, conversational system with reasoning, memory, research, and agentic capabilities.

The vision is to create a standalone AI application that combines a ChatGPT-like conversational experience with a futuristic JARVIS-inspired interface.

## Vision & Goals

EON aims to become a personal AI system capable of:

-  Natural language conversations
-  Reasoning and problem-solving
-  Short-term and long-term memory
-  Research and information retrieval
-  Document and data analysis
-  Programming assistance
-  Voice-based interaction
-  Agentic workflows and intelligent planning

**Core Principle:** EON will operate as an independent application. It will not control the user's computer, keyboard, mouse, operating system, or desktop applications.

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, JavaScript, HTML, CSS |
| Build Tool | Vite |
| Backend | Python, FastAPI |
| API Server | Uvicorn |
| AI Runtime | Ollama |
| Initial AI Model | Qwen 3 4B |
| Database | SQLite (Planned) |
| Machine Learning | PyTorch, Scikit-learn |
| Data Processing | NumPy, Pandas |
| Version Control | Git, GitHub |

## System Architecture

```text
             EON AI SYSTEM
                   |
          React + Vite Frontend
                   |
             FastAPI Backend
                   |
              AI Engine
                   |
             Ollama Runtime
                   |
               Qwen 3 4B
                   |
          Memory & Data Layer
             SQLite (Planned)
```

## Current Project Structure

```text
EON/
│
├── script/
│   └── backend/
│       └── app/
│           ├── __init__.py
│           └── main.py
│
├── .gitignore
└── README.md
```

## Current Features

- Initial FastAPI backend.
- EON welcome API endpoint.
- Backend health-check endpoint.
- Interactive API documentation.
- Local AI model downloaded and tested through Ollama.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | EON welcome endpoint |
| GET | `/health` | Backend health check |
| GET | `/docs` | Interactive API documentation |

## Getting Started

### Prerequisites

- Python 3.13+
- Ollama
- Git

### Backend Setup

Clone the repository:

```bash
git clone https://github.com/shettynaman01-cyber/EON.git
cd EON
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment (Windows PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

Install backend dependencies:

```bash
python -m pip install fastapi uvicorn
```

Start the backend server:

```bash
uvicorn app.main:app --reload --app-dir .\script\backend
```

Open the API:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

## Development Roadmap

- [x] Project initialization
- [x] Python virtual environment setup
- [x] FastAPI backend setup
- [x] Initial API endpoints
- [x] Ollama installation
- [x] Qwen 3 4B model download and testing
- [x] Git and GitHub integration
- [ ] Connect FastAPI with Ollama
- [ ] Integrate Qwen 3 4B into EON
- [ ] Develop conversational AI functionality
- [ ] Build React frontend
- [ ] Design futuristic EON dashboard
- [ ] Implement conversation history and memory
- [ ] Add voice interaction
- [ ] Develop reasoning and agentic workflows
- [ ] Experiment with custom AI/ML models

## Development Philosophy

EON follows a hybrid AI development approach:

1. Start with existing open-weight AI models.
2. Build custom AI application architecture and memory systems.
3. Develop intelligent workflows and agent capabilities.
4. Learn and experiment with machine learning and deep learning.
5. Gradually train and integrate custom AI models.

The long-term goal is to build a capable personal AI system while understanding the technologies and intelligence behind it.

---

**Project Name:** EON  
**Category:** Personal Artificial Intelligence System  
**Status:** Early Development  
**Repository:** [GitHub – EON](https://github.com/shettynaman01-cyber/EON)
