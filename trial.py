from tkinter import *
import customtkinter

root = customtkinter.CTk()
root.title('Tkinter.com')
root.geometry('700x450')

colors= ['blue','red','yellow','white']
myoption=customtkinter.CTkOptionMenu(root,values=colors)
myoption.pack(pady=10)



root.mainloop()