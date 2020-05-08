
def summarize(filename):
    """Return basic information about the contents of a csv file with the rows as scan instances."""
    import pandas as pd
    if filename.endswith('.csv'):
        loaded_file = pd.read_csv(filename)
        print("The head of the file is:" + "\n" + str(loaded_file.head()))
        print("Summary information about the file is as follows:")
        print(loaded_file.info())
        number_of_scans = str(len(loaded_file.index))
        print("The file contains information about " + number_of_scans + " scans.")
        closing_statement = filename + " has been summarized."
        return closing_statement
    else: 
        print("The file provided is not in comma separated value format. Please convert your input file to .csv format before using this package.")
        
def listColumns(filename):
    import pandas as pd
    loaded_file = pd.read_csv(filename)
    colNames_list = loaded_file.columns
    return colNames_list
