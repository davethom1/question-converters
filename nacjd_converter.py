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

victim_file = proc_data_folder + "victim.csv"

# make the offender file
# input to offender file: agencies, nibrs_offender, nibrs_incident

offender_file = proc_data_folder + "offender.csv"

# make the arrestee file
# input to arrestee: agencies, NIBRS_ARRESTEE, NIBRS_incident, NIBRS_ARRESTEE_WEAPON

arrestee_file = proc_data_folder + "arrestee.csv"

# make the group B file
# input to group B: agencies, nibrs_incident, NIBRS_ARRESTEE, NIBRS_OFFENSE, NIBRS_WEAPON

groupb_file = proc_data_folder + "groupb.csv"

# make the cleared file
#input to cleared: agencies, NIBRS_incident, NIBRS_OFFENSE

cleared_file = proc_data_folder + "cleared.csv"

# make the recover file
# input to recover: agencies, NIBRS_incident, NIBRS_PROPERTY, NIBRS_PROP_DESC, NIBBRS_SUSPECTED_DRUG, NIBRS_OFFENSE

recover_file = proc_data_folder + "recover.csv"

# make the win_arrest file
# input to win_arrest: agencies, NIBRS_incident, NIBRS_ARRESTEE, NIBRS_ARRESTEE_WEAPON

win_arrest_file = proc_data_folder + "win_arrest.csv"
