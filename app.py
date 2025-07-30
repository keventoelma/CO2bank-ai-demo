import streamlit as st

st.set_page_config(page_title="CO₂bank.AI Demo", layout="centered")

st.title("🌍 CO₂bank.AI Demo")

st.markdown("""
Welcome to the live demo of **CO₂bank.AI** — a digital wallet for farmers and landowners to earn rewards for capturing carbon.

---

### 👨‍🌾 How It Works:
1. Farmers perform eco-friendly activities (like growing plants or producing biochar).
2. Our system tracks these actions and rewards farmers with **CO₂ tokens**.
3. Each token represents real environmental value and can be converted to money later.
4. Farmers can view, save, or trade their tokens — all via this dashboard.

---

### 📱 Try the Demo:

Choose an action to simulate your CO₂ capture and see how many tokens you’d earn:

""")

activity = st.selectbox("Choose a green activity", [
    "Planting Trees",
    "Biochar Production",
    "Greenhouse Farming",
    "Agroforestry"
])

# Simulated token values
activity_token_map = {
    "Planting Trees": 12,
    "Biochar Production": 20,
    "Greenhouse Farming": 8,
    "Agroforestry": 15
}

if st.button("Submit Activity"):
    tokens = activity_token_map.get(activity, 0)
    st.success(f"✅ You earned {tokens} CO₂ Tokens for {activity}!")
    st.balloons()

st.markdown("""
---

### 🔐 Coming Soon:
- Token Wallet Dashboard
- NGO Verification Tools
- Real Money Trading Platform

🚀 Powered by EcoCapture Solutions Ltd
""")