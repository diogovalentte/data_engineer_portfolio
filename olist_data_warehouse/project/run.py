# This script run the functions that:
# * Create the Olist Database, it's tables, relations and populate it's with data from the Olist CSV files
# * Create the Data Warehouse, the Fact table, dimentional tables, relations and copy data from the Olist Database

import psycopg2
import os
from src.olist_database.create_olist_database_tables import create_olist_database_tables
from src.olist_database.populate_olist_database import populate_olist_tables
from src.data_warehouse.create_data_warehouse import create_data_warehouse_schema, create_data_warehouse_tables
from src.data_warehouse.populate_dataware_house import populate_DW_tables


if __name__ == "__main__":

    #! Database connection parameters
    _DB_NAME = "olist_database" # Olist Database Name
    _DB_USER = "username" # User name
    _DB_PASS = "password" # User password   
    _DB_HOST = "localhost" # Cluster Host
    PORT = "5432" # Cluster port

    #! Connect with olist database and create cursor
    # Conection and cursor with the Olist Database
    _connection = psycopg2.connect(dbname=_DB_NAME, user=_DB_USER, password=_DB_PASS, host=_DB_HOST, port=PORT)
    _cursor = _connection.cursor()


    #! TODO: Create the Olist Database tables and copy data from the CSV files to it
    files = os.listdir("/project/data/olist_datasets/") # Obtain the list os CSV files

    create_olist_database_tables(cursor=_cursor) # Create Olist Database Tables
    populate_olist_tables(cursor=_cursor, files=files) # Copy data from CSV files to tables

    #! TODO: Create the Data Warehouse Schema, it's tables and populate it with data from the Olist Database
    create_data_warehouse_schema(cursor=_cursor) # Create DataWarehouse Database
    create_data_warehouse_tables(cursor=_cursor)
    populate_DW_tables(cursor=_cursor)

    # Commit changes and close conection and cursor with the Olist Database
    _connection.commit()
    _cursor.close()
    _connection.close()

    