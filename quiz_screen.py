import streamlit as st

from questions import Question, MultipleChoiceQuestion, TrueFalseQuestion, questions

def quiz_screen() -> None:
    total = len(questions)
    qnum = st.session_state.question_number

    if qnum > total:
        st.session_state.screen = "end_screen"
        st.rerun()
        return

    question = questions[qnum - 1]
    st.header(f"Question {qnum} of {total}")
    st.write(question.text)

    if isinstance(question, MultipleChoiceQuestion):
        user_answer = st.radio(
            "Please select one option below:",
            question.options,
            key=f"answer_{qnum}"
        )

    elif isinstance(question, TrueFalseQuestion):
        user_answer = st.radio(
            "Please select True or False:",
            [True, False],
            key=f"answer_{qnum}"
        )
    
    if st.button("Next Question"):
        st.session_state[f"user_answer_{qnum}"] = user_answer
        st.session_state["question_number"] = qnum + 1
        st.rerun()
