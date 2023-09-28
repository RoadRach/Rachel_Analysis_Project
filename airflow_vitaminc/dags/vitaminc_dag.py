from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
default_args = {
    'owner': 'rach',
    'retries' : 5,
    'retry_delay' : timedelta(minute=2)
}

with DAG(
    dag_id='our_first_dag',
    default_args=default_args,
    description='This is my first dag',
    start_date=datetime(2023,9,13,2),
    schedule_interval='@hourly'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )
    task2 = PythonOperator(
        task_id='second_task',
        
    )

    task1