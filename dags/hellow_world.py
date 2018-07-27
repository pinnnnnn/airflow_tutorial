from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Define a python function so that it can be called later
def print_hello():
    return 'Hello world!'

dag = DAG('hello_world',  #the name of the DAG, shown in the webserver
          description='Simple tutorial DAG',
          # DAG will be triggered after start_data + schedule_interval
          schedule_interval='8 * * * *',
          # set the starting time as now
          start_date=datetime.now(), # tell the webserver when to start
          catchup=False)

# A dummy operator that does nothing. It is written to demonstrate how
# two tasks can be connected
dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

# An operator to call the function print_hellop
hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

# Connect two tasks together
dummy_operator >> hello_operator
