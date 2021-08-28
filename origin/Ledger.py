import openpyxl
from openpyxl import Workbook
import datetime
from tkinter import messagebox
from tkinter import *
import os


jzr = Tk()


jzr.title('Ledger')
jzr.geometry('300x120+700+300')
label1 = Label(jzr, text='Types of consumption:', font=('Microsoft Yahei', 10), fg='green')
label1.grid(row=0, column=0)
label2 = Label(jzr, text='Consumption amount:', font=('Microsoft Yahei', 10), fg='green')
label2.grid(row=1, column=0)
Entry1 = Entry(jzr, font=('Microsoft Yahei', 12), width=16)
Entry1.grid(row=0, column=1)
Entry2 = Entry(jzr, font=('Microsoft Yahei', 12), width=16)
Entry2.grid(row=1, column=1)


def jzcx():
    con1 = Entry1.get()
    con1 = con1.strip()
    con2 = Entry2.get()
    con2 = con2.strip()
    if con1 == '':
        messagebox.showinfo('Prompt', message='Please enter the consumption type')
    elif con2 == '':
        messagebox.showinfo('Prompt', message='Please enter the consumption amount')
    else:
        if os.path.exists('Ledger.xlsx'):
            filepath = 'Ledger.xlsx'
            zb = openpyxl.load_workbook(filepath)
            xf = zb.active
            a = datetime.datetime.now()
            b = Entry1.get()
            c = Entry2.get()
            xf.append([a, b, c])
            xf.column_dimensions['A'].width = 20
            zb.save('Ledger.xlsx')
            messagebox.showinfo('Prompt', message='Consumption data has been recorded')
            jzr.quit()
        else:
            zb = openpyxl.Workbook()
            xf = zb.active
            xf['A1'] = 'Date'
            xf['B1'] = 'Types of consumption'
            xf['C1'] = 'Consumption amount'
            a = datetime.datetime.now()
            b = Entry1.get()
            c = Entry2.get()
            xf.append([a, b, c])
            xf.column_dimensions['A'].width = 20
            zb.save('Ledger.xlsx')
            messagebox.showinfo('Prompt', message='Consumption data has been recorded')
            jzr.quit()


Button1 = Button(jzr, text='Record data', font=('Microsoft Yahei', 10), width=12, command=jzcx)
Button1.grid(row=3, column=0, sticky=W)
Button2 = Button(jzr, text='Exit', font=('Microsoft Yahei', 10), width=8, command=jzr.quit)
Button2.grid(row=3, column=1, sticky=E)
jzr.mainloop()