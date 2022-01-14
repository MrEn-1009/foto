from tkinter import *
def rotik():
    if var_rot.get()=='rot':
        c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")
    elif var_rot.get()=='tühi':
        c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="#ccb35a", outline='#ccb35a')
def ovalik():
    oval=var_oval.get()
    nos=var_nos.get()
    brov=var_brov.get()
    rot=var_rot.get()
    glaz=var_glaz.get()
    if oval=='oval' :
        c.create_oval((10, 10, 290, 290),fill='#ccb35a')
        if glaz=='glaz' and nos=='nos' and brov=='brov' and rot=='rot':
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz
            c.create_line((80, 100), (220, 100),width="3")#brov
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot

        elif glaz=='glaz' and nos=='nos' and brov=='brov' and rot=='tühi':
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57')
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') 
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') 
            c.create_oval((130,120,95,165),fill='#508dad')
            c.create_oval((205,120,170,165),fill='#508dad')
            c.create_line((80, 100), (220, 100),width="3")#galz/nos/brov

        elif glaz=='glaz' and nos=='nos' and brov=='tühi' and rot=='tühi':
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz/nos

        elif glaz=='glaz' and nos=='tühi' and brov=='tühi' and rot=='tühi':
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz

        elif glaz=='tühi' and nos=='nos' and brov=='brov' and rot=='rot':
            c.create_line((80, 100), (220, 100),width="3")#brov
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos/brov/rot

        elif  glaz=='tühi' and nos=='tühi' and brov=='brov' and rot=='rot':
            c.create_line((80, 100), (220, 100),width="3")#brov
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot/brov

        elif glaz=='tühi' and nos=='tühi' and brov=='tühi' and rot=='rot':
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot

        elif glaz=='tühi' and nos=='nos' and brov=='tühi' and rot=='tühi':
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos

        elif glaz=='tühi' and nos=='nos' and brov=='brov' and rot=='tühi':
            c.create_line((80, 100), (220, 100),width="3")#brov
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #brov/nos

        elif glaz=='tühi' and nos=='tühi' and brov=='brov' and rot=='tühi':
            c.create_line((80, 100), (220, 100),width="3")#brov

        elif glaz=='glaz' and nos=='tühi' and brov=='brov' and rot=='tühi':
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz
            c.create_line((80, 100), (220, 100),width="3")#brov/glaz

        elif glaz=='glaz' and nos=='tühi' and brov=='brov' and rot=='rot':
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz
            c.create_line((80, 100), (220, 100),width="3")#brov
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot/brov/glaz

        elif glaz=='glaz' and nos=='tühi' and brov=='tühi' and rot=='rot':
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz/rot

        elif glaz=='tühi' and nos=='nos' and brov=='tühi' and rot=='rot':
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos/rot

        elif glaz=='glaz' and nos=='nos' and brov=='tühi' and rot=='rot':
            c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57') #nos
            c.create_oval((80, 120, 145, 165),fill='white',outline='black') #glaz
            c.create_oval((155, 120, 220, 165),fill='white',outline='black') #glaz
            c.create_oval((130,120,95,165),fill='#508dad') #glaz
            c.create_oval((205,120,170,165),fill='#508dad')#glaz
            c.create_arc((100, 235, 200, 235), style=CHORD, start=195, extent=150, fill="black")#rot/glaz/nos

        elif glaz=='tühi' and nos=='tühi' and brov=='tühi' and rot=='tühi':
            c.create_oval((10, 10, 290, 290),fill='#ccb35a')

    elif oval=='tühi':
        c.create_oval((10, 10, 290, 290),outline='white',fill='white') 
def nosik():
    if var_nos.get()=='nos':
        c.create_polygon([(145, 225), (175,225), (150, 150)],fill='#ad9950',outline='#c2aa57')
    elif var_nos.get()=='tühi':
        c.create_polygon([(145, 225), (175,225), (150, 150)],fill="#ccb35a", outline='#ccb35a')
def glazik():
    if var_glaz.get()=='glaz':
        c.create_oval((80, 120, 145, 165),fill='white',outline='black') 
        c.create_oval((155, 120, 220, 165),fill='white',outline='black') 
        c.create_oval((130,120,95,165),fill='#508dad')
        c.create_oval((205,120,170,165),fill='#508dad')
    elif var_glaz.get()=='tühi':
        c.create_oval((80, 120, 145, 165),fill='#ccb35a',outline='#ccb35a') 
        c.create_oval((155, 120, 220, 165),fill='#ccb35a',outline='#ccb35a') 
def brovik():
    if var_brov.get()=='brov':
        c.create_line((80, 100), (220, 100),width="3")
    elif var_brov.get()=='tühi':
        c.create_line((80, 100), (220, 100),width="3",fill='#ccb35a')
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
brovi=Checkbutton(f1,text='Бровь',variable=var_brov,onvalue='brov',offvalue='tühi',command=brovik)
brovi.pack(side=TOP)

#c.create_oval((10, 10, 290, 290),fill='#ccb35a') 
c.pack()
aken.mainloop() 
