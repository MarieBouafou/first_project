import tkinter as tk
from datetime import datetime


def date():
    now = datetime.now()
    current_date = now.strftime("%d %B %Y")
    date_label.config(text=current_date)
    a.after(1000, date)  # run le programme apres 1second


a = tk.Tk()  # fenetre de l'application
date_label = tk.Label(a)
date_label.pack(pady=5, fill="x")
date()
a.mainloop()  # run l'application
