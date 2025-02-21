import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize chatbot model
model = genai.GenerativeModel("gemini-pro")

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("💬 AI Chatbot - Powered by Gemini")
st.write("Ask me anything!")

# Maintain chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous chats
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Generate response
    response = model.generate_content(user_input).text
    
    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add bot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
