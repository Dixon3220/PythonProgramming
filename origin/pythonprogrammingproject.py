# Bug Solved

import tkinter as tk
import tkinter.messagebox
import pickle

def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get() 
    
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        # if cannot find the user, creat a file with a Admin 'python'
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'python': 'python'}
            pickle.dump(usrs_info, usr_file)
            usr_file.close()  
 
    # See whether the username match in the file
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tkinter.messagebox.showinfo(message='Welcome back! ' + usr_name)
        # if username match while password wrong
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again.')
    else:  # if cannot find the username in file 
        is_sign_up = tkinter.messagebox.askyesno('Hi there./n', 'You have not sign up yet. Please sign up')
        # ask for sign up
        if is_sign_up:
            usr_sign_up()

# Sign up
def usr_sign_up():
    
    def sign_to_python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            # if cannot find the user, creat a file with a Admin 'python'
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'python': 'python'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()  
        
        # If username already exit in the file 
        if nn in exist_usr_info:
            tkinter.messagebox.showerror('Error', 'You has already signed up!')
 
        elif np != npf:
            tkinter.messagebox.showerror('Error', 'Password and confirm password must be the same!')
 
        else:
            if len(np) > 15:
                tkinter.messagebox.showerror('Error', 'Password must be less than 15 characters!')
            elif len(np) < 3:
                tkinter.messagebox.showerror('Error', 'Password must be more than 3 characters')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                    tkinter.messagebox.showinfo('Welcome', 'You have successfully signed up!')
                    window_sign_up.destroy()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x300')
    window_sign_up.title('Sign up window')
 
    new_name = tk.StringVar() 
    usr_sign = tk.Label(window_sign_up, text='Username')
    usr_sign.pack()
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.pack()
 
    new_pwd = tk.StringVar()
    pwd_sign = tk.Label(window_sign_up, text='Password')
    pwd_sign.pack()
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.pack()
 
    new_pwd_confirm = tk.StringVar()
    confirm_sign = tk.Label(window_sign_up, text='Confirm Password')
    confirm_sign.pack()
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.pack()
 
    btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_python)
    btn_confirm_sign_up.pack()

window = tk.Tk()
window.title('Python Expenses Recorder')
window.geometry('500x300')  

welcome_lable = tk.Label(window, text='\n\nWelcome to Python Expenses Recorder!\n')
welcome_lable.pack()
 

# Uesername
usr_lable = tk.Label(window, text='Username')
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window, 
                          textvariable=var_usr_name, font=('Arial', 14))
usr_lable.pack()
entry_usr_name.pack()

# Password
pwd_lable = tk.Label(window, text='Password')
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, 
                         textvariable=var_usr_pwd, font=('Arial', 14), show='*')
pwd_lable.pack()
entry_usr_pwd.pack() 

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.pack()
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.pack()

window.mainloop()