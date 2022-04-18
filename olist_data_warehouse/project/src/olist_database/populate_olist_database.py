# This file contains the function "populate_tables" that populate the olist database with data from the CSV files of the folder "data/olist_datasets"


def populate_olist_tables(cursor, files=list):
    """
    Summary: It populaes the Olist Database tables with Olist CSV data.

    * First, a loop is created that defines which table should copy the data from its file.
    * Secondly copy the data.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
      : files (Python List): List of CSV files with data
    """

    # Loop that copy data from CSV files to tables
    for file in files:
      
      # If the file name is not "product_category_name_translation.csv", it will cut the file name and turn the name of the table that will be added the data
      if file != "product_category_name_translation.csv":
          table = file[6:-12]

      # If the file name is "product_category_name_translation.csv", the table name is the file name without the extension ".csv"
      else:
          table = file[:-4]

      # Copy the data from the CSV file to the respective table
      cursor.execute("""
                        
                        COPY {table} FROM '/project/data/olist_datasets/{file}' USING DELIMITERS ',' CSV HEADER;

      """.format(table=table, file=file))

