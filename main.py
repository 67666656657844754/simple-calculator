#Import module
from tkinter import*


#create  a window
root = Tk()

#name of the window
root.title("calculator") 

#size of the window
root.geometry("200x200+0+0")

#background color 
root['bg'] = "blue"

root.resizable(False, False)

def write(text):
    #Append the supplied text to the calculator's input field.
    
    ent.insert(END, text)

    
def clear():
    #Remove all text from the calculator's input field
    ent.delete(0, END)


def cl():
    try:
        # Read the expression, calculate it, and show the result as text.
        res = eval(ent.get())
        resl.config(text=res)
        if res == str:
            reslconfig(text="error")
        
        
    except Exception:
        # Display a generic message if evaluating the expression fails.
        resl.config(text="ERROR!")
    except ZeroDivisionError:
        resl.config(text="You cannot divide by zero")
 
    
ent = Entry()
ent.pack()
clear = Button(text="ca", command=clear, width=40)
clear.pack(side=BOTTOM)
resl = Label(root, text="", bg="blue")
resl.pack()



fr = Frame(root, bg="yellow", bd=2, relief=SOLID, padx=10, pady=10)
fr.pack(padx=20, pady=0)

#+-*/.
pb = Button(fr, text="+", command=lambda: write("+"))
pb.grid(row=4, column=5)
mb = Button(fr, text="-", command=lambda: write("-"))
mb.grid(row=4, column=6)
mmb = Button(fr, text="*", command=lambda: write("*"))
mmb.grid(row=4, column=7)
db = Button(fr, text="/", command=lambda: write("/"))
db.grid(row=4, column=8)
nb = Button(fr, text=".", command=lambda: write("."))
nb.grid(row=4, column=9)

#numbers
nm0 = Button(fr, text="0", command=lambda: write("0"))
nm0.grid(row=6, column=5)
nm1 = Button(fr, text="1", command=lambda: write("1"))
nm1.grid(row=6, column=6) 
nm2 = Button(fr, text="2", command=lambda: write("2"))
nm2.grid(row=6, column=7)
nm3 = Button(fr, text="3", command=lambda: write("3"))
nm3.grid(row=6, column=8)
nm4 = Button(fr, text="4", command=lambda: write("4"))
nm4.grid(row=6, column=9)
nm5 = Button(fr, text="5", command=lambda: write("5"))
nm5.grid(row=7, column=5)
nm6 = Button(fr, text="6", command=lambda: write("6"))
nm6.grid(row=7, column=6)
nm7 = Button(fr, text="7", command=lambda: write("7"))
nm7.grid(row=7, column=7)
nm8 = Button(fr, text="8", command=lambda: write("8"))
nm8.grid(row=7, column=8)
nm9 = Button(fr, text="9", command=lambda: write("9"))
nm9.grid(row=7, column=9)





resb = Button(fr, text="=", command=cl)
resb.grid(row=8, column=7)


root.mainloop()
