class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0

    def next_question(self):
        index = self.question_number
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.questions_list[index].print()}")
        self.check_answer(answer, self.questions_list[index].answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            print("You've got it!")
            self.score += 1
        else:
            print("That's wrong...")
        print (f"The correct answer was: {question_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")