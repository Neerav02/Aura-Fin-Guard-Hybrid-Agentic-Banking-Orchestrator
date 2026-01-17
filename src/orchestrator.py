import ollama
import os 
from typing import Annotated, Union
from typing_extensions import TypedDict
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph.message import add_messages

from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from src.classifier import classify_intent 
from src.tools import get_balance, report_fraud

load_dotenv()

# 1. SETUP
tools = [get_balance, report_fraud]
tool_node = ToolNode(tools)
memory = MemorySaver()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("GROQ_API_KEY")
).bind_tools(tools)

# Define State with the messages reducer
class AgentState(TypedDict):
    messages: Annotated[list, add_messages] # This handles the chat history
    query: str
    intent: str
    response: str # Final text to show the user
    cost_saved: float
    model_used: str

# 2. NODES

def intent_routing_node(state: AgentState):
    print(f"\n[SYSTEM] Analyzing Query: {state['query']}")
    intent = classify_intent(state['query'])
    # Initialize messages with the user query if empty
    return {"intent": intent, "messages": [HumanMessage(content=state['query'])]}

def call_local_slm(state: AgentState):
    print("--- [ROUTING] -> LOCAL/FALLBACK SLM ---")
    try:
        # Try local Ollama (Works when running locally)
        output = ollama.chat(model='phi4', messages=[{'role': 'user', 'content': state['query']}])
        response_text = output['message']['content']
        model_name = "Microsoft Phi-4 (Local)"
    except Exception:
        # Fallback to a small cloud model (Works when deployed on the web)
        print("⚠️ Local Ollama offline. Using Cloud Fallback...")
        fallback_llm = ChatGroq(model="llama-3.2-1b-preview", groq_api_key=os.getenv("GROQ_API_KEY"))
        res = fallback_llm.invoke([HumanMessage(content=state['query'])])
        response_text = res.content
        model_name = "Llama-3.2-1b (Cloud Fallback)"

    return {
        "response": response_text, 
        "messages": [AIMessage(content=response_text)],
        "cost_saved": 0.05, 
        "model_used": model_name
    }

def call_premium_llm(state: AgentState):
    print("--- [ROUTING] -> PREMIUM AI (THINKING...) ---")
    # Pass the full message history to the LLM
    response = llm.invoke(state['messages'])
    
    return {
        "messages": [response], 
        "response": response.content, # Update response for the UI
        "model_used": "Groq (Llama-3.3-70b)",
        "cost_saved": 0.0
    }

# 3. ROUTING LOGIC

def route_decision(state: AgentState):
    return "local_ai" if state['intent'] == 'simple' else "premium_ai"

# 4. BUILD THE WORKFLOW
workflow = StateGraph(AgentState)

workflow.add_node("intent_node", intent_routing_node)
workflow.add_node("local_ai", call_local_slm)
workflow.add_node("premium_ai", call_premium_llm)
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "intent_node")

workflow.add_conditional_edges(
    "intent_node",
    route_decision,
    {"local_ai": "local_ai", "premium_ai": "premium_ai"}
)

# FIXED: tools_condition looks at state["messages"] automatically
workflow.add_conditional_edges(
    "premium_ai",
    tools_condition,
    {
        "tools": "tools",   # Matches the name in add_node
        "__end__": "__end__" 
    }
)

# After a tool runs, it goes back to premium_ai to explain the result
workflow.add_edge("tools", "premium_ai")
workflow.add_edge("local_ai", END)

aura_app = workflow.compile(checkpointer=memory)

# --- TESTING ---
if __name__ == "__main__":
    # Test Query
    inputs = {"query": "Check the balance for account ACC_101"}
    config = {"configurable": {"thread_id": "test_thread"}}
    
    print("\n[PROCESS] Running the Aura Fin-Guard Graph...")
    final_state = aura_app.invoke(inputs, config=config)
    
    print("\n" + "="*30)
    print("       FINAL AI REPORT")
    print("="*30)
    print(f"MODEL USED  : {final_state.get('model_used')}")
    print(f"INTENT      : {final_state.get('intent').upper()}")
    print(f"SAVINGS     : ${final_state.get('cost_saved')}")
    print("-" * 30)
    print(f"AI RESPONSE : \n{final_state.get('response')}")
    print("="*30)