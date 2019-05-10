# PyCsv
Created by [Riche Tarkowski](https://github.com/tarkowr)

### What is PyCsv?
PyCsv is the easiest way to connect to and use a CSV file in Python.

### Installation
1. Copy the PyCsv class into your project.
2. Create a new CSV file in your project directory.
3. Instantiate a PyCsv object and provide it the name of the CSV file.  
`pycsv = PyCsv("data")`

#### Get CSV File Content
Returns a list of strings from the CSV file.  
`data = pycsv.get_values()`

#### Append a Value to the CSV File
Returns a list of strings from the updated CSV file.  
`data = pycsv.append_value("Add Me!")`

#### Bulk Add Values to the CSV File
Returns a list of strings from the updated CSV file.     
`data = pycsv.bulk_add(["Rich", "Jon", "James"])`

#### Delete the Contents of the CSV File
Returns an empty list.  
`data = pycsv.delete_contents()`


