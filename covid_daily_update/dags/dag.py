import sys
import psycopg2
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow import DAG

# Add src to library path
sys.path.append("/opt/airflow/project/src")
from data.update_data import update_data_covid_brazil, update_data_covid_states
from data.create_tables import create_tables


#! Database connection parameters
_DB_NAME = "Covid_Daily_Update" # Database Name
_DB_USER = "airflow" # User name
_DB_PASS = "airflow" # User password
DB_HOST = "postgres" # Host of database
PORT = "5432" # Port

# Create connection and cursor with the database
connection = psycopg2.connect(dbname=_DB_NAME, user=_DB_USER, password=_DB_PASS, host=DB_HOST, port=PORT)
cursor = connection.cursor()



#! Function that commit changes and close connection
def commit_and_close_connection(connection, cursor):
    connection.commit() # Commit changes
    cursor.close() # Close Cursor
    connection.close()  # Close connection
    
    return None 
    
    
with DAG(dag_id="daily_update_covid_tables",
         start_date=datetime(2021, 9, 8),
         schedule_interval="1 13 * * *",
         ) as dag:

    # Task that performs the function that creates tables if they do not exist
    create_tables = PythonOperator(
        task_id="create_tables",
        python_callable=create_tables,
        op_kwargs={'cursor': cursor}
    )

    # Task that performs the function that updates the daily data of the "covid_states" table
    update_states_table = PythonOperator(
        task_id="update_states_table",
        python_callable=update_data_covid_states,
        op_kwargs={'cursor': cursor}
    )

    # Task that performs the function that updates the daily data of the "covid_brazil" table
    update_brazil_table = PythonOperator(
        task_id="update_brazil_table",
        python_callable=update_data_covid_brazil,
        op_kwargs={'cursor': cursor}
    )
    
    # Task that commit changes and close cursor and connection with the Database
    commit_and_close_connection = PythonOperator(
    	task_id="commit_and_close_connection",
    	python_callable=commit_and_close_connection,
    	op_kwargs={'connection': connection, 'cursor': cursor}
    )

    # Organizes the dependency
    create_tables >> [update_states_table, update_brazil_table] >> commit_and_close_connection
