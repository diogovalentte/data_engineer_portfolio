# This file contains the functions "" that create the dataware house, fact table, dimentional tables, etc.

def create_data_warehouse_schema(cursor):
    """
    Summary: Creates the Olist Data Warehouse Database Schema.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    _DW_DB_NAME = "olist_data_warehouse" # Data Warehouse Database Name

    cursor.execute("""CREATE SCHEMA IF NOT EXISTS {db_name}""".format(db_name=_DW_DB_NAME)) # Execute the SQL command that create the DW Schema


def create_data_warehouse_tables(cursor):
    """
    Summary: Creates the Olist Data Warehouse Database tables.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_customers (
                            customer_id VARCHAR(32) PRIMARY KEY,
                            customer_unique_id VARCHAR(32),
                            customer_zip_code_prefix VARCHAR(5) NOT NULL
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Orders_Fact (
                            order_id VARCHAR(32),
                            customer_id VARCHAR(32) REFERENCES olist_data_warehouse.Dim_customers (customer_id),
                            payment_value NUMERIC(12, 2) CHECK (payment_value >= 0) NOT NULL
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_payments (
                            order_id VARCHAR(32),
                            payment_installments VARCHAR(3) NOT NULL,
                            payment_type VARCHAR(20) NOT NULL
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_geolocation (
                            geolocation_zip_code_prefix VARCHAR(5),
                            geolocation_lat VARCHAR(30) NOT NULL,
                            geolocation_lng VARCHAR(30) NOT NULL,
                            geolocation_city VARCHAR(40) NOT NULL,
                            geolocation_state VARCHAR(2)
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_order_items (
                            order_id VARCHAR(32),
                            product_id VARCHAR(32) NOT NULL,
                            product_category_name VARCHAR(60),
                            order_item_id VARCHAR(2),
                            price NUMERIC(12, 2) CHECK (price > 0) NOT NULL,
                            freight_value NUMERIC(12, 2) CHECK (freight_value >= 0) NOT NULL,
                            PRIMARY KEY (order_id, order_item_id)
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_date (
                            order_id VARCHAR(32),
                            order_status VARCHAR(20) NOT NULL,
                            order_purchase_timestamp TIMESTAMP NOT NULL,
                            order_delivered_customer_date TIMESTAMP,
                            order_estimated_delivery_date TIMESTAMP        
    )""")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS olist_data_warehouse.Dim_review (
                            order_id VARCHAR(32),
                            order_review_score NUMERIC(2)
    )""")

