import xmltodict
import json
import xml.etree.ElementTree as ET
import configparser
import ast
from CreateCSV import CSVFile
import os

config = configparser.ConfigParser()
config.read("ExtractNmapLogs.ini")
Log_Source = config["Directories"]["Nmap_XML_dir"]


def get_Files(File_filter):
    if "nmap" in File_filter:
        return True


list_of_files = filter(get_Files, os.listdir(Log_Source))
Return_list = []

for File in list_of_files:

    tree = ET.parse(Log_Source+File)
    root = tree.getroot()
    return_d = []
    title_csv = []
    for child in root.findall("host"):
        log_att = []

        for keys in config["Extract"]:
            if keys not in title_csv: title_csv.append(keys)
            log_append = []
            for x in child.findall(config["host"][keys] + "*"):
                if x.tag == keys:
                    for att in ast.literal_eval(config["Extract"][x.tag]):
                        log_append.append(x.attrib[att])

            if len(log_append) == 1:
                log_att.append(log_append[0])
            elif len(log_append) > 0:

                log_att.append(log_append)
            else:
                log_att.append("")
        return_d.append(log_att)
    CSVFile("/Users/iddolamprecht/Desktop/Normalize_Test/EXTRACT_"+File+ ".csv",return_d,title_csv)
