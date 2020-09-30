from tkinter import *

root = Tk()
root.title('Simple Calculator')
e = Entry(root,width = 35,borderwidth=5)
e.grid(row=0,column=0,padx=10,pady=10,columnspan=3)

def buttonClick(number):
    #
    current_num = e.get()
    e.delete(0,END)
    e.insert(0,str(current_num)+str(number))

def buttonClear():
    e.delete(0,END)

def buttonAdd():
    first_number = e.get()
    global f_num 
    global math 
    math = 'add'
    f_num = int(first_number)
    e.delete(0,END)

def buttonSub():
    first_number = e.get()
    global f_num 
    global math
    math = 'sub'
    f_num = int(first_number)
    e.delete(0,END)

def buttonMul():
    first_number = e.get()
    global f_num 
    global math 
    math = 'mul'
    f_num = int(first_number)
    e.delete(0,END)

def buttonDiv():
    first_number = e.get()
    global f_num 
    global math
    math = 'div'
    f_num = int(first_number)
    e.delete(0,END)

def buttonEqual():
    second_number = e.get()
    e.delete(0,END)

    if math == 'add':
        e.insert(0,f_num + int(second_number))

    elif math == 'sub':
        e.insert(0,f_num - int(second_number))

    elif math == 'mul':
        e.insert(0,f_num * int(second_number))

    elif math == 'div':
        e.insert(0,f_num / int(second_number))






# define buttons   
button_1 = Button(root,text='1', padx=40,pady=20,command=lambda: buttonClick(1))    
button_2 = Button(root,text='2', padx=40,pady=20,command=lambda: buttonClick(2))    
button_3 = Button(root,text='3', padx=40,pady=20,command=lambda: buttonClick(3))    
button_4 = Button(root,text='4', padx=40,pady=20,command=lambda: buttonClick(4))    
button_5 = Button(root,text='5', padx=40,pady=20,command=lambda: buttonClick(5))    
button_6 = Button(root,text='6', padx=40,pady=20,command=lambda: buttonClick(6))    
button_7 = Button(root,text='7', padx=40,pady=20,command=lambda: buttonClick(7))    
button_8 = Button(root,text='8', padx=40,pady=20,command=lambda: buttonClick(8))    
button_9 = Button(root,text='9', padx=40,pady=20,command=lambda: buttonClick(9))    
button_0 = Button(root,text='0', padx=40,pady=20,command=lambda: buttonClick(0))  

button_add = Button(root,text='+', padx=39,pady=20,command= buttonAdd)    
button_clear = Button(root,text='Clear', padx=79,pady=20,command= buttonClear)    
button_equal = Button(root,text='=', padx=91,pady=20,command= buttonEqual)    
button_sub = Button(root,text='-', padx=41,pady=20,command= buttonSub)    
button_mul = Button(root,text='*', padx=40,pady=20,command= buttonMul)    
button_div = Button(root,text='/', padx=41,pady=20,command= buttonDiv)    



#grid the buttons to display
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)
button_clear.grid(row=4,column=1,columnspan=2)

button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)



root.mainloop()