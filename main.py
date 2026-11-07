#Import module
from tkinter import*

#create  a window
root = Tk()

#name of the window
root.title("calculator") 

#size of the window
root.geometry("200x200+0+0")

#background color 
root['bg'] = "white"

root.resizable(False, False)

def write(text):
    #Append the supplied text to the calculator's input field.
    ent.insert(END, text)
    

    
def clear():
    #Remove all text from the calculator's input field
    ent.delete(0, END)
    resl.config(text="")


def cl():
    try:
        # Read the expression, calculate it, and show the result as text.
        res = eval(ent.get())
        resl.config(text=res)
        resl.config(fg="blue")
        
  # Display a generic message if evaluating the expression fails.
    except ZeroDivisionError:
        resl.config(text="You cannot divide by zero")
        resl.config(fg="yellow")    
    except Exception:
        resl.config(text="ERROR!")
        resl.config(fg="red")
   

 
    
# Create the text-entry field where the user types or builds a calculation.
ent = Entry()
ent.pack()
# Create a wide button that runs clear() when clicked to erase the entry field.
clear = Button(text="ca", command=clear, width=40)
clear.pack(side=BOTTOM)
resl = Label(root, text="", bg="white", fg="white")
resl.pack()



# Create a frame to group and organize the calculator buttons.
fr = Frame(root, bg="lightgray", bd=2, relief=SOLID, padx=10, pady=10)
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
dotb = Button(fr, text=".", command=lambda: write("."))
dotb.grid(row=4, column=9)

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

# Create the equals button; clicking it runs cl() to evaluate the entered expression.
resb = Button(fr, text="=", command=cl)
# Place the equals button in the calculator frame at row 8, column 7.
resb.grid(row=8, column=7)

root.mainloop()
