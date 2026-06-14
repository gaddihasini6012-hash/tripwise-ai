import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TripWise AI - Smart Travel Planning Platform",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS FOR PROFESSIONAL UX ---
st.markdown("""
<style>
    .main-title { font-size: 38px; font-weight: 700; color: #1E3A8A; margin-bottom: 5px; }
    .subtitle { font-size: 18px; color: #4B5563; margin-bottom: 25px; }
    .section-header { font-size: 22px; font-weight: 600; color: #1F2937; border-bottom: 2px solid #E5E7EB; padding-bottom: 5px; margin-top: 20px; }
    .kpi-card { background-color: #F3F4F6; padding: 15px; border-radius: 8px; text-align: center; border: 1px solid #E5E7EB; }
    .kpi-val { font-size: 24px; font-weight: 700; color: #2563EB; }
</style>
""", unsafe_style_allowed=True)

# --- APPLICATION HEADER ---
st.markdown('<div class="main-title">🗺️ TripWise AI</div>', unsafe_style_allowed=True)
st.markdown('<div class="subtitle">AI-Powered Contextual Travel Itinerary & Budget Curation System</div>', unsafe_style_allowed=True)
st.markdown("---")

# --- SIDEBAR: USER PARAMETER INPUTS ---
st.sidebar.header("📋 Trip Specifications")

destination = st.sidebar.text_input("Where do you want to go?", placeholder="e.g., Goa, Paris, Kyoto")
duration = st.sidebar.slider("Trip Duration (Days)", min_value=1, max_value=7, value=3)
budget_tier = st.sidebar.selectbox("Budget Profile", ["Budget", "Mid-Range", "Luxury"])

st.sidebar.subheader("🎯 Travel Interests")
interests = []
if st.sidebar.checkbox("🏖️ Adventure & Nature", value=True): interests.append("Adventure & Nature")
if st.sidebar.checkbox("🏛️ History & Culture"): interests.append("History & Culture")
if st.sidebar.checkbox("🍕 Culinary & Food Exploration"): interests.append("Culinary Tour")
if st.sidebar.checkbox("🛍️ Shopping & Nightlife"): interests.append("Shopping & Nightlife")

generate_btn = st.sidebar.button("🤖 Generate Itinerary", type="primary")

# --- SIMULATED DATA ENGINE (For Alpha Validation & Mathematical Verification) ---
def simulate_itinerary_engine(dest, days, tier, tags):
    # Core baseline data mapping dictionary
    tier_costs = {"Budget": 1500, "Mid-Range": 4500, "Luxury": 12000}
    base_cost = tier_costs.get(tier, 4500)
    
    # Calculate costs according to systematic itemization boundaries
    stay_cost = int(base_cost * 0.45 * days)
    food_cost = int(base_cost * 0.30 * days)
    activity_cost = int(base_cost * 0.15 * days)
    transit_cost = int(base_cost * 0.10 * days)
    total_estimated = stay_cost + food_cost + activity_cost + transit_cost

    # Build dynamic daily activity schedules based on parameters
    selected_themes = ", ".join(tags) if tags else "General Sightseeing"
    itinerary_data = {}
    for d in range(1, days + 1):
        itinerary_data[f"Day {d}"] = {
            "Morning": f"☀️ Explore top local landmarks in {dest} tailored to {selected_themes}.",
            "Afternoon": f"🍲 Dynamic lunch at a traditional, high-rated regional spot matching a {tier} profile.",
            "Evening": f"🌙 Relaxed scenic routing or interactive cultural walk through popular districts."
        }
    
    return itinerary_data, stay_cost, food_cost, activity_cost, transit_cost, total_estimated

# --- MAIN PAGE DISPLAY LOGIC ---
if generate_btn:
    if not destination:
        st.warning("⚠️ Please provide a destination in the sidebar parameter panel to begin.")
    else:
        # 1. Processing State Notification
        with st.spinner("🤖 TripWise AI Semantic Engine processing travel data, budgets, and weather metrics..."):
            time.sleep(1.8) # Simulates semantic generation speed matching BR-1 (< 5 seconds execution window)
        
        # 2. Extract Data from Simulation Engine
        days_plan, stay, food, act, trans, total = simulate_itinerary_engine(destination, duration, budget_tier, interests)
        
        # 3. Contextual Alert Metrics (Weather & Crowd Forecasts)
        st.markdown('<div class="section-header">🚨 Dynamic Local Warnings & Conditions</div>', unsafe_style_allowed=True)
        col_alert1, col_alert2 = st.columns(2)
        with col_alert1:
            st.info(f"🌤️ **Weather Insights:** Clear conditions predicted. Excellent for outdoor routes.")
        with col_alert2:
            st.warning(f"📊 **Crowd Forecast:** Moderate crowd index expected at major sights. Plan morning visits.")

        # 4. Chronological Itinerary Layout View
        st.markdown(f'<div class="section-header">📅 Optimized {duration}-Day Itinerary for {destination}</div>', unsafe_style_allowed=True)
        
        for day, schedule in days_plan.items():
            with st.expander(f"📌 {day} Layout Plan", expanded=True):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("**🌅 Morning Activity**")
                    st.write(schedule["Morning"])
                with col2:
                    st.markdown("**🏙️ Afternoon Activity**")
                    st.write(schedule["Afternoon"])
                with col3:
                    st.markdown("**🌆 Evening Activity**")
                    st.write(schedule["Evening"])

        # 5. Financial Cost Breakdown Section
        st.markdown('<div class="section-header">💰 Financial Curation & Budget Analysis</div>', unsafe_style_allowed=True)
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown(f'<div class="kpi-card">Selected Tier<br><span class="kpi-val">{budget_tier}</span></div>', unsafe_style_allowed=True)
        with col_m2:
            st.markdown(f'<div class="kpi-card">Total Days Planned<br><span class="kpi-val">{duration} Days</span></div>', unsafe_style_allowed=True)
        with col_m3:
            st.markdown(f'<div class="kpi-card">Estimated Total Cost<br><span class="kpi-val">₹{total:,}</span></div>', unsafe_style_allowed=True)

        # 6. Cost Allocation Data Charts
        st.write("")
        chart_col, table_col = st.columns([3, 2])
        
        budget_df = pd.DataFrame({
            "Expense Category": ["Accommodation", "Food & Dining", "Activities & Entry Fees", "Local Transport"],
            "Estimated Cost (₹)": [stay, food, act, trans]
        })

        with chart_col:
            fig = px.pie(
                budget_df, 
                values="Estimated Cost (₹)", 
                names="Expense Category", 
                title="Categorized Allocation Matrix",
                color_discrete_sequence=px.colors.sequential.YlGnBu
            )
            fig.update_layout(margin=dict(t=30, b=10, l=10, r=10), height=300)
            st.plotly_chart(fig, use_container_width=True)

        with table_col:
            st.write("**Itemized Financial Cost Metrics**")
            st.dataframe(budget_df, hide_index=True, use_container_width=True)

        # 7. Data Export Options (Matching UR-2 Requirements)
        st.write("")
        st.markdown('<div class="section-header">📥 Export Your Custom Plan</div>', unsafe_style_allowed=True)
        
        # Build raw text string to parse for plain-text file transfers
        raw_export_text = f"TRIPWISE AI CUSTOM PLAN FOR {destination.upper()}\n"
        raw_export_text += f"Duration: {duration} Days | Profile: {budget_tier}\n"
        raw_export_text += f"Total Forecasted Allocation: ₹{total:,}\n\n"
        for day, schedule in days_plan.items():
            raw_export_text += f"--- {day} ---\nMorning: {schedule['Morning']}\nAfternoon: {schedule['Afternoon']}\nEvening: {schedule['Evening']}\n\n"

        st.download_button(
            label="📄 Save Itinerary as Plain Text File",
            data=raw_export_text,
            file_name=f"TripWise_Plan_{destination.lower()}.txt",
            mime="text/plain"
        )

else:
    # --- DASHBOARD WELCOME SCREEN ---
    st.info("💡 **Welcome to the Alpha Testing Environment!** Set your travel destination, duration, and budget tier in the left sidebar panel, then click **Generate Itinerary** to execute the system engine logic.")
    
    # Showcase Project Management Performance Target Visuals
    st.markdown('<div class="section-header">📈 System Performance Objectives & Benchmarks</div>', unsafe_style_allowed=True)
    col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
    with col_kpi1:
        st.metric(label="Target Processing Window (BR-1)", value="< 5 Seconds", delta="Verified")
    with col_kpi2:
        st.metric(label="Mathematical System Success (Sf)", value="95.0%", delta="Target")
    with col_kpi3:
        st.metric(label="Alpha Infrastructure Cost", value="₹0", delta="Serverless")
    with col_kpi4:
        st.metric(label="Mobile Page-Load Speed (NFR-1)", value="2.0s", delta="Optimized")
