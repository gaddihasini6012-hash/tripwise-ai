import streamlit as st

st.set_page_config(
    page_title="TripWise AI",
    page_icon="✈️"
)

st.title("✈️ TripWise AI")

st.write("Plan your trip in seconds using AI")

destination = st.text_input("Destination")

budget = st.number_input(
    "Budget",
    min_value=0
)

start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

interests = st.multiselect(
    "Interests",
    [
        "Food",
        "Nature",
        "Shopping",
        "Adventure",
        "Beaches",
        "Museums"
    ]
)

if st.button("Generate Itinerary"):

    st.success(
        f"Your trip to {destination} is ready!"
    )

    st.subheader("Day 1")
    st.write("Explore city center")

    st.subheader("Day 2")
    st.write("Visit attractions")

    st.subheader("Day 3")
    st.write("Shopping and local food")
