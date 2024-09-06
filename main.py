from tkinter import *


window = Tk()
window.title("Typing Speed Test")
window.config(width=600, height=400, padx=32, pady=32)

TIME_LIMIT = 1

# def countdown(count)


canvas = Canvas(width=400, height=150, bg='white', highlightthickness=0)
canvas.create_text(200, 75, text="Hello, Tkinter!", font=('Arial', 24))
canvas.pack()

typingArea = Text(width=50, height=4, padx=12, pady=8)
typingArea.pack(pady=12)

startBtn = Button(text="Start Timer", bg='blue', highlightthickness=0, padx=8, pady=2)
startBtn.pack()


window.mainloop()