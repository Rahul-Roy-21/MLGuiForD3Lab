from customtkinter import *
import tkinter as tk
from PIL import Image
from my_utils import *
from my_util_functions import *

set_appearance_mode('light')

root=CTk()
root.title('CSL for D3 lab')
root.grid_columnconfigure(tuple(range(1,8)), weight=1) # 8 columns
root.grid_rowconfigure(tuple(range(2,11)),weight=1) # Only Side_panel and task_panel will expand

# FONTS
my_font1 = CTkFont(family='courier prime', size=13, weight='normal')
RESULTS_LOADING_IMG_PATH = getImgPath('loading.gif')

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
    border_width=0,
    corner_radius=0,
    font=my_font1
)
train_entry.bind('<FocusIn>',lambda e: on_focus_in(train_entry))
train_entry.bind('<FocusOut>',lambda e: on_focus_out(train_entry))

test_entryVar=tk.StringVar()
test_entry=CTkEntry(
    master=dataset_frame, 
    textvariable=test_entryVar, 
    border_width=0,
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
    text="HYPERPARAMETER\nOPTIMIZATION", 
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
    text="MODEL\nBUILD", 
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
model_build_panel.grid_rowconfigure(tuple(range(1,7)), weight=1)

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
    label_frame = tk.LabelFrame(masterFrame, text=label_text, font=my_font1, labelanchor=NW, background=COLORS['SKYBLUE_FG'])
    # FOR TIME BEING
    #label1 = tk.Label(label_frame, text="Label 1:")
    #label1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    return label_frame


# HYPER_PARAM_OPTIM panel
HYPER_PARAM_OPTIM_ALGORITHMS=[
    'Random Forest',
    'Support Vector Machine',
    'Logistic Regression',
    'Linear Discriminant Analysis',
    'K-Nearest Neighbors',
    'GradientBoosting',
    'Multi-Layer Perceptron (ANN)'
]

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
METHOD_OPTIONS=['GridSearchCV','RandomizedSearchCV','Optuna']
SCORING_OPTIONS=['accuracy', 'precision','s1','s2','s3','s4','s5','s6','s7','s8']

RF_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[0])
RF_labelFrame.grid_columnconfigure(tuple(range(6)), weight=1)
RF_method = build_ArgListLabelFrame(RF_labelFrame, 'Method')
RF_scoring = build_ArgListLabelFrame(RF_labelFrame, 'Scoring')
RF_crossValidFold = build_ArgListLabelFrame(RF_labelFrame, 'Cross-Validation Fold')
RF_hyperParams = build_ArgListLabelFrame(RF_labelFrame, 'HyperParameters')
RF_results = build_ArgListLabelFrame(RF_labelFrame, 'Result')
RF_labelFrame.grid_rowconfigure(2, weight=1)

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
RF_minSamplesSplit = build_ArgListLabelFrame(RF_hyperParams, 'min_sample_split')
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
RF_minSamplesLeaf = build_ArgListLabelFrame(RF_hyperParams, 'min_sample_leaf')
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

RF_inputs = {
    'METHOD': RFVar_method,
    'SCORING': RFVar_scoring,
    'CROSS_FOLD_VALID': RFVar_cross_valid_folds,
    'N_ESTIMATORS': RFVar_n_estimators,
    'CRITERIONS': RFVar_criterions,
    'MAX_DEPTH': RFVar_max_depth,
    'MIN_SAMPLE_SPLIT': RFVar_min_samples_split,
    'MIN_SAMPLE_LEAF': RFVar_min_samples_leaf
}

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
    command=lambda: RF_HP_OPTIM_SUBMIT(root, RESULTS_LOADING_IMG_PATH, RF_inputs, RF_resultsVar)
)
RF_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

RF_results.grid_columnconfigure(0, weight=1)
RF_results.grid_rowconfigure(0, weight=1)
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
SVM_labelFrame.grid_rowconfigure(2, weight=1)

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

SVMVar_kernel_options=['linear','poly','rbf', 'sigmoid']
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
SVM_results.grid_rowconfigure(0, weight=1)
SVM_resultsVar = StringVar(value="...")
SVM_resultTextBox = SyncableTextBox(
    master=SVM_results,
    text_variable=SVM_resultsVar,
    my_font=my_font1
)
SVM_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[1]]=SVM_labelFrame


# LR inputs
LR_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[2])
LR_labelFrame.grid_columnconfigure(tuple(range(7)), weight=1)
LR_method = build_ArgListLabelFrame(LR_labelFrame, 'Method')
LR_scoring = build_ArgListLabelFrame(LR_labelFrame, 'Scoring')
LR_crossValidFold = build_ArgListLabelFrame(LR_labelFrame, 'Cross-Validation Fold')
LR_hyperParams = build_ArgListLabelFrame(LR_labelFrame, 'HyperParameters')
LR_results = build_ArgListLabelFrame(LR_labelFrame, 'Result')

LR_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
LR_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
LR_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
LR_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
LR_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
LR_labelFrame.grid_rowconfigure(2, weight=1)

LRVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
LR_method.grid_columnconfigure(0, weight=1)
LR_method_dropdown=CTkOptionMenu(
        master=LR_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LR_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
LR_scoring.grid_columnconfigure(0, weight=1)
LR_scoring_dropdown=CTkOptionMenu(
        master=LR_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LR_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRVar_cross_valid_folds=tk.IntVar(value=3)
LR_crossValidFold_rangeEntry = MyIntegerEntry(parent=LR_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=LRVar_cross_valid_folds)
LR_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

LR_hyperParams.grid_columnconfigure((0,1), weight=1)

LRVar_C_options=['0.1','1','10']
LRVar_C=StringVar(value=','.join(LRVar_C_options))
LR_C_lb = build_ArgListLabelFrame(LR_hyperParams, 'C')
LR_C_lb.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
LR_C_entry= MultiSelectEntry(
    parent=LR_C_lb,
    whatToChoosePlural='C value(s)',
    my_font=my_font1,
    tkVar=LRVar_C,
    MIN_CHOOSE=2,
    options=LRVar_C_options
)
LR_C_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRVar_penalty_options=['l1','l2','elasticnet', 'None']
LRVar_penalty=StringVar(value=','.join(LRVar_penalty_options))
LR_penalty = build_ArgListLabelFrame(LR_hyperParams, 'penalty')
LR_penalty.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
LR_penalty_entry= MultiSelectEntry(
    parent=LR_penalty,
    whatToChoosePlural='penalty(s)',
    my_font=my_font1,
    tkVar=LRVar_penalty,
    MIN_CHOOSE=2,
    options=LRVar_penalty_options
)
LR_penalty_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRVar_solver_options=['lbfgs','liblinear','newton-cg','newton-cholesky','sag','saga']
LRVar_solver=StringVar(value=','.join(LRVar_solver_options))
LR_solver = build_ArgListLabelFrame(LR_hyperParams, 'solver')
LR_solver.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
LR_solver_entry= MultiSelectEntry(
    parent=LR_solver,
    whatToChoosePlural='solver value(s)',
    my_font=my_font1,
    tkVar=LRVar_solver,
    MIN_CHOOSE=2,
    options=LRVar_solver_options
)
LR_solver_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LR_submitBtn = CTkButton(
    master=LR_hyperParams,
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
LR_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

LR_results.grid_columnconfigure(0, weight=1)
LR_results.grid_rowconfigure(0, weight=1)
LR_resultsVar = StringVar(value="...")
LR_resultTextBox = SyncableTextBox(
    master=LR_results,
    text_variable=LR_resultsVar,
    my_font=my_font1
)
LR_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[2]]=LR_labelFrame


# LDA Inputs
LDA_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[3])
LDA_labelFrame.grid_columnconfigure(tuple(range(7)), weight=1)
LDA_method = build_ArgListLabelFrame(LDA_labelFrame, 'Method')
LDA_scoring = build_ArgListLabelFrame(LDA_labelFrame, 'Scoring')
LDA_crossValidFold = build_ArgListLabelFrame(LDA_labelFrame, 'Cross-Validation Fold')
LDA_hyperParams = build_ArgListLabelFrame(LDA_labelFrame, 'HyperParameters')
LDA_results = build_ArgListLabelFrame(LDA_labelFrame, 'Result')

LDA_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
LDA_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
LDA_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
LDA_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
LDA_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
LDA_labelFrame.grid_rowconfigure(2, weight=1)

LDAVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
LDA_method.grid_columnconfigure(0, weight=1)
LDA_method_dropdown=CTkOptionMenu(
        master=LDA_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=LDAVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LDA_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
LDA_scoring.grid_columnconfigure(0, weight=1)
LDA_scoring_dropdown=CTkOptionMenu(
        master=LDA_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=LDAVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LDA_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAVar_cross_valid_folds=tk.IntVar(value=3)
LDA_crossValidFold_rangeEntry = MyIntegerEntry(parent=LDA_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=LDAVar_cross_valid_folds)
LDA_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

LDA_hyperParams.grid_columnconfigure((0,1), weight=1)

LDAVar_solver_options=['svd', 'lsqr', 'eigen']
LDAVar_solver=StringVar(value=','.join(LDAVar_solver_options))
LDA_solver = build_ArgListLabelFrame(LDA_hyperParams, 'solver')
LDA_solver.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
LDA_solver_entry= MultiSelectEntry(
    parent=LDA_solver,
    whatToChoosePlural='solver(s)',
    my_font=my_font1,
    tkVar=LDAVar_solver,
    MIN_CHOOSE=2,
    options=LDAVar_solver_options
)
LDA_solver_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDA_submitBtn = CTkButton(
    master=LDA_hyperParams,
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
LDA_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

LDA_results.grid_columnconfigure(0, weight=1)
LDA_results.grid_rowconfigure(0, weight=1)
LDA_resultsVar = StringVar(value="...")
LDA_resultTextBox = SyncableTextBox(
    master=LDA_results,
    text_variable=LDA_resultsVar,
    my_font=my_font1
)
LDA_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[3]]=LDA_labelFrame


# KNN
KNN_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[4])
KNN_labelFrame.grid_columnconfigure(tuple(range(6)), weight=1)
KNN_method = build_ArgListLabelFrame(KNN_labelFrame, 'Method')
KNN_scoring = build_ArgListLabelFrame(KNN_labelFrame, 'Scoring')
KNN_crossValidFold = build_ArgListLabelFrame(KNN_labelFrame, 'Cross-Validation Fold')
KNN_hyperParams = build_ArgListLabelFrame(KNN_labelFrame, 'HyperParameters')
KNN_results = build_ArgListLabelFrame(KNN_labelFrame, 'Result')

KNN_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
KNN_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
KNN_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
KNN_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
KNN_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
KNN_labelFrame.grid_rowconfigure(2, weight=1)

KNNVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
KNN_method.grid_columnconfigure(0, weight=1)
KNN_method_dropdown=CTkOptionMenu(
        master=KNN_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=KNNVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
KNN_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)


KNNVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
KNN_scoring.grid_columnconfigure(0, weight=1)
KNN_scoring_dropdown=CTkOptionMenu(
        master=KNN_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=KNNVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
KNN_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

KNNVar_cross_valid_folds=tk.IntVar(value=3)
KNN_crossValidFold_rangeEntry = MyIntegerEntry(parent=KNN_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=KNNVar_cross_valid_folds)
KNN_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

KNN_hyperParams.grid_columnconfigure((0,1), weight=1)

KNNVar_nNeighbors={'_FROM':IntVar(value=2), '_TO':IntVar(value=20)}
KNN_nNeighbors = build_ArgListLabelFrame(KNN_hyperParams, 'n_neighbors')
KNN_nNeighbors.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
KNN_nNeighbors_entry = MyRangeEntry(
    parent=KNN_nNeighbors,
    from_var=KNNVar_nNeighbors['_FROM'],
    to_var=KNNVar_nNeighbors['_TO'],
    my_font=my_font1,
    MIN_VAL=KNNVar_nNeighbors['_FROM'].get(),
    MAX_VAL=20
)
KNN_nNeighbors_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

KNNVar_leaf_size={'_FROM':IntVar(value=10), '_TO':IntVar(value=50)}
KNN_leaf_size = build_ArgListLabelFrame(KNN_hyperParams, 'leaf_size')
KNN_leaf_size.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
KNN_leaf_size_entry = MyRangeEntry(
    parent=KNN_leaf_size,
    from_var=KNNVar_leaf_size['_FROM'],
    to_var=KNNVar_leaf_size['_TO'],
    my_font=my_font1,
    MIN_VAL=KNNVar_leaf_size['_FROM'].get(),
    MAX_VAL=50
)
KNN_leaf_size_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

KNNVar_P={'_FROM':IntVar(value=1), '_TO':IntVar(value=2)}
KNN_P_lb = build_ArgListLabelFrame(KNN_hyperParams, 'P')
KNN_P_lb.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
KNN_P_entry = MyRangeEntry(
    parent=KNN_P_lb,
    from_var=KNNVar_P['_FROM'],
    to_var=KNNVar_P['_TO'],
    my_font=my_font1,
    MIN_VAL=KNNVar_P['_FROM'].get(),
    MAX_VAL=5
)
KNN_P_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

KNN_submitBtn = CTkButton(
    master=KNN_hyperParams,
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
KNN_submitBtn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

KNN_results.grid_columnconfigure(0, weight=1)
KNN_results.grid_rowconfigure(0, weight=1)
KNN_resultsVar = StringVar(value="...")
KNN_resultTextBox = SyncableTextBox(
    master=KNN_results,
    text_variable=KNN_resultsVar,
    my_font=my_font1
)
KNN_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[4]]=KNN_labelFrame

# Gradient Boosting
GRB_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[5])
GRB_labelFrame.grid_columnconfigure(tuple(range(6)), weight=1)
GRB_method = build_ArgListLabelFrame(GRB_labelFrame, 'Method')
GRB_scoring = build_ArgListLabelFrame(GRB_labelFrame, 'Scoring')
GRB_crossValidFold = build_ArgListLabelFrame(GRB_labelFrame, 'Cross-Validation Fold')
GRB_hyperParams = build_ArgListLabelFrame(GRB_labelFrame, 'HyperParameters')
GRB_results = build_ArgListLabelFrame(GRB_labelFrame, 'Result')

GRB_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
GRB_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
GRB_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
GRB_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
GRB_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
GRB_labelFrame.grid_rowconfigure(2, weight=1)

GRBVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
GRB_method.grid_columnconfigure(0, weight=1)
GRB_method_dropdown=CTkOptionMenu(
        master=GRB_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=GRBVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
GRB_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)


GRBVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
GRB_scoring.grid_columnconfigure(0, weight=1)
GRB_scoring_dropdown=CTkOptionMenu(
        master=GRB_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=GRBVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
GRB_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_cross_valid_folds=tk.IntVar(value=3)
GRB_crossValidFold_rangeEntry = MyIntegerEntry(parent=GRB_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=GRBVar_cross_valid_folds)
GRB_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

GRB_hyperParams.grid_columnconfigure(tuple(range(6)), weight=1)

GRBVar_n_estimators={'_FROM':IntVar(value=10), '_TO':IntVar(value=200), '_STEP':IntVar(value=10)}
GRB_nEstimators = build_ArgListLabelFrame(GRB_hyperParams, 'n_estimators')
GRB_nEstimators.grid(row=0, column=2, columnspan=4, padx=10, pady=5, sticky=EW)
GRB_nEstimators_entry = MyStepRangeEntry(
    parent=GRB_nEstimators,
    from_var=GRBVar_n_estimators['_FROM'],
    to_var=GRBVar_n_estimators['_TO'],
    step_var=GRBVar_n_estimators['_STEP'],
    my_font=my_font1,
    MIN_VAL=GRBVar_n_estimators['_FROM'].get(),
    MAX_VAL=GRBVar_n_estimators['_TO'].get(),
    MAX_STEPS=GRBVar_n_estimators['_STEP'].get()
)
GRB_nEstimators_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_criterions_options=['friedman_mse', 'squared_error']
GRBVar_criterions=StringVar(value=','.join(GRBVar_criterions_options))
GRB_criterions = build_ArgListLabelFrame(GRB_hyperParams, 'criterion')
GRB_criterions.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
GRB_criterions_entry= MultiSelectEntry(
    parent=GRB_criterions,
    whatToChoosePlural='Criterions',
    my_font=my_font1,
    tkVar=GRBVar_criterions,
    MIN_CHOOSE=2,
    options=GRBVar_criterions_options
)
GRB_criterions_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_learning_rate={'_FROM':DoubleVar(value=1e-2), '_TO':DoubleVar(value=1e-1)}
GRB_learning_rate = build_ArgListLabelFrame(GRB_hyperParams, 'learning_rate')
GRB_learning_rate.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky=EW)
GRB_learning_rate_entry = MyFloatingLogRangeEntry(
    parent=GRB_learning_rate,
    from_var=GRBVar_learning_rate['_FROM'],
    to_var=GRBVar_learning_rate['_TO'],
    my_font=my_font1,
    MIN_VAL=1e-3,
    MAX_VAL=1e0
)
GRB_learning_rate_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_max_depth={'_FROM':IntVar(value=2), '_TO':IntVar(value=10)}
GRB_maxDepth = build_ArgListLabelFrame(GRB_hyperParams, 'max_depth')
GRB_maxDepth.grid(row=1, column=3, columnspan=3, padx=10, pady=5, sticky=EW)
GRB_maxDepth_entry = MyRangeEntry(
    parent=GRB_maxDepth,
    from_var=GRBVar_max_depth['_FROM'],
    to_var=GRBVar_max_depth['_TO'],
    my_font=my_font1,
    MIN_VAL=GRBVar_max_depth['_FROM'].get(),
    MAX_VAL=32
)
GRB_maxDepth_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_min_samples_split={'_FROM':IntVar(value=2), '_TO':IntVar(value=5)}
GRB_minSamplesSplit = build_ArgListLabelFrame(GRB_hyperParams, 'min_sample_split')
GRB_minSamplesSplit.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=EW)
GRB_minSamplesSplit_entry = MyRangeEntry(
    parent=GRB_minSamplesSplit,
    from_var=GRBVar_min_samples_split['_FROM'],
    to_var=GRBVar_min_samples_split['_TO'],
    my_font=my_font1,
    MIN_VAL=GRBVar_min_samples_split['_FROM'].get(),
    MAX_VAL=10
)
GRB_minSamplesSplit_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRBVar_min_samples_leaf={'_FROM':IntVar(value=1), '_TO':IntVar(value=5)}
GRB_minSamplesLeaf = build_ArgListLabelFrame(GRB_hyperParams, 'min_sample_leaf')
GRB_minSamplesLeaf.grid(row=2, column=3, columnspan=3, padx=10, pady=5, sticky=EW)
GRB_minSamplesLeaf_entry = MyRangeEntry(
    parent=GRB_minSamplesLeaf,
    from_var=GRBVar_min_samples_leaf['_FROM'],
    to_var=GRBVar_min_samples_leaf['_TO'],
    my_font=my_font1,
    MIN_VAL=GRBVar_min_samples_leaf['_FROM'].get(),
    MAX_VAL=10
)
GRB_minSamplesLeaf_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

GRB_submitBtn = CTkButton(
    master=GRB_hyperParams,
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
GRB_submitBtn.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

GRB_results.grid_columnconfigure(0, weight=1)
GRB_results.grid_rowconfigure(0, weight=1)
GRB_resultsVar = StringVar(value="...")
GRB_resultTextBox = SyncableTextBox(
    master=GRB_results,
    text_variable=GRB_resultsVar,
    my_font=my_font1
)
GRB_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[5]]=GRB_labelFrame

# MLP (ANN)
MLP_labelFrame = build_ArgListLabelFrame(hyperparam_optim_panel, HYPER_PARAM_OPTIM_ALGORITHMS[6])
MLP_labelFrame.grid_columnconfigure(tuple(range(6)), weight=1)
MLP_method = build_ArgListLabelFrame(MLP_labelFrame, 'Method')
MLP_scoring = build_ArgListLabelFrame(MLP_labelFrame, 'Scoring')
MLP_crossValidFold = build_ArgListLabelFrame(MLP_labelFrame, 'Cross-Validation Fold')
MLP_hyperParams = build_ArgListLabelFrame(MLP_labelFrame, 'HyperParameters')
MLP_results = build_ArgListLabelFrame(MLP_labelFrame, 'Result')

MLP_method.grid(row=0, column=0, columnspan=3, padx=5, pady=2, sticky=NSEW)
MLP_scoring.grid(row=0, column=3, columnspan=3, padx=5, pady=2, sticky=NSEW)
MLP_crossValidFold.grid(row=0, column=6, padx=5, pady=2, sticky=NSEW)
MLP_hyperParams.grid(row=1, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
MLP_results.grid(row=2, column=0, columnspan=7, padx=5, pady=2, sticky=NSEW)
MLP_labelFrame.grid_rowconfigure(2, weight=1)

MLPVar_method=tk.StringVar(value=METHOD_OPTIONS[0])
MLP_method.grid_columnconfigure(0, weight=1)
MLP_method_dropdown=CTkOptionMenu(
        master=MLP_method, 
        values=METHOD_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=MLPVar_method,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
MLP_method_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_scoring=tk.StringVar(value=SCORING_OPTIONS[0])
MLP_scoring.grid_columnconfigure(0, weight=1)
MLP_scoring_dropdown=CTkOptionMenu(
        master=MLP_scoring, 
        values=SCORING_OPTIONS,
        font=my_font1,
        dropdown_font=my_font1,
        variable=MLPVar_scoring,
        corner_radius=0,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
MLP_scoring_dropdown.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_cross_valid_folds=tk.IntVar(value=3)
MLP_crossValidFold_rangeEntry = MyIntegerEntry(parent=MLP_crossValidFold, min_value=3, max_value=20, my_font=my_font1, tkVar=MLPVar_cross_valid_folds)
MLP_crossValidFold_rangeEntry.grid(row=0, column=0, padx=10, pady=5)

MLP_hyperParams.grid_columnconfigure(tuple(range(2)), weight=1)

MLPVar_hidden_layer_size={'_FROM':IntVar(value=50), '_TO':IntVar(value=300), '_STEP':IntVar(value=10)}
MLP_hidden_layer_size = build_ArgListLabelFrame(MLP_hyperParams, 'hidden_layer_size')
MLP_hidden_layer_size.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=EW)
MLP_hidden_layer_size_entry = MyStepRangeEntry(
    parent=MLP_hidden_layer_size,
    from_var=MLPVar_hidden_layer_size['_FROM'],
    to_var=MLPVar_hidden_layer_size['_TO'],
    step_var=MLPVar_hidden_layer_size['_STEP'],
    my_font=my_font1,
    MIN_VAL=MLPVar_hidden_layer_size['_FROM'].get(),
    MAX_VAL=MLPVar_hidden_layer_size['_TO'].get(),
    MAX_STEPS=MLPVar_hidden_layer_size['_STEP'].get()
)
MLP_hidden_layer_size_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_activation_options=['relu', 'tanh', 'logistic']
MLPVar_activation=StringVar(value=','.join(MLPVar_activation_options))
MLP_activation = build_ArgListLabelFrame(MLP_hyperParams, 'activation')
MLP_activation.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
MLP_activation_entry= MultiSelectEntry(
    parent=MLP_activation,
    whatToChoosePlural='Activation(s)',
    my_font=my_font1,
    tkVar=MLPVar_activation,
    MIN_CHOOSE=2,
    options=MLPVar_activation_options
)
MLP_activation_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_alpha={'_FROM':DoubleVar(value=1e-6), '_TO':DoubleVar(value=1e-1)}
MLP_alpha = build_ArgListLabelFrame(MLP_hyperParams, 'alpha')
MLP_alpha.grid(row=2, column=0, padx=10, pady=5, sticky=EW)
MLP_alpha_entry = MyFloatingLogRangeEntry(
    parent=MLP_alpha,
    from_var=MLPVar_alpha['_FROM'],
    to_var=MLPVar_alpha['_TO'],
    my_font=my_font1,
    MIN_VAL=1e-6,
    MAX_VAL=1e-1
)
MLP_alpha_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_learning_rate_options=['adaptive', 'constant', 'invscaling']
MLPVar_learning_rate=StringVar(value=','.join(MLPVar_learning_rate_options[:2]))
MLP_learning_rate = build_ArgListLabelFrame(MLP_hyperParams, 'learning_rate')
MLP_learning_rate.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
MLP_learning_rate_entry= MultiSelectEntry(
    parent=MLP_learning_rate,
    whatToChoosePlural='Learning Rate(s)',
    my_font=my_font1,
    tkVar=MLPVar_learning_rate,
    MIN_CHOOSE=2,
    options=MLPVar_learning_rate_options
)
MLP_learning_rate_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLPVar_solver_options=['adam', 'sgd', 'lbfgs']
MLPVar_solver=StringVar(value=','.join(MLPVar_solver_options))
MLP_solver = build_ArgListLabelFrame(MLP_hyperParams, 'solver')
MLP_solver.grid(row=2, column=1, padx=10, pady=5, sticky=EW)
MLP_solver_entry= MultiSelectEntry(
    parent=MLP_solver,
    whatToChoosePlural='Solver(s)',
    my_font=my_font1,
    tkVar=MLPVar_solver,
    MIN_CHOOSE=2,
    options=MLPVar_solver_options
)
MLP_solver_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

MLP_submitBtn = CTkButton(
    master=MLP_hyperParams,
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
MLP_submitBtn.grid(row=3, column=0, columnspan=6, padx=10, pady=10)

MLP_results.grid_columnconfigure(0, weight=1)
MLP_results.grid_rowconfigure(0, weight=1)
MLP_resultsVar = StringVar(value="...")
MLP_resultTextBox = SyncableTextBox(
    master=MLP_results,
    text_variable=MLP_resultsVar,
    my_font=my_font1
)
MLP_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

hp_optim_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[6]]=MLP_labelFrame


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
algo_dropdown = build_featureAlgoFrame(
    masterFrame=model_build_panel,
    listOfAlgorithms=HYPER_PARAM_OPTIM_ALGORITHMS,
    listOfFeatures=['f21','f22','f23'],
    selected_features=model_build_selected_features,
    selected_algorithm=model_build_selected_algorithm
)

# Frames for different algo.. set up show_frame
model_build_algo_frames = {}
for algo in HYPER_PARAM_OPTIM_ALGORITHMS:
    # FOR TIME BEING
    model_build_algo_frames[algo]=build_ArgListLabelFrame(model_build_panel, algo)

RFmb_labelFrame = build_ArgListLabelFrame(model_build_panel, HYPER_PARAM_OPTIM_ALGORITHMS[0])
RFmb_labelFrame.grid_columnconfigure(0, weight=1)
RFmb_hyperParams = build_ArgListLabelFrame(RFmb_labelFrame, 'HyperParameters')
RFmb_results = build_ArgListLabelFrame(RFmb_labelFrame, 'Result')
RFmb_labelFrame.grid_rowconfigure(1, weight=1)

RFmb_hyperParams.grid(row=0, column=0, padx=5, pady=2, sticky=NSEW)
RFmb_results.grid(row=1, column=0, padx=5, pady=2, sticky=NSEW)
RFmb_hyperParams.grid_columnconfigure(tuple(range(5)), weight=1)

RFmbVar_nEstimators=tk.StringVar(value='100')
RFmb_nEstimators = build_ArgListLabelFrame(RFmb_hyperParams, 'n_estimators')
RFmb_nEstimators.grid(row=0, column=0, padx=10, pady=5, sticky=EW)
RFmb_nEstimators.grid_columnconfigure(0, weight=1)
RFmb_nEstimators_entry=CTkEntry(
        master=RFmb_nEstimators, 
        font=my_font1,
        textvariable=RFmbVar_nEstimators,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_nEstimators_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_criterion=tk.StringVar(value=RFVar_criterions_options[0])
RFmb_criterion = build_ArgListLabelFrame(RFmb_hyperParams, 'criterion')
RFmb_criterion.grid(row=0, column=1, padx=10, pady=5, sticky=EW)
RFmb_criterion.grid_columnconfigure(0, weight=1)
RFmb_criterion_entry=CTkOptionMenu(
        master=RFmb_criterion, 
        font=my_font1,
        variable=RFmbVar_criterion,
        values=RFVar_criterions_options,
        dropdown_font=my_font1,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
RFmb_criterion_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_maxDepth=tk.StringVar(value='None')
RFmb_maxDepth = build_ArgListLabelFrame(RFmb_hyperParams, 'max_depth')
RFmb_maxDepth.grid(row=0, column=2, padx=10, pady=5, sticky=EW)
RFmb_maxDepth.grid_columnconfigure(0, weight=1)
RFmb_maxDepth_entry=CTkEntry(
        master=RFmb_maxDepth, 
        font=my_font1,
        textvariable=RFmbVar_maxDepth,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_maxDepth_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_minSamplesSplit=tk.StringVar(value='2')
RFmb_minSamplesSplit = build_ArgListLabelFrame(RFmb_hyperParams, 'min_sample_split')
RFmb_minSamplesSplit.grid(row=0, column=3, padx=10, pady=5, sticky=EW)
RFmb_minSamplesSplit.grid_columnconfigure(0, weight=1)
RFmb_minSamplesSplit_entry=CTkEntry(
        master=RFmb_minSamplesSplit, 
        font=my_font1,
        textvariable=RFmbVar_minSamplesSplit,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_minSamplesSplit_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_minSamplesLeaf=tk.StringVar(value='1')
RFmb_minSamplesLeaf = build_ArgListLabelFrame(RFmb_hyperParams, 'min_sample_leaf')
RFmb_minSamplesLeaf.grid(row=0, column=4, padx=10, pady=5, sticky=EW)
RFmb_minSamplesLeaf.grid_columnconfigure(0, weight=1)
RFmb_minSamplesLeaf_entry=CTkEntry(
        master=RFmb_minSamplesLeaf, 
        font=my_font1,
        textvariable=RFmbVar_minSamplesLeaf,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_minSamplesLeaf_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_minImpurityDecrease=tk.StringVar(value='0.0')
RFmb_minImpurityDecrease = build_ArgListLabelFrame(RFmb_hyperParams, 'min_impurity_decrease')
RFmb_minImpurityDecrease.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
RFmb_minImpurityDecrease.grid_columnconfigure(0, weight=1)
RFmb_minImpurityDecrease_entry=CTkEntry(
        master=RFmb_minImpurityDecrease, 
        font=my_font1,
        textvariable=RFmbVar_minImpurityDecrease,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_minImpurityDecrease_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_randomState=tk.StringVar(value='None')
RFmb_randomState = build_ArgListLabelFrame(RFmb_hyperParams, 'random_state')
RFmb_randomState.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
RFmb_randomState.grid_columnconfigure(0, weight=1)
RFmb_randomState_entry=CTkEntry(
        master=RFmb_randomState, 
        font=my_font1,
        textvariable=RFmbVar_randomState,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_randomState_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_warmStart=tk.StringVar(value='False')
RFmb_warmStart = build_ArgListLabelFrame(RFmb_hyperParams, 'warm_start')
RFmb_warmStart.grid(row=1, column=2, padx=10, pady=5, sticky=EW)
RFmb_warmStart.grid_columnconfigure(0, weight=1)
RFmb_warmStart_entry=CTkOptionMenu(
        master=RFmb_warmStart, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=RFmbVar_warmStart,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
RFmb_warmStart_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_maxFeatures=tk.StringVar(value='sqrt')
RFmb_maxFeatures = build_ArgListLabelFrame(RFmb_hyperParams, 'max_features')
RFmb_maxFeatures.grid(row=1, column=3, padx=10, pady=5, sticky=EW)
RFmb_maxFeatures.grid_columnconfigure(0, weight=1)
RFmb_maxFeatures_entry=CTkEntry(
        master=RFmb_maxFeatures, 
        font=my_font1,
        textvariable=RFmbVar_maxFeatures,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_maxFeatures_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_minWeightFractionLeaf=tk.StringVar(value='0.0')
RFmb_minWeightFractionLeaf = build_ArgListLabelFrame(RFmb_hyperParams, 'min_weight_fraction_leaf')
RFmb_minWeightFractionLeaf.grid(row=1, column=4, padx=10, pady=5, sticky=EW)
RFmb_minWeightFractionLeaf.grid_columnconfigure(0, weight=1)
RFmb_minWeightFractionLeaf_entry=CTkEntry(
        master=RFmb_minWeightFractionLeaf, 
        font=my_font1,
        textvariable=RFmbVar_minWeightFractionLeaf,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_minWeightFractionLeaf_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmbVar_maxLeafNodes=tk.StringVar(value='None')
RFmb_maxLeafNodes = build_ArgListLabelFrame(RFmb_hyperParams, 'max_leaf_nodes')
RFmb_maxLeafNodes.grid(row=2, column=0, padx=10, pady=5, sticky=EW)
RFmb_maxLeafNodes.grid_columnconfigure(0, weight=1)
RFmb_maxLeafNodes_entry=CTkEntry(
        master=RFmb_maxLeafNodes, 
        font=my_font1,
        textvariable=RFmbVar_maxLeafNodes,
        corner_radius=0,
        border_width=0,
        width=40
    )
RFmb_maxLeafNodes_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

RFmb_inputs = {
    "N_ESTIMATORS": RFmbVar_nEstimators,
    "CRITERION": RFmbVar_criterion,
    "MAX_DEPTH": RFmbVar_maxDepth,
    "MIN_SAMPLE_SPLIT": RFmbVar_minSamplesSplit,
    "MIN_SAMPLE_LEAF": RFmbVar_minSamplesLeaf,
    "MIN_IMPURITY_DECREASE": RFmbVar_minImpurityDecrease,
    "RANDOM_STATE": RFmbVar_randomState,
    "WARM_STATE": RFmbVar_warmStart,
    "MAX_FEATURES": RFmbVar_maxFeatures,
    "MIN_WEIGHT_FRACTION_LEAF": RFmbVar_minWeightFractionLeaf,
    "MAX_LEAF_NODES": RFmbVar_maxLeafNodes
}

RFmb_submitBtn = CTkButton(
    master=RFmb_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=200,
    border_spacing=0,
    command=lambda: RF_MODEL_BUILD_SUBMIT(root, RESULTS_LOADING_IMG_PATH, RFmb_inputs, RFmb_resultsVar, my_font1)
)
RFmb_submitBtn.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

RFmb_results.grid_columnconfigure(0, weight=1)
RFmb_results.grid_rowconfigure(0, weight=1)
RFmb_resultsVar = StringVar(value="...")
RFmb_resultTextBox = SyncableTextBox(
    master=RFmb_results,
    text_variable=RFmb_resultsVar,
    my_font=my_font1
)
RFmb_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

model_build_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[0]] = RFmb_labelFrame

SVMmb_labelFrame = build_ArgListLabelFrame(model_build_panel, HYPER_PARAM_OPTIM_ALGORITHMS[1])
SVMmb_labelFrame.grid_columnconfigure(0, weight=1)
SVMmb_hyperParams = build_ArgListLabelFrame(SVMmb_labelFrame, 'HyperParameters')
SVMmb_results = build_ArgListLabelFrame(SVMmb_labelFrame, 'Result')
SVMmb_labelFrame.grid_rowconfigure(1, weight=1)

SVMmb_hyperParams.grid(row=0, column=0, padx=5, pady=2, sticky=NSEW)
SVMmb_results.grid(row=1, column=0, padx=5, pady=2, sticky=NSEW)
SVMmb_hyperParams.grid_columnconfigure(tuple(range(5)), weight=1)

SVMmbVar_C_field=tk.StringVar(value='1.0')
SVMmb_C_field = build_ArgListLabelFrame(SVMmb_hyperParams, 'C')
SVMmb_C_field.grid(row=0, column=0, padx=10, pady=5, sticky=EW)
SVMmb_C_field.grid_columnconfigure(0, weight=1)
SVMmb_C_field_entry=CTkEntry(
        master=SVMmb_C_field, 
        font=my_font1,
        textvariable=SVMmbVar_C_field,
        corner_radius=0,
        border_width=0,
        width=40
    )
SVMmb_C_field_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_kernel=tk.StringVar(value='rbf')
SVMmb_kernel = build_ArgListLabelFrame(SVMmb_hyperParams, 'kernel')
SVMmb_kernel.grid(row=0, column=1, padx=10, pady=5, sticky=EW)
SVMmb_kernel.grid_columnconfigure(0, weight=1)
SVMmb_kernel_entry=CTkOptionMenu(
        master=SVMmb_kernel, 
        font=my_font1,
        variable=SVMmbVar_kernel,
        values=SVMVar_kernel_options,
        dropdown_font=my_font1,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_kernel_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_degree=tk.StringVar(value='3')
SVMmb_degree = build_ArgListLabelFrame(SVMmb_hyperParams, 'degree')
SVMmb_degree.grid(row=0, column=2, padx=10, pady=5, sticky=EW)
SVMmb_degree.grid_columnconfigure(0, weight=1)
SVMmb_degree_entry=CTkEntry(
        master=SVMmb_degree, 
        font=my_font1,
        textvariable=SVMmbVar_degree,
        corner_radius=0,
        border_width=0,
        width=40
    )
SVMmb_degree_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_gamma=tk.StringVar(value=SVMVar_gamma_options[0])
SVMmb_gamma = build_ArgListLabelFrame(SVMmb_hyperParams, 'gamma')
SVMmb_gamma.grid(row=0, column=3, padx=10, pady=5, sticky=EW)
SVMmb_gamma.grid_columnconfigure(0, weight=1)
SVMmb_gamma_entry=CTkOptionMenu(
        master=SVMmb_gamma, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMmbVar_gamma,
        values=SVMVar_gamma_options,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_gamma_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_coef0=tk.StringVar(value='0.0')
SVMmb_coef0 = build_ArgListLabelFrame(SVMmb_hyperParams, 'coef0')
SVMmb_coef0.grid(row=0, column=4, padx=10, pady=5, sticky=EW)
SVMmb_coef0.grid_columnconfigure(0, weight=1)
SVMmb_coef0_entry=CTkEntry(
        master=SVMmb_coef0, 
        font=my_font1,
        textvariable=SVMmbVar_coef0,
        corner_radius=0,
        border_width=0,
        width=40
    )
SVMmb_coef0_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_tol=tk.StringVar(value='0.001')
SVMmb_tol = build_ArgListLabelFrame(SVMmb_hyperParams, 'tol')
SVMmb_tol.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
SVMmb_tol.grid_columnconfigure(0, weight=1)
SVMmb_tol_entry=CTkEntry(
        master=SVMmb_tol, 
        font=my_font1,
        textvariable=SVMmbVar_tol,
        corner_radius=0,
        border_width=0,
        width=40
    )
SVMmb_tol_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_shrinking=tk.StringVar(value='True')
SVMmb_shrinking = build_ArgListLabelFrame(SVMmb_hyperParams, 'shrinking')
SVMmb_shrinking.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
SVMmb_shrinking.grid_columnconfigure(0, weight=1)
SVMmb_shrinking_entry=CTkOptionMenu(
        master=SVMmb_shrinking, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMmbVar_shrinking,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_shrinking_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_probability=tk.StringVar(value='False')
SVMmb_probability = build_ArgListLabelFrame(SVMmb_hyperParams, 'probability')
SVMmb_probability.grid(row=1, column=2, padx=10, pady=5, sticky=EW)
SVMmb_probability.grid_columnconfigure(0, weight=1)
SVMmb_probability_entry=CTkOptionMenu(
        master=SVMmb_probability, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMmbVar_probability,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_probability_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_random_state=tk.StringVar(value='None')
SVMmb_random_state = build_ArgListLabelFrame(SVMmb_hyperParams, 'random_state')
SVMmb_random_state.grid(row=1, column=3, padx=10, pady=5, sticky=EW)
SVMmb_random_state.grid_columnconfigure(0, weight=1)
SVMmb_random_state_entry=CTkEntry(
        master=SVMmb_random_state, 
        font=my_font1,
        textvariable=SVMmbVar_random_state,
        corner_radius=0,
        border_width=0,
        width=40
    )
SVMmb_random_state_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMVar_decision_function_shape_options = ['ovr','ovo']
SVMmbVar_decision_function_shape=tk.StringVar(value=SVMVar_decision_function_shape_options[0])
SVMmb_decision_function_shape = build_ArgListLabelFrame(SVMmb_hyperParams, 'decision_function_shape')
SVMmb_decision_function_shape.grid(row=2, column=0, padx=10, pady=5, sticky=EW)
SVMmb_decision_function_shape.grid_columnconfigure(0, weight=1)
SVMmb_decision_function_shape_entry=CTkOptionMenu(
        master=SVMmb_decision_function_shape, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMmbVar_decision_function_shape,
        values=SVMVar_decision_function_shape_options,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_decision_function_shape_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmbVar_break_ties=tk.StringVar(value='False')
SVMmb_break_ties = build_ArgListLabelFrame(SVMmb_hyperParams, 'break_ties')
SVMmb_break_ties.grid(row=1, column=4, padx=10, pady=5, sticky=EW)
SVMmb_break_ties.grid_columnconfigure(0, weight=1)
SVMmb_break_ties_entry=CTkOptionMenu(
        master=SVMmb_break_ties, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=SVMmbVar_break_ties,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
SVMmb_break_ties_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

SVMmb_submitBtn = CTkButton(
    master=SVMmb_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=200,
    border_spacing=0,
    command=lambda: print('SUBMIT SVMmb !!')
)
SVMmb_submitBtn.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

SVMmb_results.grid_columnconfigure(0, weight=1)
SVMmb_results.grid_rowconfigure(0, weight=1)
SVMmb_resultsVar = StringVar(value="...")
SVMmb_resultTextBox = SyncableTextBox(
    master=SVMmb_results,
    text_variable=SVMmb_resultsVar,
    my_font=my_font1
)
SVMmb_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

model_build_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[1]] = SVMmb_labelFrame

LDAmb_labelFrame = build_ArgListLabelFrame(model_build_panel, HYPER_PARAM_OPTIM_ALGORITHMS[3])
LDAmb_labelFrame.grid_columnconfigure(0, weight=1)
LDAmb_hyperParams = build_ArgListLabelFrame(LDAmb_labelFrame, 'HyperParameters')
LDAmb_results = build_ArgListLabelFrame(LDAmb_labelFrame, 'Result')
LDAmb_labelFrame.grid_rowconfigure(1, weight=1)

LDAmb_hyperParams.grid(row=0, column=0, padx=5, pady=2, sticky=NSEW)
LDAmb_results.grid(row=1, column=0, padx=5, pady=2, sticky=NSEW)
LDAmb_hyperParams.grid_columnconfigure(tuple(range(5)), weight=1)

LDAmbVar_solver=tk.StringVar(value=LDAVar_solver_options[0])
LDAmb_solver = build_ArgListLabelFrame(LDAmb_hyperParams, 'solver')
LDAmb_solver.grid(row=0, column=0, padx=10, pady=5, sticky=EW)
LDAmb_solver.grid_columnconfigure(0, weight=1)
LDAmb_solver_entry=CTkOptionMenu(
        master=LDAmb_solver, 
        font=my_font1,
        variable=LDAmbVar_solver,
        values=LDAVar_solver_options,
        dropdown_font=my_font1,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LDAmb_solver_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAmbVar_shrinkage=tk.StringVar(value=3)
LDAmb_shrinkage = build_ArgListLabelFrame(LDAmb_hyperParams, 'shrinkage')
LDAmb_shrinkage.grid(row=0, column=1, padx=10, pady=5, sticky=EW)
LDAmb_shrinkage.grid_columnconfigure(0, weight=1)
LDAmb_shrinkage_entry=CTkEntry(
        master=LDAmb_shrinkage, 
        font=my_font1,
        textvariable=LDAmbVar_shrinkage,
        corner_radius=0,
        border_width=0,
        width=40
    )
LDAmb_shrinkage_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAmbVar_n_components=tk.StringVar(value='None')
LDAmb_n_components = build_ArgListLabelFrame(LDAmb_hyperParams, 'n_components')
LDAmb_n_components.grid(row=0, column=2, padx=10, pady=5, sticky=EW)
LDAmb_n_components.grid_columnconfigure(0, weight=1)
LDAmb_n_components_entry=CTkEntry(
        master=LDAmb_n_components, 
        font=my_font1,
        textvariable=LDAmbVar_n_components,
        corner_radius=0,
        border_width=0,
        width=40
    )
LDAmb_n_components_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAmbVar_tol=tk.StringVar(value='0.001')
LDAmb_tol = build_ArgListLabelFrame(LDAmb_hyperParams, 'tol')
LDAmb_tol.grid(row=0, column=3, padx=10, pady=5, sticky=EW)
LDAmb_tol.grid_columnconfigure(0, weight=1)
LDAmb_tol_entry=CTkEntry(
        master=LDAmb_tol, 
        font=my_font1,
        textvariable=LDAmbVar_tol,
        corner_radius=0,
        border_width=0,
        width=80
    )
LDAmb_tol_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAmbVar_store_covariance=tk.StringVar(value='False')
LDAmb_store_covariance = build_ArgListLabelFrame(LDAmb_hyperParams, 'store_covariance')
LDAmb_store_covariance.grid(row=0, column=4, padx=10, pady=5, sticky=EW)
LDAmb_store_covariance.grid_columnconfigure(0, weight=1)
LDAmb_store_covariance_entry=CTkOptionMenu(
        master=LDAmb_store_covariance, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=LDAmbVar_store_covariance,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LDAmb_store_covariance_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LDAmb_submitBtn = CTkButton(
    master=LDAmb_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=200,
    border_spacing=0,
    command=lambda: print('SUBMIT LDAmb !!')
)
LDAmb_submitBtn.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

LDAmb_results.grid_columnconfigure(0, weight=1)
LDAmb_results.grid_rowconfigure(0, weight=1)
LDAmb_resultsVar = StringVar(value="...")
LDAmb_resultTextBox = SyncableTextBox(
    master=LDAmb_results,
    text_variable=LDAmb_resultsVar,
    my_font=my_font1
)
LDAmb_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

model_build_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[3]] = LDAmb_labelFrame


LRmb_labelFrame = build_ArgListLabelFrame(model_build_panel, HYPER_PARAM_OPTIM_ALGORITHMS[2])
LRmb_labelFrame.grid_columnconfigure(0, weight=1)
LRmb_hyperParams = build_ArgListLabelFrame(LRmb_labelFrame, 'HyperParameters')
LRmb_results = build_ArgListLabelFrame(LRmb_labelFrame, 'Result')
LRmb_labelFrame.grid_rowconfigure(1, weight=1)

LRmb_hyperParams.grid(row=0, column=0, padx=5, pady=2, sticky=NSEW)
LRmb_results.grid(row=1, column=0, padx=5, pady=2, sticky=NSEW)
LRmb_hyperParams.grid_columnconfigure(tuple(range(5)), weight=1)

LRmbVar_l1_ratio=tk.StringVar(value='None')
LRmb_l1_ratio = build_ArgListLabelFrame(LRmb_hyperParams, 'l1_ratio')
LRmb_l1_ratio.grid(row=0, column=0, padx=10, pady=5, sticky=EW)
LRmb_l1_ratio.grid_columnconfigure(0, weight=1)
LRmb_l1_ratio_entry=CTkEntry(
        master=LRmb_l1_ratio, 
        font=my_font1,
        textvariable=LRmbVar_l1_ratio,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_l1_ratio_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_penalty=tk.StringVar(value=LRVar_penalty_options[1])
LRmb_penalty = build_ArgListLabelFrame(LRmb_hyperParams, 'penalty')
LRmb_penalty.grid(row=0, column=1, padx=10, pady=5, sticky=EW)
LRmb_penalty.grid_columnconfigure(0, weight=1)
LRmb_penalty_entry=CTkOptionMenu(
        master=LRmb_penalty, 
        font=my_font1,
        variable=LRmbVar_penalty,
        values=LRVar_penalty_options,
        dropdown_font=my_font1,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LRmb_penalty_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_tol=tk.StringVar(value='0.0001')
LRmb_tol = build_ArgListLabelFrame(LRmb_hyperParams, 'tol')
LRmb_tol.grid(row=0, column=2, padx=10, pady=5, sticky=EW)
LRmb_tol.grid_columnconfigure(0, weight=1)
LRmb_tol_entry=CTkEntry(
        master=LRmb_tol, 
        font=my_font1,
        textvariable=LRmbVar_tol,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_tol_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_C_field=tk.StringVar(value='1.0')
LRmb_C_field = build_ArgListLabelFrame(LRmb_hyperParams, 'C')
LRmb_C_field.grid(row=0, column=3, padx=10, pady=5, sticky=EW)
LRmb_C_field.grid_columnconfigure(0, weight=1)
LRmb_C_field_entry=CTkEntry(
        master=LRmb_C_field, 
        font=my_font1,
        textvariable=LRmbVar_C_field,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_C_field_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_fit_intercept=tk.StringVar(value='True')
LRmb_fit_intercept = build_ArgListLabelFrame(LRmb_hyperParams, 'fit_intercept')
LRmb_fit_intercept.grid(row=0, column=4, padx=10, pady=5, sticky=EW)
LRmb_fit_intercept.grid_columnconfigure(0, weight=1)
LRmb_fit_intercept_entry=CTkOptionMenu(
        master=LRmb_fit_intercept, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRmbVar_fit_intercept,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LRmb_fit_intercept_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_intercept_scaling=tk.StringVar(value='1.0')
LRmb_intercept_scaling = build_ArgListLabelFrame(LRmb_hyperParams, 'intercept_scaling')
LRmb_intercept_scaling.grid(row=1, column=0, padx=10, pady=5, sticky=EW)
LRmb_intercept_scaling.grid_columnconfigure(0, weight=1)
LRmb_intercept_scaling_entry=CTkEntry(
        master=LRmb_intercept_scaling, 
        font=my_font1,
        textvariable=LRmbVar_intercept_scaling,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_intercept_scaling_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_randomState=tk.StringVar(value='None')
LRmb_randomState = build_ArgListLabelFrame(LRmb_hyperParams, 'random_state')
LRmb_randomState.grid(row=1, column=1, padx=10, pady=5, sticky=EW)
LRmb_randomState.grid_columnconfigure(0, weight=1)
LRmb_randomState_entry=CTkEntry(
        master=LRmb_randomState, 
        font=my_font1,
        textvariable=LRmbVar_randomState,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_randomState_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_solver=tk.StringVar(value=LRVar_solver_options[0])
LRmb_solver = build_ArgListLabelFrame(LRmb_hyperParams, 'solver')
LRmb_solver.grid(row=1, column=2, padx=10, pady=5, sticky=EW)
LRmb_solver.grid_columnconfigure(0, weight=1)
LRmb_solver_entry=CTkOptionMenu(
        master=LRmb_solver, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRmbVar_solver,
        values=LRVar_solver_options,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LRmb_solver_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_warmStart=tk.StringVar(value='False')
LRmb_warmStart = build_ArgListLabelFrame(LRmb_hyperParams, 'warm_start')
LRmb_warmStart.grid(row=1, column=3, padx=10, pady=5, sticky=EW)
LRmb_warmStart.grid_columnconfigure(0, weight=1)
LRmb_warmStart_entry=CTkOptionMenu(
        master=LRmb_warmStart, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRmbVar_warmStart,
        values=['True', 'False'],
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LRmb_warmStart_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_max_iter=tk.StringVar(value='100')
LRmb_max_iter = build_ArgListLabelFrame(LRmb_hyperParams, 'max_iter')
LRmb_max_iter.grid(row=1, column=4, padx=10, pady=5, sticky=EW)
LRmb_max_iter.grid_columnconfigure(0, weight=1)
LRmb_max_iter_entry=CTkEntry(
        master=LRmb_max_iter, 
        font=my_font1,
        textvariable=LRmbVar_max_iter,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_max_iter_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRVar_multi_class_options = ['auto', 'ovr', 'multinomial']
LRmbVar_multi_class=tk.StringVar(value=LRVar_multi_class_options[0])
LRmb_multi_class = build_ArgListLabelFrame(LRmb_hyperParams, 'multi_class')
LRmb_multi_class.grid(row=2, column=0, padx=10, pady=5, sticky=EW)
LRmb_multi_class.grid_columnconfigure(0, weight=1)
LRmb_multi_class_entry=CTkOptionMenu(
        master=LRmb_multi_class, 
        font=my_font1,
        dropdown_font=my_font1,
        variable=LRmbVar_multi_class,
        values=LRVar_multi_class_options,
        corner_radius=0,
        anchor=CENTER,
        button_color=COLORS['GREY_FG'],
        button_hover_color=COLORS['GREY_FG'],
        fg_color=COLORS['GREY_FG']
    )
LRmb_multi_class_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmbVar_n_jobs=tk.StringVar(value='None')
LRmb_n_jobs = build_ArgListLabelFrame(LRmb_hyperParams, 'n_jobs')
LRmb_n_jobs.grid(row=2, column=1, padx=10, pady=5, sticky=EW)
LRmb_n_jobs.grid_columnconfigure(0, weight=1)
LRmb_n_jobs_entry=CTkEntry(
        master=LRmb_n_jobs, 
        font=my_font1,
        textvariable=LRmbVar_n_jobs,
        corner_radius=0,
        border_width=0,
        width=40
    )
LRmb_n_jobs_entry.grid(row=0, column=0, padx=10, pady=5, sticky=EW)

LRmb_submitBtn = CTkButton(
    master=LRmb_hyperParams,
    text='Submit',
    font=my_font1,
    fg_color=COLORS['MEDIUMGREEN_FG'],
    hover_color=COLORS['MEDIUMGREEN_HOVER_FG'],
    text_color='white',
    corner_radius=0,
    width=200,
    border_spacing=0,
    command=lambda: print('SUBMIT LR !!')
)
LRmb_submitBtn.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

LRmb_results.grid_columnconfigure(0, weight=1)
LRmb_results.grid_rowconfigure(0, weight=1)
LRmb_resultsVar = StringVar(value="...")
LRmb_resultTextBox = SyncableTextBox(
    master=LRmb_results,
    text_variable=LRmb_resultsVar,
    my_font=my_font1
)
LRmb_resultTextBox.grid(row=0, column=0, padx=10, pady=5, sticky=NSEW)

model_build_algo_frames[HYPER_PARAM_OPTIM_ALGORITHMS[2]] = LRmb_labelFrame




def show_modelBuild_AlgoLabelFrame(option):
    for frame in model_build_algo_frames.values():
        frame.grid_remove()
    model_build_algo_frames[option].grid(row=1,column=0,rowspan=6, columnspan=7,sticky=NSEW,padx=8,pady=(2,5))
    model_build_algo_frames[option].grid_columnconfigure(tuple(range(7)), weight=1)

algo_dropdown.configure(command=show_modelBuild_AlgoLabelFrame)

# Setting Default model_build_selected_algorithm to index 0 and also displaying that frame (as set doesn't trigger command)
model_build_selected_algorithm.set(HYPER_PARAM_OPTIM_ALGORITHMS[0])
show_modelBuild_AlgoLabelFrame(HYPER_PARAM_OPTIM_ALGORITHMS[0])

root.mainloop()