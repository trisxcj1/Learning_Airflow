# Learning_Airflow
Learning how to orchestrate ETL pipelines using Airflow

## Installation
```
pip install apache-airflow
```
## DAG dir
```
Ensure that the docker-compose dag dir is pointing to the appropriate dag dir within code

For example
- my dag dir is: `./dags`
- therefore, volumes in docker-compose should point to: `- ./dags:/usr/local/airflow/dags`
```

## Running bash and python scripts
```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# -- DAG
dag = DAG(
    'dagID',
    default_args=default_args,
    description='Some DAG description',
    schedule_interval=timedelta(days=1)
)

# -- Tasks
bash_task = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

def python_func(my_input):
    
    # should print in console
    print(str(my_input))

    # should print in Airflow logs
    return str(my_input)

python_task = PythonOperator(
    task_id='python_script',
    python_callable=python_func,
    op_kwargs={'my_input': 'Hey, man! Wudditdooo?'},
    dag=dag
)

# -- Dependencies/Task orchestration
bash_task >> python_task
```