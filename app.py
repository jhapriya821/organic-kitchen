import streamlit as st

st.set_page_config(page_title="Priya's Organic Kitchen", page_icon="🥗")

# Sidebar
st.sidebar.title("🌿 Navigation")
st.sidebar.info("Welcome to my Organic Food Project!")

# Main Content
st.title("🥘 Organic Recipe Hub")
st.markdown("### Healthy Living through Python")

# Create a simple recipe search or filter
category = st.selectbox("Choose a category:", ["Salads", "Breakfast", "Smoothies"])

if category == "Salads":
    st.subheader("🥗 Kale & Avocado Crunch")
    st.write("- **Ingredients:** Organic Kale, Avocado, Lemon, Hemp Seeds.")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with a cooking video link!

elif category == "Breakfast":
    st.subheader("🥣 Overnight Oats")
    st.write("- **Ingredients:** Organic Oats, Almond Milk, Chia Seeds, Berries.")