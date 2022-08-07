from tkinter import *
import random

timer = None
count_letters = 0
wrong_letters = 0
count_seconds = 0

#open the text file and then make list of words
#then create own list and added words
word_list = []
with open("neo.txt") as letter:
    list_words = letter.readlines()
    for word in list_words:
        word_list.append(word.strip())

#random text
random_word = random.choice(word_list)
print(len(random_word))
random_words = random_word.split(" ")


def reset():
    window.after_cancel(timer)


def print_key(event):
    #function get any key typed and show
    global count_letters, wrong_letters
    count_letters += 1
    args = event.keysym, event.keycode, event.char
    #arg keycode have number of 16 which is shift, on press shift we deduct the count
    if args[1] == 16:
        count_letters -= 1
    #backspace or value 8 from event.keycode we use to delete wrong letter
    elif args[1] == 8:
        wrong_letters += 1



def start(*args):
    if len(entry_text.get()) < 1:
        #if we have input we call counter for 60 seconds
        countdown(60)
    print_key(args[0])
    #comparations from random text to entry, make connection and comparation if its correct or not
    if not canvas.itemcget(canvas_text, 'text').startswith(entry_text.get()):
        canvas.itemconfig(canvas_text, fill="red")
    else:
        canvas.itemconfig(canvas_text, fill="white")
    if entry_text.get() == canvas.itemcget(canvas_text, 'text'):
        canvas.itemconfig(canvas_text, fill="green")


def countdown(count):
    #setup the counter
    global timer, count_seconds
    sec = count
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(canvas_head, text=f"{sec}")

    if count > 0:
        count_seconds += 1
        timer = window.after(1000, countdown, count - 1)

    else:
        #when timer works he counts_seconds double, so we must divade by 2 in calculations
        cps = round(len(entry_text.get()) / count_seconds / 2, 2)
        print(cps)
        cpm = round(cps * 60, 2)
        print(cpm)
        wps = round(len(entry_text.get().split(" ")) / count_seconds, 2)
        print(wps)
        wpm = round(wps * 60, 2)
        print(wpm)
        window.after_cancel(timer)
        canvas.itemconfig(canvas_head, text="Finished")
        result_label.config(text=f"Speed:\n {cps} CPS\n{cpm} CPM\n{wps} WPS\n{wpm} WPM", font=("Ubuntu Medium", 24))
        entry_text.destroy()


window = Tk()

window.title("Typing Speed")
window.config(padx=100, pady=50)


title_label = Label(text="Typing Speed", font=("Arial", 48, "italic"))
title_label.grid(column=0, row=0)

canvas = Canvas(width=500, height=500, bg="blue")
canvas_head = canvas.create_text((250, 50), text="60", font=("Arial", 36))
canvas_text = canvas.create_text(250, 250, text=random_word, fill="white", font=("Arial", 16, "italic"), width=480)
canvas.grid(column=0, row=1, pady=20)

entry_text = Entry(width=40)
entry_text.grid(column=0, row=2, pady=20)
#pointer starts from entry
entry_text.focus()
#starts function when type any key on keyboard
entry_text.bind("<KeyPress>", start)

result_label = Label(text="")
result_label.grid(column=0, row=3)


window.mainloop()
