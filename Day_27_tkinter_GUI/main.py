from tkinter import *

def click_me():
    miles = float(input.get())
    kilometres = miles * 1.609
    my_label3.config(text=kilometres)

window = Tk()
window.title("Scott")
window.minsize(width=500, height=300)
window.config(padx=30, pady=50)


#labels
my_label1 = Label(text="Miles", font=("Ariel", 12, "bold"))
my_label1.grid(column=2, row=0)
my_label1.config(padx=20, pady=20)

my_label2 = Label(text="is equal to", font=("Ariel", 12, "bold"))
my_label2.grid(column=0, row=1)
my_label2.config(padx=20, pady=20)

my_label3 = Label(text="0", font=("Ariel", 12, "bold"))
my_label3.grid(column=1, row=1)
my_label3.config(padx=20, pady=20)

my_label4 = Label(text="Km", font=("Ariel", 12, "bold"))
my_label4.grid(column=2, row=1)
my_label4.config(padx=20, pady=20)

#button
button1 = Button(text="Calculate", command=click_me)
button1.grid(column=1, row=2)


#entry
input = Entry(width=10)
input.insert(END, string="Enter miles")
#input.config(padx=20, pady=20)
input.grid(column=1, row=0)
#input.pack()





window.mainloop()

