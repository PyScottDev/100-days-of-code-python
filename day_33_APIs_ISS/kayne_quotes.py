from tkinter import *
import requests

def get_quote():
    url = "https://api.kanye.rest"

    responce = requests.get(url)
    responce.raise_for_status()

    data = responce.json()

    quote = data["quote"]
    return quote

    #Write your code here.
quote = get_quote()



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day_33_APIs_ISS/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day_33_APIs_ISS/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()