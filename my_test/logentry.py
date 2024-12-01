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

class FloatingLogEntry(CTkFrame):
    def __init__(self, parent: CTkFrame, my_font: CTkFont, tkVar: DoubleVar, min_value=1e-5, max_value=1e5):
        super().__init__(parent)
        parent.grid_columnconfigure(0, weight=1)

        self.grid(row=0, column=0)
        self.grid_columnconfigure(1, weight=1)
        self.configure(fg_color="lightblue")

        self.min_value = min_value
        self.max_value = max_value
        self.current_value = tkVar
        self.hold_job = None  # To track repeating commands

        # Bind a trace to update the display value
        self.current_value.trace_add("write", self.update_display)

        # Decrement button
        self.decrement_button = CTkButton(
            self, text="-",
            fg_color="lightblue",
            hover_color="lightcoral",
            command=self.decrement, width=20
        )
        self.decrement_button.grid(row=0, column=0)
        self.decrement_button.bind("<ButtonPress-1>", lambda event: self.start_repeat(self.decrement))
        self.decrement_button.bind("<ButtonRelease-1>", self.stop_repeat)

        # Value label
        self.value_label = CTkEntry(
            self, font=my_font, border_width=0, justify=CENTER,
            fg_color="white", text_color="black", state='readonly', width=100
        )
        self.value_label.grid(row=0, column=1)

        # Increment button
        self.increment_button = CTkButton(
            self, text="+",
            fg_color="lightblue",
            hover_color="lightgreen",
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


app = CTk()
app.geometry("300x200")
app.title("FloatingLogEntry Demo")

# Define a font and DoubleVar
font = CTkFont(family="Arial", size=14)
float_var = DoubleVar(value=0.001)

# Create a FloatingLogEntry widget
log_entry = FloatingLogEntry(app, font, float_var, min_value=1e-5, max_value=1e5)
log_entry.grid(padx=20, pady=20)

app.mainloop()

