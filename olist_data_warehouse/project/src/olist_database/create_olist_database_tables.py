# This file contains the function "create_tables" that create the olist database, it tables, relations, etc.

def create_olist_database_tables(cursor):
    """
    Summary: Creates the Olist Database tables if them do not exist.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    #! Creates the Olist Database tables if they do not exist.


    cursor.execute("""CREATE TABLE IF NOT EXISTS geolocation (
                            geolocation_zip_code_prefix CHAR(5),
                            geolocation_lat VARCHAR(30) NOT NULL,
                            geolocation_lng VARCHAR(30) NOT NULL,
                            geolocation_city VARCHAR(40) NOT NULL,
                            geolocation_state VARCHAR(2) NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                            customer_id CHAR(32) PRIMARY KEY,
                            customer_unique_id CHAR(32),
                            customer_zip_code_prefix CHAR(5) NOT NULL,
                            customer_city VARCHAR(40) NOT NULL,
                            customer_state VARCHAR(2) NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS products (
                            product_id CHAR(32) PRIMARY KEY,
                            product_category_name VARCHAR(60),
                            product_name_lenght NUMERIC(3),
                            product_description_lenght NUMERIC(5),
                            product_photos_qty NUMERIC(2),
                            product_weight_g NUMERIC(6),
                            product_length_cm NUMERIC(6),
                            product_height_cm NUMERIC(6),
                            product_width_cm NUMERIC(6)
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                            order_id CHAR(32) PRIMARY KEY,
                            customer_id CHAR(32) NOT NULL REFERENCES customers (customer_id),
                            order_status VARCHAR(20) NOT NULL,
                            order_purchase_timestamp TIMESTAMP NOT NULL,
                            order_approved_at TIMESTAMP,
                            order_delivered_carrier_date TIMESTAMP,
                            order_delivered_customer_date TIMESTAMP,
                            order_estimated_delivery_date TIMESTAMP
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS sellers(
                            seller_id CHAR(32) PRIMARY KEY,
                            seller_zip_code_prefix CHAR(5) NOT NULL,
                            seller_city VARCHAR(40) NOT NULL,
                            seller_state VARCHAR(2) NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS order_items (
                            order_id CHAR(32) NOT NULL,
                            order_item_id SMALLINT NOT NULL,
                            product_id CHAR(32) NOT NULL,
                            seller_id CHAR(32) NOT NULL REFERENCES sellers (seller_id),
                            shipping_limit_date TIMESTAMP,
                            price NUMERIC(12, 2) NOT NULL,
                            freight_value NUMERIC(12, 2),
                            PRIMARY KEY (order_id, order_item_id)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS order_payments (
                            order_id CHAR(32) REFERENCES orders (order_id),
                            payment_sequential NUMERIC(3) NOT NULL,
                            payment_type VARCHAR(20) NOT NULL,
                            payment_installments NUMERIC(3) NOT NULL,
                            payment_value NUMERIC(12, 2) NOT NULL,
                            PRIMARY KEY (order_id, payment_sequential)
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS order_reviews (
                            review_id CHAR(32),
                            order_id CHAR(32) NOT NULL,
                            review_score NUMERIC(1) NOT NULL,
                            review_comment_title TEXT,
                            review_comment_message TEXT,
                            review_creation_date TIMESTAMP NOT NULL,
                            review_answer_timestamp TIMESTAMP,
                            PRIMARY KEY (review_id, order_id)
    )""")
    

    cursor.execute("""CREATE TABLE IF NOT EXISTS product_category_name_translation(
                            product_category_name VARCHAR(60) NOT NULL,
                            product_category_name_english VARCHAR(60)
    )""")    

    return None

