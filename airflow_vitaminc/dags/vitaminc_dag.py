from airflow import DAG 
from datetime import datetime

with DAG(
    dag_id='our_first_dag',
    description='This is my first dag',
    start_date=datetime(2023,9,13,2),
    schedule_interval='@hourly'
) as dag:
    pass