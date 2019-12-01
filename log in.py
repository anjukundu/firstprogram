from tkinter import *
def crt():
    global e1
    global e2
    global l3
    n1=e1.get()
    n2=e2.get()
    file=open("password.txt","r")
    file1=open("number.txt",'r')
    n=int(file1.read())
    f=file.readline(n)
    f1=file.readline(len(n1))
    f2=file.readline(len(n2))
    if n1==f1 and n2==f2:
        master.destroy()
        root=Tk()
        root.title('Account')
        t=Text(root,width=15,height=3)
        t.insert(END,'Access granted')
        t.pack()
        root.mainloop()
    else:
        l3['text']='Incorrect username or password.'
    
master=Tk()
master.geometry('300x225')
def hide():
    e2['show']='*'
    b1['text']='Show'
    b1['command']=show
def show():
    e2['show']=''
    b1['text']='Hide'
    b1['command']=hide
master.title('Log in')
master.config(bg='royalblue4')
l1=Label(master,bg='royalblue4',fg='white',text='Enter username',font=(' Segoe UI',15))
l1.pack(side='top')
e1=Entry(master,width=15)
e1.pack(side='top')
e1.focus_set()
l2=Label(master,bg='royalblue4',fg='white',text='Enter password',font=(' Segoe UI',15))
l2.pack(side='top')
e2=Entry(master,width=15,show='*')
e2.pack(side='top')
e2.focus_set()
b1=Button(master,text='Show',bd=3,width=4,state='normal',bg='navy',fg='white',command=show,font=(' Segoe UI',11))
b1.pack()
b2=Button(master,text='Login in',bg='navy',bd=3,fg='white',command=crt,font=(' Segoe UI',11))
b2.pack()
l3=Label(master,bg='royalblue4',fg='red',font=(' Segoe UI',15))
l3.pack()
master.mainloop()
