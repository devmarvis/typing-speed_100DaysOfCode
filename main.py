import math
import time
import tkinter
from tkinter import *
import textwrap


window = Tk()
window.title("Typing Speed Test")
window.config(width=600, height=400, padx=32, pady=32)

TIME_LIMIT = 0.1
TEXT_TO_TYPE = ("A text widget manages a multi-line text area. Like the canvas widget, Tk's text widget is an "
                "immensely flexible and powerful tool that can be used for a wide variety of tasks.")
wrapped_text = textwrap.fill(TEXT_TO_TYPE, width=50)


def countdown(count):
    count_mins = math.floor(count / 60)
    count_secs = int(count % 60)

    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")

    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        typing_area.config(state="disabled")
        text_entered = typing_area.get('1.0', tkinter.END).strip()
        print(text_entered)
        try:
            if text_entered[0]:
                text_split_arr = text_entered.split(" ")
                print(f'You typed {len(text_split_arr)} words in 6 seconds.')
                canvas.itemconfig(notif_text, text=f'You typed {len(text_split_arr)} words in 6 seconds.', )
        except IndexError:
            pass


def start_timer():
    typing_area.config(state='normal')
    typing_area.delete('1.0', tkinter.END)

    time.sleep(0.5)
    count_ = TIME_LIMIT * 60
    countdown(count_)


canvas = Canvas(width=500, height=200, bg='white', highlightthickness=0)
canvas.create_text(250, 100, text=wrapped_text, font=('Arial', 14))
timer_text = canvas.create_text(425, 20, text="00:00", font=("Arial", 24, "bold"))
notif_text = canvas.create_text(125, 20,
                                text='',
                                fill='blue',
                                font=('Comic', 11))

canvas.pack()

typing_area = Text(width=50, height=4, padx=12, pady=8, state='disabled')
typing_area.pack(pady=12)

start_btn = Button(
    text="Start Timer",
    bg='blue',
    highlightthickness=0,
    padx=8,
    pady=2,
    command=start_timer
)
start_btn.pack()


window.mainloop()
