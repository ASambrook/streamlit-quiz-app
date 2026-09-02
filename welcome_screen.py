import streamlit as st

import re

class NameValidator:
    def length_check(self, name: str) -> bool:
        return 3 <= len(name.strip()) <= 30

    def pattern_check(self, name: str) -> bool:
        pattern = r"[A-Za-z\s'-]+"
        return bool(re.fullmatch(pattern, name.strip()))

    def error_handler(self, message: str):
        st.error(message)

    def validate_name(self, name: str) -> bool:
        if not self.length_check(name):
            self.error_handler("The name should be between 3 and 30 characters")
            return False
        elif not self.pattern_check(name):
            self.error_handler("The name should only contain letters, hyphens, apostrophes and spaces")
            return False
        return True

validator = NameValidator()

def welcome_screen():
    st.title("The Business Conduct Guidlines Quiz")
   
    st.write("""
    Welcome! This Quiz is for employees of IBM to complete. It ensures all employees are aware of the organisation's values and guidelines.

    You will be faced with a series of multiple choice questions testing your knowledge of the business conduct guidelines.
    """)

    name = st.text_input("Please enter your name in the box below to begin!")

    if st.button("Begin Quiz!"):
        if validator.validate_name(name):
            st.session_state["name"] = name.title()
            st.session_state["screen"] = "quiz_screen"



