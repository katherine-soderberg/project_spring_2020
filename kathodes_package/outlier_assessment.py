
def outlierStats(outlier_list):
    """Takes a list of outliers and computes the mean and standard deviation"""
    try:
        outlierMean = outlier_list.mean()
        outlierStdev = outlier_list.std()
        return outlierMean, outlierStdev
    except TypeError :
        explanation = "Cannot compute statistics on a list of non-numerical elements."
        return explanation
    
def outlierExclude(cleaned_dataframe, column_number, stdev_cutoff_factor):
    """Uses outlierStats to determine which scans have outlying volumes above a specified threshold and removes them."""
    column_as_series = cleaned_dataframe[column_number]
    column_as_list = column_as_series.tolist()
    mean, stdev = outlierStats(column_as_list)
    upper_threshold = mean + (stdev * stdev_cutoff_factor)
    lower_threshold = mean - (stdev * stdev_cutoff_factor)
    noOutlier_list = []
    for row in cleaned_dataframe.index:
        if cleaned_dataframe[column_number][row] > upper_threshold | cleaned_dataframe[column_number][row] < lower_threshold:
            print("Dropping subject scan " + cleaned_dataframe[0][row] " due to " + str(cleaned_dataframe[column_number][row]) + " outlying volumes." )
        else:
            noOutlier_list.append(cleaned_dataframe[:][row])
    noOutlier_dataframe = pd.DataFrame(noOutlier_list)
