
def outlierStats(outlier_list):
    """Takes a list of outliers and computes the mean and standard deviation"""
    import statistics
    try:
        outlierMean = statistics.mean(outlier_list)
        outlierStdev = statistics.stdev(outlier_list)
        return outlierMean, outlierStdev
    except TypeError :
        explanation = "Cannot compute statistics on a list of non-numerical elements."
        return explanation
    
def outlierExclude(cleaned_dataframe, column_number, stdev_cutoff_factor):
    """Uses outlierStats to determine which scans have outlying volumes above a specified threshold and removes them."""
    import pandas as pd
    import matplotlib.pyplot as plt
    column_as_series = cleaned_dataframe.iloc[:,column_number]
    column_as_list = column_as_series.tolist()
    mean, stdev = outlierStats(column_as_list)
    upper_threshold = mean + (stdev * stdev_cutoff_factor)
    lower_threshold = mean - (stdev * stdev_cutoff_factor)
    noOutlier_list = []
    for row in range(cleaned_dataframe.index.size - 1):
        if (cleaned_dataframe.iloc[row, column_number] > upper_threshold) or (cleaned_dataframe.iloc[row, column_number] < lower_threshold):
            print("Dropping subject scan " + cleaned_dataframe.iloc[row, 0] + " due to " + str(cleaned_dataframe.iloc[row, column_number]) + " outlying volumes." )
        else:
            noOutlier_list.append(cleaned_dataframe.iloc[row])
    noOutlier_dataframe = pd.DataFrame(noOutlier_list)
    return column_as_list, noOutlier_dataframe
