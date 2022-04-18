import sys
import psycopg2
from src.data.populate_database import add_data_in_covid_states_table, add_data_in_brazil_covid_table
from src.data.create_tables import create_tables

#! Database connection parameters
_DB_NAME = "Covid_Daily_Update" # Database Name
_DB_USER = "airflow" # User name
_DB_PASS = "airflow" # User password
DB_HOST = "postgres" # Host of database
PORT = "5432" # Port

# Create connection and cursor with the database
connection = psycopg2.connect(dbname=_DB_NAME, user=_DB_USER, password=_DB_PASS, host=DB_HOST, port=PORT)
cursor = connection.cursor()


#! Execute functions
create_tables(cursor=cursor) # Create Tables

add_data_in_covid_states_table(cursor=cursor) # Populate "covid_states" table

add_data_in_brazil_covid_table(cursor=cursor) # Populate "covid_brazil" table


connection.commit() # Commit changes
cursor.close() # Close Cursor
connection.close()  # Close connection
