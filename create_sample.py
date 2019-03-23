import pandas as pd
import random

ids = 1
csv_list = []
for i in range(10000,10011):
    anken_id = i
    for j in range(1,6):
        type_1 = j
        for k in range(1,6):
            type_2 = k
            for l in range(1,6):
                type_3 = l
                for m in range(1,6):
                    type_4 = m
                    score = random.uniform(0,100)
                    item = [ids, anken_id, type_1, type_2, type_3, type_4, score]
                    csv_list.append(item)
                    ids = ids + 1
                    
df = pd.DataFrame(csv_list, columns= ['id', 'anken_id', 'type_1', 'type_2', 'type_3', 'type_4', 'score'])
df = df.set_index('id')
df.to_csv('sample.csv')
