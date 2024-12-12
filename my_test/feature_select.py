import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd

# Function to check if both files have identical column sets
def CHECK_FILES(train_path, test_path):
    try:
        train_columns = set(pd.read_excel(train_path).columns)
        test_columns = set(pd.read_excel(test_path).columns)
        return train_columns == test_columns, list(train_columns)
    except Exception as e:
        messagebox.showerror("Error", f"Error reading files: {e}")
        return False, []

# Function to populate the featureMultiSelectEntry with column names
def POPULATE_LOADED_FEATURES(entry_var, columns):
    entry_var.set(", ".join(columns))

class FileSelectorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("File Selector App")
        self.geometry("600x300")

        # Variables to hold file paths
        self.train_file_path = ctk.StringVar()
        self.test_file_path = ctk.StringVar()
        self.feature_entry_var = ctk.StringVar()

        # Train file entry
        self.train_label = ctk.CTkLabel(self, text="Train File:")
        self.train_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.train_entry = ctk.CTkEntry(self, width=400, textvariable=self.train_file_path)
        self.train_entry.grid(row=0, column=1, padx=10, pady=10)
        self.train_button = ctk.CTkButton(self, text="Browse", command=self.select_train_file)
        self.train_button.grid(row=0, column=2, padx=10, pady=10)

        # Test file entry
        self.test_label = ctk.CTkLabel(self, text="Test File:")
        self.test_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.test_entry = ctk.CTkEntry(self, width=400, textvariable=self.test_file_path)
        self.test_entry.grid(row=1, column=1, padx=10, pady=10)
        self.test_button = ctk.CTkButton(self, text="Browse", command=self.select_test_file)
        self.test_button.grid(row=1, column=2, padx=10, pady=10)

        # Feature selection entry
        self.feature_label = ctk.CTkLabel(self, text="Features:")
        self.feature_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.feature_entry = ctk.CTkEntry(self, width=400, textvariable=self.feature_entry_var)
        self.feature_entry.grid(row=2, column=1, padx=10, pady=10)

        # Feature selection button
        self.feature_button = ctk.CTkButton(self, text="Select Features", command=self.select_features)
        self.feature_button.grid(row=3, column=1, pady=20)

    def select_train_file(self):
        path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if path:
            self.train_file_path.set(path)
            self.validate_files()

    def select_test_file(self):
        path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if path:
            self.test_file_path.set(path)
            self.validate_files()

    def validate_files(self):
        if self.train_file_path.get() and self.test_file_path.get():
            valid, columns = CHECK_FILES(self.train_file_path.get(), self.test_file_path.get())
            if valid:
                POPULATE_LOADED_FEATURES(self.feature_entry_var, columns)
            else:
                messagebox.showwarning("Warning", "Train and Test files do not have identical column sets.")
                self.feature_entry_var.set("")

    def select_features(self):
        if not self.train_file_path.get() or not self.test_file_path.get():
            messagebox.showwarning("Warning", "Please select both Train and Test files first.")
            return

        valid, columns = CHECK_FILES(self.train_file_path.get(), self.test_file_path.get())
        if not valid:
            messagebox.showwarning("Warning", "Train and Test files do not have identical column sets.")
            self.feature_entry_var.set("")
        else:
            messagebox.showinfo("Info", "Features are ready for selection!")

if __name__ == "__main__":
    app = FileSelectorApp()
    app.mainloop()
