""" Demo of PyBase
"""
import PyBase
#constructor :
obj = PyBase.PyBase()

# open #myfile (no .txt) , create if #myfile doesn't exist
data = obj.getData("myfile")



# create a New Table, check if her already exist when newTab(data,table,1 or None) not when newTab(data,table,0)
#obj.newTab(data, "Louis")

# check if a Table (here : Hello world) exist in data (bool)
#if obj.findTab(data, "Hello world"):
	#print("exist")

#delete table with her name (return True if it delete a Table) WARNING can delete the complet data, tape the exact name 
#obj.delTab(data, "Name")

#add content into a table 
obj.appendTab(data, "Louis", "Joseph")

# delete from Table a content (here : content)
#obj.delCont(data, "Louis", "Joseph")


obj.getCont(data, "Louis")

# show content of Data
obj.showData(data)

print("debbogage : ")