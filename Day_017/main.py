# The task of day 17 was creating a quiz game, following the OOP paradigm.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was {quiz.score}/{len(quiz.questions_list)}")