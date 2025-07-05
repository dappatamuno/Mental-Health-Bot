import streamlit as st
from bot_logic import get_bot_response

st.set_page_config(page_title="MindEase – Mental Health Chat", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        .main {
            background-color: #f7fbff;
        }
        .block-container {
            padding-top: 2rem;
        }
        .stChatMessage {
            border-radius: 10px;
            padding: 10px;
        }
        .stChatMessage.user {
            background-color: #e6f0ff;
        }
        .stChatMessage.assistant {
            background-color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("## MindEase – Your Mental Health Chat Companion")
st.markdown("Welcome. This is a safe, non-judgmental space to share how you're feeling. 🌿")

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("What's on your mind?")

if prompt:
    st.session_state.chat.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    response = get_bot_response(prompt)
    st.session_state.chat.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
