import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(patients)):
        p_id = patients['patient_id'][i]
        p_name = patients['patient_name'][i]
        conditions = patients['conditions'][i]
        for condition in conditions.split():
            if condition.startswith('DIAB1'):
                result.append([p_id,p_name,conditions])

    return pd.DataFrame(result, columns =['patient_id','patient_name','conditions'])     
        