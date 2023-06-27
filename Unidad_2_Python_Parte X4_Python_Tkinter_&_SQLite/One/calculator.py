from tkinter import * 
aux = ''

class CalculatorTK(Tk):
    def __init__(self):
        super(CalculatorTK,self).__init__()

        self.title('Calculator Tkinter')
        self.config(width=300,height=200)

        self.display = Label(self,text='Ingrese su operación...')
        self.display.grid(row=0,column=0)

        self.button0 = Button(self,text = '0',command= lambda: self.updateDisplay(self.button0))
        self.button0.grid(row=2,column=0)

        self.button1 = Button(self,text = '1',command= lambda: self.updateDisplay(self.button1))
        self.button1.grid(row=2,column=1)

        self.button2 = Button(self,text = '2',command= lambda: self.updateDisplay(self.button2))
        self.button2.grid(row=2,column=2)

        self.button3 = Button(self,text = '3',command= lambda: self.updateDisplay(self.button3))
        self.button3.grid(row=3,column=0)

        self.button4 = Button(self,text = '4',command= lambda: self.updateDisplay(self.button4))
        self.button4.grid(row=3,column=1)

        self.button5 = Button(self,text = '5',command= lambda: self.updateDisplay(self.button5))
        self.button5.grid(row=3,column=2)

        self.button6 = Button(self,text = '6',command= lambda: self.updateDisplay(self.button6))
        self.button6.grid(row=4,column=0)

        self.button7 = Button(self,text = '7',command= lambda: self.updateDisplay(self.button7))
        self.button7.grid(row=4,column=1)

        self.button8 = Button(self,text = '8',command= lambda: self.updateDisplay(self.button8))
        self.button8.grid(row=4,column=2)

        self.button9 = Button(self,text = '9',command= lambda: self.updateDisplay(self.button9))
        self.button9.grid(row=5,column=0)

        self.delete = Button(self,text = 'C',command= self.cleanDisplay)
        self.delete.grid(row=5,column=1)

        self.equal = Button(self,text = '=',command= lambda: self.evaluateExpression(self.display))
        self.equal.grid(row=5,column=2)

        self.addition = Button(self,text = '+',command= lambda: self.updateDisplay(self.addition))
        self.addition.grid(row=2,column=3)

        self.subtraction = Button(self,text = '-',command= lambda: self.updateDisplay(self.subtraction))
        self.subtraction.grid(row=3,column=3)

        self.multiplication = Button(self,text = '*',command= lambda: self.updateDisplay(self.multiplication))
        self.multiplication.grid(row=4,column=3)

        self.divition = Button(self,text = '/',command= lambda: self.updateDisplay(self.divition))
        self.divition.grid(row=5,column=3)

    def updateDisplay(self,button):

        global aux
        aux += button.cget("text")
        self.display.config(text=aux)

    def evaluateExpression(self,button):
        global aux
        
        expr = eval(button.cget("text"))
        aux = str(expr)
        self.display.config(text=expr)
        print(button.cget("text"))

    def cleanDisplay(self):
        global aux
        self.display.config(text='')
        aux = ''

calculatorTest = CalculatorTK()
calculatorTest = mainloop()