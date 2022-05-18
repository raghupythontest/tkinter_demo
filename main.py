from tkinter import *

window = Tk()
window.title("My first GUI Application")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.grid(row=0,column=0)

my_label["text"] = "New Text"
my_label.config(text="new text1")

# 1)pack(),place(x,y),grid(row,column)
# Button
def button_clicked():
    input_text = input.get()
    my_label.config(text=input_text)


button = Button(text="click me", command=button_clicked)
button.grid(row=1,column=1)

new_button=Button(text="new button",command=button)
new_button.grid(row=0,column=2)
# Entry

input=Entry(width=14)
input.grid(row=2,column=3)


















window.mainloop()

