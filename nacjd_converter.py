# Overview
# Goal: Produce eleven different CSV files that contain data from multiple CSV files at the FBI.
# Mapping for sources to file is available in docs/MappingExcel.

import pandas
import numpy

# set common variables. These are the folders that will store the input and output files.
fbi_data_folder = "data/raw/"
proc_data_folder = "data/processed/"

# make the admin file
# inputs to admin file: agencies, nibrs_incident

admin_file = proc_data_folder + "admin.csv"

# make the offense file
# inputs to offense file: agencies, NIBRS_OFFENSE, NIBRS_SUSPECT_USING, NIBRS_CRIMINAL_ACT, NIBRS_WEAPON, NIBRS_BIAS_MOTIVATION

offense_file = proc_data_folder + "offense.csv"

# make the property file
# input to property file: agencies, NIBRS_PROPERTY, NIBRS_incident, NIBRS_PROP_DESC, NIBRS_SUSPECTED_DRUG

property_file = proc_data_folder + "property.csv"

# make the victim file
# input to victim file: agencies, NIBRS_VICTIM, NIBRS_incident, NIBRS_OFFENSE_TYPE, NIBRS_VICTIM_CIRCUMSTANCES

