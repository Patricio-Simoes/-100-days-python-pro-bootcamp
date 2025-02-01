class Question:
    """Represents a single question in the quiz.

    This class is used to store the text of a question and its corresponding answer.

    Attributes:
        text (str): The text of the question.
        answer (str): The correct answer to the question.
    """

    def __init__(self, q_text, q_answer):
        """Initializes a Question instance with the provided text and answer.

        Args:
            q_text (str): The text of the question.
            q_answer (str): The correct answer to the question.
        """
        self.text = q_text
        self.answer = q_answer
