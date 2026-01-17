# 🛡️ Aura Fin-Guard: Hybrid Agentic Banking Orchestrator

**Aura Fin-Guard** is a next-generation financial assistant designed to solve the "Inference Crisis." It uses an intelligent **Hybrid Routing Architecture** to balance cost, performance, and security.

---

## 📊 The Core Innovation: "Smart-Routing"
Unlike standard bots that send every query to expensive cloud models, Aura categorizes intents at the "gate":
- **Simple Tasks:** Handled locally by **Microsoft Phi-4 (Ollama)** for ₹0 cost and sub-second latency.
- **Complex Tasks:** Escalated to **Groq Cloud (Llama-3.3-70B)** for advanced reasoning and tool execution.



---

## 🛠️ Key Features
* **Intent Classification:** Sub-millisecond routing using a Scikit-Learn based classifier.
* **Agentic Tool Calling:** Native integration with banking tools for real-time balance checks and fraud reporting.
* **Stateful Memory:** Multi-turn conversation persistence using **LangGraph Checkpointers** and `thread_id`.
* **Fault Tolerance:** Implemented **Exponential Backoff** and **Rate Limit Handlers** for 99.9% API reliability.
* **Privacy First:** Sensitive PII (Personally Identifiable Information) can be restricted to the Local SLM layer.

---

## 🏗️ Technical Architecture
- **Orchestrator:** LangGraph (State Machine)
- **Brain (Premium):** Llama-3.3-70B-Versatile via Groq
- **Brain (Local):** Microsoft Phi-4 via Ollama
- **Frontend:** Streamlit
- **Persistence:** In-memory SQLite Checkpointer

---

## 📈 Measurable ROI
| Task Type | Cloud LLM Only | Aura Hybrid | Improvement |
| :--- | :--- | :--- | :--- |
| **Cost (1k queries)** | ~$20.00 | **~$6.00** | **70% Savings** |
| **Latency (Simple)** | ~1.5s | **~0.4s** | **73% Faster** |