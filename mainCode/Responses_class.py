from google_sheet_class import Gsheet
import pandas as pd
import numpy as np


class responsessheet():
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

def AbstractSheet(object):
	def __init__(self, sheet):
		'''
		'''
		pass
