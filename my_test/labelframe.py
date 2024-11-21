from customtkinter import CTk, CTkFrame, CTkLabel, CTkFont, set_default_color_theme

# Create the main window
root = CTk()
root.geometry("400x300")
root.title("Custom LabelFrame Example")
set_default_color_theme("dark-blue")

# Define a custom font for the label
custom_font = CTkFont(family="Helvetica", size=16, weight="bold")

# Create the main frame to act as a LabelFrame
frame = CTkFrame(master=root, width=300, height=200, corner_radius=10)
frame.pack(pady=20, padx=20)

# Create the label for the frame
label = CTkLabel(master=root, text="Custom LabelFrame", font=custom_font)
label.place(x=40, y=30)  # Adjust x and y to position above the frame

# Place widgets inside the frame
inner_label = CTkLabel(master=frame, text="Content inside the frame")
inner_label.pack(pady=20, padx=20)

root.mainloop()
