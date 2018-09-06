from google_sheet_class import Gsheet
from sheets_id import *
'''
every sheet needs to:
add/substract a count from an item
get the count of an item
show all the items
add an item
delete an item

'''

class Inventorysheet():
	def __init__(self, SHEET_ID):
		# start the connection with google sheets
		self.sheet = Gsheet(SHEET_ID)

		# create instance of each sheet
		self.resistors = Resistors(self.sheet)


class AbstractSheet(object):
	def __init__(self, sheet):
		self.sheet = sheet

	def add_to_count(self):
		pass

	def subs_to_count(self):
		pass

	def show_items(self):
		return self.sheet.get_values(range_name=self.item_ranges)

	def delete_item(self):
		pass

	def item_count(self, item):
		values = self.sheet.get_values(range_name=self.total_ranges)
		i = 0
		for x in values[0]:
			if "Quantity" in x:
				break
			i = i + 1

		for row in values:
			if item in row[0]:
				return row[i]

	def __count(self, item):
		pass


class Resistors(AbstractSheet):
	def __init__(self, sheet=None):
		#self.sheet = sheet
		super(Resistors, self).__init__(sheet)

		self.sheet_name = "Resistors!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"


		
def main():
	invt = Inventorysheet(MAINSPREADSHEET_ID)
	print invt.resistors.show_items()
	print invt.resistors.item_count("1")

if __name__ == '__main__':
	main()
