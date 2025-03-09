#1873. Calculate Special bonus

#Method 1: Through Python
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
      result = []
    for i in range(len(employees)):
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if (e_id % 2 !=0) and (name[0])!='M':
            result.append([e_id,employees['salary'][i]])
        else:
            result.append([e_id,0]) 
    return pd.DataFrame(result,columns = ['employee_id','bonus']).sort_values('employee_id')


#Method 2


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy()
    df['bonus'] = df.apply(
        lambda row: row['salary'] if row['employee_id'] % 2 != 0 and row['name'][0] != 'M' else 0,
        axis=1
    )
    return df[['employee_id','bonus']].sort_values('employee_id')
