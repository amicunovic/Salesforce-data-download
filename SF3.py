from salesforce_bulk import SalesforceBulk
import json
from salesforce_bulk.util import IteratorBytesIO
import unicodecsv
import pandas as pd
import time
import xlsxwriter

print("This program is used to download all IBs from the system \n\n\nOnce all the data is downloaded you have two options: \n\n1. Write to existing file (Note that this program and that file have to be in the same place) \n2. Create a new file")

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
batch = bulk.query(job, "select Id,Name, Service_ID__c, Account_Name__c, ChikPeaTOM__Status__c, ChikPeaTOM__Unit_MRC__c, Last_Billed_On__c, Plan_Name__c, Billing_Stop_Date__c from ChikPeaTOM__Install_Base__c")
bulk.close_job(job)
while not bulk.is_batch_done(batch):
    time.sleep(10)


for result in bulk.get_all_results_for_query_batch(batch):
    reader = unicodecsv.DictReader(result, encoding='utf-8')

    for row in reader:
    	dict1 = dict(row)
    	list1.append(dict1)
df = pd.DataFrame(list1)
df = df[['Id', 'Name', 'Service_ID__c', 'Account_Name__c', 'Id', 'ChikPeaTOM__Status__c', 'ChikPeaTOM__Unit_MRC__c', 'Last_Billed_On__c', 'Plan_Name__c', 'Billing_Stop_Date__c']]

answerme = input("\nPlease choose one of the options explained above, type only the number of the option ")



if answerme == '2':
	exfile = input("\nName the new file ")
	sheet_name = input("\nEnter the sheet name ")
	writer = pd.ExcelWriter(exfile+'.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name=sheet_name, index=False)
	workbook  = writer.book
	worksheet = writer.sheets[sheet_name]
	format1 = workbook.add_format({'num_format': '#,##0.00'})
	worksheet.set_column('G:G', None, format1)
	writer.save()


elif answerme == '1':
	exfile = input("\nName the existing file (It has to be in xlsx fromat) ")
	sheet_name = input("\nEnter the sheet name ")
	writer = pd.ExcelWriter(exfile+'.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name=sheet_name, index=False)
	workbook  = writer.book
	worksheet = writer.sheets[sheet_name]
	format1 = workbook.add_format({'num_format': '#,##0.00'})
	worksheet.set_column('G:G', None, format1)
	writer.save()