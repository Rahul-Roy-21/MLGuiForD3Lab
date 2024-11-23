import customtkinter as ctk
from PIL import Image

class CustomOptionMenu(ctk.CTkOptionMenu):
    def __init__(self, *args, dropdown_image=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Modify dropdown button appearance with an image
        if dropdown_image:
            self.configure(button_image=dropdown_image)

# Main window setup
root = ctk.CTk()
root.title("Custom Option Menu with Dropdown Image")
root.geometry("300x150")

# Load an image for the dropdown button
dropdown_image = ctk.CTkImage(Image.open("images/search.png"), size=(20, 20))

# Create the customized CTkOptionMenu
options = ["Option 1", "Option 2", "Option 3"]
custom_menu = CustomOptionMenu(
    root, values=options, dropdown_image=dropdown_image, fg_color="white", text_color="black", button_hover_color="lightblue"
)
custom_menu.pack(pady=20, padx=20)

root.mainloop()
