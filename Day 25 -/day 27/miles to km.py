from tkinter import *
window = Tk()
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

def button_clicked():
    label = Label(text = int(input.get())*1.6)
    label.grid(column=1,row=4)


my_label = Label(text="Convert from Miles to KM", font=("Arial", 10, "bold"))
my_label.grid(column=1, row=0)
mileslabel = Label(text = "Miles")
mileslabel.grid(column=0,row=2)
input = Entry(width=20)
input.grid(column=1, row=2)
button = Button(text = "Convert", command=button_clicked)
button.grid(column=2, row=2)
kmlabel = Label(text = "KM")
kmlabel.grid(column=0,row=4)

window.mainloop()