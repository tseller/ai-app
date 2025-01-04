from floggit import flog
import streamlit as st
from gemini import generate_content

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'last_qa' not in st.session_state:
    st.session_state.last_qa = []

st.title("Sigma")

@flog
def update_history():
    st.session_state.chat_history.append(st.session_state.chat_input)
    gemini_response = generate_content(st.session_state.chat_history)
    st.session_state.chat_history.append(gemini_response)
    st.session_state.last_qa = [st.session_state.chat_input, gemini_response]

st.write(st.session_state.last_qa)
st.chat_input(on_submit=update_history, key='chat_input')

def text_clear():
    '''display only the last question and answer'''
    st.write(st.session_state.last_qa)