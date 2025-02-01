import html

class QuizBrain:
    """Manages the quiz logic and keeps track of the score and questions.

    This class is responsible for handling the quiz flow, including
    tracking the current question, checking answers, and maintaining
    the user's score.

    Attributes:
        question_number (int): The index of the current question.
        score (int): The user's current score.
        question_list (list): A list of Question objects.
        current_question (Question): The current Question object being asked.
    """

    def __init__(self, q_list):
        """Initializes the QuizBrain with a list of questions.

        Args:
            q_list (list): A list of Question objects to be used in the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if there are more questions left in the quiz.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Retrieves the next question in the quiz.

        This method updates the current question and increments the
        question number. It also unescapes any HTML entities in the
        question text.

        Returns:
            str: The formatted question text, including the question number.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {question_text}"

    def check_answer(self, user_answer):
        """Checks the user's answer against the correct answer.

        Args:
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        return False
