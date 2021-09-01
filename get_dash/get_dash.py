import pandas as pd
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import pickle
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame


main = tk.Tk()
main.title('Main Menu')
main.geometry('700x500')
# read excel
expense = pd.read_excel('expense.xlsx')  # [ignore this comment, only for testing] expense = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\expense.xlsx')
budget  = pd.read_excel('budget.xlsx')   # [ignore this comment, only for testing]  budget = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\\budget.xlsx')


# get information from the user, this could be changed in main, especially for month.
today = date.today()
today = '2021-08-30'               # testing value
month = str(today).split('-')[1]
userid = 'Dixon3220'

# get the data required
user_expense = expense[(expense['userId'] == userid)].drop(['userId'], axis=1, inplace=False)
user_budget  = budget [(budget ['userId'] == userid)].drop(['userId'], axis=1, inplace=False)


def get_today_data(user_expense, day):
    # get user's expense on this day
    today_data = user_expense[(user_expense['date'] == str(day))]
    return today_data


def get_month_data(user_expense, day):
    # get user's expense in this month
    year, month = day.split('-')[0], day.split('-')[1]
    index = [int(str(x).split('-')[1]) == int(month) for x in user_expense['date'] if int(str(x).split('-')[0]) == int(year)]
    month_data = user_expense[index]
    return month_data


def get_year_data(user_expense, day):
    # get user's expense in this year
    year= day.split('-')[0]
    index = [int(str(x).split('-')[0]) == int(year) for x in user_expense['date']]
    year_data = user_expense[index]
    return year_data


def get_plot_data(User_expense, day, flag):
    # get data for the pie chart
    # flag = 'day' means getting data for this day, flag = 'month' means getting data for month containing this day
    if flag == 'day':
        user_expense = get_today_data(User_expense, day)
    else:
        user_expense = get_month_data(User_expense, day)
    type_all = user_expense['type']
    type_name = type_all[type_all.duplicated(keep='first') == False]
    pie = {}
    for key in type_name:
        user_expense_type = user_expense[(user_expense['type'] == str(key))]
        pie[key] = sum([float(amount) for amount in user_expense_type['amount']])

    # get data for the bar chart
    # flag = 'day' means getting bar chart data for this month, flag = 'month' means getting data for this year
    if flag == 'day':
        user_expense = get_month_data(User_expense, day)
        thedate = user_expense['date']
        date_name = thedate[thedate.duplicated(keep='first') == False]
        bar = {}
        for key1 in date_name:
            user_expense_day = user_expense[(user_expense['date'] == str(key1))]
            bar[key1] = sum([float(amount) for amount in user_expense_day['amount']])
    else:
        user_expense = get_year_data(User_expense, day)
        month_name = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Sep', 11:'Nov', 12:'Dec'}
        bar = {}
        for thismonth in range(12):
            index = [int(str(x).split('-')[1]) == thismonth for x in user_expense['date']]
            if not True in index:
                bar[month_name[thismonth]] = 0
            else:
                user_expense_month = user_expense[index]
                bar[month_name[thismonth]] = sum([float(amount) for amount in user_expense_month['amount']])

    return pie, bar


def show_date(today):
    # get data
    today_data = get_today_data(user_expense, today)
    today_total = sum(today_data['amount'])
    today_budget = 100                                                    # need to update
    month_budget = 100                                                    # need to update
    month_names = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', \
                   9: 'September', 10: 'September', 11: 'November', 12: 'December'}
    month_data = get_month_data(user_expense, today)
    month_total = sum(month_data['amount'])
    month_name = month_names[int(today.split('-')[1])]

    # Textbox1
    today_label = tk.Label(main, text='Today', font=('Arial', 13))
    today_label.place(x=305, y=20)

    textbox1 = tk.Text(main, height=4, width=30, font=("Arial", 10))
    textbox1.insert("1.0", "Spend:  $" + str(today_total) + "\n")
    textbox1.insert("2.0", "Budget:  $" + str(today_budget) + "\n")
    textbox1.insert("3.0", "\n")
    if today_total > today_budget:
        textbox1.insert("4.0", "Over budget! Please be careful!\n")
    else:
        textbox1.insert("4.0", "Good job! Keep working!\n")

    textbox1.place(x=220, y=50)

    # Textbox2
    today_label = tk.Label(main, text=month_name, font=('Arial', 13))
    today_label.place(x=530, y=20)

    textbox2 = tk.Text(main, height=4, width=30, font=("Arial", 10))
    textbox2.insert("1.0", "Spend:  $" + str(month_total)+ "\n")
    textbox2.insert("2.0", "Budget:  $" + str(month_budget)+ "\n")
    textbox2.insert("3.0", "\n")
    if month_total > month_budget:
        textbox2.insert("4.0", "Over budget! Please be careful!\n")
    else:
        textbox2.insert("4.0", "Good job! Keep working!\n")
    textbox2.place(x=450, y=50)

    # Display today's date
    today_date = tk.Label(main, text='Today: ' + str(today), font=("Arial", 13))
    today_date.place(x=10, y=20)

    # Display logo
    logo = tk.Canvas(main, height=70, width=70) #change size of logo
    image_file = tk.PhotoImage(file='normal.gif') #change our logo here
    image = logo.create_image(0, 0, anchor='nw', image=image_file)
    logo.place(x=50, y=50)

    # all the functions buttons
    logout_button = tk.Button(main, text="Log out", width=13, command=logout)  # add command for the function
    logout_button.place(x=550, y=450)

    change_button = tk.Button(main, text="Change Budget", width=13, command=change_budget)
    change_button.place(x=400, y=450)

    detail_button = tk.Button(main, text="Details", width=13, command=check_detail)
    detail_button.place(x=250, y=450)

    add_button = tk.Button(main, text="Add", width=13, command=add_expenses)
    add_button.place(x=100, y=450)

    # optionlist
    option_list = ['Week', 'Month', 'Year']
    value_inside1 = tk.StringVar()
    date_menu1 = tk.OptionMenu(main, value_inside1, *option_list)
    date_menu1.place(x=500, y=140)
    value_inside2 = tk.StringVar()
    date_menu2 = tk.OptionMenu(main, value_inside2, *option_list)
    date_menu2.place(x=600, y=140)


def show_today_exp(user_expense, day):
    # Plot bar charts
    pie, bar = get_plot_data(user_expense, day, 'day')
    bar_keys = [x for x in bar.keys()]
    bar_values = [y for y in bar.values()]

    data1 = {'Date': bar_keys,
             'Expense': bar_values
             }
    df1 = DataFrame(data1, columns=['Date', 'Expense'])
    figure1 = plt.Figure(figsize=(5, 3), dpi=80)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, main)
    bar1.get_tk_widget().place(x=300, y=180)
    df1 = df1[['Date', 'Expense']].groupby('Date').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Date Vs. Expense')

    # Plot pie charts
    fig = Figure(figsize=(3, 2.4))  # create a figure object
    ax = fig.add_subplot(111)  # add an Axes to the figure
    ax.pie(pie.values(), radius=1.2, labels=pie.keys(), autopct='%0.2f%%', shadow=True, )
    chart1 = FigureCanvasTkAgg(fig, main)
    chart1.get_tk_widget().place(x=0, y=180)


def show_month_exp(user_expense, day):
    # Plot bar charts
    pie, bar = get_plot_data(user_expense, day, 'month')
    bar_keys = [x for x in bar.keys()]
    bar_values = [y for y in bar.values()]

    data1 = {'Date': bar_keys,
             'Expense': bar_values
             }
    df1 = DataFrame(data1, columns=['Months', 'Expense'])
    figure1 = plt.Figure(figsize=(5, 3), dpi=80)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, main)
    bar1.get_tk_widget().place(x=300, y=180)
    df1 = df1[['Months', 'Expense']].groupby('Months').sum()
    df1 = df1[bar_keys].groupby('Months').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('Months Vs. Expense')


# Change budget interface
def change_budget():
    def change_success():
        c_window = tk.Toplevel(budget_window)
        c_window.title('Success')
        c_window.geometry('150x150')
        change_label = tk.Label(c_window, text='Success!', font=('Arial', 15)).pack()
        btn_main = tk.Button(c_window, text='Main', width=10, command=budget_window.destroy)
        btn_main.place(x=30, y=50)

    budget_window = tk.Toplevel(main)
    budget_window.title('Change Budget')
    budget_window.geometry('500x300')

    new_budget = tk.IntVar()
    budget_title = tk.Label(budget_window, text='Change Your Budget', font=('Arial', 15))
    budget_title.place(x=160, y=80)
    budget_label = tk.Label(budget_window, text='Budget: ')
    budget_label.place(x=150, y=120)
    budegte_entry = tk.Entry(budget_window, textvariable=new_budget)
    budegte_entry.place(x=200, y=120)

    # Confirm & back button
    btn_confirm_budget = tk.Button(budget_window, text='Confirm', width=13, command=change_success)
    btn_confirm_budget.place(x=220, y=150)
    btn_back = tk.Button(budget_window, text='Back', width=13, command=budget_window.destroy)
    btn_back.place(x=20, y=20)


def check_detail():

    def checkdetail_editdetail():
        #tList.delete(ACTIVE)
        s_window = tk.Toplevel(detail_window)
        s_window.title('Edit')
        s_window.geometry('400x250')
        edit_label = tk.Label(s_window, text='Edit', font=('Arial', 15))
        edit_label.place(x=185, y=20)
        # new amount
        edit_amount = tk.IntVar()
        edit_amount_label = tk.Label(s_window, text='Amount: ')
        edit_amount_label.place(x=90, y=75)
        edit_amount_entry = tk.Entry(s_window, textvariable=edit_amount)
        edit_amount_entry.place(x=160, y=75)
        # Type
        edit_type = tk.StringVar()
        edit_types = ttk.Combobox(s_window, width=18, textvariable=edit_type)
        edit_types['values'] = ('Food', 'Entertainment', 'Rent', 'Transportation', 'Others')
        edit_types.place(x=160, y=135)
        edit_type_label = tk.Label(s_window, text='Type: ')
        edit_type_label.place(x=90, y=135)
        # button
        btn_yes = tk.Button(s_window, text='Cancel', width=10, command=s_window.destroy)
        btn_yes.place(x=120, y=200)
        btn_no = tk.Button(s_window, text='Confirm', width=10, command=s_window.destroy)
        btn_no.place(x=220, y=200)

    def checkdetail_removedetail():
        #tList.delete()
        s_window = tk.Toplevel(detail_window)
        s_window.title('Remove')
        s_window.geometry('250x150')
        remove_label = tk.Label(s_window, text='Remove?', font=('Arial', 15))
        remove_label.place(x=88, y=20)
        btn_yes = tk.Button(s_window, text='Yes', width=10, command=s_window.destroy)
        btn_yes.place(x=40, y=75)
        btn_no = tk.Button(s_window, text='No', width=10, command=s_window.destroy)
        btn_no.place(x=140, y=75)

    detail_window = tk.Toplevel(main)
    detail_window.title('Check Details')
    detail_window.geometry('500x340')

    # Title
    detail_title = tk.Label(detail_window, text='Check Details', font=('Arial', 15))
    detail_title.place(x=185, y=20)

    # Date
    detail_date_type = tk.StringVar()
    detail_date = ttk.Combobox(detail_window, width=8, textvariable=detail_date_type)
    detail_date['values'] = tuple((x,) for x in user_expense['date'])
    detail_date.place(x=380, y=60)
    days_label = tk.Label(detail_window, text='Date: ')
    days_label.place(x=340, y=60)

    # Detail Expense
    today_data = get_today_data(user_expense, today)
    #detail_expense = tk.Tk()
    # scrollbar
    tScroll = tk.Scrollbar(detail_window, orient=tk.VERTICAL)
    tScroll.place(x=445, y=110, height=140)
    # list box
    tList = tk.Listbox(detail_window, selectmode=tk.BROWSE, yscrollcommand=tScroll.set, font=('Arial', 12))
    tList.place(x=80, y=110, width=360, height=140)
    for row in range(today_data.shape[0]):
        text = today_data.iloc[row]
        tList.insert(tk.END, "(" + str(row+1) + ")  Type: " + text['type'] + ",  Amount: " + str(text['amount']))
    tScroll.config(command=tList.yview)
    # edit button
    teditbutton = tk.Button(detail_window, text='edit', command=checkdetail_editdetail)
    teditbutton.place(x=130, y=280, width=100)
    # remove button
    tremovebutton = tk.Button(detail_window, text='remove', command=checkdetail_removedetail)
    tremovebutton.place(x=280, y=280, width=100)


    # back button
    btn_back = tk.Button(detail_window, text='Back', width=13, command=detail_window.destroy)
    btn_back.place(x=20, y=20)


# Add new expenses
def add_expenses():

    def addexp_success():
        s_window = tk.Toplevel(add_window)
        s_window.title('Success')
        s_window.geometry('250x150')
        success_label = tk.Label(s_window, text='Success!', font=('Arial', 15)).pack()
        btn_main = tk.Button(s_window, text='Main', width=10, command=add_window.destroy)
        btn_main.place(x=40, y=75)
        btn_addmore = tk.Button(s_window, text='Add More', width=10, command=s_window.destroy)
        btn_addmore.place(x=140, y=75)

    add_window = tk.Toplevel(main)
    add_window.title('Add Expenses')
    add_window.geometry('500x300')

    # Title
    add_title = tk.Label(add_window, text='Add New Expense', font=('Arial', 15))
    add_title.place(x=170, y=50)

    # new date
    new_date = tk.StringVar()
    date_label = tk.Label(add_window, text='Date: ')
    date_label.place(x=130, y=120)
    date_entry = tk.Entry(add_window, textvariable=new_date)
    date_entry.place(x=180, y=120)

    # new amount
    amount = tk.IntVar()
    amount_label = tk.Label(add_window, text='Amount: ')
    amount_label.place(x=120, y=150)
    amount_entry = tk.Entry(add_window, textvariable=amount)
    amount_entry.place(x=180, y=150)

    # Type
    add_type = tk.StringVar()
    types = ttk.Combobox(add_window, width=18, textvariable=add_type)
    types['values'] = ('Food', 'Entertainment', 'Rent', 'Transportation', 'Others')
    types.place(x=180, y=180)
    type_label = tk.Label(add_window, text='Type: ')
    type_label.place(x=130, y=180)

    # Confirm & back button
    btn_add = tk.Button(add_window, text='Add', width=13, command=addexp_success)
    btn_add.place(x=200, y=230)
    btn_back = tk.Button(add_window, text='Back', width=13, command=add_window.destroy)
    btn_back.place(x=20, y=20)


# Log out Function
def logout():
    msgBox = tk.messagebox.askquestion("Log out", "Do you wish to Log out?")
    if msgBox == 'yes':
        tk.messagebox.showinfo("Thank you", "See you Again!")
        main.destroy()



show_date(str(today))
show_today_exp(user_expense, str(today))

main.mainloop()