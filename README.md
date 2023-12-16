# COMP4710-World-Vaccine-Adverse-Reactions

Team Members:
- Rutu Barvaliya
- Dharmit Anghan
- Breanna Brown

Group: 8  
Course: COMP4710  
Section: A01  
Professor: Carson

## Repository and File Structure

- Files starting with 'Group8' are exclusively used for paper writing and dataset preprocessing.
  
- The 'Extra_stuff' directory contains experimental code.

- Files ending with 'pre_processing' demonstrate our data preprocessing steps but won't execute due to missing original file sources.

## Obtaining the Original Dataset (2020-2022)

- For the original VAERS data, visit [this link](https://vaers.hhs.gov/data/datasets.html).

- More information about the fields and dataset can be found [here](https://vaers.hhs.gov/docs/VAERSDataUseGuide_en_September2023.pdf).

## Accessing the Pre-Processed Dataset (2020-2022)

- Please note that downloading the dataset may require a Kaggle account due to file size restrictions and cloud storage limitations we could not find any free cloud storage other than Kaggle.

- Follow [this link](https://www.kaggle.com/datasets/rutubarvaliya/covid-19-vaccine-adverse-reaction-effect-2020-2022/data?select=cleaned_vers_data_covid19_vaccine_2020-2022_duplicate_removed.csv).

- Download the CSV file named `cleaned_vers_data_covid19_vaccine_2020-2022_duplicate_removed.csv`.

- Place the CSV file into the root level of the cloned repository.

## Running Apriori Code

- After placing the `cleaned_vers_data_covid19_vaccine_2020-2022_duplicate_removed.csv` file, execute `Group8_fp_mining_based_on_vaccine_type.ipynb` and `Group8_fp_mining_based_on_vax_med_hist_allerg.ipynb` to obtain the expected results.

## Optional

- Supplementary work is stored in the 'Extra_stuff' directory.

- To view our COVID-19 visualizations, access the CSV file from [this link](https://www.kaggle.com/datasets/rutubarvaliya/covid-19-dataset?select=covid-19_vaccination_US_Data_2020-2022.csv).
