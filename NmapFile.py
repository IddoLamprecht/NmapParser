import xmltodict
import json
import xml.etree.ElementTree as ET
import configparser
import ast
from CreateCSV import CSVFile
import os

config = configparser.ConfigParser()
config.read("ExtractNmapLogs.ini")


# function that returns if a list has only one value or more
def one_value_list(list_one):
    if len(list_one) == 1:
        return list_one[0]
    elif len(list_one) > 0:

        return list_one
    else:
        return ""


class NmapFile:
    # function in object that returns the data and title names
    def Extract_Attrib(self, ElemType):
        return_d = []
        title_csv = []

        # run on all the elements you want to return from the logs
        for Log in config[ElemType]:

            # runs on the logs that are in the config file and are the first element in the tree
            for child in self.root.findall(Log):
                log_att = []
                # run on the elements you want to return from the specific log type
                for keys in config[Log]:

                    # append the columns names
                    if keys not in title_csv: title_csv.append(keys)
                    log_append = []
                    # get the element based on the path in the config file
                    for x in child.findall(config[Log][keys] + "*"):
                        # get the relevant attrib in the element
                        if x.tag == keys:
                            multi_res = []
                            for att in ast.literal_eval(config["Extract"][x.tag]):
                                multi_res.append(x.attrib[att])
                            log_append.append(one_value_list(multi_res))

                    log_att.append(one_value_list(log_append))
                return_d.append(log_att)
        return title_csv, return_d

    # runs on the file and returns the data thats relevant to all the logs
    def Extract_Elem(self, ElemType):
        return_d = []
        title_csv = []

        # get the log thats relevant to the specific file
        for Log in config[ElemType]:
            # get the data of the log
            for child in self.root.findall(Log):
                log_att = []
                # get all the attributes you want from the file log
                for keys in config[Log]:
                    if keys not in title_csv: title_csv.append(keys)
                    log_append = []
                    # get the data from the file log and insert it into the data array
                    if keys in child.attrib:

                        for att in ast.literal_eval(config["Extract"][keys]):
                            log_append.append(one_value_list(child.attrib[att]))

                    log_att.append(one_value_list(log_append))

                return_d.append(one_value_list(log_att))
        return title_csv, return_d

    def __init__(self, fileName):
        self.filename = fileName
        # parse the file
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()
        self.Log_Results = []

        self.Log_Titles = []

        self.File_Titles = []
        self.File_Results = []

    # get the data from  the file logs and the data logs and append them into a csv file format
    def ExtractFile(self):

        self.Log_Titles, self.Log_Results = self.Extract_Attrib("LogElem")
        self.File_Titles, self.File_Results = self.Extract_Elem("FileElem")
        # for each log append the data from the file (relevant for all the logs)
        for Log_Row in range(len(self.Log_Results)):
            self.Log_Results[Log_Row].append(one_value_list(self.File_Results))
        # append the titles for the csv file
        self.Log_Titles.append(one_value_list(self.File_Titles))

        return self.Log_Results
