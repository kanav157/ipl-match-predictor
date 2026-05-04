# 🏏 IPL Match Winner Predictor

A Machine Learning web app that predicts IPL match winners using historical data from 2008 to 2025.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-RandomForest-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Accuracy](https://img.shields.io/badge/Accuracy-77%25-green)

---

## 🔗 Live Demo
👉 https://kanav157-ipl-match-predictor-app-spxw2v.streamlit.app/

---

## 📌 About the Project

This project predicts the winner of an IPL match before it starts, based on:
- Which two teams are playing
- Who won the toss and what they decided
- Which venue the match is at
- Historical win rates of each team
- Home ground advantage

---

## 🧠 How it Works

Raw IPL Data -> Data Cleaning & Merging -> Feature Engineering -> Random Forest Model -> Streamlit Web App -> Predict Winner !


---

## 📊 Model Details

| Detail | Value |
|---|---|
| Algorithm | Random Forest Classifier |
| Training Data | 1181 IPL matches |
| Accuracy | 77% |
| Features | 9 |
| Trees | 500 |

---

## 🔧 Features Used

| Feature | Description |
| team1, team2 | Teams playing the match |
| toss_winner | Who won the toss |
| toss_decision | Bat or field |
| team1_is_home | Is team1 at home ground |
| team2_is_home | Is team2 at home ground |
| team1_win_rate | Historical win % of team1 |
| team2_win_rate | Historical win % of team2 |
| toss_winner_won | Historical toss impact |

---

## 📁 Project Structure

ipl-match-predictor/
├── data/
│   ├── ipl_2023.csv          # 2023 season data
│   ├── ipl_2024.csv          # 2024 season data
│   ├── ipl_2025.csv          # 2025 season data
│   └── new_matches.csv       # cleaned merged data
├── models/
│   ├── match_winner_model.pkl # trained model
│   ├── team_encoder.pkl       # team label encoder
│   ├── toss_encoder.pkl       # toss label encoder
│   ├── winner_classes.json    # winner class mapping
│   └── win_rate.json          # team win rates
├── _EDA.ipynb                 # exploratory data analysis
├── _merge_data.ipynb          # data cleaning and merging
├── _match_winner.ipynb        # model training
├── app.py                     # streamlit web app
├── requirements.txt
└── README.md


---

## 🛠️ Tech Stack

- **Python** — core language
- **Pandas** — data manipulation
- **Scikit-learn** — machine learning
- **Streamlit** — web app
- **Matplotlib / Seaborn** — data visualization
- **Pickle** — model saving

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/kanav157/ipl-match-predictor.git
cd ipl-match-predictor
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📈 Results

| Model | Accuracy |
|---|---|
| Baseline (random guess) | 10% |
| Basic Random Forest | 48% |
| Improved with features | 77% |

---

## 🏆 Teams Supported

| Team | Home Ground |
|---|---|
| Mumbai Indians | Wankhede Stadium |
| Chennai Super Kings | MA Chidambaram Stadium |
| Kolkata Knight Riders | Eden Gardens |
| Royal Challengers Bengaluru | M Chinnaswamy Stadium |
| Sunrisers Hyderabad | Rajiv Gandhi Intl Stadium |
| Delhi Capitals | Feroz Shah Kotla |
| Rajasthan Royals | Sawai Mansingh Stadium |
| Punjab Kings | Punjab Cricket Association Stadium |
| Gujarat Titans | Narendra Modi Stadium |
| Lucknow Super Giants | Ekana Cricket Stadium |

---

## 🔮 Future Improvements

- Add player form and availability
- Add head to head win rate feature
- Add last 5 matches win rate
- Build score predictor model
- Deploy on Streamlit Cloud

---

## 👨‍💻 Author

**Kanav Garg**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](your-linkedin-link)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/kanav157)

---

## ⭐ If you found this useful, please star the repo!
