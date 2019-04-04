from google_sheet_class import Gsheet
import pandas as pd
import numpy as np


class responsessheet():
	def __init__(self, SHEET_ID):
		# start the connection with google sheets
		self.sheet = Gsheet(SHEET_ID)

		# create instance of each sheet