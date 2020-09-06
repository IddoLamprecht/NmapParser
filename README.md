# NmapParser

NmapParser is a project purposed to read nmap logs and normalise the logs into a csv file.


## Prerequisites
```
  configparser -  basic module in python
  os - basic module in python
```



### Getting Started

 In order to make the project work, you must know from what directory and the file you wish to read the nmap logs from.
 once given you will be able to parse the file into a csv file.
 
 The parse is able to parse any attribute to your choosing. 
 So in order to choose what attributes you want to parse you must go into the config file and give the relevant information there.
 
 The parameters you need to eneter are in order to extract the requested attribute: 
 1. Base Element: you need to know what is the first element in the xml file (the first element from which the requested attribute is in).
 2. Path: you need to know the path of the attribute in order to extract the data. 
 3. Column Name : you need to put the data under the column name you wish to give it in the CSV file.
 
  
 In the nmap file, there are two types of logs.
 - File Logs - Logs that accure once in the file, and are relevant for each row in the csv file.
 - Element Logs- Logs that reaccure in the file multiple times, and each log represents a row in the csv file.
 
 
 ```
 config["log_type"] = {
    "base_element": "",
}

config["host"] = {
    "column_name": "path",
}

config["Extract"] = {
    "column_name": ["attribute_name"]

}
 
```
the config file also accepts directories, from where you can read all the nmap files of the given directory, and the directory you wish to write the final CSV file.

 
All the data you need to know about the each attribute you wish to extracy is in the [dtd file](https://svn.nmap.org/nmap/docs/nmap.dtd).
 
the project itself contains multiple objects.

The first object is NmapFile.
In order to initialise the object you need to give it the object file name (with directory)
To extract the relevant data into an array (contained in the Log_Results property you need to run the ExtractFile function.
This function know how to go to the nmap xml, and extract the data you wish, according to the configuration that the project contains.
This function will also insert into the property Log_Titles the array of titles you have given in the configuration file.

once this function has run, you will be able to use those arrays, and insert them into a CSV file, which is the second object this file contains.

in order to create the csv file, all you have to do is initalise the object.
to initalise this object, you must give it the parameter:
- file_name - this is the file name that the data that was extracted from the files, will enter the csv with this name (with directory)
- data_array - this is the array that contains the values of each row in the csv.
- title_names - this is the array of titles, that will be in the csv file.



### Usage
```
from CreateCSV import CSVFile
import configparser 
import os
  
 
 from NmapFile import NmapFile
 File_To_Extract = "Nmap.xml"
  
 Extract_File = NmapFile(File_To_Extract)
 Extract_File.ExtractFile()

 CSVFile(csv_file_name, data_array, title_names)
  ```
  

##### License

Iddo Lamprecht

  
