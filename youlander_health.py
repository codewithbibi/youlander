import tkinter as tk
from tkinter import colorchooser
import ttkbootstrap as ttkb
from ttkbootstrap import *
from datetime import datetime, timedelta, time
from calendar import monthrange

class Cycle(ttkb.Toplevel):
    def __init__(self, parent, selected_date,selected_hour):
        super().__init__(parent)
        self.title("Add Activity")
        self.geometry("900x900")
        self.customstyle = parent.style
        self.resizable(False,False)
        
        self.selected_date = selected_date
        self.current_display_time = datetime.combine(selected_date.date(), datetime.min.time())
        self.selected_time = self.current_display_time

        if self.customstyle.theme_use() == "minty":        
            self.customstyle.configure("Custom.TLabel", font=("Helvetica", 14, "bold"), background="#F3969A", foreground="#0D716D")
            self.customstyle.configure("Custom.TButton", font=("Helvetica", 14, "bold"), background="white", foreground="#0D716D")
        else:
            self.customstyle.configure("Custom.TLabel", font=("Helvetica", 14, "bold"), background="#94A2A3", foreground="#002A36")
            self.customstyle.configure("Custom.TButton", font=("Helvetica", 14, "bold"), background="#002A36", foreground="white")

        self.Main_UI()

    def Main_UI(self):
        self.iconbitmap("img/icon.ico")

        main_frame = ttkb.Frame(self, style="secondary.TFrame")
        main_frame.pack(fill=BOTH, expand=YES)

        ttkb.Label(
            main_frame,
            text="Track Your Cycle",
            style="Custom.TLabel",
            width=15
        ).pack(anchor=NW)



class Health(ttkb.Toplevel):
    def __init__(self, parent, selected_date,selected_hour):
        super().__init__(parent)
        self.title("Add Activity")
        self.geometry("900x900")
        self.customstyle = parent.style
        self.resizable(False,False)
        
        self.selected_date = selected_date
        self.current_display_time = datetime.combine(selected_date.date(), datetime.min.time())
        self.selected_time = self.current_display_time

        if self.customstyle.theme_use() == "minty":        
            self.customstyle.configure("Custom.TLabel", font=("Helvetica", 14, "bold"), background="#F3969A", foreground="#0D716D")
            self.customstyle.configure("Custom.TButton", font=("Helvetica", 14, "bold"), background="white", foreground="#0D716D")
        else:
            self.customstyle.configure("Custom.TLabel", font=("Helvetica", 14, "bold"), background="#94A2A3", foreground="#002A36")
            self.customstyle.configure("Custom.TButton", font=("Helvetica", 14, "bold"), background="#002A36", foreground="white")

        self.Main_UI()

    def Main_UI(self):
        self.iconbitmap("img/icon.ico")

        main_frame = ttkb.Frame(self, style="secondary.TFrame")
        main_frame.pack(fill=BOTH, expand=YES)

        ttkb.Label(
            main_frame,
            text="Track Your Health",
            style="Custom.TLabel",
            width=15
        ).pack(anchor=NW)


