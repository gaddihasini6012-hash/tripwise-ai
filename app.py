import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="TripWise AI", page_icon="✈️", layout="wide")

st.title("✈️ TripWise AI")
st.subheader("Plan Your Perfect Trip in Seconds")

st.markdown("""
TripWise AI helps travelers create personalized itineraries based on:
- Destination
- Budget
- Travel Dates
- Interests
- Crowd Awareness
- Weather Insights
""")

st.image(
    "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    use_container_width=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("🌍 Destination")
    start_date = st.date_input("📅 Start Date", value=date.today())

with col2:
    budget = st.number_input("💰 Budget ($)", min_value=0, value=1000)
    end_date = st.date_input("📅 End Date", value=date.today())

interests = st.multiselect(
    "✨ Interests",
    ["Food", "Shopping", "Nature", "Adventure", "Beaches",
     "Museums", "Photography", "Nightlife"]
)

activities = [
    "City Center Tour",
    "Local Food Experience",
    "Beach Visit",
    "Shopping District",
    "Museum Exploration",
    "Nature Park Visit",
    "Sunset Viewpoint",
    "Cultural Show",
    "Photography Walk",
    "Historic Landmarks"
]

if st.button("🚀 Generate Trip Plan", use_container_width=True):

    trip_days = max((end_date - start_date).days + 1, 1)

    st.success(f"Your {trip_days}-Day Trip to {destination} is Ready!")

    st.header("📅 Personalized Itinerary")

    for day in range(1, trip_days + 1):
        morning = random.choice(activities)
        afternoon = random.choice(activities)
        evening = random.choice(activities)

        st.subheader(f"Day {day}")

        st.info(f"""
🌅 Morning: {morning}

🍽 Afternoon: {afternoon}

🌇 Evening: {evening}
""")

    st.divider()

    st.header("💰 Estimated Cost Breakdown")

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
    st.write("✔ Book hotels early for better prices.")
    st.write("✔ Visit attractions in the morning to avoid crowds.")
    st.write("✔ Keep one flexible day in your itinerary.")
    st.write("✔ Use local transport to save money.")
