# The task of day 17 was creating a quiz game, following the OOP paradigm.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create a list to hold the question objects.
question_bank = []

# Populate the question bank with Question objects created from the question data.
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

# Initialize the QuizBrain with the question bank.
quiz = QuizBrain(question_bank)

# Main loop to continue asking questions until there are no more left.
while quiz.still_has_questions():
    quiz.next_question()

# Print the completion message and the final score.
print("You've completed the Quiz!")
print(f"Your final score was {quiz.score}/{len(quiz.questions_list)}")
