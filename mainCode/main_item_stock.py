# Author: Cesar Galan
# Date created: 9/5/2018
# Functions: main script to control all the excel sheet

#from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google_sheet_class import Gsheet
from lab_class import Inventorysheet#, MAINSPREADSHEET_ID

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets' #.readonly

# External files
#from sheets_id import *
MAINSPREADSHEET_ID = '1pSunRFAVAG7vR3N1zd6jIbJcco_tn_KDaE7jA8uIUjI' 
RESPONSESSPREADSHEET_ID = '1VqtD8A9ouW31R_Bpwvt4pyhXv2HpsUMRM2fl5xjnSRs'

def main():
	IMU_id = '4220.75832'
	# Access 
	ig = Inventorysheet(MAINSPREADSHEET_ID)
	#ig.sensor.item_checkout(IMU_id, 'Cesar')
	ig.sensor.item_checkin(IMU_id)


	#lab_stock = Gsheet(MAINSPREADSHEET_ID)
	#print lab_stock.get_values(range_name="Sensors!A1:E")

	# Access excel sheet with return taken items
	# Acess the main excel sheet
	# find the item
	# Decrease or increase the item



if __name__ == '__main__':
	main()