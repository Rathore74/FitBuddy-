import streamlit as st
import os
from services import get_fitness_plan

# Title of the app
st.set_page_config(page_title="FitBuddy AI", page_icon="💪")
st.title("💪 FitBuddy AI Planner")
st.write("Generate your custom 3-day workout and meal plan instantly.")

# User Inputs
weight = st.number_input("Enter your weight (kg)", min_value=10, max_value=200, value=70)
goal = st.selectbox("What is your goal?", ["Weight Loss", "Muscle Gain", "General Fitness", "Endurance"])

if st.button("Generate My Plan"):
    with st.spinner("AI is crafting your plan..."):
        # This calls your existing logic from services.py
        plan = get_fitness_plan(weight, goal)
        st.markdown("### Your Custom Plan")
        st.write(plan)
