import tkinter as tk
import tkinter.messagebox
import pickle
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame


#main menu
main = tk.Tk()
main.title('Main Menu')
main.geometry('700x500')

#Textbox1
textbox1 = tk.Text(main, height = 7, width = 30)
#textbox1.insert()
textbox1.place(x=200, y=30)

#Textbox2
textbox2 = tk.Text(main, height = 7, width = 30)
#textbox2.insert()
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

figure1 = plt.Figure(figsize=(5,3), dpi=80)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, main)
bar1.get_tk_widget().place(x=300,y=180)
df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Country Vs. GDP Per Capita')




#all the functions buttons
logout_button = tk.Button(main,text="Log out",width= 13) #add command for the function
logout_button.place(x=550, y=450)

change_button = tk.Button(main,text="Change Budget",width= 13)
change_button.place(x=400, y=450)

detail_button = tk.Button(main,text="Details",width= 13)
detail_button.place(x=250, y=450)

add_button = tk.Button(main,text="Add",width= 13)
add_button.place(x=100, y=450)
main.mainloop()


