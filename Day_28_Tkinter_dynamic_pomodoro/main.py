from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    #count_down(5 * 60)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # If it's the 1st/3rd/5th/7th rep:
    if reps % 8 ==0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED, highlightthickness=0)
        count_down(long_break_sec)
    # if reps % 2 != 0:
    #     count_down(work_sec)
    # If it's the 8th rep:
    # if reps % 8 ==0:
    #     count_down(long_break_sec)
    # If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        timer_label.config(text="Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK, highlightthickness=0)
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day_28_Tkinter_dynamic_pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

#canvas.pack()

# labels
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(column=1, row=0)

check_label = Label(font=(FONT_NAME, 14, "bold"), bg=YELLOW, fg=GREEN,highlightthickness=0)
check_label.grid(column=1, row=3)

#buttons
start_button = Button(text="Start", command=start_timer, font=(FONT_NAME, 6), padx=10, pady=5, bg=YELLOW, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, font=(FONT_NAME, 6), padx=10, pady=5, bg=YELLOW, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
