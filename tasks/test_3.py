
# coding: utf-8


import pandas as pd
data = {"name" : "Doraemon",
        "City" : "Fukuoka",
        "Age": 100}
df = pd.DataFrame([data], columns = data.keys())
df.to_csv("/Users/pinnzhang/Documents/airflow_test/tasks/Doraemon.csv")
