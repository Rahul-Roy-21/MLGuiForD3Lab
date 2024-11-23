from customtkinter import *
from PIL import Image
from os import path as os_path

# COLORS
COLORS={
    'MEDIUMGREEN_FG':'#218530',
    'MEDIUMGREEN_HOVER_FG':'#319941',
    'LIGHTRED_FG':'#c94259',
    'LIGHTRED_HOVER_FG':'#d9596e',
    'SKYBLUE_FG':'#99e6ff',
    'GREY_FG':'#727372',
    'GREY_HOVER_FG':'#919191'
}

def getImgPath (img_name, image_dir='images'):
    return os_path.join(image_dir, img_name)

class MultiSelectDialog(CTkToplevel):
    def __init__(self, parent:CTkFrame, 
            whatToChoosePlural:str, options:list[str], selectedOptions_StringVar: StringVar, 
            my_font:CTkFont, MIN_CHOOSE: int = 2
        ):
        super().__init__(parent)
        self.title(f'Choose {whatToChoosePlural}')
        self.geometry("300x300")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.MIN_CHOOSE=MIN_CHOOSE

        self.selectedOptions_StringVar = selectedOptions_StringVar
        self.selectedOptions = set(selectedOptions_StringVar.get().split(','))
        if len(self.selectedOptions)<MIN_CHOOSE:
            raise Exception(f'Num. of selectedOptions must be {self.MIN_CHOOSE} or more for {whatToChoosePlural}')

    
        # Row0,1,2,3: ScrollableFrame (with Label)
        scrollable_frame = CTkScrollableFrame(
            self, 
            label_text=f'{whatToChoosePlural} List', 
            label_font=my_font,
            label_fg_color=COLORS['LIGHTRED_FG'],
            label_text_color='white',
            scrollbar_button_color='#333',
            scrollbar_button_hover_color=COLORS['GREY_HOVER_FG'],
            fg_color=COLORS['SKYBLUE_FG']
        )
        scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        scrollable_frame.grid_columnconfigure(0, weight=1)

        self.checkboxes = {}
        for idx, option in enumerate(options):
            ctkCheckBox = CTkCheckBox(
                scrollable_frame,
                text=option,
                font=my_font,
                corner_radius=0,
                fg_color=COLORS['MEDIUMGREEN_FG'],
                hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
                border_width=1,
                border_color='#000',
                command=lambda opt=option: self.check_num_of_options(opt)
            )
            ctkCheckBox.grid(row=idx, column=0, padx=10, pady=(10, 0), sticky=W)
            if option in self.selectedOptions:
                ctkCheckBox.select()
            self.checkboxes[option]=ctkCheckBox

        CTkLabel(
            scrollable_frame, text=f'* Num. of {whatToChoosePlural} must be >= {self.MIN_CHOOSE} !!', text_color='red',
            font=my_font, anchor=CENTER
        ).grid(row=idx+1, column=0, padx=10, pady=(10, 0), sticky=NSEW)

        # Row4: Submit Btn
        submit_button = CTkButton(
            self, 
            text="Submit", 
            font=my_font,
            fg_color=COLORS['MEDIUMGREEN_FG'],
            hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
            text_color='white',
            corner_radius=0,
            width=100,
            border_spacing=0,
            command=self.submit
        )
        submit_button.grid(row=4, column=0, padx=10, pady=10, sticky=EW)

    def submit(self):
        # Update selected options based on the state of the checkboxes
        self.selectedOptions=[]
        for option, checkBox in self.checkboxes.items():
            if checkBox.get():
                self.selectedOptions.append(option)

        # Update the ctk.StringVar with the selected options
        self.selectedOptions_StringVar.set(
            ','.join(sorted(self.selectedOptions)).strip(',')
        )
        self.destroy()

    def check_num_of_options(self, choice):
        print(f'RUNNING check_num_of_options ({choice})')
        # If choice is DESELECTED and Num.of selected < MIN_CHOOSE
        if self.checkboxes[choice].get()==0 and sum(cbox.get() for cbox in self.checkboxes.values()) < self.MIN_CHOOSE:
            self.checkboxes[choice].select()
