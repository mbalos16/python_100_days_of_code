# Exercise 17.1. Quiz Game
# Find more questions and answers for this game in the Trivia api: https://opentdb.com/api_config.php

from exercise17_1_quiz_game_question_model import Question
from exercise17_1_quiz_game_data import question_data
from exercise17_1_quiz_game_quiz_brain import QuizBrain

question_bank = []
for element in question_data:
    question_bank.append(Question(element["question"], element["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz. \nYour final score was {quiz.score}/{len(quiz.questions_list)}.")