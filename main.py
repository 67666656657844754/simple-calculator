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

def write(text):
    #Append the supplied text to the calculator's input field.
    ent.insert(END, text)
    


def clear():
    #Remove all text from the calculator's input field
    ent.delete(0, END)
    resl.config(text="=", fg="black")


def cl():
    try:
        # Read the expression, calculate it, and show the result as text.
        res = eval(ent.get())
        resl.config(text=f"= {res:.2f}")
        resl.config(fg="blue")
        if res == str:
            resl.config("eror")
        
  # Display a generic message if evaluating the expression fails.
    except ZeroDivisionError:
        resl.config(text="You cannot divide by zero")
        resl.config(fg="yellow")    
    except Exception:
        resl.config(text="ERROR!")
        resl.config(fg="red")



# Create the text-entry field where the user types or builds a calculation.
ent = Entry(root, bd=20, font=("Arial", 10))
resl = Label(root, text="=", bg="lightgray", fg="black", font=("Arial", 10))
resl.pack(expand=True, fill="both")
ent.pack(expand=True, fill="both")



LB = [
    ["+", "-", "*", "/"],
    ["4", "5", "6", "7"],
    ["1", "2", "3", "8"],
    ["C", "9", "0", "="]
]

for row in LB:
    # Create a frame to group and organize the calculator buttons.
    fr = Frame(root, bg="lightgray", bd=0, relief=SOLID)
    fr.pack(expand=True, fill="both")

    for ch in row:
        if ch == "C":
            cmd = clear
        elif ch == "=":
            cmd = cl  
        else:
            cmd = lambda x=ch: write(x)

        Button(fr, text=ch,  command=cmd, font=("Arial", 10)).pack(side="left", expand=True, fill="both")


root.mainloop()
