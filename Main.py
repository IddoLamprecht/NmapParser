import xmltodict
import json
import xml.etree.ElementTree as ET
import configparser
import ast
from CreateCSV import CSVFile
import os
from NmapFile import NmapFile

config = configparser.ConfigParser()
config.read("ExtractNmapLogs.ini")
Log_Source = config["Directories"]["Nmap_XML_dir"]


# Function that gets the files and returns the relevant ones
def get_Files(File_filter):
    if "nmap" in File_filter:
        return True


# return into a list the relevant nmap files
list_of_files = filter(get_Files, os.listdir(Log_Source))
Return_list = []
# run the parse on the all the files that we have
for File in list_of_files:
    # create an nmap file object with the full name of the file and extract the relevant data
    Extract_File = NmapFile(Log_Source + File)
    Extract_File.ExtractFile()

    # create the csv file for all the nmap log files
    CSVFile("/Users/iddolamprecht/Desktop/Normalize_Test/EXTRACT_" + File + ".csv", Extract_File.Log_Results,
            Extract_File.Log_Titles)
