from tkinter import *
import sqlite3

Houses = []
First = []
Second = []
Third = []
Fourth = []

def setWindow():
    root = Tk()
    root.geometry('580x230')
    race = Frame(root)
    race.pack(side=TOP)
    score = Label(race,text = "Live scoreboard")
    score.config(font = ('courier, 15'))
    score.grid(row=1, column = 2)
    tkvar00 = StringVar(race)
    tkvar00.set("         ")
    choices00 = {'Pizza', 'Burger', 'Pasta'}
    races = OptionMenu(race, tkvar00, *choices00)
    races.grid(row = 1, column = 3, padx = 10, pady = 10)
    frame = Frame(root)
    frame.pack(side = LEFT)
    p1 = Label(frame,text = "1:")
    p1.grid(row = 0, column = 0, padx = 5, pady = 10)
    e1 = Entry(frame)
    e1.grid(row = 0 , column = 1, padx = 5, pady = 10)
    p2 = Label(frame,text = "2:")
    p2.grid(row = 1, column = 0, padx = 5, pady = 10)
    e2 = Entry(frame)
    e2.grid(row = 1 , column = 1, padx = 5, pady = 10)
    p3 = Label(frame,text = "3:")
    p3.grid(row = 2, column = 0, padx = 5, pady = 10)
    e3 = Entry(frame)
    e3.grid(row = 2 , column = 1, padx = 5, pady = 10)
    p4 = Label(frame,text = "4:")
    p4.grid(row = 3, column = 0, padx = 5, pady = 10)
    e4 = Entry(frame)
    e4.grid(row = 3 , column = 1, padx = 5, pady = 10)
    Frame2 = Frame(root)
    Frame2.pack(side = RIGHT)
    #
    Houselabel1 = Label(Frame2, text = "House: " )
    Houselabel1.grid(row = 0, column = 0, padx = 5, pady = 5)
    tkvar01 = StringVar(Frame2)
    tkvar01.set("         ")
    choices01 = {'Red', 'Blue', 'Green', 'Yellow'}
    Houses1 = OptionMenu(Frame2, tkvar01, *choices01)
    Houses1.grid(row = 0, column = 1, padx = 5, pady = 5)
    Gradelabel1= Label(Frame2, text = "Grade: " )
    Gradelabel1.grid(row = 0, column = 2, padx = 5, pady = 5)
    tkvar02 = StringVar(Frame2)
    tkvar02.set("         ")
    choices02 = {'6', '7', '8', '9' , '10' , '11' , '12'}
    Grades1 = OptionMenu(Frame2, tkvar02, *choices02)
    Grades1.grid(row = 0, column = 3, padx = 5, pady = 5)
    Sectionlabel1= Label(Frame2, text = "Section: " )
    Sectionlabel1.grid(row = 0, column = 4, padx = 5, pady = 5)
    tkvar03 = StringVar(Frame2)
    tkvar03.set("         ")
    choices03 = {'A','B','C','D','E','F','G'}
    Sections1 = OptionMenu(Frame2, tkvar03, *choices03)
    Sections1.grid(row = 0, column = 5, padx = 5, pady = 5)
    #
    Houselabel2 = Label(Frame2, text = "House: " )
    Houselabel2.grid(row = 1, column = 0, padx = 5, pady = 5)
    tkvar11 = StringVar(Frame2)
    tkvar11.set("         ")
    choices11 = {'Red', 'Blue', 'Green', 'Yellow'}
    Houses2 = OptionMenu(Frame2, tkvar11, *choices11)
    Houses2.grid(row = 1, column = 1, padx = 5, pady = 5)
    Gradelabel2= Label(Frame2, text = "Grade: " )
    Gradelabel2.grid(row = 1, column = 2, padx = 5, pady = 5)
    tkvar12 = StringVar(Frame2)
    tkvar12.set("         ")
    choices12 = {'6','7','8','9','10','11','12'}
    Grades2 = OptionMenu(Frame2, tkvar12, *choices12)
    Grades2.grid(row = 1, column = 3, padx = 5, pady = 5)
    Sectionlabel2= Label(Frame2, text = "Section: " )
    Sectionlabel2.grid(row = 1, column = 4, padx = 5, pady = 5)
    tkvar13 = StringVar(Frame2)
    tkvar13.set("         ")
    choices13 = {'A','B','C','D','E','F','G'}
    Sections2 = OptionMenu(Frame2, tkvar13, *choices13)
    Sections2.grid(row = 1, column = 5, padx = 5, pady = 5)
    #
    Houselabel3 = Label(Frame2, text = "House: " )
    Houselabel3.grid(row = 2, column = 0, padx = 5, pady = 5)
    tkvar21 = StringVar(Frame2)
    tkvar21.set("         ")
    choices21 = {'Red', 'Blue', 'Green', 'Yellow'}
    Houses3 = OptionMenu(Frame2, tkvar21, *choices21)
    Houses3.grid(row = 2, column = 1, padx = 5, pady = 5)
    Gradelabel3= Label(Frame2, text = "Grade: " )
    Gradelabel3.grid(row = 2, column = 2, padx = 5, pady = 5)
    tkvar22 = StringVar(Frame2)
    tkvar22.set("         ")
    choices22 = {'6','7','8','9','10','11','12'}
    Grades2 = OptionMenu(Frame2, tkvar22, *choices22)
    Grades2.grid(row = 2, column = 3, padx = 5, pady = 5)
    Sectionlabel3= Label(Frame2, text = "Section: " )
    Sectionlabel3.grid(row = 2 , column = 4, padx = 5, pady = 5)
    tkvar23 = StringVar(Frame2)
    tkvar23.set("         ")
    choices23 = {'A','B','C','D','E','F','G'}
    Sections3 = OptionMenu(Frame2, tkvar23, *choices23)
    Sections3.grid(row = 2, column = 5, padx = 5, pady = 5)
    #
    Houselabel4 = Label(Frame2, text = "House: " )
    Houselabel4.grid(row = 3, column = 0, padx = 5, pady = 5)
    tkvar31 = StringVar(Frame2)
    tkvar31.set("         ")
    choices31 = {'Red', 'Blue', 'Green', 'Yellow'}
    Houses4 = OptionMenu(Frame2, tkvar31, *choices31)
    Houses4.grid(row = 3, column = 1, padx = 5, pady = 5)
    Gradelabel4= Label(Frame2, text = "Grade: " )
    Gradelabel4.grid(row = 3, column = 2, padx = 5, pady = 5)
    tkvar32 = StringVar(Frame2)
    tkvar32.set("         ")
    choices32 = {'6','7','8','9','10','11','12'}
    Grades2 = OptionMenu(Frame2, tkvar32, *choices32)
    Grades2.grid(row = 3, column = 3, padx = 5, pady = 5)
    Sectionlabel3= Label(Frame2, text = "Section: " )
    Sectionlabel3.grid(row = 3, column = 4, padx = 5, pady = 5)
    tkvar33 = StringVar(Frame2)
    tkvar33.set("         ")
    choices33 = {'A','B','C','D','E','F','G'}
    Sections3 = OptionMenu(Frame2, tkvar33, *choices33)
    Sections3.grid(row = 3, column = 5, padx = 5, pady = 5)
    real = sqlite3.connect('Samyak.db')
    real.execute('''CREATE table IF NOT EXISTS main (
                Name TEXT NOT NULL,
                Position INT NOT NULL,
                Race TEXT NOT NULL,
                Grade TEXT NOT NULL,
                Section TEXT NOT NULL,
                House TEXT NOT NULL)''')
    real.execute('''CREATE table IF NOT EXISTS house (
                Red INT NOT NULL,
                Blue INT NOT NULL,
                Green INT NOT NULL,
                Yellow INT NOT NULL)''')
    cur = real.cursor()
    cur.execute("SELECT * FROM house")
    blah = cur.fetchall()
    for j in blah:
        mainlist = [j[0],j[1],j[2],j[3]]
    real.commit()
    def callback():
        real.execute('''INSERT into main
                    (Name, Position, Race, Grade, Section, House)
                    Values (?,?,?,?,?,?)''',(str(e1.get()),1,str(tkvar00.get()),str(tkvar01.get()),str(tkvar02.get()),str(tkvar03.get())))
        real.execute('''INSERT into main
                    (Name, Position, Race, Grade, Section, House)
                    Values (?,?,?,?,?,?)''',(str(e2.get()),2,str(tkvar00.get()),str(tkvar11.get()),str(tkvar12.get()),str(tkvar13.get())))
        real.execute('''INSERT into main
                    (Name, Position, Race, Grade, Section, House)
                    Values (?,?,?,?,?,?)''',(str(e3.get()),3,str(tkvar00.get()),str(tkvar21.get()),str(tkvar22.get()),str(tkvar23.get())))
        real.execute('''INSERT into main
                    (Name, Position, Race, Grade, Section, House)
                    Values (?,?,?,?,?,?)''',(str(e4.get()),4,str(tkvar00.get()),str(tkvar31.get()),str(tkvar32.get()),str(tkvar33.get())))
        real.commit()
        global Houses,First,Second,Third,Fourth
        Houses = [tkvar01.get(), tkvar11.get(), tkvar21.get(), tkvar31.get()]
        First = [str(e1.get()),1,str(tkvar00.get()),str(tkvar01.get()),str(tkvar02.get()),str(tkvar03.get())]
        Second = [str(e2.get()),2,str(tkvar00.get()),str(tkvar11.get()),str(tkvar12.get()),str(tkvar13.get())]
        Third = [str(e3.get()),3,str(tkvar00.get()),str(tkvar21.get()),str(tkvar22.get()),str(tkvar23.get())]
        Fourth = [str(e4.get()),4,str(tkvar00.get()),str(tkvar31.get()),str(tkvar32.get()),str(tkvar33.get())]
        pass


    submit = Button(race, text = "OK", command = callback)
    submit.grid(row = 1, column = 4, padx = 10, pady = 10, ipadx = 15)
    root.mainloop()
    return Houses,mainlist,First,Second,Third,Fourth
