import tkinter as tk
from tkinter import ttk


class MadlibApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Madlib")
        self.geometry("320x240")
        self.resizable(False, False)

        self.page_frames = {
            "home": tk.Frame(self),
            "page1": tk.Frame(self),
            "page2": tk.Frame(self),
            "page3": tk.Frame(self),
        }

        self.story_templates = {
            "page1": "Today I went to the {adjective1} zoo. I saw a {adjective2} {animal}.",
            "page2": "I went on a {adjective1} roller coaster and then ate a {adjective2} {food}.",
            "page3": "On the way {adjective1}, I saw a {adjective2} car and a {adjective3} person."
        }

        self.current_selections = {}  # Dictionary to store user selections


        self.create_home_page()
        self.create_page1()
        self.create_page2()
        self.create_page3()

        self.show_page("home")

    def create_home_page(self):
        page0 = self.page_frames["home"]
        page0.grid(row=0, column=0, sticky="nsew")

        Label0 = tk.Label(page0, text="Select a Story", justify="center", width=45, height=2)
        Label0.pack()

        button1 = tk.Button(
            page0, text="Story 1", width=25, height=2, command=lambda: self.show_page("page1")
        )
        button1.pack()

        button2 = tk.Button(
            page0, text="Story 2", width=25, height=2, command=lambda: self.show_page("page2")
        )
        button2.pack()

        button3 = tk.Button(
            page0, text="Story 3", width=25, height=2, command=lambda: self.show_page("page3")
        )
        button3.pack()

    def create_page1(self):
        page1 = self.page_frames["page1"]
        page1.grid(row=0, column=0, sticky="nsew")

        Label1 = tk.Label(page1, text="Story 1",justify="center", width=45, height=2)
        Label1.pack()

        # Create comboboxes with options and handlers
        self.create_comboboxes(page1, [["","wonderful", "enormous", "tiny"],["","angry","cute","mad"],["","panther","duck","mountain goat"]],"page1")

        button_home = tk.Button(page1, text="Home", width=10, height=2, command=lambda: self.show_page("home"))
        button_home.pack()

        button_generate = tk.Button(
            page1, text="Generate Story", width=15, height=2, command=self.generate_story1
        )
        button_generate.pack()

    def create_page2(self):
        page2 = self.page_frames["page2"]
        page2.grid(row=0, column=0, sticky="nsew")

        Label2 = tk.Label(page2, text="Story 2",justify="center", width=45, height=2)
        Label2.pack()

        # Create comboboxes with options and handlers
        self.create_comboboxes(page2, [["","terrifying", "delicious", "greasy"],["","tiny","Salty","Smoky"],["","pizza","egg","rise"]],"page2")

        button_home = tk.Button(page2, text="Home", width=10, height=2, command=lambda: self.show_page("home"))
        button_home.pack()

        button_generate = tk.Button(
            page2, text="Generate Story", width=15, height=2, command=self.generate_story2
        )
        button_generate.pack()

    def create_page3(self):
        page3 = self.page_frames["page3"]
        page3.grid(row=0, column=0, sticky="nsew")

        Label3 = tk.Label(page3, text="Story 3",justify="center", width=45, height=2)
        Label3.pack()
        
        
        # Create comboboxes with options and handlers
        self.create_comboboxes(page3, [["","home", "gym", "office"],["","yellow", "black", "white"],["","classy", "crazy", "Loaded"]],"page3")

        button_home = tk.Button(page3, text="Home", width=10, height=2, command=lambda: self.show_page("home"))
        button_home.pack()

        button_generate = tk.Button(
            page3, text="Generate Story", width=15, height=2, command=self.generate_story3
        )
        button_generate.pack()

        # Create comboboxes with options and
    def create_comboboxes(self, page_frame, options,name_page):
        """Creates three comboboxes with given options on the specified frame."""
        combobox1 = ttk.Combobox(page_frame, values=options[0], state="readonly")
        combobox1.current(0)  # Set first option as default
        combobox1.bind("<<ComboboxSelected>>", lambda event, frame=page_frame, index=1: self.handle_selection(event, frame, index,name_page))
        combobox1.pack()

        combobox2 = ttk.Combobox(page_frame, values=options[1], state="readonly")
        combobox2.current(0)  # Set first option as default
        combobox2.bind("<<ComboboxSelected>>", lambda event, frame=page_frame, index=2: self.handle_selection(event, frame, index,name_page))
        combobox2.pack()

        combobox3 = ttk.Combobox(page_frame, values=options[2], state="readonly")
        combobox3.current(0)  # Set first option as default
        combobox3.bind("<<ComboboxSelected>>", lambda event, frame=page_frame, index=3: self.handle_selection(event, frame, index,name_page))
        combobox3.pack()

    def handle_selection(self, event, frame, index,name_page):
        """Stores user selection for the specified combobox index on the given frame."""
        page_name = frame.winfo_name()  # Get the page name from the frame's name
        
        selected_option = event.widget.get()
        print(111,f"{name_page}_combobox{index}", selected_option,page_name)
        self.current_selections[f"{name_page}_combobox{index}"] = selected_option

    def generate_story1(self):
        """Generates the story for page 1 using the stored selections."""
        story_template = self.story_templates["page1"]
        adjective1 = self.current_selections.get("page1_combobox1")
        adjective2 = self.current_selections.get("page1_combobox2")
        animal1 = self.current_selections.get("page1_combobox3")
        print(adjective1,adjective2,animal1, self.current_selections)

        story = story_template.format(adjective1=adjective1 or "___", adjective2=adjective2 or "___" ,animal=animal1 or "___")
        self.display_story(story)

    def generate_story2(self):
        """Generates the story for page 2 using the stored selections."""
        # Similar logic as generate_story1, replace placeholders with your implementation
        story_template = self.story_templates["page2"]
        adjective1 = self.current_selections.get("page2_combobox1")
        adjective2 = self.current_selections.get("page2_combobox2")
        food = self.current_selections.get("page2_combobox3")
        print(adjective1,adjective2,food, self.current_selections)


        story = story_template.format(adjective1=adjective1 or "___",adjective2=adjective2 or "___",food=food or "___")
        self.display_story(story)

    def generate_story3(self):
        """Generates the story for page 3 using the stored selections."""
        # Similar logic as generate_story1, replace placeholders with your implementation
        story_template = self.story_templates["page3"]
        adjective1 = self.current_selections.get("page3_combobox1")
        adjective2 = self.current_selections.get("page3_combobox2")
        adjective3 = self.current_selections.get("page3_combobox3")


        story = story_template.format(adjective1=adjective1 or "___",adjective2=adjective2 or "___",adjective3=adjective3 or "___")
        self.display_story(story)
        
    def display_story(self, story):
        """Displays the generated story in a new window."""
        story_window = tk.Toplevel(self)
        story_window.title("Your Madlib Story")
        story_label = tk.Label(story_window, text=story, font=("Arial", 12))
        story_label.pack()

    def show_page(self, page_name):
        for frame in self.page_frames.values():
            frame.grid_remove()
        self.page_frames[page_name].grid()

if __name__ == "__main__":
    app = MadlibApp()
    app.mainloop()