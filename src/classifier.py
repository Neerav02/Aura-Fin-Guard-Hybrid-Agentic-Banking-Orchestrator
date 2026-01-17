import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# 1. MOCK DATA: Training our 'Brain' on FinTech intents
data = {
    'text': [
        "What is my current balance?", "Show my account statement", "Check balance", # Simple
        "I want to report a fraudulent transaction", "Someone stole my card",       # Complex/Fraud
        "Why was my payment of 5000 failed?", "Payment stuck at processing",        # Action/Complex
        "How do I change my profile photo?", "Where is the settings menu?"          # Simple/General
        "Check the balance for account ACC_101", "What is my current balance?",      # COMPLEX (Needs DB)
        "Report fraud on ACC_102", "Someone stole my money",                        # FRAUD/COMPLEX
        "Why did my transaction fail?", "Payment status for ACC_105"               # COMPLEX
    ],
    'label': [
        'simple', 'simple', 'simple', 
        'fraud', 'fraud', 
        'complex', 'complex', 
        'simple', 'simple'
        'complex', 'complex', 
        'complex', 'complex', 
        'complex', 'complex'
    ]
}

df = pd.DataFrame(data)

# 2. VECTORIZATION: Converting text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. TRAINING: A lightweight algorithm for millisecond speed
model = LogisticRegression()
model.fit(X, y)

def classify_intent(user_input):
    """Decides the complexity of the user query."""
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]
    return prediction

# --- TEST THE BRAIN ---
test_query = "My money was deducted but the transaction failed"
intent = classify_intent(test_query)

print(f"User Query: {test_query}")
print(f"Detected Intent: {intent.upper()}")

if intent == 'simple':
    print("ACTION: Routing to Local SLM (Cost: $0.00)")
else:
    print("ACTION: Routing to Premium LLM (Cost: $0.02)")