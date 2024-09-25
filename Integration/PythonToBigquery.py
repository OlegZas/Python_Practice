from google.cloud import bigquery 
from google.oauth2 import service_account # object that we created for credentials for the service account 
# importing bq module that we installed : 

# now the goal is to connect to the table we created in BQ

#1. step. path to json file which we downloaded which has the cridentials from service account  
key_path = '/home/ozamericos/mysqlpractice.json' # change the path to backslashes 


# creating a credentials object 

credentials = service_account.Credentials.from_service_account_file(key_path)   # part of service account module that we importing 

# connect to bq
client = bigquery.Client(credentials=credentials, project= 'mysqlpractice-436322')

query = "SELECT * FROM `mysqlpractice-436322.SamplePractice.Example1` "

res_set = client.query(query)

for row in res_set :
    print(row)
