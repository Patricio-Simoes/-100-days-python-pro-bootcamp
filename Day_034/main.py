# On Day 34, the quiz brain app from day 17 was revisited and had some improvements, namely: 
# - A UI was added to it, using the tkinter module.
# - Instead of having the questions all stored locally on a file, calls to the open trivia API are now being made, in order to fetch the questions randomly.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)   
