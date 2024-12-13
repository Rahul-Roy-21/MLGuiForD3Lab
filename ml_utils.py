import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef, cohen_kappa_score, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report, RocCurveDisplay, roc_curve
import matplotlib.pyplot as plt

PLOT_PROPS = {
    'ROC_CURVE': {
        'COLOR': 'blue',
        'LW': 2
    },
    'DIAGONAL_REF_LINE': {
        'COLOR': 'green'
    },
    'TITLE' : {
        'FONT_SIZE': 23,
        'FONT_WEIGHT': "bold",
        'FONT_STYLE' : "Marker Felt"
    }
}

def CHECK_DIR(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

# Function to check if both files have identical column sets
def CHECK_XLS_FILES(train_file_path: str, test_file_path: str):
    warnings=[]
    try:
        train_df = pd.read_excel(train_file_path)
    except ImportError as e:
        if 'openpyxl' in str(e):
            warnings.append("Missing dependency: openpyxl is required to read Excel files.")
        else:
            warnings.append(f"Error reading Train file: {e}")
        train_df = None
    except Exception as e:
        warnings.append(f"Error reading Train file: {e}")
        train_df = None
    
    try:
        test_df = pd.read_excel(test_file_path)
    except ImportError as e:
        if 'openpyxl' in str(e):
            warnings.append("Missing dependency: openpyxl is required to read Excel files.")
        else:
            warnings.append(f"Error reading Test file: {e}")
        test_df = None
    except Exception as e:
        warnings.append(f"Error reading Test file: {e}")
        test_df = None

    if train_df is not None and test_df is not None:
        if set(train_df.columns) != set(test_df.columns):
            warnings.append("The files do not have the same columns.")
        else:
            try:
                # Drop the first and last columns
                common_cols = train_df.iloc[:, 1:-1]  
                return True, common_cols
            except Exception as e:
                warnings.append(f"Error filtering columns: {e}")

    if len(warnings):
        return False, []
    
def RF_MODEL_BUILD_PROCESS (RfMB_ValidatedInputs: dict, trainFilePath: str, testFilePath: str):
    regressor = RandomForestClassifier(
        n_estimators= RfMB_ValidatedInputs["N_ESTIMATORS"],
        criterion= RfMB_ValidatedInputs["CRITERION"],
        max_depth= RfMB_ValidatedInputs["MAX_DEPTH"],
        min_samples_split= RfMB_ValidatedInputs["MIN_SAMPLE_SPLIT"],
        min_samples_leaf= RfMB_ValidatedInputs["MIN_SAMPLE_LEAF"],
        min_impurity_decrease= RfMB_ValidatedInputs["MIN_IMPURITY_DECREASE"],
        random_state= RfMB_ValidatedInputs["RANDOM_STATE"],
        warm_start= RfMB_ValidatedInputs["WARM_START"],
        max_features= RfMB_ValidatedInputs["MAX_FEATURES"],
        min_weight_fraction_leaf= RfMB_ValidatedInputs["MIN_WEIGHT_FRACTION_LEAF"],
        max_leaf_nodes= RfMB_ValidatedInputs["MAX_LEAF_NODES"],
        oob_score=True
    )

    trainDF = pd.read_excel(trainFilePath)
    testDF = pd.read_excel(testFilePath)
    columnsToSelect = RfMB_ValidatedInputs["FEATURES"]
    x_train = trainDF.loc[:, columnsToSelect]
    y_train = trainDF.iloc[:, -1]
    x_test = testDF.loc[:, columnsToSelect]
    y_test = testDF.iloc[:,-1]

    # MODEL TRAINING
    regressor.fit(x_train, y_train)
    y_train_pred = regressor.predict(x_train)
    y_test_pred = regressor.predict(x_test)
    y_score1 = regressor.predict_proba(x_train)[:,1]
    y_score2 = regressor.predict_proba(x_test)[:,1]

    # PREPARE RESULTS..
    results = {
        'accuracy_train' : f'%.4f' % accuracy_score(y_train, y_train_pred),
        'accuracy_test' : f'%.4f' % accuracy_score(y_test, y_test_pred),
        'precision_train' : f'%.4f' % precision_score(y_train, y_train_pred),
        'precision_test' : f'%.4f' % precision_score(y_test, y_test_pred),
        'recall_train' : f'%.4f' % recall_score(y_train, y_train_pred),
        'recall_test' : f'%.4f' % recall_score(y_test, y_test_pred),
        'f1_score_train' : f'%.4f' % f1_score(y_train, y_train_pred),
        'f1_score_test' : f'%.4f' % f1_score(y_test, y_test_pred),
        'matthews_corrcoef_train' : f'%.4f' % matthews_corrcoef(y_train, y_train_pred),
        'matthews_corrcoef_test' : f'%.4f' % matthews_corrcoef(y_test, y_test_pred),
        'cohen_kappa_score_train' : f'%.4f' % cohen_kappa_score(y_train, y_train_pred),
        'cohen_kappa_score_test' : f'%.4f' % cohen_kappa_score(y_test, y_test_pred),
        'roc_auc_score_train' : f'%.4f' % roc_auc_score(y_train, y_score1),
        'roc_auc_score_test' : f'%.4f' % roc_auc_score(y_test, y_score2),
    }

    # GENERATE RFC.xlsx 
    rfr_pred1 = pd.DataFrame(
        {'Y_train': y_train, 'Y_train_pred': y_train_pred}
    )
    rfr_pred2 = pd.DataFrame(
        {'Y_test': y_test,'Y_test_pred': y_test_pred}
    )
    rfr_results = pd.concat([rfr_pred1, rfr_pred2], axis=1)
    
    CHECK_DIR('output')
    rfr_results.to_excel(
        excel_writer=os.path.join('output', 'RFC.xlsx'), 
        index=False
    )

    # GENERATE RFC_Results.txt
    output_list_rfr = [
        'Confusion Matrix of Training set:',
        confusion_matrix(y_train, y_train_pred),
        'Confusion Matrix of Test set:',
        confusion_matrix(y_test, y_test_pred),
        'Classification Report for Training set:',
        classification_report(y_train, y_train_pred),
        'Classification Report for Test set:',
        classification_report(y_test, y_test_pred),
        'parameters:',
        str(regressor.get_params())
    ]

    with open(file=os.path.join('output','RFC_Results.txt'), mode='w', encoding='utf-8') as my_file_rfr:
        for output in output_list_rfr:
            my_file_rfr.write(str(output) + '\n')

    # GENERATE RFC_RocCurve_Test.png
    roc_te = RocCurveDisplay.from_estimator(regressor, x_test, y_test)
    plt.clf()
    plt.subplots(1, figsize=(10,10))
    roc_te.plot(
        color=PLOT_PROPS['ROC_CURVE']['COLOR'], 
        lw=PLOT_PROPS['ROC_CURVE']['LW']
    )
    plt.plot(
        [0, 1], 
        ls="--", 
        color=PLOT_PROPS['DIAGONAL_REF_LINE']['COLOR']
    )
    plt.title(
        'ROC Curve for Test data', 
        fontsize=PLOT_PROPS['TITLE']['FONT_SIZE'], 
        fontweight=PLOT_PROPS['TITLE']['FONT_WEIGHT'], 
        fontname=PLOT_PROPS['TITLE']['FONT_STYLE']
    )
    plt.savefig(
        os.path.join('output', 'RFC_RocCurve_Test.png')
    )

    # GENERATE RFC_RocCurve_Train.png
    roc_tr = RocCurveDisplay.from_estimator(regressor, x_train, y_train)
    plt.clf()
    plt.subplots(1, figsize=(10,10))
    roc_tr.plot(
        color=PLOT_PROPS['ROC_CURVE']['COLOR'], 
        lw=PLOT_PROPS['ROC_CURVE']['LW']
    )
    plt.plot(
        [0, 1], 
        ls="--", 
        color=PLOT_PROPS['DIAGONAL_REF_LINE']['COLOR']
    )
    plt.title(
        'ROC Curve for Train data', 
        fontsize=PLOT_PROPS['TITLE']['FONT_SIZE'], 
        fontweight=PLOT_PROPS['TITLE']['FONT_WEIGHT'], 
        fontname=PLOT_PROPS['TITLE']['FONT_STYLE']
    )
    plt.savefig(
        os.path.join('output', 'RFC_RocCurve_Train.png')
    )

    return results