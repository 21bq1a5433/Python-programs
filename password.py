import random, string
from tkinter import * 
root =Tk()
root.geometry("600x600") 
root.title("Random Password Generator") 
output_pass = StringVar()
all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]
def randPassGen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   
        password = password + random.choice(char_type)
    output_pass.set(password) 
def copyPass():
    pyperclip.copy(output_pass.get()) 
pass_head = Label(root, text = 'Password Length', font = 'Arial 14 bold').pack(pady=10)  
pass_len = IntVar() 
length = Spinbox(root, from_ = 4, to_ = 20 , textvariable = pass_len , width = 30, font='Bold 20').pack()
Button(root, command = randPassGen, text = "Generate Password", font="bold 16", bg='yellow', fg='black', activebackground="Teal", padx=6, pady=6 ).pack(pady= 20) 
pass_label = Label(root, text = 'Random Generated Password', font = 'Arial 16 bold').pack(pady="30 10")
Entry(root , textvariable = output_pass, width = 30, font='Bold 16').pack() 
Button(root, text = 'Copy to Clipboard', command = copyPass, font="Bold 16", bg='yellow', fg='black', activebackground="Teal", padx=6, pady=6 ).pack(pady= 20)
root.mainloop()  