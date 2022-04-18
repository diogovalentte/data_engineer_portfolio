# The "add_data_in_covid_states_table" function adds data to the "covid_states" table. It makes API requests
# with Covid data from each Brazilian state for each day to the yesterday's date and adds it to the table.

# The "add_data_in_brazil_covid_table" function adds data to the "covid_brazil" table. It makes API requests
# with Covid data in Brazil for each day until the yesterday's date and adds them to the table.

def add_data_in_covid_states_table(cursor):
    """
    Summary: It populaes the "covid_states" table with daily Covid data from each Brazilian state.

    * It first sets the API base URL and creates a list of dates, starting from the date "2020-05-20" to the yesterday's date.
    * Third creates a loop that makes a request in the API for each date in the date list and adds the data returned from JSON response to the "covid_states" table of the data collection.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    import os
    import requests
    import pandas as pd
    from datetime import datetime, timedelta

    #! Define API URL and parameters
    API_URL = "http://covid-api.com/api/reports"  # Base Api Url

    # Creates a list of dates from "2020-05-20" to the yesterday's date
    # Obs: First date with COVID data from the Brazilian states is "2020-05-20"
    date_list = pd.date_range(
        start="2020-05-20", end=(datetime.today() - timedelta(days=1))).tolist()

    #! Loop that add data in the table "covid_states" in database
    # First Loop: Makes a request in the API for a date within the "date_list" list and returns a JSON with information about all states from that date
    for d in date_list:

        #! Define API parameters and make the request
        # Converts the date of the "date_list" list to a format that can be used in the API query ("YYYY-mm-dd")
        date = str(d)[:10]

        # Shows which date the loop is adding data
        os.system(f'echo "Adding data from date {date} to covid_states table"')

        query = {"date": date, "q": "Brazil",
                 "region_name": "Brazil", "iso": "BRA"}

        json = requests.request("GET", API_URL, params=query).json()["data"]

        # Second Loop: Adds within the "covid_states" table the Covid data of each given date state from the json response
        for i in range(0, 27):
            # Define which data of which line
            state = json[i]["region"]["province"]
            confirmated = json[i]["confirmed"]
            deaths = json[i]["deaths"]
            last_update = json[i]["last_update"]
            confirmated_difference = json[i]["confirmed_diff"]
            deaths_difference = json[i]["deaths_diff"]

            #! Add the Covid data of the state
            cursor.execute(
                f"INSERT INTO covid_states VALUES ('{state}', '{date}', {confirmated}, {confirmated_difference}, {deaths}, {deaths_difference}, '{last_update}')")

    os.system(f'echo -e "\nSucefully add data in covid_states table\n"')
    
    return None


def add_data_in_brazil_covid_table(cursor):
    """
    Summary: It populaes the "covid_brazil" table with daily Covid data from Brazil

    * It first sets the API base URL and creates a list of dates, starting from the date "2020-05-20" to the yesterday's date.
    * Third creates a loop that makes a request in the API for each date in the date list and adds the data returned to the "covid_brazil" table of the data collection.

    Args:
      : cursor (DataBase cursor): Cursor of the connection with the database
    """

    import os
    import requests
    import pandas as pd
    from datetime import datetime, timedelta

    #! Define API URL and parameters
    API_URL = "http://covid-api.com/api/reports/total"  # Base Api Url

    # Creates a list of dates from "2020-02-26" to the yesterday's date
    # Obs: First date with COVID data from Brazil is "2020-02-26"
    date_list = pd.date_range(
        start="2020-02-26", end=(datetime.today() - timedelta(days=1))).tolist()

    #! Loop that makes a request in the API for a date within the "date_list" list and returns a JSON with information about Covid in Brazil of that date
    for d in date_list:

        # Converts the date of the "date_list" list to a format that can be used in the API query ("YYYY-mm-dd")
        date = str(d)[:10]

        # Shows which date the loop is adding data
        os.system(f'echo "Adding data from date {date} to covid_brazil table"')

        query = {"date": date, "q": "Brazil",
                 "region_name": "Brazil", "iso": "BRA"}

        # Make the request
        json = requests.request("GET", API_URL, params=query).json()["data"]

        #! Define which data of which line
        confirmated = json["confirmed"]
        deaths = json["deaths"]
        last_update = json["last_update"]
        confirmated_difference = json["confirmed_diff"]
        deaths_difference = json["deaths_diff"]

        #! Add the Covid data of the date
        cursor.execute(
            f"INSERT INTO covid_brazil VALUES ('{date}', {confirmated}, {confirmated_difference}, {deaths}, {deaths_difference}, '{last_update}')")
    
    os.system(f'echo "Data entered in the covid_brazil successfully entered."')
    
    return None
    
