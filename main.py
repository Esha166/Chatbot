import streamlit as st
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']

st.set_page_config(page_title="My Custom App", page_icon="🔥")

# Initialize session state for chat history
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("Gemini Chatbot")

# User input
user_input = st.chat_input("You:", key="user_input")

# Handle input and response
if user_input:
    reply = get_gemini_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", reply))
    
    st.session_state.input = ""
    st.rerun()
    
st.subheader("Chat History")
# Display chat history
for speaker, message in st.session_state.history:
    st.write(f"**{speaker}:** {message}")
