import streamlit as st
import pickle
import json

# ---- Load everything saved from training ----
with open('models/match_winner_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/team_encoder.pkl', 'rb') as f:
    le_team = pickle.load(f)

with open('models/toss_encoder.pkl', 'rb') as f:
    le_toss = pickle.load(f)

with open('models/winner_classes.json', 'r') as f:
    winner_classes = json.load(f)

with open('models/win_rate.json', 'r') as f:
    win_rate = json.load(f)

reverse_encoding = {idx: team for idx, team in enumerate(winner_classes)}

# ---- Teams and venues ----
teams = sorted([
    'Mumbai Indians',
    'Chennai Super Kings',
    'Kolkata Knight Riders',
    'Royal Challengers Bengaluru',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Rajasthan Royals',
    'Punjab Kings',
    'Gujarat Titans',
    'Lucknow Super Giants'
])

home_grounds = {
    'Mumbai Indians'              : 'Wankhede',
    'Chennai Super Kings'         : 'Chidambaram',
    'Kolkata Knight Riders'       : 'Eden Gardens',
    'Royal Challengers Bengaluru' : 'Chinnaswamy',
    'Sunrisers Hyderabad'         : 'Rajiv Gandhi',
    'Delhi Capitals'              : 'Feroz Shah',
    'Rajasthan Royals'            : 'Sawai Mansingh',
    'Punjab Kings'                : 'Punjab Cricket',
    'Gujarat Titans'              : 'Narendra Modi',
    'Lucknow Super Giants'        : 'Ekana'
}

venues = sorted([
    'Wankhede Stadium',
    'MA Chidambaram Stadium',
    'Eden Gardens',
    'M Chinnaswamy Stadium',
    'Rajiv Gandhi Intl Stadium',
    'Feroz Shah Kotla',
    'Sawai Mansingh Stadium',
    'Punjab Cricket Association Stadium',
    'Narendra Modi Stadium',
    'Ekana Cricket Stadium'
])

def is_home(team, venue):
    keyword = home_grounds.get(team, '')
    return 1 if keyword.lower() in str(venue).lower() else 0

# ---- UI ----
st.set_page_config(page_title="IPL Predictor", page_icon="🏏")
st.title("🏏 IPL Match Winner Predictor")
st.markdown("Predict IPL match winners using Machine Learning — 77% accurate!")
st.divider()

col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("Team 1", teams, key='team1')
with col2:
    team2 = st.selectbox("Team 2", teams, key='team2')

toss_winner   = st.selectbox("Toss Winner", [team1, team2])
toss_decision = st.radio("Toss Decision", ['bat', 'field'])
venue         = st.selectbox("Venue", venues)

st.divider()

if st.button("Predict Winner 🏆", use_container_width=True):

    if team1 == team2:
        st.error("Please select two different teams!")
    else:
        # Encode using EXACT same encoders from training
        team1_enc         = int(le_team.transform([team1])[0])
        team2_enc         = int(le_team.transform([team2])[0])
        toss_winner_enc   = int(le_team.transform([toss_winner])[0])
        toss_decision_enc = int(le_toss.transform([toss_decision])[0])
        team1_is_home     = is_home(team1, venue)
        team2_is_home     = is_home(team2, venue)
        team1_win_rate    = win_rate.get(team1, 0)
        team2_win_rate    = win_rate.get(team2, 0)
        toss_winner_won   = 0

        input_data = [[
            team1_enc,
            team2_enc,
            toss_winner_enc,
            toss_decision_enc,
            team1_is_home,
            team2_is_home,
            team1_win_rate,
            team2_win_rate,
            toss_winner_won
        ]]

        # Debug — print encoding to check
        print(f"team1: {team1} → {team1_enc}")
        print(f"team2: {team2} → {team2_enc}")
        print(f"prediction encoded: {int(model.predict(input_data)[0])}")
        print(f"winner classes: {winner_classes}")

        prediction_encoded = int(model.predict(input_data)[0])
        predicted_winner   = winner_classes[prediction_encoded]

        st.success(f"🏆 Predicted Winner: **{predicted_winner}**")
        st.divider()

        col3, col4 = st.columns(2)
        with col3:
            st.metric(
                label=f"{team1} win rate",
                value=f"{win_rate.get(team1, 0):.0%}"
            )
        with col4:
            st.metric(
                label=f"{team2} win rate",
                value=f"{win_rate.get(team2, 0):.0%}"
            )

        if team1_is_home:
            st.info(f"🏠 {team1} is playing at home!")
        elif team2_is_home:
            st.info(f"🏠 {team2} is playing at home!")