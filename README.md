# PyBase
PyBase is a python module to allow the storage of variables or other
# Mini Wiki :
description and use of PyBase
<h2> -Initialization</h2>
To install the package : <code>pip install PyBase-manager</code><br>introduce your code by :<code>from PyBase import *</code><br><br>
 <h2>- initiator and spectator functions :</h2>
 These functions are both unnecessary and mandatory.<br>
 The first : 
 <code>(obj).getData("myfile")</code>
  It plays the role of <i>dataName = open(myfile.txt, "at")</i> and therefore can easily be replaced by it, but one of the two is required.
  <b>Warning :</b>   Do not give the file extension (here .txt) It will not be able to find it.
 <br><br>
 The second :
 <code>(obj).showData(data)</code>the only purpose of this function is to display the complete contents of what has been recorded by PyBase
<h2>- Table and content management function</h2>
The record base functions from table and in its tables one and/or contents. So there are the functions related to the tables and those related to the contents
<h3>1) Table management :</h3>
<i>newTab()</i>
<code>(obj).newTab(data, "Name")</code>
 1 checks if the table already exists and if it already exists he does not recreate it. 2 does not care if a table of the same does not exist or not, can be dangerous because when deleting one of the tables, the 2 will be.
<br><br>
<i>delTab()</i>
<code>(obj).delTab(data, "Name")</code>
This function allows you to delete a complete table and with it are contained
<i>Here the 'Name' table will be deleted.</i>
<br><br>
<i>appendTab()</i><code>(obj).appendTab(data, "Name", "Andrew")</code>This function allows to add to a table (here <i>'Name'</i>) content (here <i>'Andrew'</i>)
<br>The result in the file: <code>tN::Name : {Andrew}</code>
<br><br>
<i>findTab()</i><code>(obj).findTab(data, "Hello world")</code>This boolean function only allows you to search for a table in the database, it returns True if the table exists.<br><i>Here we search for 'Hello world' among 'data'</i>
<br><br>
<h3>2) Content management :</h3>
<br><br><i>getCont()</i><code>(obj).getCont(data, "Name")</code> Allows to retrieve the contents of a table <i> Here the table 'Name'</i>
<br><br><i>delCont()</i><code>(obj).delCont(data, "Name", "Joseph")</code> Deletes a particular content in a particular table <i> Here, delete 'Joseph' in table 'Name'</i>
<br><br><i>replaceCont()</i><code>(obj).replaceCont(data, "Name", "Chloé")</code> replaces all the existing content of a table with the given content <i>Here, replace the contents of 'Name' by 'Chloe'.</i><br><br>
<h2>- More information </h2><br><br> The constructor used is by default <code>obj = PyBase.PyBase()</code><br>As well as 'data' comes from <code>data = obj.getData("myfile")</code><br><br>The PyBase.py python isn't yet commented but it will be soon ;)

