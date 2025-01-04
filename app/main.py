from floggit import flog
import streamlit as st
from gemini import generate_content

st.header("RojosBrother's Chatbot")
st.write("This is a chatbot that generates responses based on the input you provide.")
@flog
def update_history():
    st.session_state.chat_history.append(st.session_state.chat_input)
    gemini_response = generate_content(st.session_state.chat_history)
    st.session_state.chat_history.append(gemini_response)



if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if len(st.session_state.chat_history):
    st.write(st.session_state.chat_history[-1])
st.chat_input(on_submit=update_history, key='chat_input')
