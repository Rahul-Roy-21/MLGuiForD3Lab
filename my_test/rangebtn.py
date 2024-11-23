import customtkinter as ctk
from PIL import Image
from os import path as os_path

def getImgPath (img_name, image_dir='images'):
    return os_path.join(image_dir, img_name)

COLORS={
    'MEDIUMGREEN_FG':'#218530',
    'MEDIUMGREEN_HOVER_FG':'#319941',
    'LIGHTRED_FG':'#c94259',
    'LIGHTRED_HOVER_FG':'#d9596e',
    'SKYBLUE_FG':'#99e6ff',
    'GREY_FG':'#727372',
    'GREY_HOVER_FG':'#919191'
}

class CustomRangeEntry(ctk.CTkFrame):
    def __init__(self, parent, min_value=0, max_value=100, initial_value=0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.min_value = min_value
        self.max_value = max_value
        self.current_value = initial_value

        # Load images for buttons
        self.minus_image = ctk.CTkImage(Image.open(getImgPath("minus.png")), size=(24, 24))
        self.plus_image = ctk.CTkImage(Image.open(getImgPath("add.png")), size=(24, 24))
        
        # Decrement button with image
        self.decrement_button = ctk.CTkButton(
            self, image=self.minus_image, text="",
            fg_color=COLORS['LIGHTRED_FG'], 
            hover_color=COLORS['LIGHTRED_HOVER_FG'],
            command=self.decrement, width=30
        )
        self.decrement_button.pack(side="left", fill="y")
        
        # Value label
        self.value_label = ctk.CTkLabel(
            self, text=str(self.current_value), font=("Arial", 14), corner_radius=0, width=50, fg_color="white", text_color="black"
        )
        self.value_label.pack(side="left", fill="y")
        
        # Increment button with image
        self.increment_button = ctk.CTkButton(
            self, image=self.plus_image, text="",
            fg_color=COLORS["MEDIUMGREEN_FG"], 
            hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
            command=self.increment, width=30
        )
        self.increment_button.pack(side="left", fill="y")
    
    def increment(self):
        """Increase the current value, ensuring it doesn't exceed max_value."""
        if self.current_value < self.max_value:
            self.current_value += 1
            self.update_value_label()
    
    def decrement(self):
        """Decrease the current value, ensuring it doesn't go below min_value."""
        if self.current_value > self.min_value:
            self.current_value -= 1
            self.update_value_label()
    
    def update_value_label(self):
        """Update the value displayed in the label."""
        self.value_label.configure(text=str(self.current_value))

# Main window setup
root = ctk.CTk()
root.title("Custom Range Entry with Image Buttons")
root.geometry("300x150")

# Create and add the CustomRangeEntry widget to the window
custom_range_entry = CustomRangeEntry(root, min_value=3, max_value=20, initial_value=10)
custom_range_entry.pack(pady=20, padx=20)

# Run the application
root.mainloop()
