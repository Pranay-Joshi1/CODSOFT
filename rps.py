import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("650x650")
window.config(bg="#DA136E")

choices= ["ROCK","PAPER", "SCISSORS"]
cpu_choice = random.randint(0,2)
#Initialize the scores
rnd_c, rnd_d, rnd_u = 0,0,0     
label1 = tk.Label(window, text="Welcome to\nRock-Paper-Scissors!",font=("Segoe UI Bold", 30),fg="white",bg="#DA136E")
label1.pack(pady=10)
label2= tk.Label(window, font= ("Intro Black Inline", 50),bg="#DA136E")
label2.pack(pady = 10)
label3 = tk.Label(window,text= "Your Choice", font= ("Brother 1816", 25),bg="#DA136E", fg="white")
label3.pack(pady=10)
user_choice = ttk.Combobox(window,font=("Brother 1816", 15), value =("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)    
result_label = tk.Label(window,text="",font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
result_label.pack(pady=10)
def spin():
    global rnd_u
    global rnd_c
    global rnd_d
    label1.config(text="Computer Choice",font=("Segoe UI Bold", 30),fg="white",bg="#DA136E")
    cpu_choice = random.randint(0,2)
    label2.config(text = choices[cpu_choice], font= ("Intro Black Inline", 50),bg="white")
    #0=Rock, 1=Scissors, 2=Paper
    if user_choice.get() == "Rock":
        user_value = 0
    elif user_choice.get() == "Paper":
        user_value = 1
    elif user_choice.get() == "Scissors":
        user_value = 2
    if cpu_choice == user_value:
        result_label.config(text="It's a Draw.",font= 
                            ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
        rnd_d += 1
    elif  ((cpu_choice==0 and user_value==2) or
          (cpu_choice==1 and user_value==0) or
          (cpu_choice==2 and user_value==1)): 
        result_label.config(text="Computer Wins.",font= 
                            ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
        rnd_c +=1
    else:
        result_label.config(text="You Win.",font= 
                            ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
        rnd_u +=1
    #Update scoreboard after each round
    score_u.config(text = (rnd_u,"Wins"),font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
    score_d.config(text = (rnd_d,"Draws"),font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
    score_c.config(text = (rnd_c,"Losses"),font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
 
btn_spin = tk.Button(window, text= "Play", command = spin,font=("Segoe UI",15) )
btn_spin.pack(pady=10)
label4 = tk.Label(window,text= "Scorecard", font= ("Intro Regular Alt", 20),bg="#DA136E", fg="white")
label4.pack(pady=10)
frame1 = tk.Frame(window,background="#DA136E")
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.columnconfigure(2,weight=1)
score_u = tk.Label(frame1,text =(rnd_u,"Wins") ,font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
score_d = tk.Label(frame1,text = (rnd_d,"Draws"),font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
score_c = tk.Label(frame1,text = (rnd_c,"Losses"),font= ("Brother 1816 Printed", 20),fg="white",bg="#DA136E")
score_u.grid(row=0, column=0, padx=10)
score_d.grid(row=0, column=1, padx=10)
score_c.grid(row=0, column=2, padx=10)
frame1.pack(pady=15) 

window.mainloop()