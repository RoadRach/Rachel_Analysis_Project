from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
# from airflow_docker.vitamincscraper.vitamincscraper.spiders.vitamincspider import VitamincspiderSpider

default_args = {
    'owner': 'rachang',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='ourfirst_dag',
    default_args=default_args,
    description='this is first dag',
    start_date=datetime(2023,9,29),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="/opt/airflow/scripts/bash1.sh "
    )

    # task2 = PythonOperator(
    #     task_id='scrapy_vitaminc',
    #     python_callable=VitamincspiderSpider
    # )

    task1