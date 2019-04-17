# Author: Cesar Galan
# Date created: 9/5/2018
# Functions: main script to control all the excel sheet

#from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google_sheet_class import Gsheet
from lab_class import Inventorysheet#, MAINSPREADSHEET_ID
import pandas as pd
import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets' #.readonly

# External files
#from sheets_id import *
MAINSPREADSHEET_ID = '1pSunRFAVAG7vR3N1zd6jIbJcco_tn_KDaE7jA8uIUjI' 
RESPONSESSPREADSHEET_ID = '1VqtD8A9ouW31R_Bpwvt4pyhXv2HpsUMRM2fl5xjnSRs'

# waiting time
delay_time = 5 # minutes

def main():
	# infinite loop

	# Open Access to Inventory
	ig = Inventorysheet(MAINSPREADSHEET_ID)

	# Open Access to Response sheet
	lab_stock = Gsheet(RESPONSESSPREADSHEET_ID)

	# Read response sheet
	temp = lab_stock.get_values(range_name="Form responses 1!A1:D")
	
	# Get the last x minutes 
	values = False
	right_now = datetime.datetime.today()
	for idx, row in enumerate(temp[1:]):
		if datetime.datetime.strptime(row[0],"%m/%d/%Y %H:%M:%S") > right_now - datetime.timedelta(minutes=delay_time):
			check_hist = pd.DataFrame(data=temp[idx+1:],
										columns=temp[0])
			values = True

			break

	# Check if there has being a
	if values: 
		# Check if it is check out or check in and update the sheet
		#ig.sensor.item_checkout(IMU_id, 'Cesar')
		#ig.sensor.item_checkin(IMU_id)
		for row in check_hist.values:
			timestamp, status, SN, Name = row
			if "In" in status:
				print status, SN, Name
				ig.sensor.item_checkin(SN)
			elif "Out" in status:
				print status, SN, Name
				ig.sensor.item_checkout(SN, Name)
	

	# wait for 5 minutes to pass
	# repeat


if __name__ == '__main__':
	main()