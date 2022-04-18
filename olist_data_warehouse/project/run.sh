#!/bin/bash

# Update repositories
apt-get update

# Install python 3.8.10
apt-get install python3 -y

python3 --version

# Install pip
apt-get install python3-pip -y

# Install the necessary python libraries
pip install -r /project/requiriments.txt

# Execute the main script that:
# * Create the Olist Database, it's tables, relations and populate it's with data from the Olist CSV files
# * Create the Data Warehouse Schema, the Fact table, dimentional tables, relations and copy data from the Olist Database
python3 /project/run.py
