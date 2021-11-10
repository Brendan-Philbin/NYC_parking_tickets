Brendan Philbin
CIS9760 - Project 1

I. Introduction

	For this project, I was tasked with analyzing a large volume of NYC parking ticket data. In order to accomplish this, I launched an
	EC2 instance to run python scripts and ingested this data via Elasticsearch. Once ingested in Elasticsearch, 
	I used Kibana to create a dashboard that provides an analysis of the data. Inside of this zip folder, you will find all 
	of the source code to create a docker image inside EC2, and run the program for yourself.

II. Requirements

	In order to run this code successfully, there are several preliminary steps to complete first. From a scripting perspective,
	you will need to install several python modules to run the code. This has been provided for you in the requirements.txt file.
	Additionally, you will need several tokens, usernames, and passwords to run the data. Below is the full list needed:
	
	- NYC Open Data App Token (link to set up account: data.cityofnewyork.us)
	- NYC Open Dataset ID - for this project, the ID is "nc67-uf89"
	- Elasticsearch host address (provided once an ES domain is created on AWS)
	- Elasticsearch username
	- Elasticsearch password
	
	All of these tokens must be provided as enviornment variables when running inside your docker container.
	The appropriate command line input will be provided below.

III. Python Code Background

	When running inside your docker container, you will have the ability to choose your page size and number of pages
	for data ingestion. This will allow you to set the total number of records requested for this project.
	Selecting a page size is required, but the number of pages is not. 
	
	Please note: If the number of pages is not provided, the code will ingest the entire dataset (Approximately 57 million records).
	
	The python code can be broken down into 4 main elements:
	
	1. Using argparse to read page size and number of pages requested
	2. Using the Socrata API to connect to the NYC dataset
	3. A callable function to create an index inside Elasticsearch
	4. A callable funciton to "push" or ingest data from the API into Elasticsearch
	
	Try/Except statements are included in the code to avoid a total script stoppage during the data upload process in Elascticsearch.

IV. Command Line Inputs

	Once your EC2 and Elasticsearch instances are running, please run the following lines in EC2:
	
	1. Building Docker container: "docker build -t bigdata1:1.0 ."
	
	2. Running the script and ingesting data:
	
		docker run \
		 -v ${PWD}:/app \
		 --network="host" \
		 -e DATASET_ID="your-dataset-id" \
		 -e APP_TOKEN="your-app-token" \
		 -e ES_HOST="https://your-es-host" \
		 -e ES_USERNAME="your-es-username" \
		 -e ES_PASSWORD="your-es-password" \
		 bigdata1:1.0 --page_size=[user input] --num_pages[user input]


V. Contact Me!

	For any questions regarding the code, or any errors found, please reach out to me at:
	
	bphilbin70@gmail.com





