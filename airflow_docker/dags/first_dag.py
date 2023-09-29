from airflow import DAG
from datetime import datetime,timedelta

default_args = {
    'owner': 'rachang',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='ourfirst_dag',
    description='this is first dag',
    start_date=datetime(2023,9,29),
    schedule_interval='@daily'
) as dag:
    pass