import tkinter as tk
import tkinter.messagebox
import pickle
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from pandas import DataFrame


def get_info(userid):
    # read excel
    expense = pd.read_excel('expense.xlsx')  # [ignore this comment, only for testing] expense = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\expense.xlsx')
    budget  = pd.read_excel('budget.xlsx')   # [ignore this comment, only for testing]  budget = pd.read_excel('D:\Python\Python_Programming\project\coding\PythonProgramming\get_dash\\budget.xlsx')
    # get this user's expense and budget
    user_expense = expense[(expense['userId'] == userid)].drop(['userId'], axis=1, inplace=False)
    user_budget  = budget [(budget ['userId'] == userid)].drop(['userId'], axis=1, inplace=False)
    return user_expense, user_budget


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

def show_date(main, today):
    # Textbox1
    textbox1 = tk.Text(main, height=7, width=30)
    # textbox1.insert()
    textbox1.place(x=200, y=30)

    # Textbox2
    textbox2 = tk.Text(main, height=7, width=30)
    # textbox2.insert()
    textbox2.place(x=450, y=30)

    # Display today's date
    today_date = tk.Label(main, text='Today: ' + str(today), font=("Arial", 13))
    today_date.place(x=10, y=20)

    # Display logo
    logo = tk.Canvas(main, height=70, width=70) #change size of logo
    image_file = tk.PhotoImage(file='normal.gif') #change our logo here
    image = logo.create_image(0, 0, anchor='nw', image=image_file)
    logo.place(x=50, y=50)

    # all the functions buttons
    logout_button = tk.Button(main, text="Log out", width=13)  # add command for the function
    logout_button.place(x=550, y=450)

    change_button = tk.Button(main, text="Change Budget", width=13)
    change_button.place(x=400, y=450)

    detail_button = tk.Button(main, text="Details", width=13)
    detail_button.place(x=250, y=450)

    add_button = tk.Button(main, text="Add", width=13)
    add_button.place(x=100, y=450)


def show_today_exp(main, user_expense, day):
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


def show_month_exp(main, user_expense, day):
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


def main():
    # get information from the user, this could be changed in main, especially for month.
    today = date.today()
    today = '2021-08-30'               # testing value
    month = str(today).split('-')[1]
    userid = 'Dixon3220'

    # get the data required
    user_expense, user_budget = get_info(userid)

    # need some output if userid is not in excel or user_expense is empty, better read as an independent function!!!

    # main menu
    main = tk.Tk()
    main.title('Main Menu')
    main.geometry('700x500')
    show_date(main, str(today))
    show_today_exp(main, user_expense, str(today))
    main.mainloop()

if __name__ == "__main__":
    main()