
import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Get categories from trained OneHotEncoder
encoder = pipe.named_steps['step1'].named_transformers_['trf']

teams = sorted(encoder.categories_[0].tolist())
cities = sorted(encoder.categories_[2].tolist())

st.title("IPL First Innings Score Predictor")
st.write("Predict the expected final score using the current match situation.")

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select batting team", teams)

with col2:
    bowling_team = st.selectbox("Select bowling team", teams)

city = st.selectbox("Select City", cities)

st.subheader("Current Match Situation")

col3, col4, col5 = st.columns(3)

with col3:
    curr_score = st.number_input(
        "Current Score", min_value=0, max_value=500, value=120
    )

with col4:
    overs_done = st.number_input(
        "Completed overs", min_value=0, max_value=19, value=15
    )

with col5:
    balls_in_over = st.number_input(
        "Balls in current over", min_value=0, max_value=5, value=0
    )

wickets = st.number_input(
    "Wickets Out", min_value=0, max_value=10, value=5
)

last_five = st.number_input(
    "Runs in last 30 deliveries", min_value=0, max_value=100, value=45
)

if st.button("Predict Score"):

    if batting_team == bowling_team:
        st.error("Batting and bowling teams cannot be the same.")

    elif wickets >= 10:
        st.error("All wickets have fallen. The innings is complete.")

    else:
        # Calculate match features
        balls_bowled = overs_done * 6 + balls_in_over
        balls_left = 120 - balls_bowled
        wickets_left = 10 - wickets

        if balls_left <= 0:
            st.error("The 20-over innings is complete.")

        else:
            # Calculate current run rate
            if balls_bowled == 0:
                curr_rate = 0
            else:
                curr_rate = curr_score / (balls_bowled / 6)

            # Create input DataFrame
            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'curr_score': [curr_score],
                'ball_left': [balls_left],
                'wickets_left': [wickets_left],
                'curr': [curr_rate],
                'last_five': [last_five],
                'city': [city]
            })

            # Predict score
            result = pipe.predict(input_df)

            st.success(
                f"Predicted Final Score: {round(result[0])} runs"
            )
