from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

def flameNumber(name1,name2):
    name1.replace(" ","")
    name2.replace(" ","")
    name1=list(name1)
    name2=list(name2)
    for i in range(len(name1)):
        if (name1[i] in name2):
            name2.remove(name1[i])
            name1[i]="0"
    result="".join(name1)+"".join(name2)
    result=result.replace("0","")
    return (len(result))

def flameCalci(name1,name2):

    if name1=="" or name2=="":
        messagebox.showerror("Missing","Enter the names")

    Flame=['F','L','A','M','E','S']
    flame_no=flameNumber(name1.upper(),name2.upper())
   
   

    while(len(Flame)!=1):
        pos=Flame.index(Flame[flame_no%len(Flame)-1])
        Flame=Flame[pos+1:]+Flame[:pos]
        
        
    
    return "".join(Flame)

def flames(name1,name2):

    relationship=flameCalci(name1.get(),name2.get())
  

    if (relationship=="F"):
        messagebox.showinfo("Friend","FRIENDSHIP!\nFriendship doubles your joys, and divides your sorrows.")
    elif (relationship=="L"):
        messagebox.showinfo("Love","LOVE!\nBeing loved by someone us a great feeling.")
    elif (relationship=="A"):
        messagebox.showinfo("Affection","AFFECTION!\nHuman nature is so constructed that it gives affection most readily to those who seem least to demand it.")
    elif (relationship=="M"):
        messagebox.showinfo("Marraige","MARRAIGE!\nNever marry the one you can live with, marry the one you cannot live without.")
    elif (relationship=="E"):
        messagebox.showinfo("Enemy","ENEMY!\nAlways forgive your enemies; nothing annoys them so much.")
    elif (relationship=="S"):
        messagebox.showinfo("Sibiling","SIBILING!\nSiblings-the definition that comprises love, strife, competition and forever friends.")
    
    name1.set("")
    name2.set("")

    

    

if __name__=="__main__":
    window = Tk()
    name1=StringVar()
    name2=StringVar()
    window.columnconfigure(4,weight=1)
    imgsrc=Image.open("Flames poster.png")
    imgsrc=imgsrc.resize((200,60),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(imgsrc)
    Label(window,image=img).grid(row=0,column=0,rowspan=2,columnspan=2,padx=60,pady=5)
    Label(window,text="Enter your name").grid(row=2,column=0,pady=5)
    Label(window,text="Enter another person name").grid(row=3,column=0,pady=5)
    entry1=Entry(window,textvariable=name1).grid(row=2,column=1,pady=5)
    entry2=Entry(window,textvariable=name2).grid(row=3,column=1,pady=5)
    button=Button(window,text="FLAMES",command=lambda:flames(name1,name2),bg="blue",fg="white")
    button.grid(row=4,column=0,padx=50,pady=10,columnspan=2,)
    window.title("FLAMES")
    window.geometry('320x200')
    window.mainloop()
    