# Exercise 34.1. Quizz app improvement


from exercise_34_1_quizz_app_improvement_question_model import Question
from exercise_34_1_quizz_app_improvement_data import question_data
from exercise_34_1_quizz_app_improvement_quiz_brain import QuizBrain
from exercise_34_1_quizz_app_improvement_quiz_brain_ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
