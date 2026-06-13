import streamlit as st

st.set_page_config(
    page_title="TripWise AI",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ TripWise AI")

st.write("Your AI Travel Planner")

st.markdown("""
Plan your trips faster and smarter.

✔ Personalized Itineraries

✔ Budget-Friendly Recommendations

✔ Crowd Predictions

✔ Weather Insights
""")

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("Destination")
    start_date = st.date_input("Start Date")

with col2:
    budget = st.number_input("Budget")
    end_date = st.date_input("End Date")

interests = st.multiselect(
    "Select Your Interests",
    [
        "Food",
        "Shopping",
        "Nature",
        "Adventure",
        "Beaches",
        "Museums"
    ]
)

if st.button("Generate Trip"):

    st.success(f"Trip Plan Generated for {destination}")

    st.subheader("📅 Day 1")
    st.info("""
    🌅 Morning: Explore city center

    🍽 Afternoon: Local food tour

    🌇 Evening: River walk
    """)

    st.subheader("💰 Estimated Cost")

    c1, c2, c3 = st.columns(3)

    c1.metric("Hotel", "$400")
    c2.metric("Food", "$150")
    c3.metric("Transport", "$80")

    st.subheader("👥 Crowd Forecast")

    st.success("Beach - Low Crowd")
    st.warning("City Center - Medium Crowd")
