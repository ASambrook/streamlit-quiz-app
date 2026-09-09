import streamlit as st

from questions import Question, MultipleChoiceQuestion, TrueFalseQuestion, questions

def quiz_screen() -> None:
    """
    This displays the quiz interface and allows for user progression through the questions.
    The `st.session_state` allows the user interactions to be stored and remembered so that the question number, selected answer and score are all tracked, preventing the quiz from reseting.
    It is also ensured that the Multiple Choice questions and True or False questions have different prompts for selecting an answer.
    The `if qnum > total` block also checks when all questions have been answered. When the question number exceeds the total (10) then the end screen should be displayed, allowing for smooth user navigation.
    """
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

        if user_answer == question.correct_answer:
            st.session_state.score += 1

        st.session_state["question_number"] = qnum + 1
        st.rerun()


