from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Other files
from sheets_id import *

SCOPES = 'https://www.googleapis.com/auth/spreadsheets' #.readonly

class Gsheet():
	def __init__(self, ID):
		self.SHEET_ID = ID 
		store = file.Storage(TOKEN)
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

	def mod_cell(self, range_name=None, value='' ):

		
		body = {
			"values":[
			[value]
			]
		}
		self.service.spreadsheets().values().update(
			spreadsheetId=self.SHEET_ID,
			range=range_name,
			valueInputOption="RAW",
			body=body
			).execute()

def main():
	mainsheet = Gsheet(MAINSPREADSHEET_ID)
	print mainsheet.get_values(range_name="Resistors!A1:C999")
	mainsheet.mod_cell(range_name="Bits!A2", value='It works') 

if __name__ == '__main__':
	main()