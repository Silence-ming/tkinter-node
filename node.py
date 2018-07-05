from tkinter import *
from tkinter import scrolledtext
from tkinter.filedialog import *
from tkinter import messagebox
import webbrowser
from tkinter import simpledialog  #.askstring(title=,)
import os
root=Tk()
root.title('记事本')
# root.attributes('-topmost',1)
root.geometry('500x300+200+50')

#设定变量
state = IntVar(0)  #监听内容是否改变的变量
filename = StringVar() #保存文件的变量
flag=IntVar(0) #监听welcome是否隐藏

def close():
    if state.get():
        if messagebox.askokcancel('提示消息','是否保存已修改内容？'):
            save()
        else:
            root.destroy()
    else:
        root.destroy()
def change(event):
    global state
    state.set(1)
def create(event=''):
    global state
    if flag.get():
        if state.get():
            if messagebox.askokcancel('提示消息', '是否保存已修改内容？'):
                save()
            text.delete(0.0,END)
    else:
        welcome.pack_forget()
        flag.set(1)
        text.pack(fill=BOTH, expand=1)
    root.title('记事本')
    state.set(0)
def save(evnt=''):
    global state,filename
    if state.get()==1:
        if not filename.get():
            saves()
        else:
            message = text.get(1.0, END)
            fh = open(filename.get(), 'w')
            fh.write(message)
            fh.close()
            state.set(0)
def saves():
    global state,filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt", initialdir='c://')
    if f:
        message = text.get(1.0, END)
        fh = open(f, 'w')
        fh.write(message)
        fh.close()
        filename.set(f)
        state.set(0)
        root.title("记事本-" + os.path.basename(f))
def opens(event=''):
    global state,filename
    if not flag.get():
        welcome.pack_forget()
        flag.set(1)
        text.pack(fill=BOTH, expand=1)
    if state.get():
        if messagebox.askokcancel('提示消息','是否保存已修改内容？'):
            save()
    t=askopenfilename(defaultextension=".txt")
    filename.set(t)
    if filename.get():
        root.title('记事本-'+filename.get())
        text.delete(0.0,END)
        f=open(filename.get(),'r')
        text.insert(0.0,f.read())
        f.close()
    state.set(0)
def undo(event=''):
    try:
        text.edit_undo()
    except:
        pass
def redo(event=''):
    try:
        text.edit_redo()
    except:
        pass
def copy(event=''):
    text.clipboard_clear()
    try:
        text.clipboard_append(text.selection_get())
    except:
        pass
def paste(event=''):
    try:
        text.delete(SEL_FIRST,SEL_LAST)
        text.insert(SEL_FIRST,text.clipboard_get())
    except:
        pass
    text.insert(INSERT,text.clipboard_get())
def cut(event=''):
    text.clipboard_clear()
    try:
        text.clipboard_append(text.selection_get())
        text.delete(SEL_FIRST, SEL_LAST)
    except:
        pass
def copyright():
    messagebox.showinfo('版权信息','版权所有者：周明明')
def about():
    webbrowser.open('http://www.badu.com')
def find(event=''):
    def searchs():
        myentry=value.get()
        strs=str(text.get(1.0,END))
        num=strs.count(myentry)
        if myentry:
            pos = '1.0'
            while True:
                pos = text.search(myentry, pos,stopindex=END)
                if not pos: break
                lastpos = str(round(float(pos)+len(myentry)*0.1,1))  #round(float(num),1) 将小数保留一位
                text.tag_add('match', pos, lastpos)
                pos = lastpos
            text.tag_config('match',background="yellow")
        messagebox.showinfo('查找结果','匹配内容为%s个'%num)
        text.tag_remove("match", "1.0", END)
        top.destroy()
    top=Toplevel(root)
    top.title('查找')
    top.geometry('240x100+250+150')
    Label(top,text='请输入查找内容').grid(row=0,column=0)
    value=StringVar()
    entry=Entry(top,textvariable=value,width=35)
    entry.focus()
    entry.grid(row=1,column=0,padx=5,pady=5)
    Button(top,width=15,text='开始查找',command=searchs).grid(row=2,column=0,padx=5,pady=5)
#创建标题
welcome=Label(root,text='请打开或新建文件',font=('Arial',18,'bold'),bg='#ccc')
welcome.pack(fill=BOTH,expand=1)
#创建scrolltext
text=scrolledtext.ScrolledText(root,highlightthicknes=0,bg="#F6F8FA",font=('楷体',18),padx=5,pady=5,undo=True)
text.focus()
text.bind('<Key>',change)

#创建菜单
menu=Menu(root)

#文件功能
menu1=Menu(menu,tearoff=0)
menu1.add_command(label='新建',accelerator="Ctrl+n",command=create)
menu1.add_command(label='打开',accelerator="Ctrl+o",command=opens)
menu1.add_separator()
menu1.add_command(label='保存',accelerator="Ctrl+s",command=save)
menu1.add_command(label='另存为',command=saves)
menu1.add_separator()
menu1.add_command(label='退出(exit)',command=close)
menu.add_cascade(label='文件',menu=menu1)
root.config(menu=menu)

#编辑功能
edit=Menu(menu,tearoff=0)
edit.add_command(label='返回',accelerator="Ctrl+z",command=undo)
edit.add_command(label='撤销',accelerator="Ctrl+q",command=redo)
edit.add_separator()
edit.add_command(label='复制',accelerator="Ctrl+c",command=copy)
edit.add_command(label='剪切',accelerator="Ctrl+x",command=cut)
edit.add_command(label='粘贴',accelerator="Ctrl+v",command=paste)
edit.add_separator()
edit.add_command(label='查找',accelerator="Ctrl+f",command=find)
menu.add_cascade(label='编辑',menu=edit)

#帮助功能
help=Menu(menu,tearoff=0)
help.add_command(label='版权信息',command=copyright)
help.add_command(label='关于我们',command=about)
menu.add_cascade(label='帮助',menu=help)

#快捷键绑定
text.bind_all("<Control-n>",create)
text.bind_all("<Control-o>",opens)
text.bind_all("<Control-s>",save)
text.bind_all("<Control-z>",undo)
text.bind_all("<Control-q>",redo)
text.bind_all("<Control-f>",find)
root.protocol('WM_DELETE_WINDOW',close) #关闭

root.mainloop()