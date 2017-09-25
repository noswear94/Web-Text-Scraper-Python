from bs4 import BeautifulSoup
import requests
import urllib.request
from tkinter import *
import webbrowser

root=Tk()
root.title("Web Text Scraper  ")
root.resizable(width=False, height=False)
root.iconbitmap('Web_Scraper.ico')
root.geometry("350x290+0+0")

heading=Label(root,text="Welcome to the Web Text Scraper",font="Arial 10").pack()

label1=Label(root, text="Enter the url : ").place(x=10,y=30)
urlname=StringVar()
entry_box1=Entry(root,textvariable=urlname,width=25).place(x=130,y=30)


label2=Label(root, text="Enter the tag : ").place(x=10,y=60)
tag=StringVar()
entry_box2=Entry(root,textvariable=tag,width=25).place(x=130,y=60)


label3=Label(root, text="Enter the attribute : * ").place(x=10,y=90)
classes=StringVar()
entry_box3=Entry(root,textvariable=classes,width=25).place(x=130,y=90)
warn1=Label(root, text="* Leave if there is no attribute and its value ",font="Arial 8").place(x=10,y=180)

label4=Label(root, text="Enter the value : * ").place(x=10,y=120)
attr=StringVar()
entry_box4=Entry(root,textvariable=attr,width=25).place(x=130,y=120)


label5=Label(root, text="Enter the file name : ").place(x=10,y=150)
file=StringVar()
entry_box5=Entry(root,textvariable=file,width=25).place(x=130,y=150)

def spider():
    page=1
    while page==1:
        url=urlname.get()
        source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text,'html.parser')
        if classes.get()=="" :
            qt=soup.find_all(str(tag.get()) ,class_=False,id=False)
        else:
            qt=soup.find_all(str(tag.get()) , {str(classes.get()):str(attr.get())})
        for x in qt:
            title=x.text
            name=str(title)
            filename=str(file.get())+".txt"
            with open(filename, "a", encoding='utf-8') as f:
               f.write("%s \n "%(name))

        page+=1
        Done = Button(root, text="Done!", width=10, height=2, command=spider).place(x=120, y=210)
    f.close()

work=Button(root,text="Scrape",width=10,height=2,command=spider).place(x=120,y=210)

heading=Label(root,text="(c) Piyush").place(x=130,y=260)

def OpenUrl():
    webbrowser.open_new("https://github.com/noswear94")


Git=Button(root,text="Github",width=10,height=1,command=OpenUrl).place(x=265,y=260)

root.mainloop()