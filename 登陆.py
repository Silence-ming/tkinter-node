from tkinter import *
from tkinter import messagebox as m
class App:
    def __init__(self,master):
        self.master=master
        master.protocol('WM_DELETE_WINDOW',self.callback)
        self.title=Label(master,text='欢迎登陆',bg='violet',fg='blue',font=('楷体',15)).grid(row=0,column=1,pady=5)
        self.text1 = Label(master, text='账号', bg='violet').grid(row=1, column=0)
        self.val1 = StringVar(value='')
        self.input1 = Entry(master, textvariable=self.val1)
        self.input1.grid(row=1, column=1, pady=5)
        self.text2 = Label(master, text='密码', bg='violet').grid(row=2, column=0)
        self.val2 = StringVar(value='')
        self.input2 = Entry(master, textvariable=self.val2)
        self.input2.grid(row=2, column=1, pady=5)
        self.button1=Button(master,text='登陆',width=15,command=self.check).grid(row=3,column=1,pady=5)
        self.button2=Button(master,text='重置',width=15,command=self.dels).grid(row=4,column=1,pady=5)
    def check(self):
        if self.input1.get() == 'admin' and self.input2.get() == '123456':
            m.showinfo('提示信息','登陆成功')
            self.master.destroy()
        else:
            m.showerror('错误信息','输入信息有误')
    def dels(self):
        self.val1.set('')
        self.val2.set('')
    def callback(self):
        if (m.askokcancel('提示消息', '确定关闭页面？')):
            self.master.destroy()
root=Tk()
root.wm_title('登陆界面')
root.geometry('200x200+500+300')
root.attributes('-topmost',1)
root.config(bg='violet',padx=10,pady=5)
login=App(root)
root.mainloop()
