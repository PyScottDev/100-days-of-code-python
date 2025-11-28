from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=800, height=300, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score:0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(column=1, row=0)

        image_true = PhotoImage(file="day_34_gui_quiz_api/images/true.png")
        self.true_but = Button(image=image_true, command=self.choose_true, padx=50, pady=50, bg=THEME_COLOR, borderwidth=0, relief="flat", highlightthickness=0)
        self.true_but.grid(column=0, row=2)

        image_false = PhotoImage(file="day_34_gui_quiz_api/images/false.png")
        self.false_but = Button(image=image_false, command=self.choose_false, pady=50, bg=THEME_COLOR, borderwidth=0, relief="flat", highlightthickness=0)
        self.false_but.grid(column=1, row=2)

        self.question_text = self.canvas.create_text(
            400,
            150,
            width=780,
            text="Demo text",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic"))

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_but.config(state="disabled")
            self.false_but.config(state="disabled")

    def choose_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def choose_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
 




