from customtkinter import *
from my_utils import InProgressWindow
from time import sleep
from json import dumps as jsonDumps

def RF_HP_OPTIM_SUBMIT (master:CTk, loading_gif_path:str, RF_inputs: dict, RF_resultsVar: StringVar):
    inProgress = InProgressWindow(master, loading_gif_path)
    inProgress.create()
    
    RF_inputs = {
        'METHOD': RF_inputs['METHOD'].get(),
        'SCORING': RF_inputs['SCORING'].get(),
        'CROSS_FOLD_VALID.': RF_inputs['CROSS_FOLD_VALID'].get(),
        'N_ESTIMATORS': {k:v.get() for k,v in RF_inputs['N_ESTIMATORS'].items()},
        'CRITERIONS': RF_inputs['CRITERIONS'].get().split(','),
        'MAX_DEPTH': {k:v.get() for k,v in RF_inputs['MAX_DEPTH'].items()},
        'MIN_SAMPLE_SPLIT': {k:v.get() for k,v in RF_inputs['MIN_SAMPLE_SPLIT'].items()},
        'MIN_SAMPLE_LEAF': {k:v.get() for k,v in RF_inputs['MIN_SAMPLE_LEAF'].items()}
    }
    def update_progress ():
        inProgress.destroy()
        RF_resultsVar.set(jsonDumps(RF_inputs, indent=4))
        
    master.after(2000, update_progress)
    
    

    