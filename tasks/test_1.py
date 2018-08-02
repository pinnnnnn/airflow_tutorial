
# coding: utf-8

import pandas as pd

data = {"name" : "Peiyun",
        "City" : "Shanghai",
        "Age": 17}

df = pd.DataFrame([data], columns = data.keys())

#out = "/out/"

df.to_csv("/Users/pinnzhang/Documents/airflow_tutorial/tasks/Pinn.csv")
