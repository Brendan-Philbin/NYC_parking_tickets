import requests
from sodapy import Socrata




def data_push(app_tok,data,size,off_set):

    
    client = Socrata('data.cityofnewyork.us',app_tok)
    x =  client.get(data,limit = size, offset = off_set)
    return x
    
    
def total_records(app_tok,data):
    
    client = Socrata('data.cityofnewyork.us',app_tok,timeout=60)
    y = client.get(data, select = 'COUNT(*)')
    return y 