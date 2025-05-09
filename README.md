# Data Engineer Portfolio

Personal projects that I created for learning purposes.

# Projects:

### Airflow pipeline to process data in an EMR cluster using PySpark and load it into a Redshift table (_nyc_taxi_data_warehouse_):

> An infrastructure create in AWS Cloud using Terraform to process data using an Airflow pipeline and load it into a Redshift table.
>
> - **Stack**: Terraform, Spark (PySpark), Python, AWS S3, EMR, Redhisft, AWS Managed Airflow, VPC, IAM.

---

### Data lake IoT device data stream pipeline (_iot_device_data_):

> An infrastructure created in the AWS Cloud using Terraform to stream IoT device data using an AWS Firehouse stream to a data lake in S3, then validate, transform, and catalog the data.
>
> - **Stack**: Terraform, Spark (PySpark), Delta Lake, Python, AWS S3, Lambda, Firehose, Lake Formation, Glue Catalog and ETL, VPC, IAM.

### Stream of 10 crypto coins data to Elasticsearch and AWS S3 (_crypto_coins_stream_AWS_):

> An infrastructure created in the AWS Cloud using Terraform to stream data of 10 crypto coins to Opensearch (real time searching) and AWS S3 (archiving).
> An AWS Lambda function extracts the crypto data from the [mercado-bitcoin API](https://www.mercadobitcoin.net/api/), send it to an AWS Kinesis Firehose Stream which delivers the data to Opensearch (hosted in AWS) and an AWS S3 bucket.
>
> - **Stack**: Docker, Terraform, Python, AWS Lambda, VPC, IAM, Kinesis Firehose, S3, and Opensearch.

---

### Daily data of the Covid-19 statistics in Brazil and in brazilian states (_covid_daily_update_):

> A PostgreSQL database (running in a Docker container) is populated with all Covid-19 statistics in Brazil and in brazilian states available from the [covid-api](http://covid-api.com/api/) API until now.
> And an Airflow DAG (running in a Docker container) is created to daily insert new data about Covid-19 in the database.
>
> - **Stack**: Docker, Airflow, PostgreSQL, Python, and Shell Script.

---

### Olist Data Warehouse:

> Creates a Data Warehouse based on the dimensional model (fact and dimensional tables) with data from the [Olist](https://olist.com) brazilian ecommerce to answer several questions requested by an fictional CEO.
>
> - **Stack**: Docker. Python, PostgreSQL, Shell Script.

---

### Analysis of a dataset of a the fictional company **House Rocket** (_house_rocket_analysis_):

> Several analysis on a dataset of 21,000 homes avaiable to buy by the House Rocket company that works with purchase and resale of houses.
> I answer the following questions to the fictional CEO of House Rocket:
>
> 1. Which houses should House Rocket buy and by which price?
> 2. Once the houses are bought, for what price should they be sold?
> 3. What is the best time of the year to sell the houses?
> 4. The House Rocket should do renovate the houses to increase the selling price? What parts of the houses should the House Rocket renovate? What is the price increase given for each renovation option?
>
> Besides that I created a Web Dashboard with the main insights, data samples, maps, and filters to use.
>
> - **Stack**: Python, Jupyter notebooks, and Shell Script.

---

### Rock in Rio (2022) Twitter Scrapper (_rock_in_rio_twitter_scrapper_): DEPRECATED due to Twitter recent API changes.

> An application that get data tweets that contains the hashtag #RockinRio2022 (or others) on Twitter to put in Elasticsearch and MongoDB.
>
> - **Stack**: Docker, Python, Elasticsearch, and MongoDB.

---
