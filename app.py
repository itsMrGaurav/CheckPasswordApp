
from tkinter import *
from tkinter import ttk
import checkpasswd



def check_passwd(*args):
    password=passwd_entry.get()
    count=checkpasswd.check_password(password)
    if count == -1:
        res.set('Unable to connect. Check your internet connnectivity.')
    elif count == -2:
        res.set('Uable to connect to API.Check your connection')
    elif count:
        res.set(f'Password has being pawned {count} times!!!')
    else:
        res.set('You\'re in clear.')


root=Tk()
root.title('Pa$$word Checker')

mainframe=ttk.Frame(root,padding="50 25 50 25")
mainframe.grid(column=0,row=0)
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

passwd=StringVar()
passwd_entry=ttk.Entry(mainframe,width=50,textvariable=passwd)
passwd_entry.grid(column=1,row=1,sticky=(W,E))

ttk.Label(mainframe,text='Password to check = ').grid(column=0,row=1)
style = ttk.Style()
 
style.configure('W.TButton', font =
               ('calibri', 10), borderwidth = 4, relief = SUNKEN)
style.map('W.TButton', foreground = [('active', '!disabled', 'white')],
                     background = [('active', 'black')])
check_btn=ttk.Button(mainframe,text='Check',command=check_passwd, style ="W.TButton")
check_btn.grid(column=1,row=2)

res=StringVar()
res.set('')
ttk.Label(mainframe,textvariable=res).grid(column=1,row=3)

for child in mainframe.winfo_children():
    child.grid_configure(padx=10,pady=10)

passwd_entry.focus()
root.bind('<Return>',check_passwd)

root.mainloop()