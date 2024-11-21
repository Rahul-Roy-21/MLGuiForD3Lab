import customtkinter as ctk
from tkinter import LabelFrame, Label, Entry

# Initialize main window
root = ctk.CTk()
root.geometry("400x300")
root.title("Tkinter LabelFrame Inside CTkFrame")

custom_font = ("appleGothic", 14, "bold")

# Create a CTkFrame
outer_frame = ctk.CTkFrame(root, width=350, height=250, corner_radius=15, fg_color='lightgreen')
outer_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Add a LabelFrame from Tkinter inside the CTkFrame
label_frame = LabelFrame(outer_frame, text="My LabelFrame Title", font=custom_font, labelanchor="nw", background='lightgreen')
label_frame.place(relx=0.5, rely=0.5, anchor="center", width=300, height=200)

# Add widgets inside the LabelFrame
label1 = Label(label_frame, text="Label 1:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")

entry1 = Entry(label_frame, font=custom_font)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = Label(label_frame, text="Label 2:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="w")

entry2 = Entry(label_frame)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Run the application
root.mainloop()
