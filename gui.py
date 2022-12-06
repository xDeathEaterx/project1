from tkinter import *
from tkinter import ttk

import area, perimeter

class GUI:
    def __init__(self, window):

        self.window = window
        notebook = ttk.Notebook(window)
        notebook.pack(pady=10)

        cirTab = Frame(notebook)
        recTab = Frame(notebook)
        squTab = Frame(notebook)
        triTab = Frame(notebook)

        cirTab.pack(fill='both', expand=1)
        recTab.pack(fill='both', expand=1)
        squTab.pack(fill='both', expand=1)
        triTab.pack(fill='both', expand=1)

        notebook.add(cirTab, text='Circle')
        notebook.add(recTab, text='Rectangle')
        notebook.add(squTab, text='Square')
        notebook.add(triTab, text='Triangle')

        self.frameCir = Frame(cirTab)
        self.labelCir = Label(self.frameCir, text='Computes Area of a Circle', font='bold')
        self.frameCir.pack(padx=5)
        self.labelCir.pack(padx=5)
        self.frameSpace = Frame(cirTab)
        self.frameSpace.pack(anchor='w', pady=10)

        self.frameCRad = Frame(cirTab)
        self.labelCRad = Label(self.frameCRad, text='Enter Radius:')
        self.entryCRad = Entry(self.frameCRad)
        self.labelCRad.pack(padx=35, side='left')
        self.entryCRad.pack(padx=10, side='left')
        self.frameCRad.pack(anchor='w', pady=10)

        self.frameCRes = Frame(cirTab)
        self.buttonCRes = Button(self.frameCRes, text='Compute', command=self.compute(1))
        self.labelCRes = Label(self.frameCRes)
        self.buttonCRes.pack(padx=45, side='left')
        self.labelCRes.pack(padx=30, side='left')
        self.frameCRes.pack(anchor='w', pady=10)

        self.frameSpace2 = Frame(cirTab)
        self.frameSpace2.pack(anchor='w', pady=10)
        self.frameCir2 = Frame(cirTab)
        self.labelCir2 = Label(self.frameCir2, text='Computes Circle Perimeter', font='bold')
        self.frameCir2.pack(padx=5)
        self.labelCir2.pack(padx=5)
        self.frameSpace3 = Frame(cirTab)
        self.frameSpace3.pack(anchor='w', pady=10)

        self.frameCRad2 = Frame(cirTab)
        self.labelCRad2 = Label(self.frameCRad2, text='Enter Radius:')
        self.entryCRad2 = Entry(self.frameCRad2)
        self.labelCRad2.pack(padx=35, side='left')
        self.entryCRad2.pack(padx=10, side='left')
        self.frameCRad2.pack(anchor='w', pady=10)

        self.frameCRes2 = Frame(cirTab)
        self.buttonCRes2 = Button(self.frameCRes2, text='Compute', command=self.compute(2))
        self.labelCRes2 = Label(self.frameCRes2)
        self.buttonCRes2.pack(padx=45, side='left')
        self.labelCRes2.pack(padx=30, side='left')
        self.frameCRes2.pack(anchor='w', pady=10)

        self.frameRec = Frame(recTab)   #first rectangle
        self.labelRec = Label(self.frameRec, text='Computes Area of a Rectangle', font='bold')
        self.frameRec.pack(padx=5)
        self.labelRec.pack(padx=5)
        self.frameSpace4 = Frame(recTab)
        self.frameSpace4.pack(anchor='w', pady=10)

        self.frameRSides = Frame(recTab)
        self.labelRSides = Label(self.frameRSides, text='Enter Sides:')
        self.entryRSides = Entry(self.frameRSides)
        self.entryRSides2 = Entry(self.frameRSides)
        self.labelRSides.pack(padx=5, side='left')
        self.entryRSides.pack(padx=5, side='left')
        self.entryRSides2.pack(padx=5, side='left')
        self.frameRSides.pack(anchor='w', pady=10)

        self.frameRRes = Frame(recTab)
        self.buttonRRes = Button(self.frameRRes, text='Compute', command=self.compute(3))
        self.labelRRes = Label(self.frameRRes)
        self.buttonRRes.pack(padx=45, side='left')
        self.labelRRes.pack(padx=30, side='left')
        self.frameRRes.pack(anchor='w', pady=10)
        self.frameSpace5 = Frame(recTab)
        self.frameSpace5.pack(anchor='w', pady=10)

        self.frameRec2 = Frame(recTab)
        self.labelRec2 = Label(self.frameRec2, text='Computes Rectangle Perimeter', font='bold')
        self.frameRec2.pack(padx=5)
        self.labelRec2.pack(padx=5)
        self.frameSpace7 = Frame(recTab)
        self.frameSpace7.pack(anchor='w', pady=10)

        self.frameRSides2 = Frame(recTab)
        self.labelRSides2 = Label(self.frameRSides2, text='Enter Sides:')
        self.entryRSides3 = Entry(self.frameRSides2)
        self.entryRSides4 = Entry(self.frameRSides2)
        self.labelRSides2.pack(padx=5, side='left')
        self.entryRSides3.pack(padx=5, side='left')
        self.entryRSides4.pack(padx=5, side='left')
        self.frameRSides2.pack(anchor='w', pady=10)
        self.frameSpace8 = Frame(recTab)
        self.frameSpace8.pack(anchor='w', pady=10)

        self.frameRRes2 = Frame(recTab)
        self.buttonRRes2 = Button(self.frameRRes2, text='Compute', command=self.compute(4))
        self.labelRRes2 = Label(self.frameRRes2)
        self.buttonRRes2.pack(padx=45, side='left')
        self.labelRRes2.pack(padx=30, side='left')
        self.frameRRes2.pack(anchor='w', pady=10)

        self.frameSqu = Frame(squTab)
        self.labelSqu = Label(self.frameSqu, text='Computes Area of a Square', font='bold')
        self.frameSqu.pack(padx=5)
        self.labelSqu.pack(padx=5)
        self.frameSpace9 = Frame(squTab)
        self.frameSpace9.pack(anchor='w', pady=10)

        self.frameSSide = Frame(squTab)
        self.labelSSide = Label(self.frameSSide, text='Enter Side:')
        self.entrySSide = Entry(self.frameSSide)
        self.labelSSide.pack(padx=35, side='left')
        self.entrySSide.pack(padx=10, side='left')
        self.frameSSide.pack(anchor='w', pady=10)
        self.frameSpace10 = Frame(recTab)
        self.frameSpace10.pack(anchor='w', pady=10)

        self.frameSRes = Frame(squTab)
        self.buttonSRes = Button(self.frameSRes, text='Compute', command=self.compute('5'))
        self.labelSRes = Label(self.frameSRes)
        self.buttonSRes.pack(padx=45, side='left')
        self.labelSRes.pack(padx=30, side='left')
        self.frameSRes.pack(anchor='w', pady=10)
        self.frameSpace11 = Frame(squTab)
        self.frameSpace11.pack(anchor='w', pady=10)

        self.frameSqu2 = Frame(squTab)
        self.labelSqu2 = Label(self.frameSqu2, text='Computes Square Perimeter', font='bold')
        self.frameSqu2.pack(padx=5)
        self.labelSqu2.pack(padx=5)
        self.frameSpace12 = Frame(squTab)
        self.frameSpace12.pack(anchor='w', pady=10)

        self.frameSSide2 = Frame(squTab)
        self.labelSSide2 = Label(self.frameSSide2, text='Enter Side:')
        self.entrySSide2 = Entry(self.frameSSide2)
        self.labelSSide2.pack(padx=35, side='left')
        self.entrySSide2.pack(padx=10, side='left')
        self.frameSSide2.pack(anchor='w', pady=10)
        self.frameSpace13 = Frame(recTab)
        self.frameSpace13.pack(anchor='w', pady=10)

        self.frameSRes2 = Frame(squTab)
        self.buttonSRes2 = Button(self.frameSRes2, text='Compute', command=self.compute(6))
        self.labelSRes2 = Label(self.frameSRes2)
        self.buttonSRes2.pack(padx=45, side='left')
        self.labelSRes2.pack(padx=30, side='left')
        self.frameSRes2.pack(anchor='w', pady=10)
        self.frameSpace11 = Frame(squTab)
        self.frameSpace11.pack(anchor='w', pady=10)

        self.frameTri = Frame(triTab)
        self.labelTri = Label(self.frameTri, text='Computes Area of a Triangle', font='bold')
        self.frameTri.pack(padx=5)
        self.labelTri.pack(padx=5)
        self.frameSpace12 = Frame(triTab)
        self.frameSpace12.pack(anchor='w', pady=10)

        self.frameTSides = Frame(triTab)
        self.labelTSides = Label(self.frameTSides, text='Enter Sides:')
        self.entryTSides = Entry(self.frameTSides)
        self.entryTSides2 = Entry(self.frameTSides)
        self.labelTSides.pack(padx=5, side='left')
        self.entryTSides.pack(padx=5, side='left')
        self.entryTSides2.pack(padx=5, side='left')
        self.frameTSides.pack(anchor='w', pady=10)

        self.frameTRes = Frame(triTab)
        self.buttonTRes = Button(self.frameTRes, text='Compute', command=self.compute(7))
        self.labelTRes = Label(self.frameTRes)
        self.buttonTRes.pack(padx=45, side='left')
        self.labelTRes.pack(padx=30, side='left')
        self.frameTRes.pack(anchor='w', pady=10)
        self.frameSpace13 = Frame(triTab)
        self.frameSpace13.pack(anchor='w', pady=10)

        self.frameTri2 = Frame(triTab)
        self.labelTri2 = Label(self.frameTri2, text='Computes Triangle Perimeter', font='bold')
        self.frameTri2.pack(padx=5)
        self.labelTri2.pack(padx=5)
        self.frameSpace14 = Frame(triTab)
        self.frameSpace14.pack(anchor='w', pady=10)

        self.frameTSides2 = Frame(triTab)
        self.labelTSides2 = Label(self.frameTSides2, text='Enter Sides:')
        self.entryTSides3 = Entry(self.frameTSides2, width=12)
        self.entryTSides4 = Entry(self.frameTSides2, width=12)
        self.entryTSides5 = Entry(self.frameTSides2, width=12)
        self.labelTSides2.pack(padx=5, side='left')
        self.entryTSides3.pack(padx=5, side='left')
        self.entryTSides4.pack(padx=5, side='left')
        self.entryTSides5.pack(padx=5, side='left')
        self.frameTSides2.pack(anchor='w', pady=10)

        self.frameTRes2 = Frame(triTab)
        self.buttonTRes2 = Button(self.frameTRes2, text='Compute', command=self.compute(8))
        self.labelTRes2 = Label(self.frameTRes2, text='Area')
        self.buttonTRes2.pack(padx=45, side='left')
        self.labelTRes2.pack(padx=30, side='left')
        self.frameTRes2.pack(anchor='w', pady=10)

    def compute(self, num: int):

        try:
            rad = self.entryCRad.get()
            r1 = self.entryRSides.get()
            r2 = self.entryRSides2.get()
            sq = self.entrySSide.get()
            t1 = self.entryTSides.get()
            t2 = self.entryTSides2.get()
            radp = self.entryCRad2.get()
            rs1 = self.entryRSides3.get()
            rs2 = self.entryRSides4.get()
            sqp = self.entrySSide2.get()
            tp1 = self.entryTSides3.get()
            tp2 = self.entryTSides4.get()
            tp3 = self.entryTSides5.get()

            if num == 1:
                self.labelCRes.config(text=f'The area of the circle is {area.cir(float(rad))}')
            elif num == 2:
                self.labelCRes2.config(text=f'The perimeter of the circle is {perimeter.circle(float(radp))}')
            elif num == 3:
                self.labelRRes.config(text=f'The area of the rectangle is {area.rec(float(r1), float(r2))}')
            elif num == 4:
                self.labelRRes2.config(text=f'The perimeter of the rectangle is {perimeter.rectangle(float(rs1), float(rs2))}')
            elif num == 5:
                self.labelSRes.config(text=f'The area of the square is {area.squ(float(sq))}')
            elif num == 6:
                self.labelSRes2.config(text=f'The perimeter of the square is {perimeter.square(float(sqp))}')
            elif num == 7:
                self.labelTRes.config(text=f'The area of the triangle is {area.tri(float(t1), float(t2))}')
            else:
                self.labelTRes2.config(text=f'The perimeter of the triangle is {perimeter.triangle(float(tp1), float(tp2), float(tp3))}')

        except ValueError:
            self.labelCir.config(text='Enter numeric values')
        except:
            self.labelCRad.config(text='Error occurred!')


