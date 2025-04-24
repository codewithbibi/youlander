import ttkbootstrap as ttkb
from ttkbootstrap import *
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from ttkbootstrap.dialogs import Messagebox
from youlander_main import Main_Page_Window

class Youlander(ttkb.Window):
    def __init__(self):
        super().__init__(title="Youlander",themename="minty")  
        self.geometry("1880x900")

        self.style.configure("YellowLabel.TLabel", background="#ffcc66", foreground="#AB265D")
        self.protocol("WM_DELETE_WINDOW",lambda: on_close(app))

        self.main_Ui()

        def on_close(app):
            app.quit()

    def main_Ui(self):
        self.iconbitmap("img/icon.ico")

        main_frame=ttkb.Frame(self,padding=5, style='warning.TFrame')
        main_frame.pack(fill=BOTH, expand=YES)
        
#making left side
        pick_frame=ttkb.Frame(main_frame,width=600, style='warning.TFrame')
        pick_frame.pack(fill=Y,expand=YES,side=LEFT)
        bg_image = Image.open("img/icon.png")
        bg_size = bg_image.resize((1024,1024))
        bg_photo = ImageTk.PhotoImage(bg_size)

        bg_label = Label(pick_frame, image=bg_photo)
        bg_label.image = bg_photo 
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#making center side
        left_frame=ttkb.Frame(main_frame,width=200, style='warning.TFrame')
        left_frame.pack(fill=Y,expand=YES,side=LEFT)
        ttkb.Label(
            left_frame,
            text="Enter Your Mail",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N,pady=(250,0),padx=(0,0))
        global ent_Mail
        ent_Mail=ttkb.Entry(
            left_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40
        )
        ent_Mail.pack(anchor=N)
        
        ttkb.Label(
            left_frame,
            text="Enter Your Password",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        global ent_Pass
        ent_Pass=ttkb.Entry(
            left_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40,
            show="*"
        )
        ent_Pass.pack(anchor=N)

        ttkb.Button(
            left_frame,
            text="Sign In",
            command=self.sign_in,
            bootstyle="primary",
            width=45
        ).pack(anchor=N,pady=5)
#making right side
        right_frame=ttkb.Frame(main_frame,width=260, style='warning.TFrame')
        right_frame.pack(fill=Y,expand=YES,side=RIGHT)

        ttkb.Label(
            right_frame,
            text="Enter Your Name",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N,pady=(150,0),padx=(0,0))
        global ent_Name
        ent_Name=ttkb.Entry(
            right_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40
        )
        ent_Name.pack(anchor=N)

        ttkb.Label(
            right_frame,
            text="Enter Your Lastname",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        global ent_Lastname
        ent_Lastname=ttkb.Entry(
            right_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40
        )
        ent_Lastname.pack(anchor=N)

        ttkb.Label(
            right_frame,
            text="Enter Your Nickname",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        global ent_Nickname
        ent_Nickname=ttkb.Entry(
            right_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40
        )
        ent_Nickname.pack(anchor=N)

        global gender_var #this will be the variable to your chack button
        gender_var=ttkb.BooleanVar()    
        bool_frame=ttkb.Frame(right_frame,style="warning.TFrame")
        bool_frame.pack(anchor=N)   
        ttkb.Label(
            bool_frame,
            text="Are You a Woman?",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        ent_Yes=ttkb.Radiobutton(
            bool_frame,
            text="yes",
            variable=gender_var,
            value=True,
            bootstyle="success"
        )
        ent_Yes.pack(side=LEFT,padx=(80,20))
        ent_No=ttkb.Radiobutton(
            bool_frame,
            text="no",
            variable=gender_var,
            value=False,
            bootstyle="success"
        )
        ent_No.pack(side=LEFT)

        ttkb.Label(
            right_frame,
            text="Enter Your Mail",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        global ent_Create_Mail
        ent_Create_Mail=ttkb.Entry(
            right_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40
        )
        ent_Create_Mail.pack(anchor=N)

        ttkb.Label(
            right_frame,
            text="Enter Your Password",
            font=("Helvetica", 16, "bold"),
            style="YellowLabel.TLabel"
        ).pack(anchor=N)
        global ent_Create_Password
        ent_Create_Password=ttkb.Entry(
            right_frame,
            foreground="#AB265D",
            font=("Helvetica", 10, "bold"),
            width=40,

            show="*"
        )
        ent_Create_Password.pack(anchor=N)

        ttkb.Button(
            right_frame,
            text="Create an Account",
            command=self.make_account,
            bootstyle="primary",
            width=45
        ).pack(anchor=N,pady=5)
        

#button funcitons
    def sign_in(self):
        conn = sqlite3.connect("user.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        mail=ent_Mail.get().strip()
        pasword=ent_Pass.get().strip()

        if (mail=="" or pasword==""):         
            Messagebox.show_warning("You cannot leave the mail or password empty.","Empty Fields",parent=Youlander)
        else:
            cursor.execute("SELECT * FROM user WHERE mail=? AND password=?", (mail, pasword))
            is_correct=cursor.fetchone()
            if is_correct:
                self.withdraw()  # hides the login window
                main_window = Main_Page_Window(is_correct["nickname"],is_correct["sex"])
                main_window.mainloop()  # Start the main window's event loop
            else:
                Messagebox.show_warning("The password or mail is wrong.","Wrong Entry")  

        conn.close()

    def make_account(self):
        conn = sqlite3.connect("user.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        name = ent_Name.get().strip()
        lastname = ent_Lastname.get().strip()
        nickname = ent_Nickname.get().strip()
        gender = "" 
        if gender_var.get() == True :
            gender=1
        else : gender=0
        mail = ent_Create_Mail.get().strip()
        pasword = ent_Create_Password.get().strip()

        if(name=="" or lastname=="" or nickname=="" or gender=="" or mail=="" or pasword == ""):
            Messagebox.show_warning("The field can not be empty.","Empty Fields")
        else:
            cursor.execute("SELECT mail FROM user WHERE mail=?",(mail,))
            exist=cursor.fetchone()

            if exist:
                Messagebox.show_warning("This account already exist","Already Exist")
            else:
                cursor.execute("""INSERT INTO user(name, lastname, nickname, sex, mail, password)
                VALUES (?, ?, ?, ?, ?, ?)""", (name, lastname, nickname, gender, mail, pasword))
                conn.commit()
                Messagebox.show_warning("Account created successfully.","Succesfull")     
                
                                                   
                            
        conn.close()
        
app=Youlander()
app.mainloop()
app.place_window_center()