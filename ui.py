from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=30, pady=30, background=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.quiz.score}", background=THEME_COLOR, foreground="white", font=("Ariel",15))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(background="white", width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
        self.ques = self.canvas.create_text(150, 120, text="Question",
                                            width=280,
                                            font=("Ariel", 20, "italic"))

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_selected)
        self.right_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_selected)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.score_label.config(text=f"Score:{self.quiz.score}")
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            next_quest = self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text=next_quest)
        else:
            self.canvas.itemconfig(self.ques, text=f"That's a wrap\nScore:{self.quiz.score}/{self.quiz.question_number}")
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

    def true_selected(self):
        check = self.quiz.check_answer("true")
        self.background_change(check)

    def false_selected(self):
        check = self.quiz.check_answer("false")
        self.background_change(check)

    def background_change(self, check):
        if check:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, func=self.get_next_ques)
