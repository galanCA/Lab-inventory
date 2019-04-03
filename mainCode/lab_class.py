from google_sheet_class import Gsheet
import pandas as pd
import numpy as np


#from sheets_id import *
'''
every sheet needs to:
add/substract a count from an item
get the count of an item
show all the items
add/append an item
delete an item
'''

class Inventorysheet():
	def __init__(self, SHEET_ID):
		# start the connection with google sheets
		self.sheet = Gsheet(SHEET_ID)

		# create instance of each sheet
		self.resistors = Resistors(self.sheet)
		self.bits = Bits(self.sheet)
		self.electronics = Electronics(self.sheet)
		self.mechanical = Mechanical(self.sheet)
		self.sensor = Sensor(self.sheet)
		self.capacitors = Capacitors(self.sheet)
		self.tools = Tools(self.sheet)
		self.other = Other(self.sheet)

class AbstractSheet(object):
	def __init__(self, sheet):
		'''
		'''
		self.sheet = sheet

	def item_checkout(self, sn_id, person):
		'''
		'''
		SN_column = "Part Number"
		raw = self.sheet.get_values(range_name=self.total_ranges)
		data = pd.DataFrame(data=raw[1:],
							columns=raw[0])
		#print data["Part Number"]
		for i, sn in enumerate(data[SN_column]):
			try:
				if sn_id in sn:
					break
			except TypeError:
				continue

		#print "Hey", data[SN_column][i], sn_id
		for j, C in enumerate(data.columns):
			if "Check" in C:
				break

		start_cell = self.total_ranges.split("!")[1].split(":")[0]
		checkout_cell =  self.__addletters(start_cell[0],j)+str(int(start_cell[1])+i+1)
		#print checkout_cell
		self.sheet.mod_cell(range_name=self.sheet_name+checkout_cell, value=person)

		return [self.sheet_name+checkout_cell, person]

	def item_checkin(self, sn_id):
		'''
		'''
		SN_column = "Part Number"
		checkin_name = "In storage"
		raw = self.sheet.get_values(range_name=self.total_ranges)
		data = pd.DataFrame(data=raw[1:],
							columns=raw[0])

		for i, sn in enumerate(data[SN_column]):
			try:
				if sn_id in sn:
					break
			except TypeError:
				continue


		for j, C in enumerate(data.columns):
			if "Check" in C:
				break

		start_cell = self.total_ranges.split("!")[1].split(":")[0]
		checkin_cell =  self.__addletters(start_cell[0],j)+str(int(start_cell[1])+i+1)
		#print checkin_cell
		self.sheet.mod_cell(range_name=self.sheet_name+checkin_cell, value=checkin_name)

		return [self.sheet_name+checkin_cell, checkin_name]


	def append_item(self, item):
		'''
		'''
		return self.sheet.append(self.sheet_name+"A1:A", item)

	def add_to_count(self, item, value=None):
		'''
		'''
		self.__count_modifier(item, abs(value))

	def subs_to_count(self, item, value=None):
		'''
		'''
		self.__count_modifier(item, -abs(value))

	def show_items(self):
		'''
		'''
		return self.sheet.get_values(range_name=self.item_ranges)

	def delete_item(self):
		'''
		'''
		[current_count, row] = self.item_count(item)
		self.sheet.mod_cell(range_name=row, value="")

	def item_count(self, item):
		'''
		'''
		values = self.sheet.get_values(range_name=self.total_ranges)
		i = 0
		for x in values[0]:
			if "Quantity" in x:
				break
			i = i + 1

		iterable_values = Iterable_object(values)

		for row in iterable_values:
			if item in row[0]:
				try: 
					return [row[i], iterable_values.get_index()+1, i]
				except IndexError:
					return [None, iterable_values.get_index()+1, i]

	def __count_modifier(self, item, difference=0):
		'''
		'''
		try:
			current_count, row, column = self.item_count(item)
			cell = self.sheet_name+self.__int2abc(column)+str(row)

		except TypeError:
			# create the item
			msg = self.append_item(item)
			current_count = 0
			cell_temp = msg['updates']['updatedRange']
			temp = cell_temp.split("!")
			dummy = self.__int2abc(self.__abc2int(temp[1][0])+1) + temp[1][1]
			cell = "!".join([temp[0], dummy])

			

		if not current_count:
			current_count = 0

		update_count = int(current_count) + difference
		
		self.sheet.mod_cell(range_name=cell, value=str(update_count))

	def __int2abc(self, value):
		'''
		TODO work on double letter
		'''

		if value >= 0 and value <= 25:
			return chr(65+value)

	def __abc2int(self, string):
		'''
		'''
		return ord(string)-65

	def __addletters(self, c,x):
		return chr(ord(c)+x)

########################## Sheet classes #############
class Resistors(AbstractSheet):
	def __init__(self, sheet=None):
		#self.sheet = sheet
		super(Resistors, self).__init__(sheet)

		self.sheet_name = "Resistors!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Bits(AbstractSheet):
	def __init__(self, sheet=None):
		super(Bits, self).__init__(sheet)

		self.sheet_name = "Bits!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Electronics(AbstractSheet):
	def __init__(self, sheet=None):
		super(Electronics, self).__init__(sheet)

		self.sheet_name = "Electronics!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Mechanical(AbstractSheet):
	def __init__(self, sheet=None):
		super(Mechanical, self).__init__(sheet)

		self.sheet_name = "Mechanical!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Sensor(AbstractSheet):
	def __init__(self, sheet=None):
		super(Sensor, self).__init__(sheet)

		self.sheet_name = "Sensors!"
		self.item_ranges = self.sheet_name + "C3:C"
		self.total_ranges = self.sheet_name + "A2:E"

class Capacitors(AbstractSheet):
	def __init__(self, sheet=None):
		super(Capacitors, self).__init__(sheet)

		self.sheet_name = "Capacitors!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Tools(AbstractSheet):
	def __init__(self, sheet=None):
		super(Tools, self).__init__(sheet)

		self.sheet_name = "Tools!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

class Other(AbstractSheet):
	def __init__(self, sheet=None):
		super(Other, self).__init__(sheet)

		self.sheet_name = "Other!"
		self.item_ranges = self.sheet_name + "A3:A"
		self.total_ranges = self.sheet_name + "A2:C"

############################ Other classes ###############

class Iterable_object(object):
	def __init__(self, values):
		'''
		Iterable_file: allows to create an iterable object that could look ahead 
			without the need to go to the next iteration

		Input:
			list or iterable object

		Output:
			iterable_file obejct
		'''
		self.values = values
		self.location = 0
		self.step = 0

	def __iter__(self):
		'''
		iterates:

		Input:
			
		Output:
		'''
		return self

	def next(self):
		'''
		move to the next place:

		Input:
			
		Output:
		'''
		if self.location == len(self.values):
			raise StopIteration

		value = self.values[self.location]
		self.location += 1 
		self.step = 0
		return value

	def look_ahead(self):
		'''
		look_ahead: move to the next value without the 
					need to move to the next iteration

		Input:

			
		Output:
		'''
		if self.location + self.step == len(self.values):
			raise StopIteration

		
		value = self.values[self.location + self.step]
		self.step += 1 
		return value

	def get_index(self):
		'''
		'''
		return self.location

def main():
	invt = Inventorysheet(MAINSPREADSHEET_ID)
	#print invt.resistors.show_items()
	#print invt.resistors.item_count("1")
	invt.bits.add_to_count("5/16", 1)

if __name__ == '__main__':
	main()
