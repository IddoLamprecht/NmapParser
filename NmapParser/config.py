# creates a config file that contains the Normalised Names and the directories to write two
import configparser

config = configparser.ConfigParser()



config["host"] = {
    "address": "",
    "port": "ports/",
    "Status": ""
}

config["Extract"] = {
    "address": ["addr"],
    "port": ["portid","protocol"],
    "Status" : ["state"]

}
config["Directories"] = {
    "Nmap_XML_dir": "/Users/iddolamprecht/Desktop/Normalize/",

}

with open('ExtractNmapLogs.ini', 'w') as configfile:
    config.write(configfile)
