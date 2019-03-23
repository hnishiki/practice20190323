import pandas as pd
import numpy as np

df = pd.read_csv('sample.csv')
target_name_ary = ['type_1', 'type_3']
anken_id_set = set(df['anken_id'].values.tolist())

csv_list = []
for anken_id in anken_id_set:
    csv_row = []
    csv_row.append(anken_id)
    df_tmp1 = df[df['anken_id'] == anken_id]

    for target_name in target_name_ary:
        type_num_set = set(df_tmp1[target_name].values.tolist())
        min_num = min(type_num_set)
        max_num = max(type_num_set)
        
        s_min_mean = df_tmp1[df_tmp1[target_name] == min_num].mean()
        s_max_mean = df_tmp1[df_tmp1[target_name] == max_num].mean()
        csv_row.append(s_max_mean['score'] - s_min_mean['score'])

    csv_list.append(csv_row)

header = ['anken_id']
header.extend(target_name_ary)

df_csv = pd.DataFrame(csv_list, columns = header)
df_csv = df_csv.set_index('anken_id')
df_csv.to_csv('change_rate.csv')
