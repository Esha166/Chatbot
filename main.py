import streamlit as st
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
chat = []
def get_gemini_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result['candidates'][0]['content']['parts'][0]['text']


st.title("Gemini Chatbot")

user_input = st.text_input("You: ")
reply = get_gemini_response(user_input)
if user_input != "":
        st.write("You:", user_input)
        st.write("Bot:", reply)
chat.append({"role": "user", "content": user_input})
chat.append({"role": "assistant", "content": reply})

for message in chat:
    if message['role'] == "user":
        print(message['content'])
        st.write("You:", message['content'])
    else:
        st.write("Bot:", message['content'])
