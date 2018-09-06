from google_sheet_class import Gsheet

'''
every sheet needs to:
add/substract a count from an item
get the count of an item
show all the items
add an item
delete an item

'''



class AbstractSheet(object):
	def __init__(self, SHEET_ID):
		self.sheet = Gsheet(SHEET_ID)

	def add_to_count(self):
		pass

	def subs_to_count(self):
		pass

	def show_items(self):
		pass

	def __count(self):
		pass


class Electronics(AbstractSheet):
	def __init__(self, sheet_id=None):
		super(Electronics,self).__init__(sheet_id)

def main():
	sheet = Electronics(MAINSPREADSHEET_ID)

if __name__ == '__main__':
	main()
