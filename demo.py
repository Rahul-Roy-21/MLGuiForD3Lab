from customtkinter import *
import tkinter as tk
from PIL import Image
from my_utils import *

set_appearance_mode('light')

root=CTk()
root.title('CSL for D3 lab')
root.grid_columnconfigure(tuple(range(1,8)), weight=1) # 8 columns
root.grid_rowconfigure(tuple(range(2,11)),weight=1) # Only Side_panel and task_panel will expand

# FONTS
my_font1 = CTkFont(family='annai mn', size=11, weight='bold')

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

hyperparam_optim_panel.grid_rowconfigure(tuple(range(1,7)), weight=1)

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
    featureAlgo_frame.grid_columnconfigure((1,2,3,5,6), weight=1)
    # ROW (idx): featureLabel(0)--featureMultiSelectEntry(1,2,3)--algoLabel(4)--algoDropDown(5,6)

    features_label=CTkLabel(master=featureAlgo_frame, text='Features list:', font=my_font1)
    selected_features.set(','.join(listOfFeatures))
    features_multiSelectEntry = MultiSelectEntry(
        parent=featureAlgo_frame,
        whatToChoosePlural='Features',
        my_font=my_font1,
        tkVar=selected_features,
        MIN_CHOOSE=2,
        options=listOfFeatures
    )

    algo_label=CTkLabel(master=featureAlgo_frame, text='Algorithm:', font=my_font1)
    algo_dropdown=CTkOptionMenu(
        master=featureAlgo_frame, 
        values=listOfAlgorithms,
        font=my_font1,
        dropdown_font=my_font1,
        variable=selected_algorithm,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
    
    features_label.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW)
    features_multiSelectEntry.grid(row=0,column=1,columnspan=3,padx=5,pady=5,sticky=NSEW)

    algo_label.grid(row=0,column=4,padx=5,pady=5,sticky=NSEW)
    algo_dropdown.grid(row=0,column=5,columnspan=2,padx=5,pady=5,sticky=NSEW)
    # algo_dropdown needed later to configure the show_frames() function
    return algo_dropdown


# A outer CTkFrame (can be scrollable if needed) with a LabelFrame inside
# INP: masterFrame on which outerFrame will be framed
# OUT: labelFrame ref.. to be used for inserting ArgLabelFrames
def build_ArgListLabelFrame (masterFrame: CTkFrame, label_text: str):
    label_frame = tk.LabelFrame(masterFrame, text=label_text, font=my_font1, labelanchor="nw", background=COLORS['SKYBLUE_FG'])
    # FOR TIME BEING
    #label1 = tk.Label(label_frame, text="Label 1:")
    #label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    return label_frame


# HYPER_PARAM_OPTIM panel
HYPER_PARAM_OPTIM_ALGORITHMS=['Random Forest','Support Vector Machine','Logistic Regression','Linear Discriminant Analysis']

hp_optim_selected_features=tk.StringVar()
hp_optim_selected_algorithm=tk.StringVar()
algo_dropdown = build_featureAlgoFrame(
    masterFrame=hyperparam_optim_panel,
    listOfAlgorithms=HYPER_PARAM_OPTIM_ALGORITHMS,
    listOfFeatures=['f11','f12','f13','f14','f15','f16','f17','f18','f19'],
    selected_features=hp_optim_selected_features,
    selected_algorithm=hp_optim_selected_algorithm
)

# Frames for different algo.. set up show_frame
hp_optim_algo_frames = {}
for algo in HYPER_PARAM_OPTIM_ALGORITHMS:
    # FOR TIME BEING
    hp_optim_algo_frames[algo]=build_ArgListLabelFrame(hyperparam_optim_panel, algo)

# RF INPUTS-------------------
METHOD_OPTIONS=['GridSearchCV','Method2','Optuma']
SCORING_OPTIONS=['accuracy', 'precision','s1','s2','s3','s4','s5','s6','s7','s8']

RF_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[0])
RF_labelFrame.grid_columnconfigure(tuple(range(6)), weight=1)
RF_method = build_ArgListLabelFrame(RF_labelFrame, 'Method')
RF_scoring = build_ArgListLabelFrame(RF_labelFrame, 'Scoring')
RF_crossValidFold = build_ArgListLabelFrame(RF_labelFrame, 'Cross-Validation Fold')
RF_hyperParams = build_ArgListLabelFrame(RF_labelFrame, 'HyperParameters')
RF_results = build_ArgListLabelFrame(RF_labelFrame, 'Result')

RF_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
RF_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
RF_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
RF_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
RF_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)

RFVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
RF_method.grid_columnconfigure(0, weight=1)
RF_method_dropdown=CTkOptionMenu(
        master=RF_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=RFVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
RF_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)


RFVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
RF_scoring.grid_columnconfigure(0, weight=1)
RF_scoring_dropdown=CTkOptionMenu(
        master=RF_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=RFVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
RF_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFVar_cross_valid_folds=tk.IntVar(value=3)
RF_crossValidFold_rangeEntry = MyIntegerEntry(parent=RF_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=RFVar_cross_valid_folds)
RF_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

RF_hyperParams.grid_columnconfigure((0,1), weight=1)

RFVar_n_estimators={'_FROM':IntVar(value=50), '_TO':IntVar(value=200), '_STEP':IntVar(value=10)}
RF_nEstimators = build_ArgListLabelFrame(RF_hyperParams, 'n_estimators')
RF_nEstimators.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
RF_nEstimators_entry = MyStepRangeEntry(
    parent=RF_nEstimators,
    from_var=RFVar_n_estimators['_FROM'],
    to_var=RFVar_n_estimators['_TO'],
    step_var=RFVar_n_estimators['_STEP'],
    my_font=my_font1,
    MIN_VAL=RFVar_n_estimators['_FROM'].get(),
    MAX_VAL=RFVar_n_estimators['_TO'].get(),
    MAX_STEPS=RFVar_n_estimators['_STEP'].get()
)
RF_nEstimators_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFVar_criterions_options=['gini', 'entropy', 'log_loss']
RFVar_criterions=StringVar(value=','.join(RFVar_criterions_options))
RF_criterions = build_ArgListLabelFrame(RF_hyperParams, 'criterions')
RF_criterions.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
RF_criterions_entry= MultiSelectEntry(
    parent=RF_criterions,
    whatToChoosePlural='Criterions',
    my_font=my_font1,
    tkVar=RFVar_criterions,
    MIN_CHOOSE=2,
    options=RFVar_criterions_options
)
RF_criterions_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFVar_max_depth={'_FROM':IntVar(value=1), '_TO':IntVar(value=5)}
RF_maxDepth = build_ArgListLabelFrame(RF_hyperParams, 'max_depth')
RF_maxDepth.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
RF_maxDepth_entry = MyRangeEntry(
    parent=RF_maxDepth,
    from_var=RFVar_max_depth['_FROM'],
    to_var=RFVar_max_depth['_TO'],
    my_font=my_font1,
    MIN_VAL=RFVar_max_depth['_FROM'].get(),
    MAX_VAL=30
)
RF_maxDepth_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFVar_min_samples_split={'_FROM':IntVar(value=2), '_TO':IntVar(value=5)}
RF_minSamplesSplit = build_ArgListLabelFrame(RF_hyperParams, 'max_depth')
RF_minSamplesSplit.grid(row=2, column=0, padx=10, pady=5, sticky=EW)
RF_minSamplesSplit_entry = MyRangeEntry(
    parent=RF_minSamplesSplit,
    from_var=RFVar_min_samples_split['_FROM'],
    to_var=RFVar_min_samples_split['_TO'],
    my_font=my_font1,
    MIN_VAL=RFVar_min_samples_split['_FROM'].get(),
    MAX_VAL=10
)
RF_minSamplesSplit_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFVar_min_samples_leaf={'_FROM':IntVar(value=1), '_TO':IntVar(value=5)}
RF_minSamplesLeaf = build_ArgListLabelFrame(RF_hyperParams, 'max_depth')
RF_minSamplesLeaf.grid(row=2, column=1, padx=10, pady=5, sticky=EW)
RF_minSamplesLeaf_entry = MyRangeEntry(
    parent=RF_minSamplesLeaf,
    from_var=RFVar_min_samples_leaf['_FROM'],
    to_var=RFVar_min_samples_leaf['_TO'],
    my_font=my_font1,
    MIN_VAL=RFVar_min_samples_leaf['_FROM'].get(),
    MAX_VAL=10
)
RF_minSamplesLeaf_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RF_submitBtn = CTkButton(
    master=RF_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=300,
    border_spacing=0,
    command=lambda: print('Submit')
)
RF_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

RF_results.grid_columnconfigure(0, weight=1)
RF_resultsVar = StringVar(value="...")
RF_resultTextBox = SyncableTextBox(
    master=RF_results,
    text_variable=RF_resultsVar,
    my_font=my_font1
)
RF_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[0]]=RF_labelFrame


# SVM inputs
SVM_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[1])
SVM_labelFrame.grid_columnconfigure(tuple(range(7)), weight=1)
SVM_method = build_ArgListLabelFrame(SVM_labelFrame, 'Method')
SVM_scoring = build_ArgListLabelFrame(SVM_labelFrame, 'Scoring')
SVM_crossValidFold = build_ArgListLabelFrame(SVM_labelFrame, 'Cross-Validation Fold')
SVM_hyperParams = build_ArgListLabelFrame(SVM_labelFrame, 'HyperParameters')
SVM_results = build_ArgListLabelFrame(SVM_labelFrame, 'Result')

SVM_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
SVM_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
SVM_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
SVM_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
SVM_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)

SVMVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
SVM_method.grid_columnconfigure(0, weight=1)
SVM_method_dropdown=CTkOptionMenu(
        master=SVM_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVM_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
SVM_scoring.grid_columnconfigure(0, weight=1)
SVM_scoring_dropdown=CTkOptionMenu(
        master=SVM_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVM_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMVar_cross_valid_folds=tk.IntVar(value=3)
SVM_crossValidFold_rangeEntry = MyIntegerEntry(parent=SVM_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=SVMVar_cross_valid_folds)
SVM_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

SVM_hyperParams.grid_columnconfigure((0,1), weight=1)

SVMVar_C_options=['0.1','1','10','100','1000']
SVMVar_C=StringVar(value=','.join(SVMVar_C_options))
SVM_C_lb = build_ArgListLabelFrame(SVM_hyperParams, 'C')
SVM_C_lb.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
SVM_C_entry= MultiSelectEntry(
    parent=SVM_C_lb,
    whatToChoosePlural='C value(s)',
    my_font=my_font1,
    tkVar=SVMVar_C,
    MIN_CHOOSE=2,
    options=SVMVar_C_options
)
SVM_C_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMVar_kernel_options=['linear','poly','rbf']
SVMVar_kernel=StringVar(value=','.join(SVMVar_kernel_options))
SVM_kernel = build_ArgListLabelFrame(SVM_hyperParams, 'kernel')
SVM_kernel.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
SVM_kernel_entry= MultiSelectEntry(
    parent=SVM_kernel,
    whatToChoosePlural='kernel(s)',
    my_font=my_font1,
    tkVar=SVMVar_kernel,
    MIN_CHOOSE=2,
    options=SVMVar_kernel_options
)
SVM_kernel_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMVar_gamma_options=['scale','auto']
SVMVar_gamma=StringVar(value=','.join(SVMVar_gamma_options))
SVM_gamma = build_ArgListLabelFrame(SVM_hyperParams, 'gamma')
SVM_gamma.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
SVM_gamma_entry= MultiSelectEntry(
    parent=SVM_gamma,
    whatToChoosePlural='gamma value(s)',
    my_font=my_font1,
    tkVar=SVMVar_gamma,
    MIN_CHOOSE=2,
    options=SVMVar_gamma_options
)
SVM_gamma_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVM_submitBtn = CTkButton(
    master=SVM_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=300,
    border_spacing=0,
    command=lambda: print('Submit')
)
SVM_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

SVM_results.grid_columnconfigure(0, weight=1)
SVM_resultsVar = StringVar(value="...")
SVM_resultTextBox = SyncableTextBox(
    master=SVM_results,
    text_variable=SVM_resultsVar,
    my_font=my_font1
)
SVM_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)


hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[1]]=SVM_labelFrame

def show_hyperParamOptim_AlgoLabelFrame(option):
    for frame in hp_optim_algo_frames.values():
        frame.grid_remove()
    hp_optim_algo_frames[option].grid(row=1,column=0,rowspan=6, columnspan=7,sticky=NSEW,padx=8,pady=(2,5))
    hp_optim_algo_frames[option].grid_columnconfigure(tuple(range(7)), weight=1)

algo_dropdown.configure(command=show_hyperParamOptim_AlgoLabelFrame)

# Setting Default hp_optim_selected_algorithm to index 0 and also displaying that frame (as set doesn't trigger command)
hp_optim_selected_algorithm.set(HYPER_PARAM_OPTIM_ALGORITHMS[0])
show_hyperParamOptim_AlgoLabelFrame(HYPER_PARAM_OPTIM_ALGORITHMS[0])



# MODEL_BUILD panel
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