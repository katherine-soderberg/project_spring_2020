
def removeMissing(filename):
    """Takes a file that contains missing scans and removes those rows, while providing the subject name and reason for removal."""
    import pandas as pd
    import math
    loaded_file = pd.read_csv(filename)
    cleaned_list = []
    missing_counter = 0
    for row in loaded_file.index:
        if math.isnan(loaded_file.iloc[row, 3]):
            print("Dropping subject scan " + loaded_file.iloc[row, 0] + " because of " + loaded_file.iloc[row,1])
            missing_counter = missing_counter + 1
        else:
            cleaned_list.append(loaded_file.iloc[row])
    print("There were " + str(missing_counter) + " scans with missing data dropped.")
    cleaned_df = pd.DataFrame(cleaned_list)
    return cleaned_df

def voxelConsistency(cleaned_dataframe, column_number, expected_size):
    """Checks that every scan has the same voxel dimension, specified by the user."""
    import pandas as pd
    consistency_boolean = True
    for row in range(cleaned_dataframe.index.size - 1):
        if cleaned_dataframe.iloc[row, column_number] != expected_size:
            print("Subject scan " + cleaned_dataframe.iloc[row, 0] + " with row index of " + str(row) + " does not have voxel size of " + str(expected_size))
            consistency_boolean = False
        else:
            continue
    return consistency_boolean
