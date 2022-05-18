from tkinter import *

window=Tk()
window.title("Miles to Kilometer Calculator")
window.minsize(width=300,height=200)
window.config(padx=30,pady=30)

label1=Label(text="is equal to")
label1.grid(row=1,column=0)
label1.config(padx=20,pady=0)

label2=Label(text="Miles")
label2.grid(row=0,column=2)
label2.config(padx=20,pady=20)

label3=Label(text="Km")
label3.grid(row=1,column=2)
label3.config(padx=20,pady=0)

label4=Label(text="0")
label4.grid(row=1,column=1)
label4.config(padx=20,pady=0)

input=Entry()
input.config(width=10)
input.grid(row=0,column=1)

def calculate_km():
    miles=float(input.get())
    km=miles*1.6
    f_km="{:.2f}".format(km)
    label4.config(text=f_km)

button=Button(text="Calculate",command=calculate_km)
button.grid(row=2,column=1)

window.mainloop()