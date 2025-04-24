import tkinter as tk
from tkinter import colorchooser
import ttkbootstrap as ttkb
from ttkbootstrap import *
from datetime import datetime, timedelta, time
from calendar import monthrange

class Time_Hour(ttkb.Toplevel):
    def __init__(self, parent, selected_date, is_start_time=True):
        super().__init__(parent)
        self.iconbitmap("img/icon.ico")
        self.geometry("800x600")
        self.title("Select Time")
        self.resizable(False,False)
        self.selected_date = selected_date
        self.current_display_time = datetime.combine(selected_date.date(), datetime.min.time())
        self.selected_time = self.current_display_time
        self.parent = parent
        self.is_start_time = is_start_time
        self.main_ui()

    def main_ui(self):
        main_frame = ttkb.Frame(self, style="secondary.TFrame")
        main_frame.pack(fill=BOTH, expand=YES, padx=20, pady=20)
        
        button_frame = ttkb.Frame(main_frame, style="secondary.TFrame")
        button_frame.pack(fill=X, side=TOP)

        self.hours_per_page = 6
        self.page_index = 0

        
        ttkb.Label(
            button_frame,
            text="Pick an Hour",
            style="Custom.TLabel",
            width=20
        ).pack(anchor=N, side=TOP, pady=(0,10))
        
        ttkb.Button(
            button_frame,
            text="<",
            command=self.btn_Pre,
            width=5,
            style="Custom.TButton"
        ).pack(side=LEFT, anchor=N, padx=10)
        
        ttkb.Button(
            button_frame,
            text=">",
            command=self.btn_Next,
            style="Custom.TButton",
            width=5
        ).pack(side=RIGHT, anchor=N, padx=10)

        self.hour_frame = ttkb.Frame(main_frame, style="secondary.TFrame")
        self.hour_frame.pack(fill=X, side=TOP)
        ttkb.Label(
            self.hour_frame,
            text="Hours",
            style="Custom.TLabel",
            width=20
        ).pack(anchor=N, side=LEFT, padx=400)
        self.pick_Hours()

        ttkb.Button(
            main_frame,
            text="OK",
            command=self.on_ok,
            style="Custom.TButton",
            width=10
        ).pack(side=TOP, pady=10)

    def select_time(self, time):
        self.selected_time = time
        return time

    def on_ok(self):
        if self.is_start_time:
            self.parent.from_hour.config(text=f": {self.selected_time.strftime('%H:%M')}")
        else:
            self.parent.to_hour.config(text=f": {self.selected_time.strftime('%H:%M')}")
        self.destroy()

    def btn_Pre(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.pick_Hours()

    def btn_Next(self):
        max_pages = 4
        if self.page_index < max_pages - 1:
            self.page_index += 1
            self.pick_Hours()

    def pick_Hours(self):
        for widget in self.hour_frame.winfo_children():
            widget.destroy()
        # Calculate range of hours for the current page
        start_hour = self.page_index * self.hours_per_page
        end_hour = start_hour + self.hours_per_page

        for hour in range(start_hour, min(end_hour, 24)):
            current_time = datetime.combine(self.selected_date.date(), time(hour, 0))
            time_str = current_time.strftime("%H:%M")
            btn = ttkb.Button(
                self.hour_frame,
                text=time_str,
                command=lambda t=current_time: self.select_time(t),
                style="Custom.TButton",
                width=15
            )
            btn.pack(pady=2, padx=5)

class ActivityWindow(ttkb.Toplevel):
    def __init__(self, parent, selected_date):
        super().__init__(parent)
        self.title("Add Activity")
        self.geometry("900x650")
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
            text="Add Activity",
            style="Custom.TLabel",
            width=15
        ).pack(anchor=W)

        form_frame = ttkb.Frame(main_frame, style="secondary.TFrame")
        form_frame.pack(fill=X, anchor=N, pady=10)
        ttkb.Label(
            form_frame,
            text="Title",
            style="Custom.TLabel",
        ).pack(anchor=NW)
        self.ent_Title=ttkb.Entry(
            form_frame,
            bootstyle="info",
            width=40
        )
        self.ent_Title.pack(anchor=NW)

        ttkb.Label(form_frame,
            text="Description",
            style="Custom.TLabel",
        ).pack(anchor=NW)
        self.txt_description=ttkb.Text( 
            form_frame,
            height=3,        
            width=40,        
            wrap="word",     
            font=("Helvetica", 10)
        )
        self.txt_description.pack(anchor=NE,fill=BOTH)

        # Date and time display frame
        date_Frame = ttkb.Frame(form_frame, style="secondary.TFrame")
        date_Frame.pack(anchor=NE, fill=X, pady=20, padx=10)
        
        ttkb.Label(
            date_Frame,
            text="From:",
            style="Custom.TLabel",
            width=5
        ).pack(anchor=N, side=LEFT)        
        ttkb.Label(
            date_Frame,
            text=self.selected_date.strftime("%d %m %Y"),
            style="Custom.TLabel",
            width=10
        ).pack(anchor=N, side=LEFT)        
        self.from_hour = ttkb.Label(
            date_Frame,
            text="",
            style="Custom.TLabel",
            width=8
        )
        self.from_hour.pack(anchor=N, side=LEFT)        
        ttkb.Label(
            date_Frame,
            text="To:",
            style="Custom.TLabel",
            width=5
        ).pack(anchor=N, side=LEFT)        
        self.date_label = ttkb.Label(
            date_Frame,
            text="",
            style="Custom.TLabel",
            width=15
        )
        self.date_label.pack(anchor=N, side=LEFT)        
        self.to_hour = ttkb.Label(
            date_Frame,
            text="",
            style="Custom.TLabel",
            width=8
        )
        self.to_hour.pack(anchor=N, side=LEFT)

        pick_date_frame = ttkb.Frame(form_frame, style="secondary.TFrame")
        pick_date_frame.pack(anchor=N, fill=X, pady=10)
        
        ttkb.Button(
            pick_date_frame,
            text="Start Time",
            style="Custom.TButton",
            command=self.show_start_time_picker,
            width=10
        ).pack(anchor=N, side=LEFT, padx=5)
        
        ttkb.Button(
            pick_date_frame,
            text="End Time",
            style="Custom.TButton",
            command=self.show_end_time_picker,
            width=10
        ).pack(anchor=N, side=LEFT, padx=5)

        ttkb.Label(
            pick_date_frame,
            text="Year:",
            style="Custom.TLabel",
            width=6
        ).pack(anchor=N,side=LEFT)
        self.year_var = StringVar(value="2025")
        self.ent_year=ttkb.Entry(
            pick_date_frame,
            textvariable=self.year_var,
            font=("Helvetica", 10, "bold"),
            width=10,
        )
        self.ent_year.pack(anchor=N,side=LEFT)        
        ttkb.Label(
            pick_date_frame,
            text="Month:",
            style="Custom.TLabel",
            width=6
        ).pack(anchor=N,side=LEFT)
        self.month_var = StringVar(value=self.selected_date.strftime("%B"))

        self.days_n_months={"January":list(range(1,32)), "February":list(range(1, 30)), "March":list(range(1, 32)),
            "April":list(range(1, 31)), "May":list(range(1, 32)), "June":list(range(1, 31)), 
            "July":list(range(1, 32)), "August":list(range(1, 32)), "September":list(range(1, 31)),
            "October":list(range(1, 32)), "November":list(range(1, 31)), "December":list(range(1, 32))}

        self.ent_month=ttkb.Combobox(
            pick_date_frame,
            textvariable=self.month_var,
            font=("Helvetica", 10, "bold"),
            width=10,
            values=list(self.days_n_months.keys()),
            state="readonly"
        )
        self.ent_month.pack(anchor=N,side=LEFT)        
        ttkb.Label(
            pick_date_frame,
            text="Day:",
            style="Custom.TLabel",
            width=6
        ).pack(anchor=N,side=LEFT)
        self.day_var=StringVar(value=str(self.selected_date.day))
        self.num_days=self.days_n_months[self.month_var.get()]            
        self.ent_day=ttkb.Combobox(
            pick_date_frame,
            textvariable=self.day_var,
            font=("Helvetica", 10, "bold"),
            width=10,
            values=self.num_days,
            state="readonly"
        )
        self.ent_day.pack(anchor=N,side=LEFT)
        self.ent_day.bind("<<ComboboxSelected>>", self.update_date_label)
        ttkb.Label(
            pick_date_frame,
            text="hour:",
            style="Custom.TLabel",
            width=4
        ).pack(anchor=N,side=LEFT)

        recursive_frame=ttkb.Frame(form_frame,style="secondary.TFrame")
        recursive_frame.pack(anchor=N,pady=20,fill=X)
        self.recursive_var = StringVar(value="Daily")
        recursive_options = ["Daily", "Weekly", "Monthly", "Yearly"]
        for option in recursive_options:
            ttk.Radiobutton(
                recursive_frame,
                text=option,
                value=option,
                variable=self.recursive_var,
                bootstyle="primary-toolbutton"
            ).pack(side=LEFT, padx=5)        

        importance_frame=ttkb.Frame(form_frame,style="secondary.TFrame")
        importance_frame.pack(anchor=N,pady=20,fill=X)
        self.priority_var = StringVar(value="High")
        priorities = ["Low", "Medium", "High"]
        for priority in priorities:
            ttk.Radiobutton(
                importance_frame,
                text=priority,
                value=priority,
                variable=self.priority_var,
                bootstyle="primary-toolbutton"
            ).pack(side=LEFT, padx=5)

        color_frame=ttkb.Frame(form_frame,style="secondary.TFrame")
        color_frame.pack(anchor=N,pady=10,fill=X)
        ttkb.Label(
            color_frame,
            text="Event Color ",
            style="Custom.TLabel",
            width=15
        ).pack(side=LEFT)
        self.event_color_code=["#880892","#fd82da","#c70f24","#f1860e","#faef50","#61b30c","#63f689","#31e9fa","#2269f4","#6649e8"]
        self.event_color=["purple","pink","red","orange","yellow","green","darkgreen","lightblue","blue","darkblue",]
        self.style_list=list()
        for color,code in zip(self.event_color,self.event_color_code):
            stylename = f"{color}.TButton"
            self.style.configure(stylename, background=code)
            self.style_list.append(stylename)

        for code,style in zip(self.event_color_code,self.style_list):
            self.event_box=ttkb.Button(
                color_frame,
                command=lambda c=code: self.event_box_color(c),
                style=style,
                width=3
                )
            self.event_box.pack(side=LEFT,padx=5)
        ttkb.Button(
            color_frame,
            text="🐋",
            command=self.box_color,
            style="Custom.TButton"
        ).pack(side=LEFT)

        ttkb.Button(
            form_frame,
            text="Add Activity",
            command=self.btn_add,
            style="Custom.TButton",
            width=25
        ).pack(anchor=N,pady=20)

 # Update date label after all fields are created
        self.update_date_label()
 # Add trace callbacks to update date label when fields change
        self.year_var.trace_add("write", lambda *args: self.update_date_label())
        self.month_var.trace_add("write", lambda *args: self.update_date_label())
        self.day_var.trace_add("write", lambda *args: self.update_date_label())

    def show_start_time_picker(self):
        Time_Hour(self, self.selected_date, is_start_time=True).place_window_center()

    def show_end_time_picker(self):
        Time_Hour(self, self.selected_date, is_start_time=False).place_window_center()

    def btn_add(self):
        print(self.ent_year.get(), self.ent_month.get(), self.ent_day.get())
                
    def update_date_label(self):
        if hasattr(self, 'from_hour') and hasattr(self, 'to_hour'):
            self.date_label.config(text=f"{self.day_var.get()}-{self.month_var.get()}-{self.year_var.get()}")
        month=self.month_var.get()
        self.num_days=self.days_n_months[month]
        self.ent_day.config(values=self.num_days)

    def event_box_color(self,color):
        return color

    def box_color(self):
        box_Color=colorchooser.askcolor(title="box color")
        return box_Color[1]


    def add_activity(self):
        print("activity")
