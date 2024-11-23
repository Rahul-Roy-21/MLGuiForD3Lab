import customtkinter as ctk

class RangeValueEntry(ctk.CTkFrame):
    def __init__(self, parent, from_var, to_var, step_var, **kwargs):
        super().__init__(parent, **kwargs)

        # Assign the IntVars to the instance
        self.from_var = from_var
        self.to_var = to_var
        self.step_var = step_var

        # Create and place widgets in a single row
        self.label_name = ctk.CTkLabel(self, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.label_from = ctk.CTkLabel(self, text="From:")
        self.label_from.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_from = ctk.CTkEntry(self, textvariable=self.from_var, width=50)
        self.entry_from.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.label_to = ctk.CTkLabel(self, text="To:")
        self.label_to.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.entry_to = ctk.CTkEntry(self, textvariable=self.to_var, width=50)
        self.entry_to.grid(row=0, column=4, padx=5, pady=5, sticky="w")

        self.label_step = ctk.CTkLabel(self, text="Step:")
        self.label_step.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        self.entry_step = ctk.CTkEntry(self, textvariable=self.step_var, width=50)
        self.entry_step.grid(row=0, column=6, padx=5, pady=5, sticky="w")


# Example Usage
if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("600x100")
    app.title("Range Value Entry Example")

    # Create IntVars for from, to, and step
    from_var = ctk.IntVar(value=0)
    to_var = ctk.IntVar(value=100)
    step_var = ctk.IntVar(value=10)

    # Create and place the RangeValueEntry instance
    range_entry = RangeValueEntry(app, from_var, to_var, step_var)
    range_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    app.mainloop()
