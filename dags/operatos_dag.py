from airflow.sdk import dag, task

@dag(
    dag_id="bash_dag",
)

def bash_dag():

    @task.python
    def first_task():
        print("This is my first task")
    
    @task.bash
    def bash_task():
        return "echo https://airflow.apache.org/"
    
    first_task >> bash_task
    
bash_dag()