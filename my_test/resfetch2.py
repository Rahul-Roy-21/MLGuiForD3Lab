import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageSequence
import json

# Reference to the progress window
progress_window = None

# Function to handle submit button click
def on_submit():
    global progress_window

    # Check if the progress window already exists
    if progress_window is not None and progress_window.winfo_exists():
        progress_window.lift()  # Bring the existing window to the front
        return

    # Create the progress window
    progress_window = ctk.CTkToplevel(root, fg_color='white')
    progress_window.geometry("120x120")
    progress_window.title("In Progress")
    
    # Label to display the GIF
    gif_label = ctk.CTkLabel(progress_window, text="Loading", compound=ctk.TOP)
    gif_label.pack(pady=20)
    
    # Load and play GIF using CTkImage
    gif_path = "images/loading.gif"
    gif_image = Image.open(gif_path)

    frames = [ctk.CTkImage(frame.copy(), size=(100, 100)) for frame in ImageSequence.Iterator(gif_image)]

    def play_gif(frame=0):
        gif_label.configure(image=frames[frame])
        frame = (frame + 1) % len(frames)  # Loop the GIF
        progress_window.after(100, lambda: play_gif(frame))

    play_gif()  # Start the GIF animation

    # After 5 seconds, close the window and update the result
    def update_result():
        global progress_window
        if progress_window and progress_window.winfo_exists():
            progress_window.destroy()
            progress_window = None
        result = {'results': var_A.get()}
        var_B.set(json.dumps(result, indent=4))

    progress_window.after(5000, update_result)

# Create main window
root = ctk.CTk()
root.geometry("500x300")
root.title("Customtkinter Example")

# Create StringVar for A and B
var_A = tk.StringVar()
var_B = tk.StringVar()

# Entry for A
ctk.CTkLabel(root, text="Input A:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_A = ctk.CTkEntry(root, textvariable=var_A)
entry_A.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Submit Button
submit_button = ctk.CTkButton(root, text="Submit", command=on_submit)
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

# Textbox for B
ctk.CTkLabel(root, text="Result B:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
textbox_B = ctk.CTkTextbox(root, height=10)
textbox_B.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Bind var_B to update textbox
def update_textbox(*args):
    textbox_B.delete("1.0", tk.END)
    textbox_B.insert(tk.END, var_B.get())

var_B.trace_add("write", update_textbox)

# Configure grid
root.columnconfigure(1, weight=1)

root.mainloop()

