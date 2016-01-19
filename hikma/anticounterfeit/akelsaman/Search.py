import re

class Search:
	def __init__(self):
		pass

	def getWhere(self, searchArraysDictionary):
		ands= ''
		for array in searchArraysDictionary:
			columnName = array
			array = searchArraysDictionary[array].split("::,::")
			ors = '('
			for element in array:
				ors = ors + ' OR ' + columnName + ' ' + element[0:2] + ' ' + element[3:]
			ors = ors + ')'
			ands = ands + " AND " + ors

			ands = re.sub('\( OR ','(',ands)
			ands = re.sub('^ AND ','',ands)
		return ands