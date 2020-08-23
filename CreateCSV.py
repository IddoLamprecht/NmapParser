import csv

# creates a csv file with the data and column names given
class CSVFile:

    def __init__(self, csv_file_name, data_array, title_names):
        self.csvFileName = csv_file_name
        self.dataArray = data_array
        self.titleNames = title_names
        try:
            with open(csv_file_name, "w", newline='') as cf:
                writer = csv.writer(cf)
                # Writes the columns names
                writer.writerow(self.titleNames)
                # Writes all the rows underneath
                for i in self.dataArray:
                    writer.writerow(i)
            cf.close()
        except Exception:
            raise Exception("couldn't create CSV File")

