#!/bin/bash
# This script set the environment within the container.

# Update pip
sudo docker exec covid_daily_update_airflow-webserver_1 /usr/local/bin/python3 -m pip install --upgrade pip

# Installs the required libraries in the container environment
sudo docker exec covid_daily_update_airflow-webserver_1 pip install -r /opt/airflow/project/requiriments.txt

# Unpause the "daily_update_covid_tables" Dag
sudo docker exec covid_daily_update_airflow-webserver_1 airflow dags unpause daily_update_covid_tables

