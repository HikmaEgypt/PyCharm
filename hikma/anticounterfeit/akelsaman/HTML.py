import re

class HTMLTable():
	def __init__(self, table=''):
		self.table = table
		self.header = ''
		self.rows = ''

	def getHeader(self, thList):
		header = ''
		header =  header + '<tr>'
		for th in thList:
			header = header + '<th>'+ str(th) + '</th>'
		header = header + '</tr>'
		self.header = self.header + header
		return header

	def getRow(self, tdList):
		row = ''
		row = row + '<tr>'
		for td in tdList:
			row = row + '<td>' + str(td) + '</td>'
		row = row + '</tr>'
		self.rows = self.rows + row
		return row

	def setHeader(self, header):
		self.header = header

	def setRow(self, row):
		self.rows = self.rows + row

	def tabs(self, tabsCount):
		tabs = ''
		for i in range (0, tabsCount):
			tabs = tabs + '\t'
		return tabs

	def indent(self, tableTabs):
		elements = {
			'<table': tableTabs, '</table>': tableTabs,
			'<thead>': tableTabs + 1, '</thead>': tableTabs + 1,
			'<tbody>': tableTabs + 1, '</tbody>': tableTabs + 1,
			'<tfoot>': tableTabs + 1, '</tfoot>': tableTabs + 1,
			'<tr>': tableTabs + 2, '</tr>': tableTabs + 2,
			'<th>': tableTabs + 3, '<td>': tableTabs + 3,
		}
		for element in elements:
			elementTabs = elements[element]
			#print(self.tabs(elementTabs) + element)
			self.table = re.sub(element, (self.tabs(elementTabs) + element), self.table)
		return self.table

	def newLine(self):
		elements = { '<table', '</table>', '<thead>', '</thead>', '<tbody>', '</tbody>', '<tfoot>', '</tfoot>',
			'<tr>', '</tr>', '<th>', '<td>' }
		for element in elements:
			self.table = re.sub(element, '\n' + element, self.table)
		return self.table

	def createTable(self,  cssClass):
		self.table='<table class="' + str(cssClass) + '">'
		self.table = self.table + '<thead>' + self.header + '</thead>'
		self.table = self.table + '<tfoot></tfoot>'
		self.table = self.table + '<tbody>' + self.rows + '</tbody>'
		self.table = self.table + '</table>'
		self.newLine()
		self.indent(2)
		return self.table
