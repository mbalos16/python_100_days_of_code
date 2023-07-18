from tkinter import *
from exercise_34_1_quizz_app_improvement_quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("BMM • Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        # Text image
        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",
            highlightthickness=0,
        )
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        check_img = PhotoImage(file="day_34/exercise_34_1_quizz_app_improvement_true.png")
        self.check_button = Button(image=check_img,
                                   highlightthickness=0,
                                   command=self.check_if_true)
        self.check_button.grid(row=2, column=0)

        error_img = PhotoImage(file="day_34/exercise_34_1_quizz_app_improvement_false.png")
        self.error_button = Button(image=error_img,
                                   highlightthickness=0,
                                   command=self.check_if_false)
        self.error_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz.")
            self.check_button.config(state="disabled")
            self.error_button.config(state="disabled")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
