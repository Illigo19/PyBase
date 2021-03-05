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
<i>newTab()</i>
<code>(obj).newTab(data, "Name")</code>
 1 checks if the table already exists and if it already exists he does not recreate it. 2 does not care if a table of the same does not exist or not, can be dangerous because when deleting one of the tables, the 2 will be.
<br>
<i>delTab()</i>
<code>(obj).delTab(data, "Name")</code>
This function allows you to delete a complete table and with it are contained
<i>Here the 'Name' table will be deleted.</i>
