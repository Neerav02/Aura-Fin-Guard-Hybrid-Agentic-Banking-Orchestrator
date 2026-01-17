from langchain.tools import tool

# 1. MOCK DATABASE (Zero-cost simulation)
MOCK_DB = {
    "ACC_101": {"name": "User_One", "balance": 5000.75, "status": "Active"},
    "ACC_102": {"name": "User_Two", "balance": 120.50, "status": "Blocked"}
}

# 2. THE TOOLS
@tool
def get_balance(account_id: str):
    """
    Fetches the current account balance for a specific account ID.
    Use this when the user asks 'How much money do I have?' or 'Check my balance'.
    """
    # Simulate a database lookup
    data = MOCK_DB.get(account_id)
    if data:
        return f"Account {account_id} balance is ₹{data['balance']}. Status: {data['status']}."
    else:
        return "Error: Account ID not found. Please provide a valid ID (e.g., ACC_101)."

@tool
def report_fraud(account_id: str, description: str):
    """
    Initiates a fraud investigation for a specific account.
    Use this when a user says 'My money was stolen' or 'Fraud report'.
    """
    # Simulate an action
    return f"FRAUD ALERT: Investigation {account_id}-FRD started for: '{description}'. The card has been temporarily locked."