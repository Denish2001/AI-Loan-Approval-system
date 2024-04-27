import tkinter as tk
from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import customtkinter
import mysql.connector
import ttkthemes
from datetime import datetime
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import MinMaxScaler
import warnings
from collections import Counter
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler as ss
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
'''

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

window=customtkinter.CTk()
window.title("LOAN APPROVAL SYSTEM LOGIN")
window.resizable(FALSE,FALSE)
window.geometry('800x600')

def login():
    if e1.get() == "admin" and e2.get()=="12345":
        window.withdraw()
        top=customtkinter.CTkToplevel()
        top.title("my second window")
        top.geometry("1000x600")
        top.resizable(FALSE,FALSE)

        def approve():
            if en1.get() == "" or en2.get() == "" or en3.get() == "" or en4.get() == "" or en5.get() == "":
                messagebox.showerror('Error', 'All fields are required!!')
            else:
                top.withdraw()
                topwin=customtkinter.CTkToplevel()
                topwin.title("my second window")
                topwin.geometry("1000x600")
                topwin.resizable(FALSE,FALSE)

                def proceed():
                    import pandas as pd
                    import numpy as np
                    import matplotlib.pyplot as plt
                    import seaborn as sns
                    import pickle
                    from sklearn.model_selection import train_test_split
                    from sklearn.metrics import accuracy_score, confusion_matrix
                    from imblearn.over_sampling import SMOTE
                    from sklearn.preprocessing import MinMaxScaler
                    import warnings
                    from collections import Counter
                    warnings.filterwarnings('ignore')
                    from sklearn.preprocessing import StandardScaler as ss
                    from sklearn.ensemble import RandomForestClassifier
                    from sklearn import metrics
                    from sklearn.tree import DecisionTreeClassifier
                    from sklearn.neighbors import KNeighborsClassifier

                def abort():
                    topwin.destroy()

                l2=customtkinter.CTkLabel(master=topwin,text="Details To be Submitted For Processing",font=('Century Gothic',24))
                l2.place(x=100,y=20)
                l3=customtkinter.CTkLabel(master=topwin,text="Gender",font=('Century Gothic',18))
                l3.place(x=350,y=90)
                l4=customtkinter.CTkLabel(master=topwin,text="Married",font=('Century Gothic',18))
                l4.place(x=350,y=120)
                l5=customtkinter.CTkLabel(master=topwin,text="Dependants",font=('Century Gothic',18))
                l5.place(x=350,y=150)
                l6=customtkinter.CTkLabel(master=topwin,text="Education",font=('Century Gothic',18))
                l6.place(x=350,y=180)
                l7=customtkinter.CTkLabel(master=topwin,text="Self Employed",font=('Century Gothic',18))
                l7.place(x=350,y=210)
                l8=customtkinter.CTkLabel(master=topwin,text="Applicant Income",font=('Century Gothic',18))
                l8.place(x=350,y=240)
                l9=customtkinter.CTkLabel(master=topwin,text="Coapplicant Income",font=('Century Gothic',18))
                l9.place(x=350,y=270)
                l10=customtkinter.CTkLabel(master=topwin,text="Loan Amount",font=('Century Gothic',18))
                l10.place(x=350,y=300)
                l11=customtkinter.CTkLabel(master=topwin,text="Loan Amount Term",font=('Century Gothic',18))
                l11.place(x=350,y=330)
                l12=customtkinter.CTkLabel(master=topwin,text="Credit History",font=('Century Gothic',18))
                l12.place(x=350,y=360)
                l12=customtkinter.CTkLabel(master=topwin,text="Property Area",font=('Century Gothic',18))
                l12.place(x=350,y=390)

                val1=op1.get()
                val2=op2.get()
                val3=en1.get()
                val4=op3.get()
                val5=op4.get()
                val6=en2.get()
                val7=en3.get()
                val8=en4.get()
                val9=en5.get()
                val10=op5.get()
                val11=op6.get()

                values = [val1, val2, val3, val4, val5, val6, val7, val8, val9,val10, val11]
                

               
                l3=customtkinter.CTkLabel(master=topwin,text=val1,font=('Century Gothic',18))
                l3.place(x=600,y=90)
                l4=customtkinter.CTkLabel(master=topwin,text=val2, font=('Century Gothic',18))
                l4.place(x=600,y=120)
                l5=customtkinter.CTkLabel(master=topwin,text=val3,font=('Century Gothic',18))
                l5.place(x=600,y=150)
                l6=customtkinter.CTkLabel(master=topwin,text=val4,font=('Century Gothic',18))
                l6.place(x=600,y=180)
                l7=customtkinter.CTkLabel(master=topwin,text=val5,font=('Century Gothic',18))
                l7.place(x=600,y=210)
                l8=customtkinter.CTkLabel(master=topwin,text=val6,font=('Century Gothic',18))
                l8.place(x=600,y=240)
                l9=customtkinter.CTkLabel(master=topwin,text=val7,font=('Century Gothic',18))
                l9.place(x=600,y=270)
                l10=customtkinter.CTkLabel(master=topwin,text=val8,font=('Century Gothic',18))
                l10.place(x=600,y=300)
                l11=customtkinter.CTkLabel(master=topwin,text=val9,font=('Century Gothic',18))
                l11.place(x=600,y=330)
                l12=customtkinter.CTkLabel(master=topwin,text=val10,font=('Century Gothic',18))
                l12.place(x=600,y=360)
                l12=customtkinter.CTkLabel(master=topwin,text=val11,font=('Century Gothic',18))
                l12.place(x=600,y=390)
                btn=customtkinter.CTkButton(master=topwin, text="Proceeed",width=400, height=35, corner_radius=5 ,font=('Century Gothic',18,'bold'), command=proceed)
                btn.place(x=300, y=450)
                btn=customtkinter.CTkButton(master=topwin, text="Abort",width=400, height=35, corner_radius=5 ,font=('Century Gothic',18,'bold'),command=abort)
                btn.place(x=300, y=490)
                



            
        


        img=ImageTk.PhotoImage(Image.open("ai.jpg").resize((1000,600),Image.LANCZOS))
        la=customtkinter.CTkLabel(master=top,image=img)
        la.pack()

        frame2=customtkinter.CTkFrame(master=la,width=900,height=500,corner_radius=15)
        frame2.place(relx=0.5,rely=0.5, anchor=customtkinter.CENTER)
        
        l2=customtkinter.CTkLabel(master=frame2,text="Loan Approval system, Enter Your Details",font=('Century Gothic',20))
        l2.place(x=50,y=30)

    

        gender=["male", "female"]
        married=["Yes","No"]
        education=["graduate","not graduate"]
        selfemployed=["yes","no"]
        credithistory=["yes","no"]
        propertyarea=["rural", "urban", "semi-urban"]

        l3=customtkinter.CTkLabel(master=frame2,text="Gender",font=('Century Gothic',18))
        l3.place(x=150,y=90)
        l4=customtkinter.CTkLabel(master=frame2,text="Married",font=('Century Gothic',18))
        l4.place(x=150,y=120)
        l5=customtkinter.CTkLabel(master=frame2,text="Dependants",font=('Century Gothic',18))
        l5.place(x=150,y=150)
        l6=customtkinter.CTkLabel(master=frame2,text="Education",font=('Century Gothic',18))
        l6.place(x=150,y=180)
        l7=customtkinter.CTkLabel(master=frame2,text="Self Employed",font=('Century Gothic',18))
        l7.place(x=150,y=210)
        l8=customtkinter.CTkLabel(master=frame2,text="Applicant Income",font=('Century Gothic',18))
        l8.place(x=150,y=240)
        l9=customtkinter.CTkLabel(master=frame2,text="Coapplicant Income",font=('Century Gothic',18))
        l9.place(x=150,y=270)
        l10=customtkinter.CTkLabel(master=frame2,text="Loan Amount",font=('Century Gothic',18))
        l10.place(x=150,y=300)
        l11=customtkinter.CTkLabel(master=frame2,text="Loan Amount Term",font=('Century Gothic',18))
        l11.place(x=150,y=330)
        l12=customtkinter.CTkLabel(master=frame2,text="Credit History",font=('Century Gothic',18))
        l12.place(x=150,y=360)
        l12=customtkinter.CTkLabel(master=frame2,text="Property Area",font=('Century Gothic',18))
        l12.place(x=150,y=390)
        
        
        op1=customtkinter.CTkOptionMenu(master=frame2, values=gender, width=300, )
        op1.place(x=450,y=90)
        op2=customtkinter.CTkOptionMenu(master=frame2, values=married, width=300)
        op2.place(x=450,y=120)
        en1=customtkinter.CTkEntry(master=frame2,width=300,placeholder_text="Dependants")
        en1.place(x=450,y=150)
        op3=customtkinter.CTkOptionMenu(master=frame2, values=education, width=300)
        op3.place(x=450,y=180)
        op4=customtkinter.CTkOptionMenu(master=frame2, values=selfemployed, width=300)
        op4.place(x=450,y=210)
        en2=customtkinter.CTkEntry(master=frame2,width=300,placeholder_text="applicant's income")
        en2.place(x=450,y=240)
        en3=customtkinter.CTkEntry(master=frame2,width=300,placeholder_text="coapplicant's income")
        en3.place(x=450,y=270)
        en4=customtkinter.CTkEntry(master=frame2,width=300,placeholder_text="loan ammount")
        en4.place(x=450,y=300)
        en5=customtkinter.CTkEntry(master=frame2,width=300,placeholder_text="loan ammount term")
        en5.place(x=450,y=330)
        op5=customtkinter.CTkOptionMenu(master=frame2, values=credithistory, width=300)
        op5.place(x=450,y=360)
        op6=customtkinter.CTkOptionMenu(master=frame2, values=propertyarea, width=300)
        op6.place(x=450,y=390)
        
        bn1=customtkinter.CTkButton(master=frame2,text="Approve",width=450,corner_radius=5,font=('Century Gothic',18,'bold'),height=25 ,command=approve)
        bn1.place(x=250,y=450)
    

    else:
        messagebox.showerror('Error','Wrong credentials')


img = ImageTk.PhotoImage(Image.open("cards.jpg").resize((800,600),Image.LANCZOS))
l1=customtkinter.CTkLabel(master=window,image=img)
l1.pack()
frame1=customtkinter.CTkFrame(master=l1,width=400,height=500,corner_radius=15)
frame1.place(relx=0.5,rely=0.5, anchor=customtkinter.CENTER)
l2=customtkinter.CTkLabel(master=frame1,text="log into your account",font=('Century Gothic',20),anchor=CENTER)
l2.place(x=50,y=200)
l2=customtkinter.CTkLabel(master=frame1,text="Loan Approval system",font=('Century Gothic',20))
l2.place(x=50,y=45)
e1=customtkinter.CTkEntry(master=frame1,width=300,placeholder_text="username")
e1.place(x=50,y=200)
e2=customtkinter.CTkEntry(master=frame1,width=300,placeholder_text="password")
e2.place(x=50,y=250)
e2.configure(show="*")
b1=customtkinter.CTkButton(master=frame1,text="log in",width=300,corner_radius=5,font=('Century Gothic',15,'bold'),height=20,command=login)
b1.place(x=50,y=300)


window.mainloop()