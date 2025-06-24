from airflow import DAG

from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email": ["mlops@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=3),
}

with DAG(
    dag_id="mlops_pipeline_demo",
    description="An example ML pipeline DAG for demo purposes",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["mlops", "demo"],
) as dag:

    fetch_data = BashOperator(
        task_id="fetch_data",
        bash_command="echo 'Fetching data from source...'; sleep 3"
    )

    preprocess_data = BashOperator(
        task_id="preprocess_data",
        bash_command="echo 'Cleaning and preprocessing data...'; sleep 4"
    )

    train_model = BashOperator(
        task_id="train_model",
        bash_command="echo 'Training ML model...'; sleep 5"
    )

    evaluate_model = BashOperator(
        task_id="evaluate_model",
        bash_command="echo 'Evaluating model accuracy...'; sleep 3"
    )

    deploy_model = BashOperator(
        task_id="deploy_model",
        bash_command="echo 'Deploying model to production...'; sleep 2"
    )

    # Set task dependencies
    fetch_data >> preprocess_data >> train_model >> evaluate_model >> deploy_model
