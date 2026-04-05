import streamlit as st
import pandas as pd

# --- PAGE SETUP ---
st.set_page_config(page_title="Priya's Organic Kitchen", page_icon="🥗", layout="centered")

# --- SIDEBAR ---
with st.sidebar:
    st.title("👩‍🍳 About the Chef")
    st.info("Built by Priya Jha | Python Enthusiast")
    st.markdown("[🔗 My LinkedIn](https://www.linkedin.com/in/jhapriya821)")
    st.divider()
    st.write("This app uses Python to help you plan healthy, organic meals effortlessly.")

# --- MAIN UI ---
st.title("🌿 Organic Kitchen & Recipe Hub")
st.subheader("Healthy Eating Made Simple with Python")

st.markdown("""
Welcome to my **Organic Kitchen** project! This app is designed to help you:
* 🥗 Discover fresh, organic recipes.
* 🍎 Learn the health benefits of organic ingredients.
* 📈 Track your nutritional goals interactively.
""")

st.divider()

# --- RECIPE INTERACTION ---
st.header("📖 Explore Recipes")
category = st.selectbox("What are you craving today?", ["Choose a category...", "Salads", "Smoothies", "Breakfast"])

if category == "Salads":
    st.subheader("🥗 Quinoa & Kale Power Bowl")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Ingredients:**")
        st.write("- Organic Quinoa\n- Fresh Kale\n- Lemon Tahini Dressing\n- Chickpeas")
    with col2:
        st.success("✨ **Health Benefit:** High in fiber and plant-based protein!")

elif category == "Smoothies":
    st.subheader("🥤 Berry Blast Immunity")
    st.write("**Ingredients:** Organic Blueberries, Almond Milk, Chia Seeds, Spinach.")
    st.info("💡 **Pro-Tip:** Add a pinch of ginger for an extra immunity boost.")

elif category == "Breakfast":
    st.subheader("🥣 Overnight Chia Pudding")
    st.write("**Ingredients:** Organic Chia Seeds, Coconut Milk, Honey, Topped with Mango.")
    st.warning("⏳ **Prep Time:** Needs to sit in the fridge for at least 4 hours!")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Priya's Organic Kitchen | Made with Streamlit")