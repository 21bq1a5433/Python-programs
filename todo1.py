from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Empty field')  
    else:  
        tasks.append(task_string)  
        the_cursor.execute('insert to task value', (task_string ,))  
        list_update()  
        task_field.delete(0, 'end')  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_listbox.insert('end', task)    
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())  
        if the_value in tasks:  
            tasks.remove(the_value)  
            list_update()  
            the_cursor.execute('delete tasks', (the_value,))  
    except:  
        messagebox.showinfo('Error', 'No task selected')            
def clear_list():  
    task_listbox.delete(0, 'end')  
def close():  
    print(tasks)  
    guiWindow.destroy()    
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])    
if __name__ == "__main__":  
    guiWindow = Tk()  
    guiWindow.title("To-Do List ")  
    guiWindow.geometry("665x400+550+250")  
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "red")    
    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')  
    tasks = []
    functions_frame = Frame(guiWindow, bg = "white")   
    functions_frame.pack(side = "top", expand = True, fill = "both")  
    task_label = Label( functions_frame,text = "Enter the Task:",  
        font = ("arial", "16", "italic"),  
        background = "black", 
        foreground="white"
    )  
    task_label.place(x = 20, y = 30)  
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "16"),  
        width = 42,  
        foreground="black",
        background = "white",  
    )  
    task_field.place(x = 180, y = 30)    
    add_button =Button(  
        functions_frame,  
        text = "Add Task",  
        width = 15,
        bg='red',font=("arial", "16", "italic"),
        command = add_task,        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 15,
        bg='red', font=("arial", "16", "italic"),
        command = delete_task,  
    )  
    exit_button = Button(  
        functions_frame,  
        text = "Exit",  
        width = 52,
        bg='red',  font=("arial", "16", "italic"),
        command = close  
    )  
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    exit_button.place(x = 17, y = 330)    
    task_listbox = Listbox(  
        functions_frame,  
        width = 57,  
        height = 7,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "red",  
        selectforeground="BLACK"
    )  
    task_listbox.place(x = 17, y = 140)    
    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()