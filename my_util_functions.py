from customtkinter import *
from my_utils import InProgressWindow
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
    
    

    