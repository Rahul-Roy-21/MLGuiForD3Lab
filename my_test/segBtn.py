from customtkinter import *

# Create main window
root = CTk()
root.geometry("400x200")
root.title("CTkSegmentedButton Example")

tabview = CTkTabview(master=root)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)

root.mainloop()
