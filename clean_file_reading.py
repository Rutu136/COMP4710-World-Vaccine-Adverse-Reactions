import pandas as pd

cleaned_data_frame_2020 = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/COMP4710-World-Vaccine-Adverse-Reactions/cleaned_vers_data_2020.csv", encoding='latin-1')
print(cleaned_data_frame_2020.shape)

cleaned_data_frame_2021 = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/COMP4710-World-Vaccine-Adverse-Reactions/cleaned_vers_data_2021.csv", encoding='latin-1')
print(cleaned_data_frame_2021.shape)

cleaned_data_frame_2022 = pd.read_csv("C:/Users/rutub/OneDrive/Desktop/Fall 2023/Comp4710/COMP4710-World-Vaccine-Adverse-Reactions/cleaned_vers_data_2022.csv", encoding='latin-1')
print(cleaned_data_frame_2022.shape)

# columns_to_check = cleaned_data_frame_2022.columns.tolist()
# print(columns_to_check)
# # Find distinct values in specified columns
# for column in columns_to_check:
#     unique_values = cleaned_data_frame_2022[column].unique()
#     print(f"Unique values in '{column}':")
#     print(unique_values)
#     print("\n\n")
