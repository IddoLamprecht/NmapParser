# NmapParser

NmapParser is a project purposed to read nmap logs and put them in a CSV file.

## How To use
 The project creates a config file named "ExtractNmapLogs.ini" there you can choose what logs you want extract and what values.
 
 There you choose from which directory you read ("Nmap_XML_dir") your nmap file and write ("Nmap_CSV_write") your result under the "Directories" property.
 
 Once you choose your directories you can choose which attributes you want to read. there are two types of attributes, one that are in the file (ex: scaninfo) 
 and log attributes, attributes that are in the file multiple times and each represnt a row in the intended CSV file.
 
 In order to retrieve the relevant data you must put a few parameters that are relevant in order to extract the data:
 
 1. Base Element: you need to know what is the first element in order to know where to search in the file ("FileElem" or "LogElem")
 2. Path: you need to know from where the data is in order to retrieve it (under a property with the name of the base element). 
 3. Column Name : you need to put the data under the column name of your choosing.
 
All the data you need to know about where to extract is in the [dtd file] (https://svn.nmap.org/nmap/docs/nmap.dtd)
 
 ### Usage
  from CreateCSV import CSVFile
  import os
  from NmapFile import NmapFile
  
  Log_Source = config["Directories"]["Nmap_XML_dir"]
  
  Extract_File = NmapFile(Log_Source + File)
  Extract_File.ExtractFile()

  CSVFile(csv_file_name, data_array, title_names)
  
  
