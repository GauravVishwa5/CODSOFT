from tkinter import *
import os

class ToDolist:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry('700x450+350+200')

        self.label = Label(self.root, text='TO-Do List', font='ariel, 25 bold', width=10, bd=5,
                           bg='#03fca1', fg="black")
        self.label.pack(side='top', fill=BOTH)

        self.label_2 = Label(self.root, text='Add List', font='ariel, 18 bold', width=10, bd=5,
                             bg='#03fca1', fg="black")
        self.label_2.place(x=40, y=54)

        self.label_3 = Label(self.root, text='Lists', font='ariel, 18 bold', width=10, bd=5,
                             bg='#03fca1', fg="black")
        self.label_3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=16, bd=5, width=40, font='ariel,20')
        self.main_text.place(x=250, y=100)

        self.text = Text(self.root, bd=5, height=2, width=30, font='ariel, 10 bold')
        self.text.place(x=20, y=100)

        # =================Add Tasks===========================
        self.check_file()

        self.button = Button(self.root, text='Add', font='20', width=10, bd=5,
                             bg='#03fca1', fg="black", command=self.add)
        self.button.place(x=30, y=180)

        self.button_1 = Button(self.root, text='Delete', font='20', width=10, bd=5,
                               bg='#03fca1', fg="black", command=self.delT)
        self.button_1.place(x=30, y=220)

        self.button_2 = Button(self.root, text='Update', font='20', width=10, bd=5,
                               bg='#03fca1', fg="black", command=self.update_task)
        self.button_2.place(x=30, y=260)

    def check_file(self):
        if not os.path.exists('To-Dolist/list.txt'):
            with open('To-Dolist/list.txt', 'w'):
                pass

        with open('To-Dolist/list.txt', 'r') as file:
            read = file.readlines()
            for i in read:
                readt = i.split()
                self.main_text.insert(END, readt)

    def add(self):
        addlist = self.text.get(1.0, END)
        self.main_text.insert(END, addlist)
        with open('To-Dolist/list.txt', 'a') as file:
            file.write(addlist)
        self.text.delete(1.0, END)

    def delT(self):
        del_text = self.main_text.curselection()
        if del_text:
            self.main_text.delete(del_text)
            self.save_to_file()

    def update_task(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            updated_task = self.text.get(1.0, END)
            self.main_text.delete(selected_index)
            self.main_text.insert(selected_index, updated_task)
            self.save_to_file()
            self.text.delete(1.0, END)

    def save_to_file(self):
        with open('To-Dolist/list.txt', 'w') as file:
            for task in self.main_text.get(0, END):
                file.write(task)

def main():
    root = Tk()
    ui = ToDolist(root)
    root.mainloop()

if __name__ == "__main__":
    main()
