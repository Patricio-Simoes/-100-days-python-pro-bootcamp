class QuizBrain:
    """Represents the brain of the quiz game, managing questions and user responses."""

    def __init__(self, list):
        """
        Initializes a new QuizBrain object.

        :param list: A list of question objects to be used in the quiz.
        """
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def next_question(self):
        """
        Displays the next question to the user and checks their answer.

        Increments the question number and prompts the user for an answer.
        Calls the check_answer method to validate the user's response.

        :return: None
        """
        index = self.question_number
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {self.questions_list[index].print()}"
        )
        self.check_answer(answer, self.questions_list[index].answer)

    def still_has_questions(self):
        """
        Checks if there are more questions left in the quiz.

        :return: True if there are more questions, otherwise False.
        """
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, question_answer):
        """
        Validates the user's answer against the correct answer.

        Increments the score if the answer is correct and provides feedback to the user.

        :param user_answer: The answer provided by the user.
        :param question_answer: The correct answer for the current question.
        :return: None
        """
        if user_answer.lower() == question_answer.lower():
            print("You've got it!")
            self.score += 1
        else:
            print("That's wrong...")
        print(f"The correct answer was: {question_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
