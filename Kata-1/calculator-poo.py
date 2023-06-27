#!/usr/bin/env
from tkinter import *
import os
i=0
class calculator:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.geometry('330x340')
        self.window.config(bg= "white")
        self.window.resizable(0,0)
        self.window.title('Calculadora IFST')
        self.frame = Frame(self.window)
        self.frame.grid(column=0, row=0, padx=6, pady=3)
        self.results = Entry(self.frame, width=20, relief='groove', font = 'Arial 16',justif = 'right')
        self.Button1 = Button(self.frame, text= "1", borderwidth=2, height=2, width=5, font= ('Arial',12,'bold'),relief = "raised", bg = '#2A16F7',  anchor="center", command=lambda: self.get_number(1))  

        self.Button2 = Button(self.frame, text= "2", height=2, width=5, font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7', anchor="center",command=lambda: self.get_number(2))  

        self.Button3 = Button(self.frame, text= "3", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg ='#2A16F7', anchor="center",command=lambda: self.get_number(3))  

        self.Button_back = Button(self.frame, text= "⌫", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg='#FD0371',  anchor="center",command=lambda: self.delete_one())  

        self.Button4 = Button(self.frame, text= "4",height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg ='#2A16F7', anchor="center",command=lambda: self.get_number(4)) 

        self.Button5 = Button(self.frame, text= "5", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7', anchor="center",command=lambda: self.get_number(5))  

        self.Button6 = Button(self.frame, text= "6", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7',  anchor="center",command=lambda: self.get_number(6))  

        self.Button_more = Button(self.frame, text= "+", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg='#2FEC71',  anchor="center",command=lambda: self.get_number('+'))  

        self.Button7 = Button(self.frame, text= "7",height=2, width=5, font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7',  anchor="center",command=lambda: self.get_number(7))  

        self.Button8 = Button(self.frame, text= "8", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7', anchor="center",command=lambda: self.get_number(8))  

        self.Button9 = Button(self.frame, text= "9", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7',  anchor="center",command=lambda: self.get_number(9))  

        self.Button_less = Button(self.frame, text= "-", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg='#2FEC71',  anchor="center",command=lambda: self.get_number('-'))  

        self.Button0 = Button(self.frame, text= "0",height=5, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7',  anchor="center",command=lambda: self.get_number(0))  

        self.Button_dot = Button(self.frame, text= ".", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2A16F7', anchor="center",command=lambda: self.get_number('.'))  

        self.Button_entry = Button(self.frame, text= "÷", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised",bg ='#2FEC71',  anchor="center",command=lambda: self.get_number('/'))  

        self.Button_x = Button(self.frame, text= "x", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg='#2FEC71',  anchor="center",command=lambda: self.get_number('*'))  

        self.Button_equal = Button(self.frame, text= "=", height=2, width=12,font= ('Arial',12,'bold'), borderwidth=2,  relief = "raised", bg ='#FD5603', anchor="center",command=lambda: self.operation())  

        self.Button_delete = Button(self.frame, text= "C", height=2, width=5,font= ('Arial',12,'bold'), borderwidth=2, relief = "raised", bg='#FD0371', anchor="center",command=lambda: self.delete_all())  

    def get_number(self,data):
        global i
        i+=1
        self.results.insert(i, data)
        
    def operation(self):
        global i

        equation = self.results.get()
        
        if i !=0:		
            
            try:
                result = str(eval(equation))
                self.results.delete(0,END)
                self.results.insert(0,result)
                longitud = len(result)
                i = longitud
    

            except:
                result = 'ERROR'
                self.results.delete(0,END)
                self.results.insert(0,result)
        else:
            pass

    def delete_one(self):
        global i 
        if i==-1:
            pass
        else:
            self.results.delete(i,last =None)
            i-=1
            
    def delete_all(self):
        self.results.delete(0, END)	
        i=0
    
    def callWin(self):
        
        self.results.grid(columnspan=4 , row=0, pady=3,padx=1, ipadx=1, ipady=1) 

        self.Button1.grid( column= 0 ,row=1, pady=1,padx=3)

        self.Button2.grid(column =1 , row=1, pady=1,padx=1)

        self.Button3.grid(column =2, row=1, pady=1,padx=1)

        self.Button_back.grid(column =3, row=1, pady=2,padx=2)


        self.Button4.grid( column= 0 ,row=2, pady=1,padx=1)

        self.Button5.grid(column =1 , row=2, pady=1,padx=1)

        self.Button6.grid(column =2, row=2, pady=1,padx=1)

        self.Button_more.grid(column =3, row=2, pady=2,padx=2)

        self.Button7.grid( column= 0 ,row=3, pady=1,padx=1)

        self.Button8.grid(column =1 , row=3, pady=1,padx=1)

        self.Button9.grid(column =2, row=3, pady=1,padx=1)

        self.Button_less.grid(column =3, row=3, pady=2,padx=2)


        self.Button0.grid( column= 0,row=4, rowspan=2,  pady=1,padx=1)

        self.Button_dot.grid(column =1 , row=4, pady=1,padx=1)

        self.Button_entry.grid(column =2, row=4, pady=1,padx=1)

        self.Button_x.grid(column =3, row=4, pady=2,padx=2)

        self.Button_equal.grid(column =1 ,columnspan=2, row=5, pady=1,padx=1)

        self.Button_delete.grid(column =3, row=5, pady=2,padx=2)





        self.window.mainloop()


calculatorPOO = calculator()

calculatorPOO.callWin()
