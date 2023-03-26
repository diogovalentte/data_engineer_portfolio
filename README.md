# Data Engineer Portfolio

#### In this repository I store all my data engineering projects developed in my journey of data engineering.

# Projects:

### Stream of 10 crypto coins data to Elasticsearch and AWS S3 (_crypto_coins_stream_AWS_):
> An infrastructure created in the AWS Cloud using Terraform to stream data of 10 crypto coins to Elasticsearch (real time searching) AWS S3 (archiving).
> An AWS Lambda function extract the crypto data from the [mercado-bitcoin API](https://www.mercadobitcoin.net/api/), send to an AWS Kinesis Firehose Stream that delivery the data to Elasticsearch (hosted in AWS Opensearch) and an AWS S3 bucket.
> - **Stack**: Docker, Terraform, Python, and AWS Lambda, IAM, Kinesis Firehose, S3 and Elasticsearch.
---

### Daily data of the Covid-19 statistics in Brazil and in brazilian states (_covid_daily_update_):
> A PostgreSQL database (running in a Docker container) is populated with all Covid-19 statistics in Brazil and in brazilian states available from the [covid-api](http://covid-api.com/api/) API until now.
> And an Airflow DAG (running in a Docker container) is created to daily insert new data about Covid-19 in the database.
> - **Stack**: Docker, Airflow, PostgreSQL, Python, and Shell Script.
---

### Rock in Rio (2022) Twitter Scrapper (_rock_in_rio_twitter_scrapper_): DEPRECATED due to Twitter recent API changes.
> An application that get data tweets that contains the hashtag #RockinRio2022 (or others) on Twitter to put in Elasticsearch and MongoDB
> - **Stack**: Docker, Python, Elasticsearch, and MongoDB.
---

### Olist Data Warehouse:
> Create a Data Warehouse in the dimensional model (fact and dimensional tables) with data from the [Olist](https://olist.com) brazilian ecommerce to answer several questions requested by an imaginary CEO.
> - **Stack**: Docker. Python, PostgreSQL, Shell Script.
---

### Analysis of a dataset of a the fictional company **House Rocket** (_house_rocket_analysis_):
> In this project I made several analysis on a dataset of 21,000 homes avaiable to buy by the imaginary House Rocket company that work with purchase and resale of houses.
> I answer the following questions to the fictional CEO of House Rocket:
> 1. Which houses should House Rocket buy and by which price?
> 2. Once the houses are bought, for what price should they be sold?
> 3. What is the best time of the year to sell the houses?
> 4. The House Rocket should do renovate the houses to increase the selling price? What parts of the houses should the House Rocket renovate? What is the price increase given for each renovation option?
>
> Besides that I created a Web Dashboard witht he main insights, data samples, maps, and filters to use.
> - **Stack**: Python, Jupyter notebooks, and Shell Script.
---

