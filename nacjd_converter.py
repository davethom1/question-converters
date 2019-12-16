# Overview
# Goal: Produce eleven different CSV files that contain data from multiple CSV files at the FBI.
# Mapping for sources to file is available in docs/MappingExcel.

import pandas as pd
import pyreadstat
import numpy as np

# set common variables. These are the folders that will store the input and output files.
fbi_data_folder = "data/raw/"
proc_data_folder = "data/processed/"

# make the admin file
# inputs to admin file: agencies, nibrs_incident
# load input files
# look for relevant columns
# store data
# place data in file in appropriate location in new file

admin_file = proc_data_folder + "admin.csv"

# create agendy dataframe
df_agency = pd.read_csv(fbi_data_folder + "agencies.csv")

# make dataframe with just admin info (agency_id, state_id, and ori [original TKTK])
#create reusable list for agency columns
admin_cols = ["AGENCY_ID", "STATE_ID", "ORI"]
df_agency_admin = df_agency[admin_cols]
print(df_agency_admin.head())

# make incident dataframe
df_incident = pd.read_csv(fbi_data_folder + "NIBRS_incident.csv")
print(str(len(df_incident)) + " incidents in this file")
#create a list of columns from incident file
incident_cols = ["AGENCY_ID", "INCIDENT_ID", "INCIDENT_DATE", "REPORT_DATE_FLAG", "INCIDENT_HOUR", "CLEARED_EXCEPT_ID",
                 "CLEARED_EXCEPT_DATE", "CARGO_THEFT_FLAG"]
df_incident_admin = df_incident[incident_cols]
print(df_incident_admin.head())

#merge agency and incident admin files to create a one to many file of agency ids to incidents
df_agency_incidents = pd.merge(df_agency_admin, df_incident_admin, on='AGENCY_ID')
print(df_agency_incidents.head())

print(str(len(df_agency_incidents)) + " records when we merge agencies and incidents. Should match N-incidents above")

# create a list of column names to send SPSS

#save this file out to processed. It will be dataset 2 for curation.
pyreadstat.write_sav(df_agency_incidents, proc_data_folder + "agency_incidents.sav", file_label="agency incidents")

# # make the offense file
# # inputs to offense file: agencies, NIBRS_OFFENSE, NIBRS_SUSPECT_USING, NIBRS_CRIMINAL_ACT, NIBRS_WEAPON, NIBRS_BIAS_MOTIVATION
#
# offense_file = proc_data_folder + "offense.csv"
#
# # make the property file
# # input to property file: agencies, NIBRS_PROPERTY, NIBRS_incident, NIBRS_PROP_DESC, NIBRS_SUSPECTED_DRUG
#
# property_file = proc_data_folder + "property.csv"
#
# # make the victim file
# # input to victim file: agencies, NIBRS_VICTIM, NIBRS_incident, NIBRS_OFFENSE_TYPE, NIBRS_VICTIM_CIRCUMSTANCES
#
# victim_file = proc_data_folder + "victim.csv"
#
# # make the offender file
# # input to offender file: agencies, nibrs_offender, nibrs_incident
#
# offender_file = proc_data_folder + "offender.csv"
#
# # make the arrestee file
# # input to arrestee: agencies, NIBRS_ARRESTEE, NIBRS_incident, NIBRS_ARRESTEE_WEAPON
#
# arrestee_file = proc_data_folder + "arrestee.csv"
#
# # make the group B file
# # input to group B: agencies, nibrs_incident, NIBRS_ARRESTEE, NIBRS_OFFENSE, NIBRS_WEAPON
#
# groupb_file = proc_data_folder + "groupb.csv"
#
# # make the cleared file
# #input to cleared: agencies, NIBRS_incident, NIBRS_OFFENSE
#
# cleared_file = proc_data_folder + "cleared.csv"
#
# # make the recover file
# # input to recover: agencies, NIBRS_incident, NIBRS_PROPERTY, NIBRS_PROP_DESC, NIBBRS_SUSPECTED_DRUG, NIBRS_OFFENSE
#
# recover_file = proc_data_folder + "recover.csv"
#
# # make the win_arrest file
# # input to win_arrest: agencies, NIBRS_incident, NIBRS_ARRESTEE, NIBRS_ARRESTEE_WEAPON
#
# win_arrest_file = proc_data_folder + "win_arrest.csv"
