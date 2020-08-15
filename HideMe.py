from tkinter.filedialog import *
from tkinter import messagebox
from tkinter import messagebox as ms
from stegano import exifHeader as stg
import webbrowser
import sqlite3

new = 1
url = "https://www.gmail.com"


def OpenWeb():
    webbrowser.open(url, new=new)


with sqlite3.connect('Records.db') as db:
    c = db.cursor()

c.execute(
    'CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL, Email TEXT NO NULL, Phone_no TEXT NOT NULL);')
db.commit()
db.close()


def encode():
    enc = Tk()
    enc.title("Encode")
    enc.geometry("500x400+300+150")

    Label(enc, text="K-Encode", bg="gray", width="300", height="3", font=("Caliber", 13)).pack()
    label1 = Label(enc, text="Secret message:", bd=3, font=('', 10))
    label1.place(relx=0.1, rely=0.2, height=20, width=100)

    entry = Entry(enc, bd=3, font=('', 13))
    entry.place(relx=0.4, rely=0.2)

    label2 = Label(enc, text="File name:", bd=3, font=('', 10))
    label2.place(relx=0.1, rely=0.3, height=20, width=100)

    entrysave = Entry(enc, bd=3, font=('', 13))
    entrysave.place(relx=0.4, rely=0.3)

    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

        label3 = Label(enc, text=fileopen, bd=3, font=('', 13))
        label3.place(relx=0.3, rely=0.4)

    def encodee():
        response = messagebox.askyesno("pop up", "do you want to encode")
        if response == 1:
            stg.hide(fileopen, entrysave.get() + '.jpg', entry.get())
            messagebox.showinfo("pop up", "successfully encode")

        else:
            messagebox.showwarning("pop up", "unsuccessful")

    buttonselect = Button(enc, text="select file", bd=3, font=('', 11), command=openfile)
    buttonselect.place(relx=0.1, rely=0.4)

    buttonencode = Button(enc, text="Encode", bd=3, font=('', 13), command=encodee)
    buttonencode.place(relx=0.4, rely=0.6)


def decode():
    dnc = Tk()
    dnc.title("Decode")
    dnc.geometry("500x400+300+150")

    def openfile():
        global fileopen
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

    def decodee():
        message = stg.reveal(fileopen)

        label4 = Label(dnc, text=message, bd=3, font=('', 13))
        label4.place(relx=0.3, rely=0.3)

    buttonselect = Button(dnc, text="select file", bd=3, font=('', 13), command=openfile)
    buttonselect.place(relx=0.1, rely=0.3)

    buttondecode = Button(dnc, text="Decode", bd=3, font=('', 13), command=decodee)
    buttondecode.place(relx=0.4, rely=0.5)


def stegit():
    stg = Tk()
    stg.title("K-Encode")
    stg.geometry("500x400+300+150")

    Label(stg, text="K-Encode", bg="gray", width="300", height="3", font=("Caliber", 13)).pack()
    Label(stg, text="").pack()
    Label(stg, text="").pack()
    Button(stg, text="Encode", height="2", width="20", bd=3, font=('', 13), command=encode).pack()
    Label(stg, text="").pack()
    Button(stg, text="Decode", height="2", width="20", bd=3, font=('', 13), command=decode).pack()
    Label(stg, text="").pack()
    Button(stg, text="Share", height="2", width="20", bd=3, font=('', 13), command=OpenWeb).pack()


class main:

    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.email = StringVar()
        self.Phone_no = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.n_email = StringVar()
        self.n_Phone_no = StringVar()
        self.widgets()

    def login(self):
        with sqlite3.connect('Records.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()

        if result:
            self.logf.pack_forget()
            Label(text="Login Successful !", width="30", height="3", font=("Caliber", 13)).pack()
            Button(text="OK", height="2", width="10", bd=3, font=('', 13), command=stegit).pack()
            Label(text="").pack()

        else:
            ms.showerror('Oops!', 'Username Not Found.')

    def new_user(self):
        with sqlite3.connect('Records.db') as db:
            c = db.cursor()

        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(self.username.get())])
        if c.fetchall():
            ms.showerror('Error!', 'Username Taken Try a Different One.')
        else:
            ms.showinfo('Success!', 'Account Created!')
            self.log()
        insert = 'INSERT INTO user(username,password,email,Phone_no) VALUES(?,?,?,?)'
        c.execute(insert,
                  [(self.n_username.get()), (self.n_password.get()), (self.n_email.get()), (self.n_Phone_no.get())])
        db.commit()

    def log(self):
        self.username.set('')
        self.password.set('')
        self.email.set('')
        self.Phone_no.set('')
        self.crf.pack_forget()
        self.head['text'] = 'K-Encode'
        self.logf.pack()

    def cr(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text'] = 'Create Account'
        self.crf.pack()

    def widgets(self):
        self.head = Label(self.master, text='K-Encode', font=('', 35), pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=20)
        Label(self.logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=self.login).grid()
        Button(self.logf, text=' Register ', bd=3, font=('', 15), padx=5, pady=5, command=self.cr).grid(row=2, column=1)
        self.logf.pack()

        self.crf = Frame(self.master, padx=40, pady=50)
        Label(self.crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_username, bd=4, font=('', 16)).grid(row=0, column=1)
        Label(self.crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_password, bd=5, font=('', 16), show='*').grid(row=1, column=1)
        Label(self.crf, text='Email: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_email, bd=4, font=('', 16)).grid(row=2, column=1)
        Label(self.crf, text='Phone no: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.crf, textvariable=self.n_Phone_no, bd=5, font=('', 16)).grid(row=3, column=1)
        Label(self.crf, text="").grid()
        Button(self.crf, text='Register', bd=3, font=('', 15), padx=5, pady=10, command=self.new_user).grid()
        Button(self.crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=10, command=self.log).grid(row=5,
                                                                                                          column=1)


root = Tk()
main(root)
root.mainloop()