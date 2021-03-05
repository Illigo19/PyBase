# PyBase
PyBase is a python module to allow the storage of variables or other
# Mini Wiki :
description and use of PyBase
 <h2>- initiator and spectator functions :</h2>
 These functions are both unnecessary and mandatory.<br>
 The first : 
 <code>(obj).getData("myfile")</code>
  It plays the role of <i>dataName = open(myfile.txt, "at")</i> and therefore can easily be replaced by it, but one of the two is required.
  <b>Warning :</b>   Do not give the file extension (here .txt) It will not be able to find it.
 <br>
 The second :
 <code>(obj).showData(data)</code>the only purpose of this function is to display the complete contents of what has been recorded by PyBase
<h2>- Table and content management function</h2>
The record base functions from table and in its tables one and/or contents. So there are the functions related to the tables and those related to the contents
<h3>1) Table management :</h3>
<code>(obj).newTab(data, "Name")</code>It will create a table with a name (here Name) 
It can take two versions : <code>(obj).newTab(data, "Name", 1 or None) or  (obj).newTab(data, "Name",2)


