import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Priya's Organic Kitchen", page_icon="🥗", layout="wide")

# --- SIDEBAR: BIO & LINKS ---
with st.sidebar:
    st.title("👩‍🍳 About the Chef")
    st.info("Built by Priya Jha | Python Developer")
    # Fixed LinkedIn link from your profile data
    st.markdown("[🔗 Visit my LinkedIn](https://www.linkedin.com/in/jhapriya821)")
    st.divider()
    st.subheader("🌿 Project Goals")
    st.write("Using data and code to promote healthy, sustainable organic living.")

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

# --- DYNAMIC RECIPE SECTION ---
st.header("📖 Explore Our Recipes")

# Define categories
recipes = {
    "Salads": {
        "name": "Quinoa & Kale Power Bowl",
        "ingredients": ["Organic Quinoa", "Fresh Kale", "Lemon Tahini", "Chickpeas"],
        "benefit": "High in fiber and plant-based protein!",
        "img_query": "salad,organic"
    },
    "Smoothies": {
        "name": "Berry Blast Immunity",
        "ingredients": ["Blueberries", "Almond Milk", "Chia Seeds", "Spinach"],
        "benefit": "Packed with antioxidants and Vitamin C.",
        "img_query": "smoothie,fruit"
    },
    "Breakfast": {
        "name": "Overnight Chia Pudding",
        "ingredients": ["Chia Seeds", "Coconut Milk", "Honey", "Mango"],
        "benefit": "Great for long-lasting morning energy.",
        "img_query": "breakfast,oats"
    }
}

category = st.selectbox("What are you craving today?", ["Choose a category...", "Salads", "Smoothies", "Breakfast"])

if category != "Choose a category...":
    selected = recipes[category]
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        # AUTOMATED IMAGE GENERATOR: Pulls a fresh image based on the category name
        # This replaces the need for a manual 'assets' folder
        image_url = f"https://source.unsplash.com/featured/800x600?{selected['img_query']}"
        st.image(image_url, caption=f"Fresh {category}", use_container_width=True)
        
    with col2:
        st.subheader(selected["name"])
        st.write("**Ingredients:**")
        for item in selected["ingredients"]:
            st.write(f"- {item}")
        
        st.success(f"✨ **Health Benefit:** {selected['benefit']}")
        
        # User Interaction
        portions = st.slider("How many portions?", 1, 10, 1)
        st.write(f"Adjusting ingredient quantities for **{portions}** people...")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Priya's Organic Kitchen | Built with Python & Streamlit")