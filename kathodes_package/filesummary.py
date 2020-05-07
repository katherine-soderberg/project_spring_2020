import pandas as pd

def summarize(filename):
    if (filename[-4:] == ".csv"):
        loaded_file = pd.read_csv(filename)
    else: 
        return "The file provided is not in comma separated value format. \
Please convert your input file to .csv format before using this package."
    return "The head of the file is:" + "\n" + loaded_file.head()
    return "Summary information about the file is as follows:" + "\n" + loaded_file.info()
    return "The file contains information about " + str(len(loaded_file.index)) + "scans."
