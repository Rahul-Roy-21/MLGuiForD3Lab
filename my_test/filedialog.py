import customtkinter as ctk
from tkinter import filedialog

# Initialize the CustomTkinter application
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

class FileDialogApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("CustomTkinter File Dialog Example")
        self.geometry("400x200")

        # Button to open file dialog
        self.open_file_button = ctk.CTkButton(
            self, 
            text="Open File", 
            command=self.open_file_dialog
        )
        self.open_file_button.pack(pady=20)

        # Label to display the selected file path
        self.file_path_label = ctk.CTkLabel(
            self, 
            text="No file selected", 
            wraplength=300,
            justify="center"
        )
        self.file_path_label.pack(pady=20)
    
    def open_file_dialog(self):
        # Open a file dialog and get the selected file path
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if file_path:
            # Update the label with the selected file path
            self.file_path_label.configure(text=f"Selected File: {file_path}")

if __name__ == "__main__":
    app = FileDialogApp()
    app.mainloop()

