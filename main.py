import streamlit as st
st.title("The Business Conduct Guidlines Quiz")

user_input = st.text_input("Please enter your name in the box below to begin!")

if user_input:
    st.write(f"Hello, {user_input.title()}")


    ffijffej