

class PyBase():
	"""docstring for PyBase"""
	def __init__(self):
		super(PyBase, self).__init__()
		
	def findName(self, data):
		Test = str(data)
		a = []
		for x in range(0,len(Test)):
			char = Test[x]
			if char == "'" and "'" in a:
				break
			elif char == "'":
				a.append(char)
				a.append(Test[x+1])
			elif char in a:
				a.append(Test[x+1])
		fileName = ' '.join(a)
		fileName = fileName.replace(' ', '')
		fileName = fileName.replace("'", '')
		return fileName

	def getData(self, name):
		name = name + ".txt"
		dataName = open(name, "at")
		dataName.close()
		dataName = open(name,"rt")
		return dataName
	def showData(self, data):
		fileName = self.findName(data)
		try :
			data = open(fileName, "rt")
			print("Data recorded : \n")
			print(data.read())
			return data.read()
		except:
			print("ERROR : file doesn't found")

	def findTab(self, data, table):
		fileName = self.findName(data)
		data.close()
		table = "tN::"+table
		try: 
			dataName = open(fileName,"r")
			Line = 0
			true = 0
			for line in dataName:
				if line != None:
					if table in line:
						true = 1
			if true == 1:
				return True 
			else:
				return False
							
		except:
			print("ERROR: file error : file don't found")

	def newTab(self, data, tabName, verify=1):
		if verify == 1 and not self.findTab(data,tabName):
			fileName = self.findName(data)
			data.close()
			dataName = open(fileName, "a")
			tabName = "\ntN::" + tabName +" :"
			dataName.write(tabName)
			print("\n")
		elif verify == 0:

			fileName = self.findName(data)
			data.close()
			dataName = open(fileName, "a")
			tabName = "\ntN::" + tabName +" :"
			dataName.write(tabName)
			print("\n")
		else :
			print("Table already exist")
	def delTab(self,data, tabName):
		fileName = self.findName(data)
		data.close()
		dataName = open(fileName,"r")
		contents = dataName.readlines()
		dataName.close()
		dataName = open(fileName,"w")
		li = 0
		for line in contents:
			if not tabName in line:
				dataName.write(line)
			else:
				print("table delete in line : ",li)
				return True
			li += 1
	def appendTab(self, data, tabName, add):
		if self.findTab(data, tabName):

			fileName = self.findName(data)
			data.close()
			dataName = open(fileName,"r")
			contents = dataName.readlines()
			dataName.close()
			dataName = open(fileName,"w")
			tabName = "tN::"+tabName
			for line in contents:
				if tabName in line:
					line = line + " {"+add+"}"
					dataName.write(line)
				else:
					dataName.write(line)
		else:
			print("ERROR : table doesn't exist")
	def delCont(self, data, tabName, deletedContent):
		fileName = self.findName(data)
		data.close()
		dataName = open(fileName,"r")
		contents = dataName.readlines()
		dataName.close()
		tabName = "tN::"+tabName
		dataName = open(fileName,"w")
		deletedContent = " {"+deletedContent+"}"
		for line in contents:
			if deletedContent in line and tabName in line:
				line = line.replace(deletedContent, '')
				dataName.write(line)
			else:
				dataName.write(line)
	def getCont(self, data ,tabName):
		fileName = self.findName(data)
		data.close()
		dataName = open(fileName,"r")
		contents = dataName.readlines()
		a=[]
		for line in contents:
			if tabName in line:
				for x in range(0,len(line)):
					char = line[x]
					
					if char =='{':
						a.append(line[x])
						a.append(line[x+1])
					elif char in a:
						try:
							a.append(line[x+1])
						except:
							break
					elif char == '}':
						break
					
				contents = ' '.join(a)
				contents = contents.replace(' ', '')
				contents = contents.replace("{", '')
				contents = contents.replace("}", ' ')
				return contents
	def replaceCont(self,data, tabName, newContent):
		content = self.getCont(data, tabName)
		content = content.replace(' ','')
		self.delCont(data, tabName, content)
		self.appendTab(data, tabName, newContent)






