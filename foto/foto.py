from tkinter import *
def rotik():
    if var_rot.get()=='rot':
        c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")
    elif var_rot.get()=='tühi':
        c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="#ccb35a", outline='#ccb35a')
def ovalik():
    if var_oval.get()=='oval':
        c.create_oval((10, 10, 290, 290),fill='#ccb35a') 
    elif var_oval.get()=='tühi':
        c.create_oval((10, 10, 290, 290),outline='white') 
def nosik():
    if var_nos.get()=='nos':
        c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#c2aa57',outline='#c2aa57')
    elif var_nos.get()=='tühi':
        c.create_polygon([(145, 225), (175,225), (160, 155)],fill="#ccb35a", outline='#ccb35a')
def glazik():
    if var_glaz.get()=='glaz':
        c.create_oval((80, 120, 145, 165)) 
        c.create_oval((155, 120, 220, 165)) 
    elif var_glaz.get()=='tühi':
        c.create_oval((10, 10, 290, 290),outline='#ccb35a')
def brovik():
    if var_brov.get()=='brov':
        pass
    elif var_brov.get()=='tühi':
        pass
aken=Tk()
aken.geometry('500x500')
aken.title('Фоторобот')
aken.resizable(width=False, height=False) 
f1=Frame(aken,width=500,height=250)
f1.pack(side=TOP)
f2=Frame(aken,width=500,height=250)
f2.pack(side=BOTTOM)
c = Canvas(f2, width=300, height=300, bg="white") 

var_glaz=StringVar()
glaz=Checkbutton(f1,text='Глаза',variable=var_glaz,onvalue='glaz',offvalue='tühi',command=glazik)
glaz.pack(side=TOP)


var_oval=StringVar()
oval=Checkbutton(f1,text='Овал лица',variable=var_oval,onvalue='oval',offvalue='tühi',command=ovalik)
oval.pack(side=TOP)

var_nos=StringVar()
nos=Checkbutton(f1,text='Нос',variable=var_nos,onvalue='nos',offvalue='tühi',command=nosik)
nos.pack(side=TOP)

var_rot=StringVar()
rot=Checkbutton(f1,text='Рот',variable=var_rot,onvalue='rot',offvalue='tühi',command=rotik)
rot.pack(side=TOP)

var_brov=StringVar()
brovi=Checkbutton(f1,text='Брови',variable=var_brov,onvalue='brov',offvalue='tühi',command=brovik)
brovi.pack(side=TOP)


c.pack()
aken.mainloop() 
