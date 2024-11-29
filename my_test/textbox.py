import customtkinter as ctk

class SyncableTextBox(ctk.CTkTextbox):
    def __init__(self, master, text_variable: ctk.StringVar, **kwargs):
        """
        A CTkTextbox synchronized with a StringVar.

        :param master: The parent widget.
        :param text_variable: A StringVar to synchronize with the textbox content.
        :param kwargs: Additional arguments for CTkTextbox.
        """
        super().__init__(master, **kwargs)
        self.text_variable = text_variable

        # Bind the StringVar to update the textbox when it changes
        self.text_variable.trace_add("write", self._update_textbox)

        # Insert initial content from StringVar
        self.insert("1.0", self.text_variable.get())

        # Optionally enable editing
        self.configure(state="disabled")  # Set to "disabled" for read-only

        # Bind to update the StringVar when the content of the textbox changes
        self.bind("<KeyRelease>", self._update_stringvar)

    def _update_textbox(self, *args):
        """Update the content of the textbox when the StringVar changes."""
        self.configure(state="normal")  # Temporarily enable editing to update content
        self.delete("1.0", "end")
        self.insert("1.0", self.text_variable.get())
        self.configure(state="disabled")  # Keep editable (or set to "disabled" for read-only)

    def _update_stringvar(self, event=None):
        """Update the StringVar when the content of the textbox changes."""
        self.text_variable.set(self.get("1.0", "end-1c"))

# Example usage
if __name__ == "__main__":
    # Initialize the main window
    root = ctk.CTk()
    root.geometry("500x400")
    root.title("Syncable CTkTextbox Example")

    # Create a StringVar
    text_var = ctk.StringVar()
    text_var.set("This is the initial text.\nIt will stay synchronized.")

    # Create the syncable textbox
    textbox = SyncableTextBox(root, text_variable=text_var, width=400, height=300, wrap="word")
    textbox.pack(padx=20, pady=20, fill="both", expand=True)

    # Example: Modify the StringVar after 3 seconds
    def modify_text_variable():
        text_var.set("The content has been updated externally via StringVar!")

    root.after(3000, modify_text_variable)

    root.mainloop()
