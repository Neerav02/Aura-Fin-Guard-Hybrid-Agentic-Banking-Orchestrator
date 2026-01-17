# 🛡️ Aura Fin-Guard  
## Hybrid Agentic Banking Orchestrator (Cost-Aware AI System)

Aura Fin-Guard is an **AI-powered financial assistant** built to address a common real-world challenge:  
**balancing cost, latency, and intelligence in AI-driven systems**.

The project demonstrates a **Hybrid Agentic Routing Architecture**, where user queries are intelligently analyzed and routed to the most appropriate AI agent based on complexity — ensuring efficiency, scalability, and security.

🌐 **Live Demo (Streamlit):**  
👉 https://aura-fin-guard-hybrid-agentic-banking-orchestrator-szsw9ttiid6.streamlit.app/

---

## 📊 Core Innovation: Smart Routing at the Gate

Unlike traditional chatbots that send **every query to the same large model**, Aura Fin-Guard introduces **smart routing at the system entry point**.

Each query is classified before inference and handled accordingly:

- **Simple Queries**  
  → Processed locally using a lightweight LLM via **Ollama**  
  → ⚡ Low latency, zero inference cost  

- **Complex Queries**  
  → Routed to a more capable reasoning agent  
  → 🧠 Better contextual understanding and multi-step reasoning  

This design mirrors **enterprise AI systems**, where cost and performance must be optimized continuously.

---

## 🛠️ Key Features

- 🧭 **Intent Classification at Entry**  
  Fast intent detection to determine routing strategy (simple vs complex queries).

- 🔀 **Agentic Orchestration with LangGraph**  
  A state-machine-based workflow controlling decision flow and agent execution.

- 🤖 **Local LLM Inference (Offline-First)**  
  Uses **Ollama + lightweight models** for zero-cost, private inference.

- 🧠 **Multi-Step Reasoning for Complex Queries**  
  Handles transactional issues, escalation logic, and structured responses.

- 🧩 **Tool-Augmented Agents**  
  Designed for native integration with banking tools (e.g., balance checks, transaction status).

- 🔐 **Privacy-First Architecture**  
  Sensitive queries can be processed locally without leaving the system.

---

## 🏗️ Technical Architecture

User Query
↓
Intent Classifier
↓
LangGraph Orchestrator (State Machine)
↓
┌───────────────┬────────────────┐
│ Local LLM │ Advanced Agent │
│ (Ollama) │ (Reasoning) │
└───────────────┴────────────────┘
↓
Final Response


This architecture reflects how **modern AI platforms** build modular, agent-driven pipelines.

---

## 🧪 Example Flow

User: My money was deducted but the transaction failed
System:

Intent Detected → COMPLEX

Routed to Reasoning Agent

Response Generated with clear next steps


---

## 🛠 Tech Stack

- **Python**
- **LangGraph** (Agentic Orchestration)
- **LangChain Core & Community**
- **Ollama (Local LLM Runtime)**
- **Lightweight LLMs (Local Inference)**
- **Streamlit (UI & Deployment)**
- **SQLite (In-memory Checkpointing)**

---

## 🔐 Security & Cost Awareness

- ❌ No API keys required for core functionality  
- ❌ No paid cloud dependency  
- ✅ Offline-capable inference  
- ✅ Secrets excluded via `.gitignore`  
- ✅ GitHub Push Protection enabled  

Designed with **student-safe and production-inspired security practices**.

---

## 📈 Why This Architecture Matters

| Aspect        | Traditional Bot | Aura Fin-Guard |
|--------------|-----------------|----------------|
| Routing      | Static          | Intelligent |
| Cost Control | Poor            | Optimized |
| Privacy      | Cloud-only      | Hybrid |
| Scalability  | Limited         | Modular |
| Design Level | App-centric     | System-centric |

This project emphasizes **engineering decisions**, not just model usage.

---

## 🎓 Learning Value

Aura Fin-Guard demonstrates:
- Agent-based system design
- Cost-aware AI decision making
- Real-world trade-offs (latency vs intelligence)
- Secure handling of sensitive domains (banking)
- Clean, modular, production-inspired code

It goes beyond tutorials and reflects **how AI systems are designed in practice**.

---

## 🚧 Future Enhancements

- REST API layer using FastAPI
- Persistent memory with disk-backed storage
- Fraud detection agent
- Monitoring & analytics dashboard
- Multi-bank simulation

---

## 👤 Author

**Neerav Babel**  
B.Tech Computer Science  
Aspiring AI & Backend Engineer  

📌 *Built as a student-led, internship-focused project exploring agentic AI systems*

⭐ If you find this project interesting, consider starring the repository!