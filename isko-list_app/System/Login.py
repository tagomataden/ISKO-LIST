from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def forget_pass():
    def change_password():
        if user_entry.get()=='' or new_entry.get()=='' or confirm_entry.get()=='':
            messagebox.showerror('Error', 'All Fields Are Required',parent=window)
        elif new_entry.get()!= confirm_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password Mismatch', parent=window)
        else:
            con=pymysql.connect(host='localhost', user='root', password='1234', database='userdata2')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error', 'Incorrect Username', parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query, (new_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is Reset, Please Login with the New Password', parent=window)
                window.destroy()



    window =  Toplevel()
    window.title('Change Password')

    bgPic= ImageTk.PhotoImage(file='system2.jpeg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label= Label(window, text='Iskolist', font=('yu gothic ui',24, 'bold'), bg='#f9f6f6', fg='#1d1e24')
    heading_label.place(x=710, y=95)

    heading_label2= Label(window, text='FORGET PASSWORD', font=('Arial',18, 'bold'), bg='#f9f6f6', fg='#970000')
    heading_label2.place(x=600, y=150)

    user_label= Label(window, text='Username', font=('yu gothic ui',18, 'bold'), bg='#f9f6f6', fg='#1d1e24')
    user_label.place(x=630, y=200)

    user_entry= Entry(window, width=25, font=('yu gothic ui',11, 'bold'), bg='#f9f6f6', fg='#1d1e24', bd=1)
    user_entry.place(x=630, y=250)

    new_label= Label(window, text='New Password', font=('yu gothic ui',18, 'bold'), bg='#f9f6f6', fg='#1d1e24')
    new_label.place(x=630, y=300)

    new_entry= Entry(window, width=25, font=('yu gothic ui',11, 'bold'), bg='#f9f6f6', fg='#1d1e24', bd=1)
    new_entry.place(x=630, y=350)

    confirm_label= Label(window, text='New Password', font=('yu gothic ui',18, 'bold'), bg='#f9f6f6', fg='#1d1e24')
    confirm_label.place(x=630, y=400)

    confirm_entry= Entry(window, width=25, font=('yu gothic ui',11, 'bold'), bg='#f9f6f6', fg='#1d1e24', bd=1)
    confirm_entry.place(x=630, y=450)

    submitButton = Button(window, text='Submit', font=('yu gothic ui', 13, 'bold'), fg='#f9f6f6', bg='#970000', activeforeground='#f9f6f6', activebackground='#970000', cursor='hand2', width=19, command=change_password)
    submitButton.place(x=630, y=500)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'All Fields Are Required')
    
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection is not established try again')
            return
        query='use userdata2'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error', 'Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'Login is Successful')
            login_window.destroy()
            import iskolist2


def signup_page():
    login_window.destroy()
    import Register

def email_enter(event):
    if usernameEntry.get()=='PUP EMAIL':
        usernameEntry.delete(0, END)

def pass_enter(event):
    if passwordEntry.get()=='PASSWORD':
        passwordEntry.delete(0, END)

def hide():
    showButton.config(file='hide.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    showButton.config(file='show.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)



login_window= Tk()
login_window.title('Login Page')
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
bgImage=ImageTk.PhotoImage(file='system2.jpeg')
bgLabel=Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

headingLabel=Label(login_window, text='Iskolist', font=('yu gothic ui',24, 'bold'), bg='#F9F6F6')
headingLabel.place(x=710, y=95)

usernameEntry = Entry(login_window, width=25, font=('yu gothic ui',11,'bold'), bd=0, bg='#F9F6F6')
usernameEntry.place(x=640, y=200)
usernameEntry.insert(0, 'PUP EMAIL')
usernameEntry.bind('<FocusIn>', email_enter)

usernameLine = Canvas(login_window, width=202, height=2.0, bg='#1D1E24', highlightthickness=1)
usernameLine.place(x=640, y=223)

passwordEntry = Entry(login_window, width=25, font=('yu gothic ui',11,'bold'), bd=0, bg='#F9F6F6',)
passwordEntry.place(x=640, y=260)
passwordEntry.insert(0, 'PASSWORD')
passwordEntry.bind('<FocusIn>', pass_enter)

passwordLine = Canvas(login_window, width=202, height=2.0, bg='#1D1E24', highlightthickness=1)
passwordLine.place(x=640, y=283)

showButton= PhotoImage(file='show.png')
eyeButton = Button(login_window, image=showButton, bd=0, bg='#F9F6F6', activebackground='#F9F6F6', cursor='hand2', command=hide)
eyeButton.place(x=820, y=255)

forgetButton = Button(login_window, text='Forget Password?', bd=0, bg='#F9F6F6', activebackground='#F9F6F6',cursor='hand2', font=('yu gothic ui', 11, 'bold',), fg='#00b2ff', command=forget_pass)
forgetButton.place(x=720, y=295)

loginButton = Button(login_window, text='Sign in', font=('yu gothic ui', 13, 'bold'), fg='#f9f6f6', bg='#970000', activeforeground='#f9f6f6', activebackground='#970000', cursor='hand2', width=19, command=login_user)
loginButton.place(x=640, y=350)

signupLabel=Label(login_window, text='Dont have an account?', font=('yu gothic ui',9, 'bold'), bg='#F9F6F6')
signupLabel.place(x=640, y=400)

newaccountButton = Button(login_window, text='Sign up now', font=('yu gothic ui', 9, 'underline bold'), fg='#00b2ff', bg='#f9f6f6', activebackground='#f9f6f6', cursor='hand2',bd=0, command=signup_page)
newaccountButton.place(x=770, y=400)

login_window.mainloop()