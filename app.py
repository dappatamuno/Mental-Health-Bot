import streamlit as st
from bot_logic import get_bot_response

st.set_page_config(page_title="Mental Health Support Bot", layout="centered")
st.title(" MindEase – Your Support Companion")

if "chat" not in st.session_state:
    st.session_state.chat = []

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("How are you feeling today?")

if prompt:
    st.session_state.chat.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    response = get_bot_response(prompt)
    st.session_state.chat.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
