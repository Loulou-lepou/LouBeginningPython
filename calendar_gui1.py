from tkinter import *
import calendar


# functions for displaying calendar
def show():
    month_ = int(spinbox_month.get())
    year_ = int(spinbox_year.get())
    calendar_ = calendar.month(year_, month_,2, 1)
    print(calendar_)
    text_calendar.delete(0.0, END)
    text_calendar.insert(INSERT, calendar_)


def clear():
    text_calendar.delete(1.0, 'end')


# create main window
root = Tk()
root.title("Calendar")
root.geometry("260x180")
root.resizable(1, 1)

# create widgets
label_month = Label(root, text="Month", font=('arial', 13, 'bold'), fg="brown")
label_month.place(x=15, y=0)

spinbox_month = Spinbox(root, from_=1, to=12, width="3", fg="brown")
spinbox_month.place(x=60, y=0)

label_year = Label(root, text="Year", font=('arial', 13, 'bold'), fg="brown")
label_year.place(x=130, y=0)

spinbox_year = Spinbox(root, from_=1999, to=2100, width="6")
spinbox_year.place(x=170, y=0)

text_calendar = Text(root, width=28, height=8)
text_calendar.place(x=32, y=30)

button_show = Button(root,
                     text="Show",
                     font=('arial', 13, 'bold'), fg="brown",
                     command=show)
button_show.place(x=40, y=150)

button_clear = Button(root,
                      text="Clear",
                      font=('arial', 13, 'bold'), fg="brown",
                      command=clear)
button_clear.place(x=100, y=150)

root.mainloop()
