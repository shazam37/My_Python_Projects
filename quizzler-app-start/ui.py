from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text='some question text',
                                                     font=("Arial", 15, "bold"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        right_image = PhotoImage(file='images/true.png')
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)
        left_image = PhotoImage(file='images/false.png')
        self.left_button = Button(image=left_image, highlightthickness=0, command = self.false_pressed)
        self.left_button.grid(column=1, row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Thank You :)\n"
                                                            f"Your final score is {self.quiz.score}")
            self.right_button.config(state='disabled')
            self.left_button.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, text='Correcto!')
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, text='Wrong')
        self.window.after(1000, self.next_question)
