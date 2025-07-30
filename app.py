import streamlit as st

# Set page config
st.set_page_config(page_title="CO₂bank.AI Demo", layout="centered")

# Main title
st.title("🌍 CO₂bank.AI Demo – Carbon Credits for Farmers & Beyond")

# Intro
st.markdown("""
Welcome to the demo of **CO₂bank.AI**, a platform that tracks, verifies, and tokenizes carbon farming practices across Rwanda.  
We help farmers earn **digital tokens** for their sustainable activities — like planting trees, using biochar, or organic practices.  
These tokens can later be **redeemed or traded** for real money.

**Note:** This is just a live simulation to explain how it works!
""")

# Farmer Input Form
st.header("👩🏾‍🌾 Farmer Activity Submission")
with st.form("farmer_form"):
    name = st.text_input("Farmer Name")
    district = st.selectbox("District", ["Karongi", "Rwamagana", "Gicumbi", "Huye", "Bugesera", "Other"])
    activity = st.selectbox("Carbon Sequestration Activity", [
        "Tree planting", 
        "Biochar usage", 
        "Cover cropping", 
        "Agroforestry",
        "Conservation Tillage"
    ])
    hectares = st.number_input("Hectares Practiced On", min_value=0.1, step=0.1)
    submit = st.form_submit_button("Submit Activity")

# Result
if submit:
    st.success(f"✅ Thank you, {name} from {district}!")
    estimated_credits = round(hectares * 2.3, 2)
    st.markdown(f"🌱 Based on your activity ({activity}), you earned **{estimated_credits} Carbon Tokens** 🎉")
    st.info("💡 These tokens are stored in your CO₂ wallet. You can later redeem or trade them for cash.")

# Admin Demo
st.header("📊 Admin Dashboard Demo (Simplified)")
st.markdown("""
This section shows how we might track verified contributions across all farmers.

| Farmer | District | Activity           | Hectares | Tokens Earned |
|--------|----------|--------------------|----------|----------------|
| Jean   | Karongi  | Tree planting      | 1.5      | 3.45           |
| Aline  | Gicumbi  | Biochar usage      | 2.0      | 4.60           |
| Peter  | Bugesera | Agroforestry       | 1.0      | 2.30           |
""")

# Next Steps
st.header("🚀 What's Next?")
st.markdown("""
✅ We plan to integrate GPS-based validation, satellite data, and smart contracts for automatic payouts.  
✅ CO₂bank.AI will take the verified tokens to the **global carbon market**, and pay farmers based on tokenized value.  
✅ We also offer **white-label carbon reporting** for NGOs, ESG firms, and agribusinesses.

---

🔗 Want to partner or learn more? Contact us at:  
📧 `hello@co2bank.rw`  
📱 WhatsApp: `+250 781 392 398`
""")
