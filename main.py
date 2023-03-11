import tkinter as tk
import DataPreprocessing as dp
from pathlib import Path
import sys
from tkinter.scrolledtext import ScrolledText
import pandas as pd
#helper functions






window = tk.Tk()
window.geometry("800x700")
window.title("NCAA Application")
idsearchvar =tk.StringVar()
idsearchvar.set("waiting for input...")
predictionvar = tk.StringVar()
predictionvar.set("make a prediction bruh")

inputteam = tk.Entry()
def getInfo():
    finalstring=""
    path = 'C:\\Users\\konch\\PycharmProjects\\MarchMadnesspredictor\\Data\\MTeamSpellings.csv'
    with open(path, 'rt') as f:#replace path
        data = f.readlines()
    for line in data:
        if inputteam.get().lower() in line:
            finalstring=finalstring+" "+line
        if len(finalstring)>=800:
            idsearchvar.set(finalstring)
            return
    idsearchvar.set(finalstring)
def calculate():
    team1 = int(entry.get())
    team2 = int(entry2.get())
    numsims = int(entry3.get())
    prediction = dp.predict(team1,team2,numsims)
    predictionvar.set(" "+str(prediction)+" chance, team1 will win")


tits = r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠋⠉⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣶⣶⣦⣬⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⣰⣧⡀⠄⠄⠄⠄⠈⢙⡋⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠰⠼⢯⣿⣿⣦⣄⠄⠄⠄⠈⢡⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠸⠤⠕⠛⠙⠷⣿⡆⠄⠄⠄⣸⣿⣿⡏⣼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿⢡⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⣄⠄⢀⠄⠄⢀⣤⣾⣿⣿⣿⢃⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⣛⣡⣄⣀⠄⠠⢴⣿⣿⡿⣄⣴⣿⣿⣿⣿⣿⢃⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣩⡽⡁⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢃⣿⣿⢟⣿⣿⣿⣿⣿⣮⢫⣿⣿⣿⣿⣿⣟⢿⠃⠄⢻⣿⣿⣿⣿
⣿⣿⣿⣿⡿⣸⠟⣵⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣷⣄⢰⡄⢿⣿⣿⣿
⣿⣿⣿⣿⡇⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⡎⣿⣿⣿
⣭⣍⠛⠿⠄⢰⠋⡉⠹⣿⣿⣿⣿⣿⣿⠙⣿⣿⣿⣿⣿⣿⡟⢁⠙⡆⢡⣿⣿⣿
⠻⣿⡆⠄⣤⠈⢣⣈⣠⣿⣿⣿⣿⣿⠏⣄⠻⣿⣿⣿⣿⣿⣆⣈⣴⠃⣿⣿⣿⣿
⡀⠈⢿⠄⣿⡇⠄⠙⠿⣿⡿⠿⢋⣥⣾⣿⣷⣌⠻⢿⣿⣿⡿⠟⣡⣾⣿⣿⠿⢋
⠛⠳⠄⢠⣿⠇⠄⣷⡑⢶⣶⢿⣿⣿⣿⣽⣿⣿⣿⣶⣶⡐⣶⣿⠿⠛⣩⡄⠄⢸
"""
button1 = tk.Button(
    text="search",
    width=10,
    height=2,
    bg="grey",
    fg="white",
    command= getInfo

)
button2 = tk.Button(
    text="calculate",
    width=10,
    height=2,
    bg="grey",
    fg="white",
    command = calculate

)

labelprediction = tk.Label(textvariable=predictionvar,font=("comicsans",20),background="grey")
greeting = tk.Label(text="Welcome to Konradicals NCAA Predictor Application 2023!", background="grey",font=("comicsans",20))
entry = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
label2 = tk.Label(text="Enter the id's of the teams and press calculate")
label3 = tk.Label(text="team1")
label4 = tk.Label(text="team2")
label5 = tk.Label(text = "search for id")
label6 = tk.Label(text = "enter sim numbers")
label7 =tk.Label(text=tits)
varlabel = tk.Label(textvariable=idsearchvar)
#placing elements
button2.place(x=600,y=220)
label2.place(x=500,y=60)
greeting.pack()
entry.place(x=600,y=100)
entry2.place(x=600,y=150)
entry3.place(x=600,y=190)
label3.place(x=560,y=100)
label4.place(x=560,y=150)
label5.place(x=80,y=60)
label6.place(x=480,y=190)
inputteam.place(x=80,y=100)
varlabel.place(x=80,y=140)
button1.place(x=180,y=60)
labelprediction.place(x=100,y=600)
label7.place(x=480,y=300)

window.mainloop()#mainloop of course

