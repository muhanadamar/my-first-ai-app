
import streamlit as st

st.set_page_config(page_title="My First AI App", page_icon="🤖")

st.title("🤖 My First AI App")
st.write("Hey! Welcome to my website!")

name = st.text_input("What's your name?")

if name:
    st.success(f"Hello, {name}! Welcome to your first app! 🎉")

question = st.text_input("Ask me a question")

if question:
    st.write("You asked:", question)
    st.info("Awesome question! We'll connect the AI brain next.")
