# -- Imports 
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from datetime import timedelta

# -- Airflow setup
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
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

def print_fun(my_input):
    
    # should print in console
    print(str(my_input))

    # should print in Airflow logs
    return str(my_input)

task_4 = PythonOperator(
    task_id='python_script',
    python_callable=print_fun,
    op_kwargs={'my_input': 'Hey, man! Wudditdooo?'},
    dag=dag
)

# -- Dependencies/Task orchestration
task_3 >> [task_1, task_4] >> task_2