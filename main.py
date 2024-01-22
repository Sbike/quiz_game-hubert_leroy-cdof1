import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")

        self.score = 0
        self.question_index = 0

        self.questions = [
            {"question": "Quelle est la musique de kaaris la plus ecoutée?", "answer": "Arret du coeur"},
            {"question": "Quel est le meilleur son de kaaris et booba?", "answer": "Kalash"},
            {"question": "en quelle année kaaris a sorti or noir part 2'?", "answer": "2014"}
        ]

        self.question_label = tk.Label(master, text=self.questions[0]['question'])
        self.question_label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

    def check_answer(self):
        answer = self.answer_entry.get()
        if answer.lower() == self.questions[self.question_index]['answer'].lower():
            self.score += 1
            self.update_score()
            messagebox.showinfo("Correct", "That's correct!")
        else:
            messagebox.showinfo("Incorrect", "Sorry, that's not correct.")

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.next_question()
        else:
            messagebox.showinfo("End of Quiz", f"Your final score is: {self.score}")
            self.master.quit()

    def next_question(self):
        self.question_label.config(text=self.questions[self.question_index]['question'])
        self.answer_entry.delete(0, tk.END)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()
