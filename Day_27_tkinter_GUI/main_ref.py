from tkinter import *

def click_me():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("Scott")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#label
my_label = Label(text="I am a label", font=("Ariel", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)
#my_label.pack()

my_label["text"] = "New text"
my_label.config(text="New new text")


#button
button1 = Button(text="Click me", command=click_me)
button1.grid(column=1, row=1)
button2 = Button(text="Button 2")
button2.grid(column=2, row=0)
#button.pack()

#entry
input = Entry(width=10)
input.grid(column=3, row=2)
#input.pack()





window.mainloop()

