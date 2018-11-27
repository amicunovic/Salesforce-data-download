from salesforce_bulk import SalesforceBulk
import json
from salesforce_bulk.util import IteratorBytesIO
import unicodecsv
import pandas as pd
import time

list1 = []

bulk = SalesforceBulk(username='amicunovic@brandstate.com.au',password='Alisa200@',security_token='MoBunoVK8lsNqFVZ3CqHA0W5d')

'''
# THIS IS USED FO JSON
job = bulk.create_query_job("ChikPeaTOM__Install_Base__c", contentType='JSON')
batch = bulk.query(job, "select Id,Account_Name__c from ChikPeaTOM__Install_Base__c")
bulk.close_job(job)
while not bulk.is_batch_done(batch):
    time.sleep(10)


for result in bulk.get_all_results_for_query_batch(batch):
    result = json.load(IteratorBytesIO(result))
    print(result)
    #for row in result:
        #print(row)

'''
job = bulk.create_query_job("ChikPeaTOM__Install_Base__c", contentType='CSV')
batch = bulk.query(job, "select Id,Name, Service_ID__c, Account_Name__c from ChikPeaTOM__Install_Base__c")
bulk.close_job(job)
while not bulk.is_batch_done(batch):
    time.sleep(10)


for result in bulk.get_all_results_for_query_batch(batch):
    reader = unicodecsv.DictReader(result, encoding='utf-8')

    for row in reader:
    	dict1 = dict(row)
    	list1.append(dict1)
df = pd.DataFrame(list1)
df = df[['Id', 'Name', 'Service_ID__c', 'Account_Name__c', 'Id']]

report_name_excel = str(input('Please enter the report name '))
df.to_csv(report_name_excel+'.csv',index=False)

