from typing import Optional, Tuple, Union
from customtkinter import *
import tkinter as tk
from PIL import Image
from os import path as os_path

def getImgPath (img_name, image_dir='images'):
    return os_path.join(image_dir, img_name)

root=CTk()
root.title('CSL for D3 lab')
root.grid_columnconfigure(tuple(range(1,8)), weight=1) # 8 columns
root.grid_rowconfigure(tuple(range(2,11)),weight=1) # Only Side_panel and task_panel will expand

# FONTS
my_font1 = CTkFont(family='appleGothic', size=13, weight='bold')

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


dataset_frame = CTkFrame(master=root, fg_color=COLORS['SKYBLUE_FG'])
dataset_frame.grid(row=0,column=0,columnspan=8, sticky=EW,padx=5, pady=(7,0)) # Will span the entire width of root=8

# 8 cols: 1=label, 3=entry, 1=btn, 2=<SPACE>, 1=Logo
dataset_frame.grid_columnconfigure((1,2,3), weight=3)
dataset_frame.grid_columnconfigure((5,6), weight=1)

train_label=CTkLabel(master=dataset_frame, text='TRAIN', font=my_font1)
test_label=CTkLabel(master=dataset_frame, text='TEST', font=my_font1)

def on_focus_in(ctkEntry):
    ctkEntry.configure(border_color="#111")

def on_focus_out(ctkEntry):
    ctkEntry.configure(border_color="#bbb")

train_entryVar=tk.StringVar()
train_entry=CTkEntry(
    master=dataset_frame, 
    textvariable=train_entryVar, 
    border_width=1,
    border_color=COLORS['GREY_HOVER_FG'], 
    corner_radius=0,
    font=my_font1
)
train_entry.bind('<FocusIn>',lambda e: on_focus_in(train_entry))
train_entry.bind('<FocusOut>',lambda e: on_focus_out(train_entry))

test_entryVar=tk.StringVar()
test_entry=CTkEntry(
    master=dataset_frame, 
    textvariable=test_entryVar, 
    border_width=1,
    border_color=COLORS['GREY_HOVER_FG'],
    corner_radius=0,
    font=my_font1
)
test_entry.bind('<FocusIn>',lambda e: on_focus_in(test_entry))
test_entry.bind('<FocusOut>',lambda e: on_focus_out(test_entry))

upload_img = CTkImage(light_image=Image.open(getImgPath('upload.png')), size=(20, 20))

def open_file_dialog(field_name: str, file_path_entry_var: tk.StringVar):
    file_path = filedialog.askopenfilename(
        title=f"Select a file for {field_name}",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        # Update the label with the selected file path
        file_path_entry_var.set(file_path)

train_btn = CTkButton(
    master=dataset_frame,
    text='Upload',
    compound='left',
    image=upload_img, 
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=100,
    border_spacing=0,
    command=lambda: open_file_dialog(file_path_entry_var=train_entryVar, field_name='Train')
)
test_btn = CTkButton(
    master=dataset_frame,
    text='Upload',
    compound='left',
    image=upload_img, 
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=50,
    command=lambda: open_file_dialog(file_path_entry_var=test_entryVar, field_name='Test')
)

train_label.grid(row=0,column=0,padx=5,pady=5,sticky=EW)
train_entry.grid(row=0,column=1,columnspan=3,padx=5,pady=5,sticky=EW)
train_btn.grid(row=0,column=4,padx=5,pady=5,sticky=EW)

test_label.grid(row=1,column=0,padx=5,pady=5,sticky=EW)
test_entry.grid(row=1,column=1,columnspan=3,padx=5,pady=5,sticky=EW)
test_btn.grid(row=1,column=4,padx=5,pady=5,sticky=EW)

logo_img = CTkImage(light_image=Image.open(getImgPath('logo.png')), size=(65, 65))
logo_label = CTkLabel(master=dataset_frame, image=logo_img, text='', )
logo_label.grid(row=0, column=7, rowspan=2, padx=7, pady=7, sticky=NSEW)


# SIDE PANEL
side_panel = CTkFrame(master=root, fg_color=COLORS['SKYBLUE_FG'])
side_panel.grid(row=2,column=0,rowspan=9,sticky=NSEW,padx=(5,2),pady=5)

hp_optim_img = CTkImage(light_image=Image.open(getImgPath('hp_optim.png')), size=(40, 40))
model_build_img = CTkImage(light_image=Image.open(getImgPath('model_build.png')), size=(40, 40))

hyperparam_optim_btn=CTkButton(
    master=side_panel,
    text="HyperParameter\nOptimization", 
    image=hp_optim_img,
    compound=LEFT,
    font=my_font1,
    fg_color=COLORS['LIGHTRED_FG'],
    hover_color=COLORS['LIGHTRED_HOVER_FG'],
    text_color='white',
    corner_radius=0
)
model_build_btn=CTkButton(
    master=side_panel,
    text="Model\nBuild", 
    image=model_build_img,
    compound=LEFT,
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0
)
hyperparam_optim_btn.grid(row=0,column=0,rowspan=3,sticky=NSEW, padx=10,pady=5)
model_build_btn.grid(row=3,column=0,rowspan=3,sticky=NSEW, padx=10,pady=5)

# TASK PANEL
hyperparam_optim_panel=CTkFrame(master=root, fg_color=COLORS['SKYBLUE_FG'])
model_build_panel=CTkFrame(master=root, fg_color=COLORS['SKYBLUE_FG'])
default_panel=CTkFrame(master=root, fg_color=COLORS['SKYBLUE_FG'])

hyperparam_optim_panel.grid(row=2,column=1,rowspan=9,columnspan=7,sticky=NSEW,padx=(2,5),pady=5)
model_build_panel.grid(row=2,column=1,rowspan=9,columnspan=7,sticky=NSEW,padx=(2,5),pady=5)
default_panel.grid(row=2,column=1,rowspan=9,columnspan=7,sticky=NSEW,padx=(2,5),pady=5)

hyperparam_optim_panel.grid_columnconfigure(0,weight=1)
model_build_panel.grid_columnconfigure(0,weight=1)
default_panel.grid_columnconfigure(0,weight=1)

model_build_panel_label=CTkLabel(master=model_build_panel,text='model_build')
model_build_panel_label.grid(row=0,column=0)
default_panel_label=CTkLabel(master=default_panel,text='default_panel')
default_panel_label.grid(row=0,column=0)

def show_frame(panelList: list[CTkFrame], btnList: list[CTkButton], panelSelected: CTkFrame, btnSelected: CTkButton):
    for panel in panelList:
        panel.grid_forget()
    for btn in btnList:
        btn.configure(border_width=0)
        btn.configure(text=btn.cget('text').rstrip('*'))
    panelSelected.grid(row=2,column=1,rowspan=9,columnspan=7,sticky=NSEW,padx=(2,5),pady=5)  # Show selected frame
    if btnSelected:
        btnSelected.configure(border_width=3, border_color='#000')
        btnSelected.configure(text=btnSelected.cget('text')+'*')

panelList=[
    default_panel, 
    hyperparam_optim_panel, 
    model_build_panel
]
btnList=[
    hyperparam_optim_btn,
    model_build_btn
]
hyperparam_optim_btn.configure(command=lambda: show_frame(panelList, btnList, hyperparam_optim_panel, hyperparam_optim_btn))
model_build_btn.configure(command=lambda: show_frame(panelList, btnList, model_build_panel, model_build_btn))
show_frame(panelList, [], default_panel, None)



# FEATURE/ALGORITHM SELECTION FRAME (IN a TASK_PANEL)
class FeatureSelectionDialog(CTkToplevel):
    def __init__(self, parent, options, selected_feature_tkStringVar: tk.StringVar):
        super().__init__(parent)
        self.title("Choose Features")
        self.geometry("300x300")
        self.resizable(FALSE, FALSE)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.selected_feature_tkStringVar = selected_feature_tkStringVar
        self.selected_options = set(selected_feature_tkStringVar.get().split(','))
    
        # Row0,1,2,3: ScrollableFrame (with Label)
        scrollable_frame = CTkScrollableFrame(
            self, 
            label_text='Features List', 
            label_font=my_font1,
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
                font=my_font1,
                corner_radius=0,
                fg_color=COLORS['MEDIUMGREEN_FG'],
                hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
                border_width=1,
                border_color='#000'
            )
            ctkCheckBox.grid(row=idx, column=0, padx=10, pady=(10, 0), sticky="w")
            if option in self.selected_options:
                ctkCheckBox.select()
            self.checkboxes[option]=ctkCheckBox

        # Row4: Submit Btn
        submit_button = CTkButton(
            self, 
            text="Submit", 
            font=my_font1,
            fg_color=COLORS['MEDIUMGREEN_FG'],
            hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
            text_color='white',
            corner_radius=0,
            width=100,
            border_spacing=0,
            command=self.submit
        )
        submit_button.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    def submit(self):
        # Update selected options based on the state of the checkboxes
        self.selected_options=[]
        for option, checkBox in self.checkboxes.items():
            if checkBox.get():
                self.selected_options.append(option)

        # Update the tk.StringVar with the selected options
        self.selected_feature_tkStringVar.set(
            ','.join(sorted(self.selected_options)).strip(',')
        )
        self.destroy()


def build_featureAlgoFrame(
        masterFrame: CTkFrame, listOfAlgorithms: list[str], listOfFeatures: list[str], 
        selected_features: tk.StringVar, selected_algorithm: tk.StringVar
    ):
    featureAlgo_frame=CTkFrame(master=masterFrame, fg_color=COLORS['SKYBLUE_FG'])
    featureAlgo_frame.grid(row=0,column=0,columnspan=7,sticky=NSEW,padx=(5,2),pady=5)
    featureAlgo_frame.grid_columnconfigure((1,2), weight=3)
    featureAlgo_frame.grid_columnconfigure((5,6), weight=1)
    # ROW (idx): featureLabel(0)--featureEntry(1,2)--featureSelectBtn(3)--algoLabel(4)--algoDropDown(5,6)

    features_label=CTkLabel(master=featureAlgo_frame, text='Features list:', font=my_font1)
    features_entry=CTkEntry(
        master=featureAlgo_frame,
        textvariable=selected_features,
        border_width=1,
        border_color=COLORS['GREY_HOVER_FG'],
        corner_radius=0,
        font=my_font1,
        state=DISABLED
    )

    def open_inputDialog_for_featureSelect():
        FeatureSelectionDialog(masterFrame, listOfFeatures, selected_features)

    select_img=CTkImage(light_image=Image.open(getImgPath('search.png')), size=(30, 30))
    features_selectbtn=CTkButton(
        master=featureAlgo_frame,
        text="Select", 
        image=select_img,
        compound=LEFT,
        font=my_font1,
        fg_color=COLORS['GREY_FG'],
        hover_color=COLORS['GREY_HOVER_FG'],
        text_color='white',
        corner_radius=0,
        width=100,
        command=open_inputDialog_for_featureSelect
    )

    algo_label=CTkLabel(master=featureAlgo_frame, text='Algorithm:', font=my_font1)
    selected_algorithm.set(listOfAlgorithms[0])
    algo_dropdown=CTkOptionMenu(
        master=featureAlgo_frame, 
        values=listOfAlgorithms,
        font=my_font1,
        dropdown_font=my_font1,
        variable=selected_algorithm,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_HOVER_FG'],
        fg_color=COLORS['GREY_FG'],
        anchor=CENTER
    )

    features_label.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW)
    features_entry.grid(row=0,column=1,columnspan=2,padx=5,pady=5,sticky=NSEW)
    features_selectbtn.grid(row=0,column=3,padx=5,pady=5,sticky=NSEW)

    algo_label.grid(row=0,column=4,padx=5,pady=5,sticky=NSEW)
    algo_dropdown.grid(row=0,column=5,columnspan=2,padx=5,pady=5,sticky=NSEW)





# HYPER_PARAM_OPTIM panel
hp_optim_selected_features=tk.StringVar()
hp_optim_selected_algorithm=tk.StringVar()
build_featureAlgoFrame(
    masterFrame=hyperparam_optim_panel,
    listOfAlgorithms=['algo11','algo12','algo13'],
    listOfFeatures=['f11','f12','f13','f14','f15','f16','f17','f18','f19'],
    selected_features=hp_optim_selected_features,
    selected_algorithm=hp_optim_selected_algorithm
)

# HYPER_PARAM_OPTIM panel
model_build_selected_features=tk.StringVar()
model_build_selected_algorithm=tk.StringVar()
build_featureAlgoFrame(
    masterFrame=model_build_panel,
    listOfAlgorithms=['algo21','algo22','algo23'],
    listOfFeatures=['f21','f22','f23'],
    selected_features=model_build_selected_features,
    selected_algorithm=model_build_selected_algorithm
)

root.mainloop()