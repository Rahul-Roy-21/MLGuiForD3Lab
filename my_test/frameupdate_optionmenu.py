import customtkinter as ctk

def show_frame(option):
    """Callback to show the frame corresponding to the selected option."""
    for frame in frames.values():
        frame.grid_remove()  # Hide all frames

    frames[option].grid(row=1, column=0, sticky="nsew")  # Show the selected frame

# Create the main window
root = ctk.CTk()
root.geometry("400x300")
root.grid_rowconfigure(1, weight=1)  # Allow frame row to expand
root.grid_columnconfigure(0, weight=1)  # Allow frame column to expand

# Create a dictionary to store frames for each option
frames = {}

# Frame for Option 1
frame1 = ctk.CTkFrame(root)
label1 = ctk.CTkLabel(frame1, text="This is Frame 1 for Option 1")
label1.grid(row=0, column=0, padx=20, pady=20)
frames["Option 1"] = frame1

# Frame for Option 2
frame2 = ctk.CTkFrame(root)
label2 = ctk.CTkLabel(frame2, text="This is Frame 2 for Option 2")
label2.grid(row=0, column=0, padx=20, pady=20)
frames["Option 2"] = frame2

# Frame for Option 3
frame3 = ctk.CTkFrame(root)
label3 = ctk.CTkLabel(frame3, text="This is Frame 3 for Option 3")
label3.grid(row=0, column=0, padx=20, pady=20)
frames["Option 3"] = frame3

# Create an OptionMenu
options = ["Option 1", "Option 2", "Option 3"]
option_menu = ctk.CTkOptionMenu(root, values=options, command=show_frame)
option_menu.grid(row=0, column=0, pady=10, sticky="ew")

# Show the default frame (first option)
option_menu.set("Option 1")  # Set the initial selected value
show_frame("Option 1")

# Start the application
root.mainloop()
