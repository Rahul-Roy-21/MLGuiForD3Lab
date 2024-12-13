from customtkinter import *
from my_utils import InProgressWindow, CustomWarningBox, CustomSuccessBox
from time import sleep
from json import dumps as jsonDumps
from ml_utils import *

def convertStrToIntOrFloat(value: str):
    return float(value) if '.' in value else int(value)
    
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

def RF_MODEL_BUILD_SUBMIT (
        master:CTk, loading_gif_path:str, 
        RFmb_inputs: dict, RFmb_resultsVar: StringVar, font: CTkFont,
        trainEntryVar: StringVar, testEntryVar: StringVar):
    
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()

    def update_success (processOutput: dict):
        inProgress.destroy()
        RFmb_resultsVar.set(jsonDumps(processOutput, indent=4))
        CustomSuccessBox(master, "Calculations Completed !!", font)
        
    def update_failure (warnings: list):
        inProgress.destroy()
        RFmb_resultsVar.set('..')
        CustomWarningBox(master, warnings, font)
    
    RFmb_out = {k:v.get() for k,v in RFmb_inputs.items()}
    WARNINGS = []

    # FEATURES
    if not len(RFmb_out["FEATURES"]):
        master.after(1000, lambda warnings=['No FEATURES selected !!']: update_failure(warnings))
        return
    else:
        RFmb_out["FEATURES"] = RFmb_out["FEATURES"].split(',')

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
        RFmb_out["MIN_SAMPLE_SPLIT"] = convertStrToIntOrFloat(RFmb_out["MIN_SAMPLE_SPLIT"])
    except:
        WARNINGS.append('MIN_SAMPLE_SPLIT must be int or float')
    
    # MIN_SAMPLE_LEAF
    try:
        RFmb_out["MIN_SAMPLE_LEAF"] = convertStrToIntOrFloat(RFmb_out["MIN_SAMPLE_LEAF"])
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

    # WARM START
    RFmb_out["WARM_START"] = True if RFmb_out["WARM_START"].lower()=='true' else False

    # MAX_FEATURES
    try:
        if RFmb_out["MAX_FEATURES"].lower()=='none':
            RFmb_out["MAX_FEATURES"] = None
        elif RFmb_out["MAX_FEATURES"].lower() in ['sqrt', 'log2']:
            RFmb_out["MAX_FEATURES"] = RFmb_out["MAX_FEATURES"].lower()
        else:
            RFmb_out["MAX_FEATURES"] = convertStrToIntOrFloat(RFmb_out["MAX_FEATURES"])
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
    
    if len(WARNINGS) == 0:
        print("VALIDATED_INPUTS: ", jsonDumps(RFmb_out, indent=4))
        try:
            processResultDict = RF_MODEL_BUILD_PROCESS(
                RfMB_ValidatedInputs=RFmb_out, 
                trainFilePath=trainEntryVar.get(),
                testFilePath=testEntryVar.get()
            )
            master.after(1000, lambda processOut=processResultDict: update_success(processOut))
        except Exception as ex:
            master.after(1000, lambda warnings=[str(ex)]: update_failure(warnings))
    else:
        master.after(1000, lambda warnings=WARNINGS: update_failure(warnings))

def SVM_MODEL_BUILD_SUBMIT (master:CTk, loading_gif_path:str, SVMmb_inputs: dict, SVMmb_resultsVar: StringVar, font: CTkFont):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    SVMmb_out = {k:v.get() for k,v in SVMmb_inputs.items()}
    WARNINGS = []

    # C
    try:
        SVMmb_out["C"] = float(SVMmb_out["C"])
    except:
        WARNINGS.append('C must be int or float')

    # DEGREE
    try:
        SVMmb_out["DEGREE"] = int(SVMmb_out["DEGREE"])
    except:
        WARNINGS.append("DEGREE must be an INTEGER")

    # COEF0
    try:
        SVMmb_out["COEF0"] = float(SVMmb_out["COEF0"])
    except:
        WARNINGS.append('COEF0 must be float')

    # TOL
    try:
        SVMmb_out["TOL"] = float(SVMmb_out["TOL"])
    except:
        WARNINGS.append('TOL must be float')

    # RANDOM_STATE
    try:
        SVMmb_out["RANDOM_STATE"] = None if SVMmb_out["RANDOM_STATE"].lower()=='none' else int(SVMmb_out["RANDOM_STATE"])
    except:
        WARNINGS.append("RANDOM_STATE must be an INTEGER or 'None'")
    
    def update_success ():
        inProgress.destroy()
        SVMmb_resultsVar.set(jsonDumps(SVMmb_out, indent=4))
        
    def update_failure (warnings: list):
        inProgress.destroy()
        SVMmb_resultsVar.set('..')
        CustomWarningBox(master, warnings, font)

    if len(WARNINGS) == 0:
        master.after(2000, update_success)
    else:
        master.after(1000, lambda warnings=WARNINGS: update_failure(warnings))

def LDA_MODEL_BUILD_SUBMIT (master:CTk, loading_gif_path:str, LDAmb_inputs: dict, LDAmb_resultsVar: StringVar, font: CTkFont):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    LDAmb_out = {k:v.get() for k,v in LDAmb_inputs.items()}
    WARNINGS = []

    # SHRINKAGE
    try:
        if LDAmb_out["SHRINKAGE"].lower()=='none':
            LDAmb_out["SHRINKAGE"] = None
        elif LDAmb_out["SHRINKAGE"].lower()=='auto':
            LDAmb_out["SHRINKAGE"] = 'auto'
        else:
            LDAmb_out["SHRINKAGE"] = float(LDAmb_out["SHRINKAGE"])
    except:
        WARNINGS.append("SHRINKAGE must be a float, 'auto' or None")

    # N_COMPONENTS
    try:
        LDAmb_out["N_COMPONENTS"] = None if LDAmb_out["N_COMPONENTS"].lower()=='none' else int(LDAmb_out["N_COMPONENTS"])
    except:
        WARNINGS.append("N_COMPONENTS must be an integer or None")

    # TOL
    try:
        LDAmb_out["TOL"] = float(LDAmb_out["TOL"])
    except:
        WARNINGS.append('TOL must be float')

    def update_success ():
        inProgress.destroy()
        LDAmb_resultsVar.set(jsonDumps(LDAmb_out, indent=4))
        
    def update_failure (warnings: list):
        inProgress.destroy()
        LDAmb_resultsVar.set('..')
        CustomWarningBox(master, warnings, font)

    if len(WARNINGS) == 0:
        master.after(2000, update_success)
    else:
        master.after(1000, lambda warnings=WARNINGS: update_failure(warnings))

def LR_MODEL_BUILD_SUBMIT (master:CTk, loading_gif_path:str, LRmb_inputs: dict, LRmb_resultsVar: StringVar, font: CTkFont):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    LRmb_out = {k:v.get() for k,v in LRmb_inputs.items()}
    WARNINGS = []

    # L1_RATIO
    try:
        LRmb_out["L1_RATIO"] = None if LRmb_out["L1_RATIO"].lower()=='none' else float(LRmb_out["L1_RATIO"])
    except:
        WARNINGS.append('L1_RATIO must be float or None')

    # PENALTY
    if LRmb_out["PENALTY"].lower()=='none':
        LRmb_out["PENALTY"] = None
    
    # TOL
    try:
        LRmb_out["TOL"] = float(LRmb_out["TOL"])
    except:
        WARNINGS.append('TOL must be float')

    # C
    try:
        LRmb_out["C"] = float(LRmb_out["C"])
    except:
        WARNINGS.append('C must be float')

    # INTERCEPT_SCALING
    try:
        LRmb_out["INTERCEPT_SCALING"] = float(LRmb_out["INTERCEPT_SCALING"])
    except:
        WARNINGS.append('INTERCEPT_SCALING must be int or float')

    # RANDOM_STATE
    try:
        LRmb_out["RANDOM_STATE"] = None if LRmb_out["RANDOM_STATE"].lower()=='none' else int(LRmb_out["RANDOM_STATE"])
    except:
        WARNINGS.append("RANDOM_STATE must be an INTEGER or 'None'")

    # MAX_ITER
    try:
        LRmb_out["MAX_ITER"] = int(LRmb_out["MAX_ITER"])
    except:
        WARNINGS.append('MAX_ITER must be int')
    
    # N_JOBS
    try:
        LRmb_out["N_JOBS"] = None if LRmb_out["N_JOBS"].lower()=='none' else int(LRmb_out["N_JOBS"])
    except:
        WARNINGS.append("N_JOBS must be an integer or None")
    
    def update_success ():
        inProgress.destroy()
        LRmb_resultsVar.set(jsonDumps(LRmb_out, indent=4))
        
    def update_failure (warnings: list):
        inProgress.destroy()
        LRmb_resultsVar.set('..')
        CustomWarningBox(master, warnings, font)

    if len(WARNINGS) == 0:
        master.after(2000, update_success)
    else:
        master.after(1000, lambda warnings=WARNINGS: update_failure(warnings))
