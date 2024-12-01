from customtkinter import *
from PIL import Image
from os import path as os_path

# COLORS
COLORS={
    'MEDIUMGREEN_FG':'#218530',
    'MEDIUMGREEN_HOVER_FG':'#319941',
    'LIGHTRED_FG':'#c94259',
    'LIGHTRED_HOVER_FG':'#d9596e',
    'SKYBLUE_FG':'#99e6ff',
    'GREY_HOVER_FG':'#a3a2a3',
    'GREY_FG':'#6b6a6b',
    'LIGHT_YELLOW_FG':'#fff1cc'
}

def getImgPath (img_name, image_dir='images'):
    return os_path.join(image_dir, img_name)

class MultiSelectEntry(CTkFrame):
    def __init__(self, parent:CTkFrame, whatToChoosePlural:str, my_font:CTkFont, tkVar:StringVar, options:list[str], MIN_CHOOSE:int=2):
        super().__init__(parent)
        parent.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])

        self.whatToChoosePlural=whatToChoosePlural
        self.my_font = my_font
        self.selectedOptions_var = tkVar
        self.options=options
        self.MIN_CHOOSE = MIN_CHOOSE
        self.search_image = CTkImage(Image.open(getImgPath("search.png")), size=(24, 24))

        self.value_label = CTkEntry(
            self, textvariable=self.selectedOptions_var ,font=my_font, border_width=0, justify=CENTER,
            fg_color="white", text_color="black", state='disabled', corner_radius=0
        )
        self.value_label.grid(row=0, column=0, sticky=NSEW)

        self.select_button = CTkButton(
            self, image=self.search_image, text="", 
            fg_color=COLORS["GREY_FG"],
            hover_color=COLORS["GREY_HOVER_FG"],
            command=self.open_selection_window, width=50, corner_radius=0
        )
        self.select_button.grid(row=0, column=1)

    def open_selection_window(self):
        MultiSelectDialog(self, self.whatToChoosePlural, self.options, self.selectedOptions_var, self.my_font, self.MIN_CHOOSE)

class MyIntegerEntry(CTkFrame):
    def __init__(self, parent:CTkFrame, my_font:CTkFont, tkVar:IntVar, min_value=1, max_value=100):
        super().__init__(parent)
        parent.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0)
        self.grid_columnconfigure(1, weight=1)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])
        
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = tkVar
        self.hold_job = None  # To track repeating commands

        # Load images for buttons
        self.minus_image = CTkImage(Image.open(getImgPath("minus.png")), size=(24, 24))
        self.plus_image = CTkImage(Image.open(getImgPath("add.png")), size=(24, 24))
        
        # Decrement button with image
        self.decrement_button = CTkButton(
            self, image=self.minus_image, text="", 
            fg_color=COLORS["SKYBLUE_FG"],
            hover_color=COLORS["LIGHTRED_HOVER_FG"],
            command=self.decrement, width=20
        )
        self.decrement_button.grid(row=0, column=0)
        self.decrement_button.bind("<ButtonPress-1>", lambda event: self.start_repeat(self.decrement))
        self.decrement_button.bind("<ButtonRelease-1>", self.stop_repeat)
        
        # Value label
        self.value_label = CTkEntry(
            self, textvariable=self.current_value ,font=my_font, border_width=0, justify=CENTER,
            fg_color="white", text_color="black", state='disabled', width=60
        )
        self.value_label.grid(row=0, column=1)

        # Increment button with image
        self.increment_button = CTkButton(
            self, image=self.plus_image, text="", 
            fg_color=COLORS["SKYBLUE_FG"],
            hover_color=COLORS["MEDIUMGREEN_HOVER_FG"],
            command=self.increment, width=20
        )
        self.increment_button.grid(row=0, column=2)
        self.increment_button.bind("<ButtonPress-1>", lambda event: self.start_repeat(self.increment))
        self.increment_button.bind("<ButtonRelease-1>", self.stop_repeat)
    
    def increment(self):
        """Increase the current value, ensuring it doesn't exceed max_value."""
        if self.current_value.get() < self.max_value:
            self.current_value.set(self.current_value.get()+1)
    
    def decrement(self):
        """Decrease the current value, ensuring it doesn't go below min_value."""
        if self.current_value.get() > self.min_value:
            self.current_value.set(self.current_value.get()-1)

    def start_repeat(self, command):
        """Start repeating the given command."""
        if self.hold_job is None:
            self.hold_job = self.after(100, lambda: self.repeat_command(command))

    def repeat_command(self, command):
        """Repeat the command while the button is held."""
        command()
        self.hold_job = self.after(100, lambda: self.repeat_command(command))

    def stop_repeat(self, event):
        """Stop repeating the command when the button is released."""
        if self.hold_job is not None:
            self.after_cancel(self.hold_job)
            self.hold_job = None

class MyFloatingLogEntry(CTkFrame):
    def __init__(self, parent: CTkFrame, my_font: CTkFont, tkVar: DoubleVar, min_value=1e-5, max_value=1e5):
        super().__init__(parent)
        parent.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0)
        self.grid_columnconfigure(1, weight=1)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = tkVar
        self.hold_job = None  # To track repeating commands

        # Bind a trace to update the display value
        self.current_value.trace_add("write", self.update_display)

        # Load images for buttons
        self.minus_image = CTkImage(Image.open(getImgPath("minus.png")), size=(24, 24))
        self.plus_image = CTkImage(Image.open(getImgPath("add.png")), size=(24, 24))

        # Decrement button
        self.decrement_button = CTkButton(
            self, image=self.minus_image, text="",
            fg_color=COLORS["SKYBLUE_FG"],
            hover_color=COLORS["LIGHTRED_HOVER_FG"],
            command=self.decrement, width=20
        )
        self.decrement_button.grid(row=0, column=0)
        self.decrement_button.bind("<ButtonPress-1>", lambda event: self.start_repeat(self.decrement))
        self.decrement_button.bind("<ButtonRelease-1>", self.stop_repeat)

        # Value label
        self.value_label = CTkEntry(
            self, font=my_font, border_width=0, justify=CENTER,
            fg_color="white", text_color="black", state='readonly', width=80
        )
        self.value_label.grid(row=0, column=1)

        # Increment button
        self.increment_button = CTkButton(
            self, image=self.plus_image, text="",
            fg_color=COLORS["SKYBLUE_FG"],
            hover_color=COLORS["MEDIUMGREEN_HOVER_FG"],
            command=self.increment, width=20
        )
        self.increment_button.grid(row=0, column=2)
        self.increment_button.bind("<ButtonPress-1>", lambda event: self.start_repeat(self.increment))
        self.increment_button.bind("<ButtonRelease-1>", self.stop_repeat)

        # Initialize the display
        self.update_display()

    def update_display(self, *args):
        """Update the entry field with the formatted value."""
        value = self.current_value.get()
        formatted_value = f"{value:.6f}".rstrip("0").rstrip(".")
        self.value_label.configure(state="normal")  # Temporarily enable editing
        self.value_label.delete(0, "end")
        self.value_label.insert(0, formatted_value)
        self.value_label.configure(state="readonly")  # Revert to readonly

    def increment(self):
        """Multiply the current value by 10, ensuring it doesn't exceed max_value."""
        new_value = self.current_value.get() * 10
        if new_value <= self.max_value:
            self.current_value.set(new_value)

    def decrement(self):
        """Divide the current value by 10, ensuring it doesn't go below min_value."""
        new_value = self.current_value.get() / 10
        if new_value >= self.min_value:
            self.current_value.set(new_value)

    def start_repeat(self, command):
        """Start repeating the given command."""
        if self.hold_job is None:
            self.hold_job = self.after(100, lambda: self.repeat_command(command))

    def repeat_command(self, command):
        """Repeat the command while the button is held."""
        command()
        self.hold_job = self.after(100, lambda: self.repeat_command(command))

    def stop_repeat(self, event):
        """Stop repeating the command when the button is released."""
        if self.hold_job is not None:
            self.after_cancel(self.hold_job)
            self.hold_job = None

class MyRangeEntry(CTkFrame):
    def __init__(self, parent:CTkFrame,
            from_var:IntVar, to_var:IntVar,
            my_font:CTkFont, MIN_VAL, MAX_VAL, **kwargs
        ):
        super().__init__(parent, **kwargs)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])

        # Assign the IntVars to the instance
        self.from_var = from_var
        self.to_var = to_var

        # Validation logic
        self.from_var.trace_add("write", self.sync_to_var)
        self.to_var.trace_add("write", self.sync_from_var)

        self.label_from = CTkLabel(self, text="From:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_from.grid(row=0, column=0, padx=2, pady=5, sticky="e")
        self.entry_from = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.from_var, min_value=MIN_VAL, max_value=MAX_VAL-1)
        self.entry_from.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_to = CTkLabel(self, text="To:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_to.grid(row=0, column=2, padx=2, pady=5, sticky="e")
        self.entry_to = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.to_var, min_value=MIN_VAL+1, max_value=MAX_VAL)
        self.entry_to.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    
    def sync_to_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if from_value == to_value:
            self.to_var.set(from_value+1)

    def sync_from_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if to_value == from_value:
            self.from_var.set(to_value-1)

class MyFloatingLogRangeEntry(CTkFrame):
    def __init__(self, parent:CTkFrame,
            from_var:DoubleVar, to_var:DoubleVar,
            my_font:CTkFont, MIN_VAL:float, MAX_VAL:float, **kwargs
        ):
        super().__init__(parent, **kwargs)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])

        # Assign the IntVars to the instance
        self.from_var = from_var
        self.to_var = to_var

        # Validation logic
        self.from_var.trace_add("write", self.sync_to_var)
        self.to_var.trace_add("write", self.sync_from_var)

        self.label_from = CTkLabel(self, text="From:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_from.grid(row=0, column=0, padx=2, pady=5, sticky="e")
        self.entry_from = MyFloatingLogEntry(parent=self, my_font=my_font, tkVar=self.from_var, min_value=MIN_VAL, max_value=MAX_VAL/10)
        self.entry_from.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_to = CTkLabel(self, text="To:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_to.grid(row=0, column=2, padx=2, pady=5, sticky="e")
        self.entry_to = MyFloatingLogEntry(parent=self, my_font=my_font, tkVar=self.to_var, min_value=MIN_VAL*10, max_value=MAX_VAL)
        self.entry_to.grid(row=0, column=3, padx=5, pady=5, sticky="w")
    
    def sync_to_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if from_value == to_value:
            self.to_var.set(from_value*10)

    def sync_from_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if to_value == from_value:
            self.from_var.set(to_value/10)

class MyStepRangeEntry(MyRangeEntry):
    def __init__(self, parent:CTkFrame,
            from_var:IntVar, to_var:IntVar, step_var:IntVar, 
            my_font:CTkFont, MIN_VAL, MAX_VAL, MAX_STEPS, **kwargs
        ):
        super().__init__(parent, from_var, to_var, my_font, MIN_VAL, MAX_VAL, **kwargs)

        # Assign the IntVars to the instance
        self.step_var = step_var

        self.label_step = CTkLabel(self, text="Step:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_step.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.entry_step = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.step_var, min_value=1, max_value=MAX_STEPS)
        self.entry_step.grid(row=0, column=5, padx=5, pady=5, sticky="w")

class MyStepRangeEntry1(CTkFrame):
    def __init__(self, parent:CTkFrame,
            from_var:IntVar, to_var:IntVar, step_var:IntVar, 
            my_font:CTkFont, MIN_VAL, MAX_VAL, MAX_STEPS, **kwargs
        ):
        super().__init__(parent, **kwargs)
        self.configure(fg_color=COLORS["SKYBLUE_FG"])

        # Assign the IntVars to the instance
        self.from_var = from_var
        self.to_var = to_var
        self.step_var = step_var

        # Validation logic
        self.from_var.trace_add("write", self.sync_to_var)
        self.to_var.trace_add("write", self.sync_from_var)

        self.label_from = CTkLabel(self, text="From:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_from.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_from = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.from_var, min_value=MIN_VAL, max_value=MAX_VAL-1)
        self.entry_from.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.label_to = CTkLabel(self, text="To:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_to.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.entry_to = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.to_var, min_value=MIN_VAL+1, max_value=MAX_VAL)
        self.entry_to.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        self.label_step = CTkLabel(self, text="Step:", font=my_font, fg_color=COLORS["SKYBLUE_FG"])
        self.label_step.grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.entry_step = MyIntegerEntry(parent=self, my_font=my_font, tkVar=self.step_var, min_value=1, max_value=MAX_STEPS)
        self.entry_step.grid(row=0, column=5, padx=5, pady=5, sticky="w")
    
    def sync_to_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if from_value == to_value:
            self.to_var.set(from_value+1)

    def sync_from_var(self, *args):
        from_value = self.from_var.get()
        to_value = self.to_var.get()

        if to_value == from_value:
            self.from_var.set(to_value-1)

class MultiSelectDialog(CTkToplevel):
    def __init__(self, parent:CTkFrame, 
            whatToChoosePlural:str, options:list[str], selectedOptions_StringVar: StringVar, 
            my_font:CTkFont, MIN_CHOOSE: int = 2
        ):
        super().__init__(parent)
        self.title(f'Choose {whatToChoosePlural}')
        self.geometry("300x300")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.MIN_CHOOSE=MIN_CHOOSE

        self.selectedOptions_StringVar = selectedOptions_StringVar
        self.selectedOptions = set(selectedOptions_StringVar.get().split(','))
        if len(self.selectedOptions)<MIN_CHOOSE:
            raise Exception(f'Num. of selectedOptions must be {self.MIN_CHOOSE} or more for {whatToChoosePlural}')

        # Row0,1,2,3: ScrollableFrame (with Label)
        scrollable_frame = CTkScrollableFrame(
            self, 
            label_text=f'{whatToChoosePlural} List', 
            label_font=my_font,
            label_fg_color=COLORS['LIGHTRED_FG'],
            label_text_color='white',
            scrollbar_button_color='#333',
            scrollbar_button_hover_color=COLORS['GREY_HOVER_FG'],
            fg_color=COLORS['SKYBLUE_FG']
        )
        scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky=NSEW)
        scrollable_frame.grid_columnconfigure(0, weight=1)

        self.checkboxes = {}
        for idx, option in enumerate(options):
            ctkCheckBox = CTkCheckBox(
                scrollable_frame,
                text=option,
                font=my_font,
                corner_radius=0,
                fg_color=COLORS['MEDIUMGREEN_FG'],
                hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
                border_width=1,
                border_color='#000',
                command=lambda opt=option: self.check_num_of_options(opt)
            )
            ctkCheckBox.grid(row=idx, column=0, padx=10, pady=(10, 0), sticky=W)
            if option in self.selectedOptions:
                ctkCheckBox.select()
            self.checkboxes[option]=ctkCheckBox

        CTkLabel(
            scrollable_frame, text=f'* Num. of {whatToChoosePlural} must be >= {self.MIN_CHOOSE} !!', text_color='red',
            font=my_font, anchor=CENTER
        ).grid(row=idx+1, column=0, padx=10, pady=(10, 0), sticky=NSEW)

        # Row4: Submit Btn
        submit_button = CTkButton(
            self, 
            text="Submit", 
            font=my_font,
            fg_color=COLORS['MEDIUMGREEN_FG'],
            hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
            text_color='white',
            corner_radius=0,
            width=100,
            border_spacing=0,
            command=self.submit
        )
        submit_button.grid(row=4, column=0, padx=10, pady=10, sticky=EW)

    def submit(self):
        # Update selected options based on the state of the checkboxes
        self.selectedOptions=[]
        for option, checkBox in self.checkboxes.items():
            if checkBox.get():
                self.selectedOptions.append(option)

        # Update the StringVar with the selected options
        self.selectedOptions_StringVar.set(
            ','.join(sorted(self.selectedOptions)).strip(',')
        )
        self.destroy()

    def check_num_of_options(self, choice):
        print(f'RUNNING check_num_of_options ({choice})')
        # If choice is DESELECTED and Num.of selected < MIN_CHOOSE
        if self.checkboxes[choice].get()==0 and sum(cbox.get() for cbox in self.checkboxes.values()) < self.MIN_CHOOSE:
            self.checkboxes[choice].select()
    
class SyncableTextBox(CTkTextbox):
    def __init__(self, master, text_variable: StringVar, my_font: CTkFont, **kwargs):
        """
        A CTkTextbox synchronized with a StringVar.
        :param master: The parent widget.
        :param text_variable: A StringVar to synchronize with the textbox content.
        """
        super().__init__(master, height=100, font=my_font, fg_color=COLORS["LIGHT_YELLOW_FG"] ,**kwargs)
        self.text_variable = text_variable

        # Bind the StringVar to update the textbox when it changes
        self.text_variable.trace_add("write", self._update_textbox)

        # Insert initial content from StringVar
        self.insert("1.0", self.text_variable.get())

        # Set "normal" for optionally enable editing, Set to "disabled" for read-only
        self.configure(state="disabled")  

        # Bind to update the StringVar when the content of the textbox changes
        self.bind("<KeyRelease>", self._update_stringvar)

    def _update_textbox(self, *args):
        """Update the content of the textbox when the StringVar changes."""
        self.configure(state="normal")  # Temporarily enable editing to update content
        self.delete("1.0", "end")
        self.insert("1.0", self.text_variable.get())
        self.configure(state="disabled")  # Keep non-editable (or set to "disabled" for read-only)

    def _update_stringvar(self, event=None):
        """Update the StringVar when the content of the textbox changes."""
        self.text_variable.set(self.get("1.0", "end-1c"))