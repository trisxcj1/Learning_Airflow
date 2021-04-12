# -- Imports 
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.bash_operator import BashOperator

from datetime import timedelta

# -- Airflow setup
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utile.dates.days_ago(1),
    'email': ['airflow@example.com']
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=10)
}

# -- DAG
dag = DAG(
    'trialDAG',
    default_args=default_args,
    description='Learning Airflow and creating my first DAG',
    schedule_interval=timedelta(days=1)
)

# -- Tasks
task_1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

task_2 = BashOperator(
    task_id='sleep_5',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag
)

task_3 = BashOperator(
    task_id='sleep_10',
    depends_on_past=False,
    bash_command='sleep 10',
    dag=dag
)

# -- Dependencies/Task orchestration
task_3 >> task_1 >> task_2