import streamlit as st

# Page config
st.set_page_config(page_title="CO₂bank.AI Demo", layout="centered")

# MAIN TITLE
st.markdown("<h1 style='text-align: center;'>🌿 CO₂bank.AI Demo</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Turning Carbon Farming into Digital Tokens for Rwanda’s Green Future 🌍</h4>", unsafe_allow_html=True)

st.divider()

# INTRO SECTION
with st.container():
    st.markdown("### 👋 Welcome")
    st.markdown("""
This is a live **demo** of how **CO₂bank.AI** empowers Rwandan farmers to earn money through carbon farming.

Farmers submit sustainable practices like tree planting or biochar usage.  
We estimate how much carbon they remove, and reward them with **CO₂ tokens**, which can be **redeemed or sold**.

This version is a simulation for partners, investors, and tech pilots.
""")

st.divider()

# FARMER FORM SECTION
st.markdown("### 📝 Submit Farmer Activity")
with st.form("farmer_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Farmer Name")
        activity = st.selectbox("🌱 Activity Type", [
            "Tree planting", 
            "Biochar usage", 
            "Cover cropping", 
            "Agroforestry",
            "Conservation Tillage"
        ])
    with col2:
        district = st.selectbox("📍 District", ["Karongi", "Rwamagana", "Gicumbi", "Huye", "Bugesera", "Other"])
        hectares = st.number_input("🌾 Hectares Involved", min_value=0.1, step=0.1)

    submit = st.form_submit_button("✅ Submit Activity")

if submit:
    estimated_credits = round(hectares * 2.3, 2)
    st.success(f"🎉 Thank you, **{name}** from **{district}**!")
    st.metric(label="💰 Estimated Tokens Earned", value=f"{estimated_credits} Tokens")
    st.markdown("📦 These tokens are stored in your **CO₂ wallet** and can be redeemed for money later.")

st.divider()

# ADMIN DASHBOARD DEMO
st.markdown("### 📊 Admin Dashboard Snapshot")
st.markdown("A simplified demo of what our platform dashboard might show to partners or project verifiers:")

st.dataframe({
    "Farmer": ["Jean", "Aline", "Peter"],
    "District": ["Karongi", "Gicumbi", "Bugesera"],
    "Activity": ["Tree planting", "Biochar usage", "Agroforestry"],
    "Hectares": [1.5, 2.0, 1.0],
    "Tokens Earned": [3.45, 4.6, 2.3]
})

st.divider()

# FUTURE VISION
st.markdown("### 🚀 What’s Coming Next for CO₂bank.AI?")
st.markdown("""
- 📡 **GPS & Satellite Validation** for automatic farm detection  
- 🔐 **Smart Contracts** for secure token payouts  
- 🌐 **Integration with global carbon markets**  
- 🧾 ESG-ready reports for **NGOs**, **agritechs**, and **funders**
""")

st.divider()

# CONTACT
st.markdown("### 📬 Contact Us")
st.markdown("""
Want to partner, fund, or pilot with us?

- 📧 Email: `hello@co2bank.rw`  
- 📱 WhatsApp: `+250 78X XXX XXX`
- 🌐 Website: coming soon!
""")

# Footer
st.markdown("---")
st.markdown("<small>© 2025 CO₂bank.AI – Built with 💚 in Rwanda.</small>", unsafe_allow_html=True)
