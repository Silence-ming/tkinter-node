from tkinter import ttk
from tkinter import *
root=Tk()
root.geometry('200x350')
info={
    "山西":['太原','大同','临汾','阳泉','朔州'],
    "河北":['石家庄','保定','邯郸'],
    "甘肃":['嘉峪关','酒泉','兰州','张掖','敦煌']
}
def change(event):
    current=com1.get()
    com2['values']=info[current]
#姓名
name=Label(root,text='姓名:')
name.place(x=10,y=10)
nameVal=StringVar(value='')
input=Entry(root,textvariable=nameVal)
input.place(x=45,y=10,width=100,height=20)
#性别
year=Label(root,text='性别:')
year.place(x=10,y=40)
sexVal=StringVar(value=0)
select=Radiobutton(root,text='男',value=0,variable=sexVal)
select.place(x=45,y=40,height=20)
select1=Radiobutton(root,text='女',value=1,variable=sexVal)
select1.place(x=90,y=40,height=20)

#爱好
like=Label(root,text='爱好:')
like.place(x=10,y=70)
swim=StringVar(value=0)
selects=Checkbutton(root,text='游泳',variable=swim,onvalue=1,offvalue=0)
selects.place(x=45,y=70)
climb=StringVar(value=0)
selects1=Checkbutton(root,text='爬山',variable=climb,onvalue=1,offvalue=0)
selects1.place(x=90,y=70)

#省份
name1=Label(root,text='省份:')
name1.place(x=10,y=100)
com1Val=StringVar(value='')
com1=ttk.Combobox(root,values=tuple(info.keys()),textvariable=com1Val)
com1.bind('<<ComboboxSelected>>',change)
com1.place(width=100,height=20,x=45,y=100)

#城市
name2=Label(root,text='城市:')
name2.place(x=10,y=130)
com2Val=StringVar(value='')
com2=ttk.Combobox(root,textvariable=com2Val)
com2.place(width=100,height=20,x=45,y=130)

#按钮
def add():
    strs=""
    strs+="姓名："+nameVal.get()
    if sexVal.get()==0:
        strs+='性别：男'
    elif sexVal.get()==1:
        strs+='性别：女'
    strs+="； 所在地："+com1Val.get()+com2Val.get()
    list.insert(0,strs)
def delete():
    try:
        current=list.curselection()
        list.delete(current)
    except:
        pass
btn1=Button(root,text='添加',command=add)
btn1.place(x=10,y=160,width=50)
btn2=Button(root,text='删除',command=delete)
btn2.place(x=100,y=160,width=50)
#结果
list=Listbox(root)
list.place(width=180,height=150,x=10,y=190)
root.mainloop()
