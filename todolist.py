import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10,bg="light blue",fg="black")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(self.button_frame, text="Add Task",bg="light blue",fg="black", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task",bg="light blue",fg="black", command=self.delete_task)
        self.delete_task_button.pack(side=tk.LEFT, padx=5)

        self.clear_tasks_button = tk.Button(self.button_frame, text="Clear Tasks",bg="light blue",fg="black", command=self.clear_tasks)
        self.clear_tasks_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def clear_tasks(self):
        self.tasks = []
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()