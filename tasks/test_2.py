
# coding: utf-8


import pandas as pd
data = {"name" : "Luke",
        "City" : "D.C",
        "Age": 25}
df = pd.DataFrame([data], columns = data.keys())
df.to_csv("/Users/pinnzhang/Documents/airflow_test/tasks/Luke.csv")
