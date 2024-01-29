import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        master.title("Quiz Game")
        master.geometry("450x320")
        master.resizable(width=False, height=False)

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
            "Michaël Jakson": [
                   {"question": "What is Michael Jackson's best-selling album of all time?", "answer": "Thriller"},
                   {"question": "In what year did Michael Jackson release his iconic album Thriller?", "answer": "1982"},
                   {"question": "Which song features Michael Jackson performing the famous moonwalk during a live performance?", "answer": "Billie Jean"}
            ],
        }

        # GUI components
        self.configure_fonts()
        self.create_widgets()
        self.change_topic(self.topic_var.get())

    def configure_fonts(self):
        self.title_font = ("Helvetica", 18, "bold")
        self.label_font = ("Helvetica", 14)
        self.entry_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")

    def create_widgets(self):
        self.create_title_label()
        self.create_topic_menu()
        self.create_question_label()
        self.create_answer_entry()
        self.create_submit_button()
        self.create_score_label()

    def create_title_label(self):
        self.topic_label = tk.Label(self.master, text="Select a topic:", font=self.title_font)
        self.topic_label.pack(pady=10)

    def create_topic_menu(self):
        self.topic_var = tk.StringVar(self.master)
        self.topic_var.set(next(iter(self.topics)))
        self.topic_menu = tk.OptionMenu(self.master, self.topic_var, *self.topics.keys(), command=self.change_topic)
        self.topic_menu.pack(pady=10)

    def create_question_label(self):
        self.question_label = tk.Label(self.master, text="", font=self.label_font, wraplength=450)
        self.question_label.pack(pady=10)

    def create_answer_entry(self):
        self.answer_entry = tk.Entry(self.master, font=self.entry_font)
        self.answer_entry.pack(pady=10)

    def create_submit_button(self):
        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer, font=self.button_font)
        self.submit_button.pack(pady=10)

    def create_score_label(self):
        self.score_label = tk.Label(self.master, text="Score: 0", font=self.label_font)
        self.score_label.pack(pady=10)

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
            final_score_message = f"Your final score is: {self.score}\nDo you want to restart?"
            user_response = messagebox.askyesno("End of Quiz", final_score_message)
            
            if user_response:
                self.restart_quiz()
            else:
                self.master.quit()

    def next_question(self):
        self.question_label.config(text=self.topics[self.current_topic][self.question_index]['question'])
        self.answer_entry.delete(0, tk.END)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def restart_quiz(self):
        # Reset quiz variables
        self.score = 0
        self.question_index = 0
        self.update_score()

        # Start a new quiz with the current selected topic
        self.next_question()

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()