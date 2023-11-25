import pathlib
import pandas as pd

# reading files.
vers_data = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/Group Project/Dataset/2022VAERSDATA.csv", encoding='latin-1')
vers_vax = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/Group Project/Dataset/2022VAERSVAX.csv", encoding='latin-1')
vers_symptoms = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/Group Project/Dataset/2022VAERSSYMPTOMS.csv", encoding='latin-1')

##################################################################################################################

# Define a dictionary with columns and their respective predefined values for filling nulls
fill_values = {
    'OTHER_MEDS': 'No medication',
    'CUR_ILL': 'Not applicable',
    'HISTORY': 'No concerns',
    'PRIOR_VAX': 'Not applicable', 
    'DIED': 'N',
    'DATEDIED': 'Not applicable', 
    'L_THREAT': 'N', 
    'ER_VISIT': 'N', 
    'HOSPITAL':'N',
    'HOSPDAYS': 0,
    'X_STAY': 'N',
    'DISABLE': 'N',
    'BIRTH_DEFECT': 'N',
    'OFC_VISIT': 'N',
    'ER_ED_VISIT': 'N',
    'ALLERGIES': 'N'
}

# Fill null values with predefined values for respective columns
for column, value in fill_values.items():
    vers_data[column].fillna(value, inplace=True)

# Calculate the percentage of null values in each column
null_percentages = (vers_data.isnull().sum() / len(vers_data)) * 100
print(null_percentages)

# List to store columns with more than 50% null values
columns_to_drop = []

# Iterate through each column's null percentage
for column, percentage in null_percentages.items():
    if percentage > 50:
        columns_to_drop.append(column)

# Drop columns with more than 50% null values
if columns_to_drop:
    vers_data.drop(columns=columns_to_drop, inplace=True)
    print(f"Dropped columns: {columns_to_drop}")
else:
    print("No columns have more than 50% null values.")

##################################################################################################################

# Calculate the percentage of null values in each column
null_percentages = (vers_vax.isnull().sum() / len(vers_vax)) * 100
print(null_percentages)

# List to store columns with more than 50% null values
columns_to_drop = []

# Iterate through each column's null percentage
for column, percentage in null_percentages.items():
    if percentage > 50:
        columns_to_drop.append(column)

# Drop columns with more than 50% null values
if columns_to_drop:
    vers_vax.drop(columns=columns_to_drop, inplace=True)
    print(f"Dropped columns: {columns_to_drop}")
else:
    print("No columns have more than 50% null values.")

##################################################################################################################

# Define a dictionary with columns and their respective predefined values for filling nulls
fill_values = {
    'SYMPTOM2': 'No symptom',
    'SYMPTOMVERSION2': 0,
    'SYMPTOM3': 'No symptom',
    'SYMPTOMVERSION3': 0,
    'SYMPTOM4': 'No symptom',
    'SYMPTOMVERSION4': 0,
}

# Fill null values with predefined values for respective columns
for column, value in fill_values.items():
    vers_symptoms[column].fillna(value, inplace=True)

# Calculate the percentage of null values in each column
null_percentages = (vers_symptoms.isnull().sum() / len(vers_symptoms)) * 100
print(null_percentages) 

# List to store columns with more than 50% null values
columns_to_drop = []

# Iterate through each column's null percentage
for column, percentage in null_percentages.items():
    if percentage > 50:
        columns_to_drop.append(column)

# Drop columns with more than 70% null values
if columns_to_drop:
    vers_symptoms.drop(columns=columns_to_drop, inplace=True)
    print(f"Dropped columns: {columns_to_drop}")
else:
    print("No columns have more than 70% null values.")

##################################################################################################################

# Removing rows with NaN values
cleaned_vers_data = vers_data.dropna()

num_rows, num_columns = cleaned_vers_data.shape

print(f'Total number of rows: {num_rows}')
print(f'Total number of columns: {num_columns}')

##################################################################################################################

# Removing rows with NaN values
cleaned_vers_vax = vers_vax.dropna()

num_rows, num_columns = cleaned_vers_vax.shape

print(f'Total number of rows: {num_rows}')
print(f'Total number of columns: {num_columns}')

##################################################################################################################

# Removing rows with NaN values
cleaned_vers_symptoms = vers_symptoms.dropna()

num_rows, num_columns = cleaned_vers_symptoms.shape

print(f'Total number of rows: {num_rows}')
print(f'Total number of columns: {num_columns}')

##################################################################################################################

# Merge DataFrames based on the 'VERS_ID' column
merged_df = pd.merge(cleaned_vers_data, cleaned_vers_vax, on='VAERS_ID', how='inner')
merged_df = pd.merge(merged_df, cleaned_vers_symptoms, on='VAERS_ID', how='inner')

num_rows, num_columns = merged_df.shape
print(f'Total number of  rows in merged data: {num_rows}')
print(f'Total number of columns in merged data: {num_columns}')

# Writing it out in csv.

# output_file_name = "cleaned_vers_data.csv"
# merged_df.to_csv(output_file_name, index=False)

