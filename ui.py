from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def ans_false(self):
        ans_status = self.quiz.check_answer(user_answer="False")
        self.give_feedback(ans_status)

    def ans_true(self):
        ans_status = self.quiz.check_answer(user_answer="True")
        self.give_feedback(ans_status)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.reset_quiz_bg)

    def reset_quiz_bg(self):
        self.canvas.config(bg="white")
        self.get_next_question()

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.lblScore = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.lblScore.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.q_text = self.canvas.create_text(125, 150, text="Test", width=250,  fill=THEME_COLOR,
                                              font=("Arial", 20, "italic"))

        imgFalse = PhotoImage(file="images/false.png")
        self.btnNo = Button(image=imgFalse, command=self.ans_false)
        self.btnNo.grid(column=0, row=2)

        imgTrue = PhotoImage(file="images/true.png")
        self.btnYes = Button(image=imgTrue, command=self.ans_true)
        self.btnYes.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
            self.lblScore.config(text="Score: " + str(self.quiz.score))
        else:
            self.canvas.itemconfig(self.q_text, text="End of Quiz!")
            self.btnNo.config(state="disabled")
            self.btnYes.config(state="disabled")

