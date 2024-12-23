class Question:
    """Represents a question in the quiz with its text and answer."""

    def __init__(self, text, answer):
        """
        Initializes a new Question object.

        :param text: The text of the question.
        :param answer: The correct answer to the question (True or False).
        """
        self.text = text
        self.answer = answer

    def print(self):
        """
        Returns the formatted question text for display.

        The returned string includes the question text followed by a prompt for the user
        to answer with True or False.

        :return: A string representing the formatted question.
        """
        return self.text + " (True/False)?: "
