from parser import parse_this
from api import data_push, total_records
from es_create_index import create_index
import os
import sys
import requests
from requests.auth import HTTPBasicAuth
import datetime

DATASET_ID = os.environ["DATASET_ID"]
APP_TOKEN = os.environ["APP_TOKEN"]
ES_HOST = os.environ["ES_HOST"]
ES_USERNAME = os.environ["ES_USERNAME"]
ES_PASSWORD = os.environ["ES_PASSWORD"]

login = HTTPBasicAuth(ES_USERNAME,ES_PASSWORD)


if __name__ == '__main__':
    
    page_size,num_pages = parse_this(sys.argv)
    all_recs = total_records(APP_TOKEN,DATASET_ID)
    all_recs = all_recs[0]['COUNT']
    print('Total records in dataset:',all_recs)
    
    if num_pages != 0 :
        total = page_size*num_pages
        print('Total records requested:',total)
        
    else:
        total = int(all_recs)
        print('Total records requested:',total)
        
    
    try:
        r = create_index(ES_HOST,login)
        r.raise_for_status()
    except Exception:
        print('Index exists, skippping!')
            
    
        
    count = 1
    while count <= total:
        try:
            
            y = data_push(APP_TOKEN,DATASET_ID,1,count)
            data = y[0]
            data['issue_date'] = datetime.datetime.strptime(data['issue_date'],'%m/%d/%Y').strftime("%Y-%m-%d")
            r = requests.post(f"{ES_HOST}project1/_doc/", auth = login, json = data)
            print(r.json())
            count+=1
            r.raise_for_status()
         
                
        except Exception as e:
            print(f"Failed to insert in ES: {e}, skipping row: {data}")
            continue
        
        
       
        
   
    
 
    
    
   
    