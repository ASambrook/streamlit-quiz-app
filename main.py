import streamlit as st

from welcome_screen import welcome_screen
from quiz_screen import quiz_screen
from end_screen import end_screen

TOTAL_QUESTIONS = 10


def init_state() -> None:
    """
    Sets default values for the screens, name, question number and score.
    This allows the web application to reliably track the user's progress throughout the quiz.
    """
    st.session_state.setdefault("screen", "welcome")
    st.session_state.setdefault("name", "")
    st.session_state.setdefault("question_number", 1)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("question", None)
    st.session_state.setdefault("saved", False)
    st.session_state.setdefault("total_questions", TOTAL_QUESTIONS)


def main() -> None:
    """
    Allows a smooth, organised navigation flow of the quiz.
    The current screen stored in session state is checked and the corresponding screen is displayed.
    """
    init_state()

    screen = st.session_state.screen

    if screen == "welcome":
        welcome_screen()
    elif screen == "quiz_screen":
        quiz_screen()
    elif screen == "end_screen":
        end_screen()
    else:
        st.session_state.screen = "welcome"
        st.rerun()


if __name__ == "__main__":
    main()


