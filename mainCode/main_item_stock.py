# Author: Cesar Galan
# Date created: 9/5/2018
# Functions: main script to control all the excel sheet

#from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from google_sheet_class import Gsheet
import os, glob, sys

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets' #.readonly

# Add other folder to running path
'''
running_path = os.path.dirname(os.path.abspath(__file__))
temp = running_path.split("\\")
for i in xrange(1,3):
	temp.pop(len(temp)-1)
outsidepath = "\\".join(temp)
sys.path.append(outsidepath)

'''

# External files
from sheets_id import *

def main():
	# Access 
	lab_stock = Gsheet(MAINSPREADSHEET_ID)
	print lab_stock.get_values(range_name="Resistors!A1:C999")
	


	# Access excel sheet with return taken items
	# Acess the main excel sheet
	# find the item
	# Decrease or increase the item



if __name__ == '__main__':
	main()