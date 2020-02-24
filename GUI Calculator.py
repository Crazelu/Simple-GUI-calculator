import tkinter as tk

result = ''
total = ''
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.resizable(False,False)

        
        # The label widget

        self.text= tk.StringVar()

        self.input_entry = tk.Label(self, textvar= self.text)
        self.input_entry.grid(row=0,column=0, columnspan=4, padx=10, pady= 20 )

        

        # Defining the functions


        def on_click(number):
            global total
            global result
            
            if total =='':
                result = result+str(number)
                self.text.set(result)
           
            if total !='':
                 total = total + str(number)
                 result=total
                 self.text.set(result)
            
            
        def evaluate():
            global result
            global total
            try:
                total = str(eval(result))
                if float(total).is_integer():
                    total = int(float(total))
                self.text.set(total)
                total = str(total)
                
                # Catch divisions by zero
                
            except ZeroDivisionError:
                self.text.set('Error! Zero division')
                
                # Catch other computational errors
            except:
                self.text.set('Error!')
             
            
        def clearScreen():
            global result
            global total
            result=''
            self.text.set('')
            total=''
            
            
        

        

        # Creating the buttons
        
        self.button1= tk.Button(self, text='1', bg='purple', fg='white', activebackground='light blue', padx=51, pady=20, command=lambda: on_click(1))
        
        self.button2= tk.Button(self, text='2', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(2))
        
        self.button3= tk.Button(self, text='3', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(3))
        
        self.button4= tk.Button(self, text='4', bg='purple', fg='white', activebackground='light blue', padx=51, pady=20, command=lambda: on_click(4))
        
        self.button5= tk.Button(self, text='5', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(5))
        
        self.button6= tk.Button(self, text='6', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(6))
        
        self.button7= tk.Button(self, text='7', bg='purple', fg='white', activebackground='light blue', padx=51, pady=20, command=lambda: on_click(7))
        
        self.button8= tk.Button(self, text='8', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(8))
        
        self.button9= tk.Button(self, text='9', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(9))
        
        self.button0= tk.Button(self, text='0', bg='purple', fg='white', activebackground='light blue', padx=50, pady=20, command=lambda: on_click(0))
        
        self.button00= tk.Button(self, text='00', bg='purple', fg='white', activebackground='light blue', padx=47, pady=20, command=lambda: on_click('00'))
        
        self.decimal_button= tk.Button(self, text='.', bg='purple', fg='white', activebackground='light blue', padx=53, pady=20, command=lambda: on_click('.'))
        
        self.add_button= tk.Button(self, text='+', bg='purple', fg='white', activebackground='light blue', padx=40, pady=20, command=lambda: on_click('+'))
        
        self.subtract_button= tk.Button(self, text='-', bg='purple', fg='white', activebackground='light blue', padx=41, pady=20, command=lambda: on_click('-'))
        
        self.multiply_button= tk.Button(self, text='×', bg='purple', fg='white', activebackground='light blue', padx=40, pady=20, command=lambda: on_click('*'))
        
        self.divide_button= tk.Button(self, text='÷', bg='purple', fg='white', activebackground='light blue', padx=40, pady=20, command=lambda: on_click('/'))
        
        self.equal_to_button= tk.Button(self, text='=', bg='purple', fg='white', activebackground='light blue', padx=98, pady=20, command=evaluate)
        
        self.clear_button= tk.Button(self, text= 'Clear', bg='purple', fg='white', activebackground='light blue', padx=99, pady=20, command=clearScreen)
        

        # Throwing the buttons on the screen
        
        self.button7.grid(row= 1, column=0 )
        self.button8.grid(row= 1, column= 1)
        self.button9.grid(row= 1, column= 2)
        self.add_button.grid(row= 1, column= 3)

        self.button4.grid(row=2 , column=0 )
        self.button5.grid(row=2 , column=1 )
        self.button6.grid(row=2 , column=2 )
        self.subtract_button.grid(row=2 , column=3 )

        self.button1.grid(row=3 , column=0 )
        self.button2.grid(row=3 , column=1 )
        self.button3.grid(row=3 , column=2 )
        self.multiply_button.grid(row=3 , column=3 )

        
        self.decimal_button.grid(row=4, column=0)
        self.button0.grid(row=4, column=1)
        self.button00.grid(row=4, column=2)
        self.divide_button.grid(row=4, column=3)

        self.clear_button.grid(row=5, column=0, columnspan=2)
        self.equal_to_button.grid(row=5, column=2, columnspan=4)

        
if __name__== '__main__':
    window= Window()
    window.mainloop()
