from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)



def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
         messagebox.showerror('Error', 'Password Mismatch')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return
        try:
            query='create database userdata2'
            mycursor.execute(query)
            query='use userdata2'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata2')
        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error', 'Username Already Exist')
        
        else:
            query='insert into data (email, username, password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            signup_window.destroy()
            import Login









def login_page():
    signup_window.destroy()
    import Login

signup_window = Tk()
signup_window.title('Signup Page')
signup_window.resizable(False, False)
background=ImageTk.PhotoImage(file='system2.jpeg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame=Frame(signup_window, bg='#F9F6F6')
frame.place(x=695, y=85)

heading=Label(frame, text='Iskolist', font=('yu gothic ui',24, 'bold'), bg='#F9F6F6', fg='#1D1E24')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame, text='PUP EMAIL', font=('yu gothic ui', 13, 'bold'),bg='#F9F6F6',fg='#1D1E24')
emailLabel.grid(row=1, column=0,padx=25,sticky='w',pady=(10,0))

emailEntry=Entry(frame, width=25, font=('yu gothic ui', 13, 'bold'),fg='#1D1E24',bg='#F9F6F6')
emailEntry.grid(row=2,column=0,padx=25)

usernameLabel=Label(frame, text='Username', font=('yu gothic ui', 13, 'bold'),bg='#F9F6F6',fg='#1D1E24')
usernameLabel.grid(row=3, column=0,padx=25,sticky='w',pady=(10,0))

usernameEntry=Entry(frame, width=25, font=('yu gothic ui', 13, 'bold'),fg='#1D1E24',bg='#F9F6F6')
usernameEntry.grid(row=4,column=0,padx=25)

passwordLabel=Label(frame, text='Password', font=('yu gothic ui', 13, 'bold'),bg='#F9F6F6',fg='#1D1E24')
passwordLabel.grid(row=5, column=0,padx=25,sticky='w',pady=(10,0))

passwordEntry=Entry(frame, width=25, font=('yu gothic ui', 13, 'bold'),fg='#1D1E24',bg='#F9F6F6')
passwordEntry.grid(row=6,column=0,padx=25)

confirmLabel=Label(frame, text='Confirm Password', font=('yu gothic ui', 13, 'bold'),bg='#F9F6F6',fg='#1D1E24')
confirmLabel.grid(row=7, column=0,padx=25,sticky='w',pady=(10,0))

confirmEntry=Entry(frame, width=25, font=('yu gothic ui', 13, 'bold'),fg='#1D1E24',bg='#F9F6F6')
confirmEntry.grid(row=8,column=0,padx=25)

signupButton=Button(frame,text='Sign Up', font=('yu gothic ui', 16, 'bold'), bd=0, bg='#970000',fg='#1D1E24', activebackground='#970000', activeforeground='#1D1E24', width=17, command=connect_database)
signupButton.grid(row=9,column=0, pady=20)

alreadyaccount=Label(frame, text='Already have an account?',font=('yu gothic ui', 9, 'bold'), bd=0, bg='#F9F6F6',fg='#1D1E24')
alreadyaccount.grid (row=10, column=0, sticky='w',padx=35, pady=0)

loginButton=Button(frame,text='Log in', font=('yu gothic ui', 9, 'bold underline'), bd=0, bg='#F9F6F6',fg='#00B2FF', activebackground='#F9F6F6', activeforeground='#00b2ff',cursor='hand2', command=login_page )
loginButton.place(x=175, y=422)

signup_window.mainloop()