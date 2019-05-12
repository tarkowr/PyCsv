# PyCsv
Created by [Riche Tarkowski](https://github.com/tarkowr)

### What is PyCsv?
PyCsv is the easiest way to connect to and use a CSV file in Python.

### Installation
1. Copy the PyCsv class into your project.
2. Create a new CSV file in your project directory.
3. Instantiate a PyCsv object and provide it the name of the CSV file.  
`pycsv = PyCsv("data")`

#### Rewrite CSV File
PyCsv works only when the CSV values are all on one line. This method will rewrite your entire CSV file into one line.  
Returns a list of strings from the CSV file.  
`data = pycsv.rewrite_file()`

#### Get CSV File Content
Returns a list of strings from the CSV file.  
`data = pycsv.get_values()`  
OR  
`data = pycsv.cached_values` &nbsp;**Preferred**

#### Append a Value to the CSV File
Pass the string to add to this method.  
Returns a list of strings from the updated CSV file.  
`data = pycsv.append_value("Add Me!")`

#### Bulk Add Values to the CSV File
Pass a list of string values to add to this method.  
Returns a list of strings from the updated CSV file.     
`data = pycsv.bulk_add(["Rich", "Jon", "James"])`

#### Remove Value from CSV File by Index
Pass the index of the string value to remove from the CSV file.  
Returns a list of strings from the updated CSV file.     
`data = pycsv.remove_value(2)`

#### Delete the Contents of the CSV File
Returns an empty list.  
`data = pycsv.delete_contents()`

### Thank you for using PyCsv!


