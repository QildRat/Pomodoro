import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_mark = ""
window_after_id = ""
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(window_after_id)  # stop the running function of after() method.

    global reps, check_mark
    reps = 0
    check_mark = ""
    check.config(text=check_mark)
    titleLabel.config(text="Pomodoro")
    canvas.itemconfig(timer_text, text="00:00")  # configure the canvas.

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        titleLabel.config(text="Long break", fg=RED)
        count_down(long_break_sec)
    elif reps > 0 and reps % 2 == 0:
        titleLabel.config(text="Short break", fg=PINK)
        count_down(short_break_sec)
    else:
        titleLabel.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_remaining = math.floor(count / 60)  # get only the whole number
    sec_remaining = count % 60  # get the remainder.

    if sec_remaining < 10:
        sec_remaining = f"0{sec_remaining}"

    canvas.itemconfig(timer_text, text=f"{min_remaining}:{sec_remaining}")
    if count > 0:
        global window_after_id
        window_after_id = window.after(1000, count_down, count - 1)  # ms = delay in milliseconds. function itself, parameter of the function

    else:
        global check_mark
        if reps % 2 == 0:
            check_mark += "✔"
        check.config(text=check_mark)

        if reps < 8:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # add x and y padding. add bg color

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)  # size of the overlay, bg color, canvas boarder line.
img = PhotoImage(file="tomato.png")  # **kw file = absolute path of file.
canvas.create_image(100, 112, image=img)  # *ar x and y position(divide canvas size by 2 to get the middle position). **kw image = image file from Photo image.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))  # *ar x and y position. text, fill(color), font(a tuple).
canvas.grid(column=1, row=1)  # position

# Start button:
start = Button(text="Start", command=start_timer)  # assign a command of Start button
start.grid(column=0, row=2)

# Timer label:
titleLabel = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=("Courier", 30, "bold"))  # fg = text color
titleLabel.grid(column=1, row=0)

# Check label:
check = Label(text="", fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))
check.grid(column=1, row=3)

# Reset label:
reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()  # mainloop always listening in every event does in the window.
