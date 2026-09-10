from questions import MultipleChoiceQuestion, TrueFalseQuestion, Question


def test_multiple_choice_question_inheritance():
    """
    Test for multiple choice questions.
    """
    m = MultipleChoiceQuestion(
        text="What is 5+2?",
        options=["3", "7", "10"],
        correct_answer="7"
    )
  
    assert isinstance(m, Question)
    assert m.text == "What is 5+2?"
    assert m.options == ["3", "7", "10"]
    assert m.correct_answer == "7"


def test_true_false_question_inheritance():
    """
    Test for True or False questions.
    """
    t = TrueFalseQuestion(
        text="Dogs are cool.",
        correct_answer="True"
    )
    assert isinstance(t, Question)
    assert t.correct_answer == "True"

