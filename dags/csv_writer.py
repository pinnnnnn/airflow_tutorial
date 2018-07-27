from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime


dag = DAG(
    'write_csv',
    description = 'test code',
    start_date = datetime.now(),
    catchup = False,
    schedule_interval = '8 * * * *')

task_1 = BashOperator(
        task_id='task_1',
        bash_command='python3 /Users/pinnzhang/Documents/airflow_tutorial/tasks/test_1.py',
        dag = dag
    )

task_2 = BashOperator(
        task_id='task_2',
        bash_command='python3 /Users/pinnzhang/Documents/airflow_tutorial/tasks/test_2.py',
        dag = dag
    )

task_3 = BashOperator(
        task_id='task_3',
        bash_command='python3 /Users/pinnzhang/Documents/airflow_tutorial/tasks/test_3.py',
        dag = dag
    )

task_1 >> task_2 >> task_3
