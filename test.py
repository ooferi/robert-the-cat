import pickle, os, csv, datetime, pandas, html
from google.cloud import bigquery
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import keras_core as keras
import tensorflow as tf
html = open("post_questions_extracted-000000000000.csv", "r", encoding="utf8")
soup = BeautifulSoup(html, "html.parser")
print(soup.text)










# SERVICE_ACCOUNT_JSON = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/sion/Downloads/meow-401216-dd1762818675.json"
# client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)
# bucket_name = 'bongus'
# project = 'bigquery-public-data'
# dataset_id = 'stackoverflow'
# table_id = 'posts_questions'

# destination_uri = "gs://{}/{}".format(bucket_name, "post_questions_extracted-*.csv")
# dataset_ref = bigquery.DatasetReference(project,dataset_id)
# table_ref = dataset_ref.table(table_id)
# extract_job = client.extract_table(
# 	table_ref,
# 	destination_uri, 
# 	location="US"
# )
# timestamp = datetime.datetime.now()
# print("{}: Exported {}:{}.{} to {}".format(timestamp, project, dataset_id,table_id, destination_uri))
# extract_job.result()

# pickle.load(open('stackdata.csv','r'))
   
