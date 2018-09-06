from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import os, glob, sys

# Add other folder to running path
#running_path = os.path.dirname(os.path.abspath(__file__))
#temp = running_path.split("\\")
#for i in xrange(1,3):
#	temp.pop(len(temp)-1)
#outsidepath = "\\".join(temp)
#sys.path.append(outsidepath)

from sheets_id import *

SCOPES = 'https://www.googleapis.com/auth/spreadsheets' #.readonly

class Gsheet():
	def __init__(self, ID):
		self.SHEET_ID = ID 
		store = file.Storage('token.json')
		creds = store.get()
		if not creds or creds.invalid:
			flow = client.flow_from_clientsecrets(JSON_CLIENT, SCOPES)
			creds = tools.run_flow(flow, store)
		
		self.service = build('sheets', 'v4', http=creds.authorize(Http()))

	def get_values(self, range_name="sheet1!A1:Z999"):
		result = self.service.spreadsheets().values().get(spreadsheetId=self.SHEET_ID,
													range=range_name).execute()

		values = result.get('values', [])
		return values


def main():
	mainsheet = Gsheet(MAINSPREADSHEET_ID)
	print mainsheet.get_values(range_name="Resistors!A1:C999")

if __name__ == '__main__':
	main()