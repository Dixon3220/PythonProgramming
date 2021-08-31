import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import pickle
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame


#main menu
main = tk.Tk()
main.title('Main Menu')
main.geometry('700x500')

#Textbox1 to diaplay information
textbox1 = tk.Text(main, height = 7, width = 30)
textbox1.place(x=200, y=30)

#Textbox2 to display information
textbox2 = tk.Text(main, height = 7, width = 30)
textbox2.place(x=450, y=30)
    
#Display today's date
today = date.today()
today_date = tk.Label(main,text= 'Today: '+ str(today),font= ("Arial",13))
today_date.place(x=10,y=20)

#Display logo
logo = tk.Canvas(main, height=70,width=70) #change size of logo
image_file = tk.PhotoImage(file='normal.gif') #change our logo here
image = logo.create_image(0,0, anchor='nw',image=image_file)
logo.place(x=50,y=50)


#Plot bar charts
data1 = {'Country': ['US','CA','GER','UK','FR'], #data example
         'GDP_Per_Capita': [45000,42000,52000,49000,47000]
        }
df1 = DataFrame(data1,columns=['Country','GDP_Per_Capita']) #data example

figure1 = plt.Figure(figsize=(4.5,3), dpi=80)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, main)
bar1.get_tk_widget().place(x=330,y=180)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')



#plot pie charts
stockListExp = ['AMZN' , 'AAPL', 'JETS', 'CCL', 'NCLH'] #testing data
stockSplitExp = [15,25,40,10,10] 

fig = Figure(figsize=(3,2.4)) # create a figure object
ax = fig.add_subplot(111) # add an Axes to the figure

ax.pie(stockSplitExp, radius=1.2, labels=stockListExp,autopct='%0.2f%%', shadow=True,)

chart1 = FigureCanvasTkAgg(fig,main)
chart1.get_tk_widget().place(x=0,y=180)




#Change budget interface
def change_budget():

    def change_success():
        
        c_window = tk.Toplevel(budget_window)
        c_window.title('Success')
        c_window.geometry('150x150')
        change_label = tk.Label(c_window, text='Success!',font=('Arial', 15)).pack()
        btn_main = tk.Button(c_window, text='Main',width= 10,command= budget_window.destroy)
        btn_main.place(x= 30, y= 50)       



    budget_window = tk.Toplevel(main)
    budget_window.title('Change Budget')
    budget_window.geometry('500x300')

    new_budget = tk.IntVar() 
    budget_title = tk.Label(budget_window, text='Change Your Budget', font=('Arial', 15))
    budget_title.place(x= 160, y =80)
    budget_label = tk.Label(budget_window, text='Budget: ')
    budget_label.place(x= 150, y =120)
    budegte_entry = tk.Entry(budget_window, textvariable=new_budget)
    budegte_entry.place(x= 200, y =120)

    #Confirm & back button
    btn_confirm_budget = tk.Button(budget_window, text='Confirm',width= 13,command=change_success)
    btn_confirm_budget.place(x=220, y =150)
    btn_back = tk.Button(budget_window, text='Back',width= 13,command = budget_window.destroy)
    btn_back.place(x=20,y=20)




# Add new expenses
def add_expenses():

    
    def addexp_success():
        
        s_window = tk.Toplevel(add_window)
        s_window.title('Success')
        s_window.geometry('250x150')
        success_label = tk.Label(s_window, text='Success!',font=('Arial', 15)).pack()
        btn_main = tk.Button(s_window, text='Main',width= 10,command= add_window.destroy)
        btn_main.place(x= 40, y =75)
        btn_addmore = tk.Button(s_window, text='Add More',width= 10,command= s_window.destroy)
        btn_addmore.place(x=140,y=75)

                

    add_window = tk.Toplevel(main)
    add_window.title('Add Expenses')
    add_window.geometry('500x300')

    #Title 
    add_title = tk.Label(add_window, text='Add New Expense', font=('Arial', 15))
    add_title.place(x= 170, y =50)

    #new date
    new_date = tk.StringVar()     
    date_label = tk.Label(add_window, text='Date: ')
    date_label.place(x= 130, y =120)
    date_entry = tk.Entry(add_window, textvariable=new_date)
    date_entry.place(x= 180, y =120)

    #new amount
    amount = tk.IntVar()     
    amount_label = tk.Label(add_window, text='Amount: ')
    amount_label.place(x= 120, y =150)
    amount_entry = tk.Entry(add_window, textvariable= amount)
    amount_entry.place(x= 180, y =150)

    #Type
    add_type = tk.StringVar()
    types = ttk.Combobox(add_window, width= 18, textvariable = add_type)
    types['values'] = ('Food', 'Entertainment', 'Rent','Transportation','Others')
    types.place(x= 180, y =180)
    type_label = tk.Label(add_window, text='Type: ')
    type_label.place(x= 130, y =180)
    

    #Confirm & back button
    btn_add = tk.Button(add_window, text='Add',width= 13,command= addexp_success)
    btn_add.place(x=200, y =230)
    btn_back = tk.Button(add_window, text='Back',width= 13,command= add_window.destroy)
    btn_back.place(x=20,y=20)
    




#Log out Function
def logout():
    msgBox =tk.messagebox.askquestion("Log out", "Do you wish to Log out?")
    if msgBox == 'yes':
        tk.messagebox.showinfo("Thank you", "See you Again!")
        main.destroy()




#All the functions buttons
logout_button = tk.Button(main,text="Log out",width= 13,command = logout) #add command for the function
logout_button.place(x=550, y=450)

change_button = tk.Button(main,text="Change Budget",width= 13, command =change_budget)
change_button.place(x=400, y=450)

detail_button = tk.Button(main,text="Details",width= 13)
detail_button.place(x=250, y=450)

add_button = tk.Button(main,text="Add",width= 13,command = add_expenses)
add_button.place(x=100, y=450)
main.mainloop()


