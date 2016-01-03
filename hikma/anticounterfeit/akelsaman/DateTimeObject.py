import re
from datetime import datetime

class DateTimeObject:

	def __init__(self):
		pass

	def getDateTimeObject(self, dateTimeString):
		self.dateTimeString = dateTimeString

		dateTimeArray = re.split(r"[. :]", self.dateTimeString)
		year = int(dateTimeArray[0])
		month = int(dateTimeArray[1])
		day = int(dateTimeArray[2])
		hour = int(dateTimeArray[3])
		minute = int(dateTimeArray[4])

		return datetime(year, month, day, hour, minute)

