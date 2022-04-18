# The "create_tables" function creates two tables if they do not exist.


def create_tables(cursor):
    """
    Summary: Creates the "covid_states" and "covid_brazil" tables if them do not exist.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    #! Creates the "covid_states" and "covid_brazil" tables if they do not exist.
    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_states (
                            state VARCHAR(100),
                            date DATE,
                            confirmed_accumulated INTEGER,
                            confirmated_difference INTEGER,
                            deaths_accumulated INTEGER,
                            deaths_difference INTEGER,
                            last_update TIMESTAMP)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_brazil (
                            date DATE,
                            confirmed_accumulated INTEGER,
                            confirmated_difference INTEGER,
                            deaths_accumulated INTEGER,
                            deaths_difference INTEGER,
                            last_update TIMESTAMP)
        """)

    return None
