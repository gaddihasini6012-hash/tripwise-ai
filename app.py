import streamlit as st

st.set_page_config(
    page_title="TripWise AI",
    page_icon="✈️",
    layout="wide"
)

# HERO SECTION

st.title("✈️ TripWise AI")

st.markdown("""
## Plan Your Perfect Trip in Seconds

TripWise AI helps you create personalized travel itineraries
based on your budget, destination, travel dates, and interests.

No travel agents.
No endless research.
Just smart travel planning.
""")

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    use_container_width=True
)

st.divider()

# USER INPUTS

st.header("🌍 Travel Planner")

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("Destination")
    start_date = st.date_input("Start Date")

with col2:
    budget = st.number_input(
        "Budget ($)",
        min_value=0
    )
    end_date = st.date_input("End Date")

interests = st.multiselect(
    "Choose Interests",
    [
        "Food",
        "Shopping",
        "Adventure",
        "Nature",
        "Museums",
        "Beaches",
        "Photography",
        "Nightlife"
    ]
)

st.divider()

# GENERATE BUTTON

if st.button(
    "🚀 Generate Trip Plan",
    use_container_width=True
):

    st.success(
        f"Your Trip to {destination} is Ready!"
    )

    st.header("📅 Personalized Itinerary")

    st.info("""
🌅 Morning:
Explore the city center

🍽 Afternoon:
Try local restaurants and cafes

🌇 Evening:
Visit famous landmarks and enjoy sunset views
""")

    st.info("""
🌅 Day 2 Morning:
Nature and sightseeing

🍽 Afternoon:
Shopping district

🌇 Evening:
Local cultural experiences
""")

    st.divider()

    st.header("💰 Estimated Trip Cost")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Hotel", "$450")
    c2.metric("Food", "$180")
    c3.metric("Transport", "$90")
    c4.metric("Activities", "$220")

    st.divider()

    st.header("🌤 Weather Forecast")

    st.write("Day 1: Sunny - 24°C")
    st.write("Day 2: Cloudy - 21°C")
    st.write("Day 3: Light Rain - 19°C")

    st.divider()

    st.header("👥 Crowd Forecast")

    st.success("Beach Area → Low Crowd")

    st.warning("City Center → Medium Crowd")

    st.error("Popular Tourist Spot → High Crowd")

    st.divider()

    st.header("✨ Travel Tips")

    st.write("""
✔ Travel early in the morning to avoid crowds.

✔ Book hotels at least 2 weeks in advance.

✔ Use local transport for lower costs.

✔ Keep one free day for spontaneous activities.
""")
