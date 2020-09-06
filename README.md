# NmapParser

NmapParser is a project purposed to read nmap logs and normalise the logs into a csv file.


## Prerequisites
```
  configparser - install through pip install
  os - install through pip install
```



### Getting Started

 In order to make the project work, you must know from what directory and the file you wish to read the nmap logs from.
 once given you will be able to parse the file into a csv file.
 
 the parse is able to parse what attribute to your choosing. 
 so in order to choose what attributes you want to parse you must go into the config file and give the relevant information there.
 
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
    "attribute": "path",
}

config["Extract"] = {
    "column_name": ["attribute_value"]

}
 
```
the config file also accepts directories, from where you can read all the nmap files of the given directory, and the directory you wish to write the final CSV file.

 
All the data you need to know about the each attribute you wish to extracy is in the [dtd file] (https://svn.nmap.org/nmap/docs/nmap.dtd)
 

Example of how to run the project in order to extract the data: 

```  from CreateCSV import CSVFile
  
  import os
  
  from NmapFile import NmapFile
  File_To_Extract = "Nmap.xml"
  
  Extract_File = NmapFile(File_To_Extract)
  Extract_File.ExtractFile()

  CSVFile(csv_file_name, data_array, title_names)
  ```
  
  
##### License

Iddo Lamprecht

  
