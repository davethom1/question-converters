# Overview
# Goal: Produce four different CSV files that contain data from multiple CSV files at the FBI.
# Creating NCVS files
# Mapping for sources to file is available in docs/MappingExcel.

import pandas as pd
import pyreadstat
import numpy as np

# set common variables. These are the folders that will store the input and output files.
fbi_data_folder = "data/raw/"
proc_data_folder = "data/processed/"

incident_file = proc_data_folder + "ncvs_incident.csv"

# create agencies file dataframe
df_agencies = pd.read_csv(fbi_data_folder + "agencies.csv")
print(str(len(df_agencies)) + " agencies in incident data file")

# create list of columns from agencies, convert to dataframe
agencies_cols = ["STATE_ID", "ORI", "NIBRS_CERT_DATE", "NIBRS_START_DATE", "UCR_AGENCY_NAME", "STATE_ABBR",
                 "POPULATION_GROUP_CODE", "DIVISION_NAME", "REGION_CODE", "AGENCY_TYPE_NAME", "COVERED_BY_LEGACY_ORI", "DATA_YEAR", "NIBRS_LEOKA_START_DATE"]
df_agencies_incident = df_agencies[agencies_cols]
print(df_agencies_incident.head())

# create incident file dataframe
df_incident = pd.read_csv(fbi_data_folder + "NIBRS_incident.csv")
print(str(len(df_incident)) + " incidents in incident data file")

# create list of columns from incident, convert to dataframe
incident_cols = ["INCIDENT_DATE", "REPORT_DATE_FLAG", "INCIDENT_HOUR", "CLEARED_EXCEPT_ID", "CLEARED_EXCEPT_DATE", "CARGO_THEFT_FLAG"]
df_incident_incident = df_incident[incident_cols]
print(df_incident_incident.head())