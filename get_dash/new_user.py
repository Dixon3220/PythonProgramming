import pandas as pd
import random
import tkinter as tk
from tkinter import ttk


# read excel
expense = pd.read_excel(
    'expense.xlsx')  # [ignore this comment, only for testing] expense = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\expense.xlsx')
budget = pd.read_excel(
    'budget.xlsx')  # [ignore this comment, only for testing]  budget = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\\budget.xlsx')

# get information from the user, this could be changed in main, especially for month.
userid = str(random.random())

new_user = tk.Tk()
new_user.title('Main Menu')
new_user.geometry('500x300')

def addexp_success(date, amount, type, bud):
    global expense
    global budget

    expense = expense.append({'type': type, 'amount': amount, 'date': date, 'userId': userid}, ignore_index=True)
    budget = budget.append({'budget': bud, 'userId': userid}, ignore_index=True)
    expense['date'] = expense['date'].map(lambda x: str(x).split(' ')[0])
    budget.to_excel('budget.xlsx')
    expense.to_excel('expense.xlsx')

    s_window = tk.Toplevel(new_user)
    s_window.title('Success')
    s_window.geometry('250x150')
    success_label = tk.Label(s_window, text='Success!', font=('Arial', 15)).pack()
    btn_main = tk.Button(s_window, text='Main', width=10, command=new_user.destroy)
    btn_main.place(x=90, y=75)


# Title
add_title = tk.Label(new_user, text='Add First Expense', font=('Arial', 15))
add_title.place(x=170, y=40)

# new date
new_date = tk.StringVar()
date_label = tk.Label(new_user, text='Date: ')
date_label.place(x=130, y=100)
date_entry = tk.Entry(new_user, textvariable=new_date)
date_entry.place(x=180, y=100)

# new amount
add_amount = tk.IntVar()
amount_label = tk.Label(new_user, text='Amount: ')
amount_label.place(x=120, y=130)
amount_entry = tk.Entry(new_user, textvariable=add_amount)
amount_entry.place(x=180, y=130)

# Type
add_type = tk.StringVar()
types = ttk.Combobox(new_user, width=18, textvariable=add_type)
types['values'] = ('food', 'entertain', 'clothing', 'transport', 'study', 'others')
types.place(x=180, y=160)
type_label = tk.Label(new_user, text='Type: ')
type_label.place(x=130, y=160)

# budget
new_budget = tk.IntVar()
budget_label = tk.Label(new_user, text='Budget: ')
budget_label.place(x=120, y=190)
budegte_entry = tk.Entry(new_user, textvariable=new_budget)
budegte_entry.place(x=180, y=190)

# Confirm & back button
btn_add = tk.Button(new_user, text='Add', width=13, command=lambda: addexp_success(new_date.get(), add_amount.get(),\
                                                                                   add_type.get(), new_budget.get()))
btn_add.place(x=200, y=230)
btn_back = tk.Button(new_user, text='Back', width=13, command=new_user.destroy)
btn_back.place(x=20, y=20)

new_user.mainloop()

