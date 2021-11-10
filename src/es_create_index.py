import requests
from requests.auth import HTTPBasicAuth



#connecting to ES
def create_index(es_host,login):

   try:
       
        r = requests.put(f"{es_host}project1/", auth = login, json = {"settings": {"number_of_shards": 1}, 
        "mappings": {
            "properties": {
                "plate": {"type":"keyword"},
                "state": {"type":"keyword"},
                "summons_number": {"type":"keyword"},
                "issue_date": {"type":"date"},
                "violation_time": {"type":"keyword"},
                "violation": {"type":"keyword"},
                "fine_amount": {"type":"integer"},
                "penalty_amount": {"type":"integer"},
                "interest_amount": {"type":"integer"},
                "reduction_amount": {"type":"integer"},
                "payment_amount": {"type":"integer"},
                "amount_due": {"type":"integer"},
                "precinct": {"type":"keyword"},
                "county": {"type":"keyword"},
                "issuing_agency": {"type":"keyword"},
                "violation_status": {"type":"keyword"},
                "summons_image": {"type":"nested"},
                "description" : {"type":"keyword"}}
                
                
            }
        })
        
        r.raise_for_status()
        print("Status Code:",r.status_code)
        print("JSON", r.json())
        
   except Exception:
        print('Skipping, index already exists.')
        
    

 
    
    
    
    