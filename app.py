import os
import uuid
import torch
import streamlit as st
import nest_asyncio

from src.orchestrator import aura_app

# -----------------------------
# FIXES FOR STREAMLIT CLOUD
# -----------------------------
os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"
torch.classes.__path__ = []
nest_asyncio.apply()

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Aura Fin-Guard | Hybrid Banking AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# DARK FINTECH THEME (CSS)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #e5e7eb;
}
h1, h2, h3 {
    color: #60a5fa;
}
.card {
    background-color: #020617;
    padding: 20px;
    border-radius: 14px;
    margin-bottom: 16px;
}
.highlight {
    border-left: 4px solid #38bdf8;
    padding-left: 12px;
}
.good { color: #22c55e; }
.warn { color: #facc15; }
.ai { color: #a78bfa; }
textarea {
    background-color: #020617 !important;
    color: white !important;
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE (MEMORY)
# -----------------------------
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_savings" not in st.session_state:
    st.session_state.total_savings = 0.0

# -----------------------------
# SIDEBAR — ROI & MEMORY
# -----------------------------
st.sidebar.title("💰 ROI Dashboard")
st.sidebar.metric(
    "Total Cost Saved",
    f"${st.session_state.total_savings:.2f}"
)
st.sidebar.info(f"🧵 Session ID: {st.session_state.thread_id[:8]}")
st.sidebar.success("Memory Active (LangGraph Thread)")
st.sidebar.markdown("---")
st.sidebar.markdown(
    "🚀 **Hybrid AI Routing**\n\n"
    "- Simple → Local AI\n"
    "- Complex → Reasoning Agent"
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
# 🛡️ Aura Fin-Guard  
### Hybrid Agentic Banking Orchestrator  

_Cost-aware AI system that routes banking queries intelligently_
""")

# -----------------------------
# ARCHITECTURE VISUALIZATION
# -----------------------------
with st.expander("🏗️ System Architecture", expanded=True):
    st.markdown("""
    <div class="card">
    <b>User Query</b>  
    ⬇️  
    <b>Intent Classifier</b> (Simple vs Complex)  
    ⬇️  
    <b>LangGraph Orchestrator</b> (Decision Router)  

    🟢 <b class="good">Simple</b> → Local LLM (Ollama) → ₹0 Cost  
    🟣 <b class="ai">Complex</b> → Reasoning Agent → Better Accuracy  

    ⬇️  
    <b>Final Banking Response</b>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# MAIN DASHBOARD LAYOUT
# -----------------------------
chat_col, status_col = st.columns([2, 1])

# -----------------------------
# CHAT HISTORY
# -----------------------------
with chat_col:
    st.subheader("💬 Conversation")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# -----------------------------
# USER INPUT
# -----------------------------
prompt = st.chat_input("Ask a banking question...")

if prompt:
    # USER MESSAGE
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with chat_col:
        with st.chat_message("user"):
            st.markdown(prompt)

    # CONFIG FOR LANGGRAPH MEMORY
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    # PROCESSING
    with status_col:
        st.markdown("### 🧠 System Decision")
        with st.spinner("Analyzing & routing..."):
            result = aura_app.invoke(
                {"query": prompt},
                config=config
            )

    response_text = result["response"]
    if hasattr(response_text, "content"):
        response_text = response_text.content

    cost_saved = result.get("cost_saved", 0.0)
    model_used = result.get("model_used", "Hybrid AI")

    st.session_state.total_savings += cost_saved

    # ASSISTANT RESPONSE
    with chat_col:
        with st.chat_message("assistant"):
            st.markdown(
                f"**Model Used:** `{model_used}`"
            )
            st.markdown(response_text)

            if cost_saved > 0:
                st.success(
                    f"✅ Saved ${cost_saved:.2f} using Local AI"
                )

    st.session_state.messages.append(
        {"role": "assistant", "content": response_text}
    )

    # SYSTEM STATUS PANEL
    with status_col:
        st.markdown(f"""
        <div class="card highlight">
        🔀 <b>Routing Decision</b><br>
        Model: <b>{model_used}</b><br>
        Cost Saved: <b class="good">${cost_saved:.2f}</b>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# WHY THIS MATTERS
# -----------------------------
with st.expander("🧠 Why this architecture matters"):
    st.write("""
    Traditional AI chatbots send all queries to the same large model,
    increasing cost, latency, and privacy risk.

    **Aura Fin-Guard** optimizes this by:
    - Routing simple queries locally
    - Escalating only when required
    - Preserving user privacy
    - Demonstrating real-world AI system design
    """)
