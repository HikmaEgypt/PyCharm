from datetime import datetime
import time
import random,re
################################################################################
class UniqueRandomNumber:
	divisor = 36
	encodingSymbols = { "0":"0","1":"1","2":"2","3":"3","4":"4",
						"5":"5","6":"6","7":"7","8":"8","9":"9",
						"10":"A","11":"B","12":"C","13":"D","14":"E",
						"15":"F","16":"G","17":"H","18":"I","19":"J",
						"20":"K","21":"L","22":"M","23":"N","24":"O",
						"25":"P","26":"Q","27":"R","28":"S","29":"T",
						"30":"U","31":"V","32":"W","33":"X","34":"Y","35":"Z"}
	decodingSymbols = { "0":"0","1":"1","2":"2","3":"3","4":"4",
						"5":"5","6":"6","7":"7","8":"8","9":"9",
						"A":"10","B":"11","C":"12","D":"13","E":"14",
						"F":"15","G":"16","H":"17","I":"18","J":"19",
						"K":"20","L":"21","M":"22","N":"23","O":"24",
						"P":"25","Q":"26","R":"27","S":"28","T":"29",
						"U":"30","V":"31","W":"32","X":"33","Y":"34","Z":"35"}

		# n = 40 # n = n / 36 <=> n /= 36
		# n = 40 # n = n // 36 <=> n //= 36
		# n = 40 # n = n % 36 <=> n %= 36
		# n = 40 # n = n // 36 <=> n = int(n / 36)
		# n = 40 # n = divmod(n,36) => print(n[0] + "\n" + "n[1]")

	def __init__(self, lowerLimit=100000001, upperLimit=199999999, countOfUniqueRandomNumbers=1, key=0):
		self.countOfUniqueRandomNumbers = countOfUniqueRandomNumbers
		self.key						= key
		time.sleep(0)

	def generate(self, countOfUniqueRandomNumbers, key):
		if(countOfUniqueRandomNumbers)		:	self.countOfUniqueRandomNumbers = countOfUniqueRandomNumbers
		if(key)								:	self.key = key
		randomNumbers			= random.sample(range(100000001,199999999),self.countOfUniqueRandomNumbers)
		uniqueRandomNumbers		= []
		for randomNumber in randomNumbers	: uniqueRandomNumbers.append(int(key + str(randomNumber)))
		return uniqueRandomNumbers

	def numberIn36(self, numberIn10):
		dividend				= int((numberIn10))
		numberIn36				= ""
		while(dividend>0):
			quotient			=	dividend	//	self.divisor
			remainder			=	dividend	%	self.divisor
			dividend			=	quotient
			#numberIn36			=	str(remainder) + "." + numberIn36
			numberIn36			=	self.encodingSymbols[str(remainder)] + numberIn36
		return numberIn36

	def numberIn10(self, numberIn36):
		dividend				= numberIn36[::-1] # reverse order
		numberIn10				= 0
		for i in range (0, dividend.__len__()):
			character			= dividend[i]
			characterInNumber	= self.decodingSymbols[character]
			numberIn10			+= int(characterInNumber) * (36 ** i )
		return numberIn10

	def generateIn36(self, countOfUniqueRandomNumbers, key):
		uniqueRandomNumbers		= self.generate(countOfUniqueRandomNumbers, key)
		uniqueRandomNumbersIn36	= []
		for uniqueRandomNumber in uniqueRandomNumbers:
			uniqueRandomNumbersIn36.append(self.numberIn36(uniqueRandomNumber))
		return uniqueRandomNumbersIn36

#dt								= datetime.now()
#key     						= dt.strftime("%y%m%d%H%M")
#key								= 5000

'''
urn								= UniqueRandomNumber()
uniqueRandomNumbers				= urn.generate(100000,key)
uniqueRandomNumberIn36			= urn.numberIn36(uniqueRandomNumbers[0])
uniqueRandomNumberIn10			= urn.numberIn10(uniqueRandomNumberIn36)
print(uniqueRandomNumberIn36)
print(uniqueRandomNumberIn10)
'''
'''
urn								= UniqueRandomNumber()
uniqueRandomNumbersIn36			= urn.generateIn36(100000, key)
for uniqueRandomNumberIn36 in uniqueRandomNumbersIn36:
	print(uniqueRandomNumberIn36)
'''