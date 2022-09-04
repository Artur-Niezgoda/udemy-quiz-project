"""Model responsible for GUI of the API quiz

Classes:

    QuizInterface

Methods:
    get_next_question()
        print new question on the canvas and update the score
    press_true()
        model the function of the true button
    press_false()
        model the function of the false button
    give_feedback()
        change the color of the canvas depending on if the answer was correct or not

Constants:
    THEME_COLOR
        holds color of the theme
    FONT
        tuple containing font name, size and type
"""

import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    """
    This is a class that creates GUI for the Quiz Brain game

    Attributes:
        quiz (object): An object of QuizBrain class
        window (object): A window Widget form tkinter module displaying GUI elements
        score_label (object): A Label Widget from tkinter module
        canvas (object): An object of Canvas Widget class from tkinter module
        question_text (object): Text element displayed on a canvas object
        true_button (object): An object of Button Widget class from tkinter module
        false_button (object): An object of Button Widget class from tkinter module
    """

    def __init__(self, quiz_brain: QuizBrain):
        
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Labels
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "bold"))
        self.score_label.grid(row=0, column=1)

        # Question display
        self.canvas = tk.Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons

        true = tk.PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true,
                                     highlightthickness=0,
                                     borderwidth=0,
                                     activebackground=THEME_COLOR,
                                     command=self.press_true)
        self.true_button.grid(row=2, column=0)

        false = tk.PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false,
                                      highlightthickness=0,
                                      borderwidth=0,
                                      activebackground=THEME_COLOR,
                                      command=self.press_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self) -> None:
        """Print new question on the canvas and update the score
        """
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self) -> None:
        """Model the function of the true button
        """
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self) -> None:
        """Model the function of the true button
        """
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool) -> None:
        """Change the color of the canvas depending on if the answer was correct or not

        :param is_right: Boolean value - True if the answer was correct or False if not
        """
        if is_right:
            self.canvas.config(bg="green", highlightthickness=0,
                               borderwidth=0)
        else:
            self.canvas.config(bg="red", highlightthickness=0,
                               borderwidth=0)
        self.window.after(1000, self.get_next_question)
