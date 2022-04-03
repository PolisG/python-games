'''
    A simple wordle game with greek words using python and tk for graphics
    @autor: Polychronis Georgiadis
'''
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

class Game(Frame):
        def __init__(self, master):
                super().__init__(master)
                self.fields()
                self.create_widgets()
                self.random_word()
                
        def reset(self):
                for widgets in Frame.winfo_children(self):
                    widgets.destroy()
                self.fields()
                self.create_widgets()
                self.random_word()
                
        def fields(self):
                self.row_count = 0
                self.grey = "#C0C0C0"
                self.green = "#008000"
                self.yellow = "#FFFF33"
                self.guess = StringVar()
                self.guess.trace('w', lambda *args: self.limit(self.guess))
                
        def create_widgets(self):
                self.title_frame = Frame(self.master, bg="black", width=500, height=100)
                self.title_frame.grid_propagate(False)
                self.title_frame.grid(column=0, row=0, sticky='snew')
            
                self.letter_frame = Frame(self.master, bg="black", width=500, height=400)
                self.letter_frame.grid_propagate(False)
                self.letter_frame.grid(column=0, row=1, sticky='snew')
            
                self.control_frame = Frame(self.master, bg="black", width=500, height=100)
                self.control_frame.grid_propagate(False)
                self.control_frame.grid(column=0, row=2, sticky='snew')

                Label(self.title_frame, bg="black", fg="white", text="WORDLE GR", font=("Century 30 bold")).pack()

                self.guess_label = Label(self.control_frame, bg="black", 
                fg="white", text="Λέξη", font=("Century 15"), width=14)
                self.guess_label.pack(side="left", expand=True)

                self.guess_entry = Entry(self.control_frame, font=("Century 15"), justify = "center", 
                textvariable = self.guess, fg="black", highlightcolor="#32CD32", highlightthickness=2, width=7)
                self.guess_entry.pack(side="left", expand=True)

                self.guess_button = Button(self.control_frame, text="OK", bg=self.grey, activebackground="#00BFFF", 
                fg="white", font=("Century 15 bold"), command=self.check_guess)
                self.guess_button.pack(side="left", expand=True)

                self.back_button = Button(self.control_frame, text="⌫", bg=self.grey, activebackground="#FF4500", 
                fg="white", font=("Century 15 bold"), width=4, command=lambda:self.guess.set(""))
                self.back_button.pack(side="left", expand=True)
                
        def limit(self, guess):
                if len(guess.get()) > 0:
                    guess.set(guess.get()[:5])
                    
        def random_word(self):
                words_5_letter = open("5-letter-words-gr.txt","r",encoding="utf-8")
                self.list = words_5_letter.readlines()
                self.answer = random.choice(self.list).rstrip("\n")
                
        def check_guess(self):
                guess_entry = self.guess.get().upper()
                x = list(filter(lambda x: guess_entry in x, self.list))
                if len(x)==1 and len(guess_entry)==5:
                    self.guess_label["text"] = ""
                    print(self.answer, guess_entry)
                    if self.row_count <= 6:
                        for i, letter in enumerate(guess_entry):
                            self.letter_label = Label(self.letter_frame, width=4, fg="white", 
                            bg=self.grey, text=letter, font=("Arial 25 bold"))
                            self.letter_label.grid(column=i, row=self.row_count, padx=5, pady=5)
                            if letter == self.answer[i]:
                                self.letter_label["bg"] = self.green
                            
                            if letter in self.answer and not letter==self.answer[i]:
                                self.letter_label["bg"]= self.yellow

                            if letter not in self.answer:
                                self.letter_label["bg"]= self.grey
                    self.row_count += 1
                    
                    if self.row_count<=6 and self.answer == guess_entry:
                        msg_box = messagebox.askquestion("Νίκη", "Συγχαρητήρια, κέρδισες! Θέλεις να παίξεις ξανά;")
                        if msg_box == 'yes':
                            messagebox.showinfo('WORDLE GR','Έτοιμη η νέα σου λέξη.')
                            self.reset()
                        elif msg_box == 'no':
                            self.master.destroy()
                            self.master.quit()
                        else:
                            messagebox.showwarning('Error', 'Something went wrong!')
                            
                    if self.row_count==6 and self.answer != guess_entry:
                        msg_box = messagebox.askquestion("Ήττα", "Λυπάμαι, έχασες. Θέλεις να παίξεις ξανά;")
                        if msg_box == 'yes':
                            messagebox.showinfo('WORDLE GR','Έτοιμη η νέα σου λέξη.')
                            self.reset()
                        elif msg_box == 'no':
                            self.master.destroy()
                            self.master.quit()
                        else:
                            messagebox.showwarning('Error', 'Something went wrong!')
                else:
                    self.guess_label["text"] = "Δεν υπάρχει η λέξη"
                    
if __name__ == "__main__":
	root = tk.Tk()
	root.title("Wordle greek")
	root.config(bg="black")
    # window dimensions and position 
	root.geometry(f"{512}x{512}+{int(root.winfo_screenwidth()/2)-256}+{int(root.winfo_screenheight()/2)-256}")
	root.resizable(False, False)
	game = Game(root)
	game.mainloop()