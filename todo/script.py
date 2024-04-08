import tkinter as tk


class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []  # List to store tasks
        self.task_var = tk.StringVar()  # Variable for new task entry

        self.create_widgets()

    def create_widgets(self):
        # Label for task entry
        task_label = tk.Label(self.master, text="New Task:")
        task_label.pack(pady=10)

        # Entry field for new task
        self.task_entry = tk.Entry(self.master, textvariable=self.task_var)
        self.task_entry.pack(padx=10, pady=5)

        # Button to add task
        add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        # Listbox to display tasks
        self.task_list = tk.Listbox(self.master, height=10,width=25)
        self.task_list.pack(padx=10, pady=10)

        # Button to remove selected task
        remove_button = tk.Button(
            self.master, text="Remove Task", command=self.remove_task
        )
        remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_var.get().strip()  # Get task text and remove whitespace
        if task:  # Check if task is not empty
            self.tasks.append(task)  # Add task to the list
            self.task_list.insert(tk.END, task)  # Add task to listbox
            self.task_var.set("")  # Clear entry field for next task

    def remove_task(self):
        selected = self.task_list.curselection()  # Get index of selected item
        if selected:
            task_to_remove = self.tasks[selected[0]]  # Get task to remove
            self.tasks.remove(task_to_remove)  # Remove task from list
            self.task_list.delete(selected[0])  # Remove task from listbox


root = tk.Tk()
app = ToDoList(root)
root.mainloop()
