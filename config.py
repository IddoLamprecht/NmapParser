# creates a config file that contains the Normalised Names and the directories to write two
import configparser

config = configparser.ConfigParser()
# all the elements of the file logs (logs that are relevant for all the data logs in the file)
config["FileElem"] = {
    "scaninfo": ""
}

# all the elements in the file that have the relevant data that i want in the csv file
config["LogElem"] = {
    "host": "",
}

# a dictionary that has all the paths from each attribute that i can get the data for the data logs
config["host"] = {
    "address": "",
    "port": "ports/",
    "Status": ""
}

# a dictionary that has all the paths from each element that i can get the data for the file logs
config["scaninfo"] = {
    "type": ""
}

# the mapping of what data i want in the rows of the csv file
config["Extract"] = {
    "address": ["addr"],
    "port": ["portid", "protocol"],
    "Status": ["state"],
    "type": ["type"]

}
# the file path that im reading from
config["Directories"] = {
    "Nmap_XML_dir": "/Users/iddolamprecht/Desktop/Normalize/",

}
# create the config file
with open('ExtractNmapLogs.ini', 'w') as configfile:
    config.write(configfile)
