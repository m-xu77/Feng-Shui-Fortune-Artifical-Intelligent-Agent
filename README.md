# Feng-Shui-Fortune-Artifical-Intelligent-Agent - A GPT-based Agent Inspired by Master Chen

## 1. Project Background & Vision

In the era of Large Language Models (LLMs) and multi-modal agents, I envision creating a virtual Agent that blends traditional Chinese cultural elements with cutting-edge AI. My Agent takes the form of a fortune-teller and Feng Shui master — modeled after "Chen the Blind," a character from the Chinese novel _Ghost Blows Out the Light_ — with a distinct personality, professional abilities, and the capability to serve users across platforms.

This project demonstrates how I can engineer and deploy a GPT-powered embodied agent that performs mid-level professional services traditionally done by humans.

## 2. Character Design & Core Concept

### Virtual Persona: Master Chen (Inspired by _Ghost Blows Out the Light_)

**Key Traits:**

- Wise and experienced, with a folksy, charismatic manner
- Proficient in Feng Shui, Eight-Character astrology, and geomantic analysis
- Explains insights through storytelling and metaphors

**Agent Design Goals:**

- Maintains long-term memory and builds rapport with users
- Retrieves real-time knowledge and updates its internal domain models
- Performs voice synthesis and emotional tone adaptation
- Embeddable into web, mobile, and messaging platforms
- Extensible through tool integration (e.g., search engines, calendars, TTS, NLP APIs)

## 3. System Architecture Overview

### Core Modules

| Module                 | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| Dialogue Manager       | Context tracking, intent recognition, emotion detection                    |
| Long-term Memory       | Stores and retrieves past user interactions and character history          |
| Tool Plugin Layer      | Integrates tools for search, lunar calendar, location, voice, emails, etc. |
| Domain Knowledge Base  | Learns and updates Feng Shui & astrology knowledge                         |
| Frontend UI            | Chat interface, character avatar, voice input/output                       |
| Multi-platform Adapter | APIs to integrate with WeChat, web, mini-programs, etc.                    |

### Recommended Tech Stack

- **LLM Backend:** GPT-4 / Claude / ChatGLM (local models)
- **Vector DB:** FAISS / Weaviate / Qdrant
- **Voice Tools:** Microsoft TTS + Whisper / iFlyTek TTS
- **Emotion Detection:** OpenAI Evals / NLP-based emotion classifiers
- **Agent Framework:** LangChain or LlamaIndex + ReAct pattern
- **Deployment:** Docker + FastAPI + Redis + PostgreSQL

## 4. Product Requirements Document (PRD)

### MVP Feature List

| Feature                | Subfeature           | Description                                                |
| ---------------------- | -------------------- | ---------------------------------------------------------- |
| Conversational Ability | Multi-turn Memory    | Remembers name, birthday, family info, etc.                |
| Astrology Services     | Bazi Analysis        | User inputs birthdate/time, agent returns destiny analysis |
| Feng Shui Services     | Home Layout Analysis | User submits address or floorplan for review (optional)    |
| Tool Integration       | Lunar/Huangli Lookup | Retrieves auspicious days, holidays, solar terms           |
| Tool Integration       | Real-time Web Search | Answers like "What’s tomorrow’s weather in Beijing?"       |
| Multi-modal Feedback   | Emotion Detection    | Adjusts tone and language style based on sentiment         |
| Voice Support          | Speech Output        | Replies in Master Chen’s voice using TTS engine            |

### Advanced Features (Post-MVP)

- “Apprentice Mode”: Users can learn fortune-telling techniques
- Analytics Dashboard: Track usage and inquiry topics
- Weekly/Annual forecast push notifications
- Open API for third-party integrations

## 5. Sample User Journey

### First-time User (User A)

- Enters via WeChat Mini Program
- Inputs: “Born on June 8, 1990 (lunar), 9 AM”
- Agent recognizes astrology intent > Performs Bazi calculation > Responds in Master Chen’s tone
- Example response: “My friend, your wealth luck this year is both direct and indirect. Seize the first half of the year…”
- User data saved for future personalization

### Returning User (User B)

- Receives weekly horoscope reminders
- Asks: “Is this week good for signing contracts?”
- Agent cross-references calendar + user chart to respond

## 6. Development Timeline (Milestones)

| Phase                     | Duration   | Deliverables                                    |
| ------------------------- | ---------- | ----------------------------------------------- |
| Requirements Finalization | Week 1     | Full PRD, character design, feature scoping     |
| Tech Stack & Infra Setup  | Weeks 2–3  | LLM API integration, memory architecture, tools |
| Prototype Build           | Weeks 4–6  | Working frontend/backend with MVP features      |
| Testing & Refinement      | Weeks 7–8  | Prompt tuning, emotion handling, UI polish      |
| Deployment                | Weeks 9–10 | Publish on Web, WeChat Mini Program, etc.       |
| Final Presentation        | Week 11    | Documentation, live demo, retrospective report  |

## 7. Future Directions & Highlights

- Image-based Feng Shui interpretation (upload floor plans)
- Group chatroom functionality with multiple users
- Generative “Fortune Card” feature (for social media sharing)

## 8. Conclusion

This virtual Agent project combines tradition and innovation, demonstrating how I can build a uniquely personified, long-memory, tool-augmented LLM agent capable of delivering mid-level professional services. It also exemplifies how to engineer practical AI applications with distinct personas, modular architecture, and multi-platform deployment.
