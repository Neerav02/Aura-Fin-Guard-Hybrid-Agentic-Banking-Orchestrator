import os
import torch
import uuid # Needed for unique session tracking
os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"
torch.classes.__path__ = []

import streamlit as st
import nest_asyncio
from src.orchestrator import aura_app

nest_asyncio.apply()

# 1. PAGE CONFIGURATION
st.set_page_config(page_title="Aura Fin-Guard ROI Dashboard", layout="wide")

# 2. SESSION STATE FOR MEMORY (Thread ID)
# We generate a unique thread_id once per session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# 3. SIDEBAR: The ROI Tracker
st.sidebar.title("💰 Live ROI Tracker")
if 'total_savings' not in st.session_state:
    st.session_state.total_savings = 0.0

st.sidebar.metric("Total Money Saved", f"${st.session_state.total_savings:.2f}")
st.sidebar.info(f"Session ID: {st.session_state.thread_id[:8]}") # Visual proof of memory
st.sidebar.markdown("---")
st.sidebar.info("Memory is active. The agent will remember context within this thread.")

# 4. MAIN INTERFACE
st.title("🛡️ Aura Fin-Guard")
st.subheader("Intelligent & Cost-Aware Financial Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. CHAT INPUT & MEMORY LOGIC
if prompt := st.chat_input("Ask a banking question..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # CONFIGURE MEMORY FOR THE GRAPH
    # This config tells LangGraph which thread to look up in the Checkpointer
    config = {"configurable": {"thread_id": st.session_state.thread_id}}

    with st.spinner("Analyzing & Routing..."):
        # We pass the config to enable memory access
        result = aura_app.invoke({"query": prompt}, config=config)
        response_text = result['response']
        
        if hasattr(response_text, 'content'):
            response_text = response_text.content

    # Update Savings Tracker
    st.session_state.total_savings += result.get('cost_saved', 0.0)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(f"**[Model: {result.get('model_used')}]**")
        st.markdown(response_text)
        if result.get('cost_saved') > 0:
            st.success(f"✅ Saved ${result['cost_saved']} by using Local AI!")

    st.session_state.messages.append({"role": "assistant", "content": response_text})