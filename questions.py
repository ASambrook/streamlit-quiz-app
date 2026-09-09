class Question:
    """
    Parent class storing the question text and correct answer
    """
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

class MultipleChoiceQuestion(Question):
    """
    A child class storing multiple choice questions with different options.
    """
    def __init__(self, text, options, correct_answer):
        """
        Inherits common attributes from the parent Question class.
        Adds a list of selectable options.
        """
        super().__init__(text, correct_answer)
        self.options = options

class TrueFalseQuestion(Question):
    """
    A child class storing True or False questions.
    """
    def __init__(self, text, correct_answer):
        """
        inherits all atrributes from the parent Question class.
        """
        super().__init__(text, correct_answer)

questions = [
    MultipleChoiceQuestion(
        "Who should you report acts of violence, loss or theft of IBM assets to?",
        ["Corporate Health", "Cybersecurity Incidient Response Team", "IBM Employee Concerns Team", "IBM Corporate Secruity"],
        "IBM Corporate Secruity" 
    ),

    TrueFalseQuestion(
        "You need manager approval before giving business gifts or amenities to others.",
        True
     ),

    MultipleChoiceQuestion(
        "Violating accounting and financial reporting laws can result in what?",
        ["Fines", "Penalty restrictions", "Imprisonment", "All of the above"],
        "All of the above" 
    ),

    TrueFalseQuestion(
        "All employees are authorised to give the appearance of speaking or acting on IBM’s behalf at public events.",
        False
     ),

    TrueFalseQuestion(
        "IBM tolerates the use of insider information if it has a beneficial outcome for the organisation.",
        False
     ),

    MultipleChoiceQuestion(
        "Which team should you inform of planned cross-border travel?",
        ["IBM Business travel team", "IBM Immigration team", "IBM Travel Regulations team", "All of the above"],
        "IBM Immigration team" 
    ),

    TrueFalseQuestion(
        "There are some instances where you may make slightly misleading statements about Competitor products and services.",
        False
     ),

    MultipleChoiceQuestion(
        "What tool must be used when developing a trademark?",
        ["IBM's Naming tool", "IBM's Development tool", "IBM's Trademark tool ", "IBM's Copyright tool"],
        "IBM's Naming tool" 
    ),

    TrueFalseQuestion(
        " You must get manager’s approval before submitting a request for a social handle using IBM’s name.",
        True
     ),

    MultipleChoiceQuestion(
        "'[????] comes first?' What word is missing for this key IBM message?",
        ["Trust", "IBM", "Integrity", "Respect"],
        "Integrity" 
    ),
]

