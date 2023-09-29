from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

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
    schedule_interval='0 0 * * *'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="/opt/airflow/scripts/shell/bash1.sh "
    )

    task2 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs(
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)
            )
        """
    )

    # task2 = PythonOperator(
    #     task_id='scrapy_vitaminc',
    #     python_callable=VitamincspiderSpider
    # )

    task2