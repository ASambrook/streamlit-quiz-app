import streamlit as st
from storage import save_result

def end_screen() -> None:
    """
    Displays the final screen of the quiz, congratulating the user and presenting them with their final score.
    If the user's name and score have not yet been saved then they are written to the CSV file where the user will be greeted with a message confirming this.
    There is also a `Download results CSV` button where the user can download the results CSV file, allowing them to view and store the history of results.
    There is also a `Play again` button which allows the user to retry the quiz. This restores all the session state variables back to their default starting values, ensuring the user's new attempt is not affected by any previous attempts.
    """
    name = st.session_state.name
    score = st.session_state.score
    total = st.session_state.get("total_questions", 10)

    st.title(f"{name}, Congratulations and thank you for completing the IBM Business Conduct Guildines Quiz!")
    st.subheader(f"Your score is {score} / {total}")

    if not st.session_state.saved:
        save_result(name, score)
        st.session_state.saved = True
        st.success("Your result has been saved.")


    if st.button("Download results CSV"):
        with open("results.csv", "rb") as f:
            st.download_button(
                label="Download CSV",
                data=f.read(),
                file_name="results.csv",
                mime="text/csv"
            )


    if st.button("Play again"):
        st.session_state.question_number = 1
        st.session_state.score = 0
        st.session_state.question = None
        st.session_state.saved = False
        st.session_state.screen = "welcome"
        st.rerun()
