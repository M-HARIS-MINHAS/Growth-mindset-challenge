import streamlit as st
import pandas as pd
import numpy as np
import random
from io import BytesIO

# Set page configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stSlider>div>div>div>div {
        background-color: #4CAF50;
    }
    .stHeader {
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .stSubheader {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
    }
    .stTextArea>div>div>textarea {
        border-radius: 5px;
        padding: 10px;
    }
    .stSuccess {
        color: #4CAF50;
    }
    .stInfo {
        color: #31708f;
    }
</style>
""", unsafe_allow_html=True)

# Title and Header
st.title("🌱 Growth Mindset Challenge")
st.subheader("Unlock Your Potential with a Growth Mindset!")

# Introduction
st.write("""
A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. 
This app is designed to help you practice and adopt a growth mindset. Let's get started!
""")

# Initialize session state if not already done
if 'responses' not in st.session_state:
    st.session_state.responses = []

# Section 1: Set Your Learning Goals
st.markdown("### 🎯 Set Your Learning Goals")
goal = st.text_input("What is one learning goal you want to achieve?")
if goal:
    st.success(f"Your learning goal is: **{goal}**")

# Section 2: Rate Your Mindset
st.markdown("### 📊 Rate Your Mindset")
mindset_score = st.slider("On a scale of 1 to 10, how much do you believe in a growth mindset?", 1, 10)
st.write(f"Your current mindset score is: **{mindset_score}**")

# Section 3: Get a Motivational Quote
st.markdown("### 💬 Get a Motivational Quote")
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "It always seems impossible until it's done. – Nelson Mandela",
    "The harder you work for something, the greater you'll feel when you achieve it. – Unknown"
]
if st.button("Click for a Motivational Quote"):
    quote = random.choice(quotes)
    st.info(f"**{quote}**")

# Section 4: Track Your Progress
st.markdown("### 📈 Track Your Progress")
progress_data = pd.DataFrame({
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "Progress": np.random.randint(1, 10, size=4)
})
st.bar_chart(progress_data.set_index("Week"))

# Section 5: Share Your Growth Mindset
st.markdown("### 🧠 Share Your Growth Mindset")
questions = [
    "What does a growth mindset mean to you?",
    "Describe a time you turned a mistake into a learning opportunity.",
    "How do you stay motivated when facing difficulties?",
    "What new skill would you like to develop and why?",
    "How do you respond to constructive feedback?"
]

for idx, question in enumerate(questions):
    st.subheader(f"{idx + 1}. {question}")
    response = st.text_area("Your Response:", key=f"response{idx}")

    if st.button(f"Submit {idx + 1}", key=f"submit{idx}"):
        st.success("✅ Response Recorded!")
        st.session_state.responses.append({
            "Question": question,
            "Your Response": response
        })

# Section 6: View and Download Your Responses
if st.session_state.responses:
    st.markdown("### 📊 Your Responses")
    response_df = pd.DataFrame(st.session_state.responses)
    st.dataframe(response_df)

    # Download Options
    st.markdown("### 📥 Download Your Responses")
    file_type = st.selectbox("Select format:", ["CSV", "Excel"], key="file_type")
    
    def download_data(data, file_type):
        df = pd.DataFrame(data)
        if file_type == "CSV":
            csv = df.to_csv(index=False).encode('utf-8')
            return BytesIO(csv)
        elif file_type == "Excel":
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Growth Mindset')
            return buffer

    file = download_data(st.session_state.responses, file_type)

    st.download_button(
        label=f"Download {file_type}",
        data=file,
        file_name=f"growth_mindset_responses.{file_type.lower() if file_type else 'csv'}",
        mime="text/csv" if file_type == "CSV" else "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Section 7: Your Growth Mindset Challenge
st.markdown("### 🎯 Your Growth Mindset Challenge")
challenges = [
    "Think of a mistake you made and write down 2 things you learned.",
    "Ask for feedback on your work and apply the suggestions.",
    "Face a challenge you've been avoiding and track your progress.",
    "Celebrate the effort you put into learning today.",
    "Write down a new skill you want to develop and plan your first step."
]

if st.button("Give Me a Challenge"):
    st.session_state.current_challenge = random.choice(challenges)

if 'current_challenge' in st.session_state:
    st.info(st.session_state.current_challenge)

# Section 8: Submit Your Commitment
st.markdown("### ✍️ Submit Your Commitment")
if st.checkbox("I am ready to adopt a growth mindset!"):
    st.write("Great! You're on your way to unlocking your full potential.")
if st.button("Submit Commitment"):
    st.balloons()
    st.success("Thank you for committing to the Growth Mindset Challenge! 🎉")

# Footer
st.markdown("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io).")
st.write("Made by M Haris .")