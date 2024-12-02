import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkEntry

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("DoubleVar Validation Demo")
        self.geometry("400x200")

        self.last_valid_value = 0.0  # Track the last valid value

        # DoubleVar with trace callback
        self.double_var = tk.DoubleVar(value=self.last_valid_value)
        self.double_var.trace_add("write", self.validate_input)

        # CTkEntry
        self.entry = CTkEntry(
            master=self,
            textvariable=self.double_var,
            width=200
        )
        self.entry.pack(pady=20)

    def validate_input(self, *args):
        try:
            # Attempt to get the DoubleVar value
            print(f'Val: {self.last_valid_value}, doubleVar: {self.double_var.get()}')
            value = self.double_var.get()
            self.last_valid_value = value  # Update last valid value
        except tk.TclError:
            self.bell()  # Optional: Audible feedback for invalid input
            self.double_var.set(self.last_valid_value)  # Reset to last valid value
            messagebox.showwarning(
                "Invalid Input", 
                "Invalid input detected! Please enter a valid floating-point number."
            )

# Run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
