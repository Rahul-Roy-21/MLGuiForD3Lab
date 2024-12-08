from customtkinter import *
from my_utils import InProgressWindow, CustomWarningBox
from time import sleep
from json import dumps as jsonDumps

def format_list_display(A:list):
    nE = len(A)
    if nE>6:
        return f'[{str(A[:3])[1:-1]},..,{str(A[-2:])[1:-1]}]'
    else:
        return str(A)

def RF_HP_OPTIM_SUBMIT (master:CTk, loading_gif_path:str, RF_inputs: dict, RF_resultsVar: StringVar):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    nEstimators_values = list(range(
        RF_inputs['N_ESTIMATORS']['_FROM'].get(), 
        RF_inputs['N_ESTIMATORS']['_TO'].get()+1, 
        RF_inputs['N_ESTIMATORS']['_STEP'].get()
    ))
    maxDepth_values = list(range(
        RF_inputs['MAX_DEPTH']['_FROM'].get(), 
        RF_inputs['MAX_DEPTH']['_TO'].get()+1
    ))
    minSampleSplit_values = list(range(
        RF_inputs['MIN_SAMPLE_SPLIT']['_FROM'].get(), 
        RF_inputs['MIN_SAMPLE_SPLIT']['_TO'].get()+1
    ))
    minSampleLeaf_values = list(range(
        RF_inputs['MIN_SAMPLE_LEAF']['_FROM'].get(), 
        RF_inputs['MIN_SAMPLE_LEAF']['_TO'].get()+1
    ))

    RF_inputs = {
        'METHOD': RF_inputs['METHOD'].get(),
        'SCORING': RF_inputs['SCORING'].get(),
        'CROSS_FOLD_VALID.': RF_inputs['CROSS_FOLD_VALID'].get(),
        'N_ESTIMATORS': format_list_display(nEstimators_values),
        'CRITERIONS': RF_inputs['CRITERIONS'].get().split(','),
        'MAX_DEPTH': format_list_display(maxDepth_values),
        'MIN_SAMPLE_SPLIT': format_list_display(minSampleSplit_values),
        'MIN_SAMPLE_LEAF': format_list_display(minSampleLeaf_values)
    }
    def update_progress ():
        inProgress.destroy()
        RF_resultsVar.set(jsonDumps(RF_inputs, indent=4))
        
    master.after(2000, update_progress)

def RF_MODEL_BUILD_SUBMIT (master:CTk, loading_gif_path:str, RFmb_inputs: dict, RFmb_resultsVar: StringVar, font: CTkFont):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    RFmb_out = {k:v.get() for k,v in RFmb_inputs.items()}
    WARNINGS = []

    # n_estimators
    try:
        RFmb_out["N_ESTIMATORS"] = int(RFmb_out["N_ESTIMATORS"])
    except:
        WARNINGS.append("N_ESTIMATORS must be an INTEGER")

    # MAX_DEPTH
    try:
        RFmb_out["MAX_DEPTH"] = None if RFmb_out["MAX_DEPTH"].lower()=='none' else int(RFmb_out["MAX_DEPTH"])
    except:
        WARNINGS.append("MAX_DEPTH must be an INTEGER or 'None'")

    # MIN_SAMPLE_SPLIT
    try:
        RFmb_out["MIN_SAMPLE_SPLIT"] = float(RFmb_out["MIN_SAMPLE_SPLIT"])
    except:
        WARNINGS.append('MIN_SAMPLE_SPLIT must be int or float')
    
    # MIN_SAMPLE_LEAF
    try:
        RFmb_out["MIN_SAMPLE_LEAF"] = float(RFmb_out["MIN_SAMPLE_LEAF"])
    except:
        WARNINGS.append('MIN_SAMPLE_LEAF must be int or float')

    # MIN_IMPURITY_DECREASE
    try:
        RFmb_out["MIN_IMPURITY_DECREASE"] = float(RFmb_out["MIN_IMPURITY_DECREASE"])
    except:
        WARNINGS.append('MIN_IMPURITY_DECREASE must be float')

    # RANDOM_STATE
    try:
        RFmb_out["RANDOM_STATE"] = None if RFmb_out["RANDOM_STATE"].lower()=='none' else int(RFmb_out["RANDOM_STATE"])
    except:
        WARNINGS.append("RANDOM_STATE must be an INTEGER or 'None'")

    # MAX_FEATURES
    try:
        if RFmb_out["MAX_FEATURES"].lower()=='none':
            RFmb_out["MAX_FEATURES"] = None
        elif RFmb_out["MAX_FEATURES"].lower() in ['sqrt', 'log2']:
            RFmb_out["MAX_FEATURES"] = RFmb_out["MAX_FEATURES"].lower()
        else:
            RFmb_out["MAX_FEATURES"] = float(RFmb_out["MAX_FEATURES"])
    except:
        WARNINGS.append("MAX_FEATURES must be an INTEGER, FLOAT or either of 'sqrt'/'log2'/None")
    
    # MIN_WEIGHT_FRACTION_LEAF
    try:
        RFmb_out["MIN_WEIGHT_FRACTION_LEAF"] = float(RFmb_out["MIN_WEIGHT_FRACTION_LEAF"])
    except:
        WARNINGS.append('MIN_WEIGHT_FRACTION_LEAF must be float')
    
    # MAX_LEAF_NODES
    try:
        RFmb_out["MAX_LEAF_NODES"] = None if RFmb_out["MAX_LEAF_NODES"].lower()=='none' else int(RFmb_out["MAX_LEAF_NODES"])
    except:
        WARNINGS.append("MAX_LEAF_NODES must be an INTEGER")
    
    def update_success ():
        inProgress.destroy()
        RFmb_resultsVar.set(jsonDumps(RFmb_out, indent=4))
        
    def update_failure (warnings: list):
        inProgress.destroy()
        RFmb_resultsVar.set('..')
        CustomWarningBox(master, warnings, font)


    if len(WARNINGS) == 0:
        master.after(2000, update_success)
    else:
        master.after(1000, lambda warnings=WARNINGS: update_failure(warnings))

    