import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")

        self.score = 0
        self.question_index = 0
        self.current_topic = None

        self.topics = {
                    "Kaaris": [
                        {"question": "Quelle est la musique de Kaaris la plus écoutée?", "answer": "Arrêt du cœur"},
                        {"question": "Quel est le meilleur son de Kaaris et Booba?", "answer": "Kalash"},
                        {"question": "En quelle année Kaaris a-t-il sorti 'Or Noir Part 2'?", "answer": "2014"}
                    ],
                    "Scorpions": [
                        {"question": "What is the most famous song by Scorpions?", "answer": "Wind of Change"},
                        {"question": "In which year was Scorpions' 'Rock You Like a Hurricane' released?", "answer": "1984"},
                        {"question": "Who is the lead vocalist of Scorpions?", "answer": "Klaus Meine"}
                    ],
                     "Daft Punk": [
                            {"question": "What year did Daft Punk release their debut album 'Homework'?", "answer": "1997"},
                            {"question": "What is the title of Daft Punk's 2013 hit single featuring Pharrell Williams?", "answer": "Get Lucky"},
                            {"question": "Which movie did Daft Punk compose the soundtrack for in 2010?", "answer": "Tron: Legacy"}
                        ],

                        "Édith Piaf": [
                            {"question": "What is Édith Piaf's most famous song, often regarded as her signature song?", "answer": "La Vie en rose"},
                            {"question": "In which year was Édith Piaf's song 'Non, je ne regrette rien' released?", "answer": "1960"},
                            {"question": "Which French city was Édith Piaf born in?", "answer": "Paris"}
                        ],

                        "Justice": [
                            {"question": "Which electronic music duo released the album 'Cross' in 2007?", "answer": "Justice"},
                            {"question": "Justice is well-known for using a symbol that resembles which religious icon?", "answer": "Cross"},
                            {"question": "Which Justice song features the lyrics 'Because we are your friends, you'll never be alone again'?", "answer": "We Are Your Friends"}
                        ],

                        "The Beatles": [
                            {"question": "Which city are The Beatles originally from?", "answer": "Liverpool"},
                            {"question": "What is the title of The Beatles' album with the iconic cover on Abbey Road?", "answer": "Abbey Road"},
                            {"question": "Who was the primary songwriter duo in The Beatles?", "answer": "Lennon-McCartney"}
                        ],

                        "Queen": [
                            {"question": "Who was the lead vocalist of the rock band Queen?", "answer": "Freddie Mercury"},
                            {"question": "Which Queen song has the famous lyrics 'Is this the real life? Is this just fantasy?'", "answer": "Bohemian Rhapsody"},
                            {"question": "In what year was Queen's album 'A Night at the Opera' released?", "answer": "1975"}
                        ],

                        "Beyoncé": [
                            {"question": "Which group was Beyoncé originally a member of before her solo career?", "answer": "Destiny's Child"},
                            {"question": "What is the title of Beyoncé's visual album released in 2016?", "answer": "Lemonade"},
                            {"question": "Which song did Beyoncé perform at the 2013 Super Bowl halftime show?", "answer": "Single Ladies"}
                        ],
                }

        self.topic_label = tk.Label(master, text="Select a topic:")
        self.topic_label.pack()

        self.topic_var = tk.StringVar(master)
        self.topic_var.set(next(iter(self.topics))) # default to the first topic

        self.topic_menu = tk.OptionMenu(master, self.topic_var, *self.topics.keys(), command=self.change_topic)
        self.topic_menu.pack()

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()

        # Initialize the first topic
        self.change_topic(self.topic_var.get())

    def change_topic(self, topic):
        self.current_topic = topic
        self.question_index = 0
        self.score = 0
        self.update_score()
        self.next_question()

    def check_answer(self):
        answer = self.answer_entry.get()
        correct_answer = self.topics[self.current_topic][self.question_index]['answer']
        if answer.lower() == correct_answer.lower():
            self.score += 1
            self.update_score()
            messagebox.showinfo("Correct", "That's correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, that's not correct. The correct answer was: {correct_answer}")

        self.question_index += 1
        if self.question_index < len(self.topics[self.current_topic]):
            self.next_question()
        else:
            messagebox.showinfo("End of Quiz", f"Your final score is: {self.score}")
            self.master.quit()

    def next_question(self):
        self.question_label.config(text=self.topics[self.current_topic][self.question_index]['question'])
        self.answer_entry.delete(0, tk.END)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()
