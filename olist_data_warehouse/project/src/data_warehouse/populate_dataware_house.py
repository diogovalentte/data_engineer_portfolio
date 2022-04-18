# This file contains the function "populate_DW_tables" that populate the dataware house with data from the olist database "olist_database"

def insert_data_into_table(cursor, dw_table, olist_table_colunms, olist_db_table_name):
    cursor.execute("""INSERT INTO {dw_table}
                      SELECT {olist_table_colunms}
                      FROM {olist_db_table_name}
    """.format(
        dw_table=dw_table,
        olist_table_colunms=olist_table_colunms,
        olist_db_table_name=olist_db_table_name))

def populate_DW_tables(cursor):
    """
    Summary: It populaes the Olist Data Warehouse with data from Olist Database Schema

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    insert_data_into_table(cursor, 
                           'olist_data_warehouse.Dim_customers', 
                           'customer_id, customer_unique_id, customer_zip_code_prefix',
                           'customers')
    
    cursor.execute("""CREATE VIEW olist_data_warehouse.fact_stagging AS
                      SELECT s.order_id, s.customer_id, s.payment_value
                      FROM (SELECT o.order_id, o.customer_id, p.payment_value
                      FROM orders AS o
                      INNER JOIN order_payments AS p
                      ON o.order_id = p.order_id) AS s
    """)

    cursor.execute("""INSERT INTO olist_data_warehouse.orders_fact (order_id, customer_id, payment_value)
                      SELECT order_id, customer_id, payment_value
                      FROM olist_data_warehouse.fact_stagging
    """)

    insert_data_into_table(cursor, 
                           'olist_data_warehouse.Dim_payments',
                           'order_id, payment_installments, payment_type',
                           'order_payments')


    cursor.execute("""CREATE VIEW olist_data_warehouse.dim_stagging AS
                      SELECT o.order_id, o.product_id, p.product_category_name, o.order_item_id, o.price, o.freight_value
                      FROM order_items AS o
                      INNER JOIN products AS p
                      ON o.product_id = p.product_id
    """)

    cursor.execute("""INSERT INTO olist_data_warehouse.Dim_order_items
                      SELECT order_id, product_id, product_category_name, order_item_id, price, freight_value
                      FROM olist_data_warehouse.dim_stagging
    """)
    
    insert_data_into_table(cursor,
                           'olist_data_warehouse.Dim_geolocation',
                           'geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state',
                           'geolocation')

    insert_data_into_table(cursor, 
                           'olist_data_warehouse.Dim_date',
                           'order_id, order_status, order_purchase_timestamp, order_delivered_customer_date, order_estimated_delivery_date',
                           'orders')

    insert_data_into_table(cursor, 
                           'olist_data_warehouse.Dim_review',
                           'order_id, payment_installments',
                           'order_payments')

