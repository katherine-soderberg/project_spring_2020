
def removeMissing(filename):
    """Takes a file that contains missing scans and removes those rows, while providing the subject name and reason for removal."""
    loaded_file = pd.read_csv(filename)
    cleaned_list = []
    missing_counter = 0
    for row in loaded_file.index:
        if loaded_file[3][row] == "":
            print("Dropping subject scan " + loaded_file[0][row] + " because of " + loaded_file[1][row])
            counter = counter + 1
        else:
            cleaned_list.append(loaded_file[:][row])
    print("There were " + str(counter) + " scans with missing data dropped.")
    cleaned_df = pd.DataFrame(cleaned_list)
    return cleaned_df

def voxelConsistency(cleaned_dataframe, column_number, expected_size):
    """Checks that every scan has the same voxel dimension, specified by the user."""
    consistency_boolean = True
    for row in cleaned_dataframe.index:
        if cleaned_dataframe[column_number][row] == expected_size:
            continue
        elif cleaned_dataframe[column_number][row] != expected_size:
            print("Subject scan " + cleaned_dataframe[0][row] + " does not have voxel size of " +str(expected_size))
            consistency_boolean = False
    return consistency_boolean
