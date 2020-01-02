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

# create agency dataframe
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

# merge agency and incident admin files to create a one to many file of agency ids to incidents
df_agency_incidents = pd.merge(df_agency_admin, df_incident_admin, on='AGENCY_ID')
print(df_agency_incidents.head())

# create a dataframe from agency and incident of variables agency (STATE_ID, ORI) and incident (INCIDENT_ID, INCIDENT_DATE)
# use this as the first four variables for all the data files
agency_incidents_cols = ["STATE_ID", "ORI", "INCIDENT_ID", "INCIDENT_DATE"]
df_agency_incidents_all = df_agency_incidents[agency_incidents_cols]
print(df_agency_incidents_all.head())


# create variable that counts instances of offense ID by Incidents
# df_offense = pd.read_csv(fbi_data_folder + "NIBRS_OFFENSE.csv")
# print(str(len(df_offense)) + "offenses by ID in this file")
# offense_cols = ["INCIDENT_ID", "OFFENSE_ID"]
# df_offense_admin = df_offense[offense_cols]
# print(df_offense_admin.head())
#
# # df_offense_admin["TOT_OFFENSE"] = df_offense_admin.groupby(["INCIDENT_ID"]).count("OFFENSE_ID")
# df_offense_admin_count["INCIDENT_ID"] = df_offense_admin["INCIDENT_ID"]
# df_offense_admin_count["OFFENSE_CT"] = df_offense_admin.value_counts("OFFENSE_ID")
# print(df_offense_admin_count.head(25))
# print(str(len(df_agency_incidents)) + " records when we merge agencies and incidents. Should match N-incidents above")

# create a list of column names to send SPSS

# save this file out to processed. It will be dataset 2 for curation.
# pyreadstat.write_sav(df_agency_incidents, proc_data_folder + "agency_incidents.sav", file_label="agency incidents")

# # make the offense file
# # inputs to offense file: agencies, NIBRS_OFFENSE, NIBRS_SUSPECT_USING, NIBRS_CRIMINAL_ACT, NIBRS_WEAPON, NIBRS_BIAS_MOTIVATION
#
offense_file = proc_data_folder + "offense.csv"

# create offense dataframe
df_offense = pd.read_csv(fbi_data_folder + "NIBRS_OFFENSE.csv")
print(str(len(df_offense)) + " offenses in this file")

# create a list of columns from offense file
offense_cols = ["INCIDENT_ID", "OFFENSE_ID", "ATTEMPT_COMPLETE_FLAG", "LOCATION_ID", "NUM_PREMISES_ENTERED",
                "METHOD_ENTRY_CODE"]
df_offense_offense = df_offense[offense_cols]
print(df_offense_offense.head())

# create suspect_using dataframe
df_suspect_using = pd.read_csv(fbi_data_folder + "NIBRS_SUSPECT_USING.csv")
print(str(len(df_suspect_using)) + " names of items suspect using in this file")

# create a list of columns from suspect_using file for ofeense data file
suspect_using_cols = ["OFFENSE_ID", "SUSPECT_USING_ID"]
df_suspect_using_offense = df_suspect_using[suspect_using_cols]
print(df_suspect_using_offense.head())

# create criminal_act dataframe
df_criminal_act = pd.read_csv(fbi_data_folder + "NIBRS_CRIMINAL_ACT.csv")
print(str(len(df_criminal_act)) + " criminal acts connected to offense ID in this file")

# create a list of columns from criminal_act for offense file
criminal_act_cols = ["OFFENSE_ID", "CRIMINAL_ACT_ID"]
df_criminal_act_offense = df_criminal_act[criminal_act_cols]
print(df_criminal_act_offense.head())

# use df_agency_admin dataframe

# # merge agency and offense files to create a one to many file of agency ids to incidents
# df_agency_incidents = pd.merge(df_agency_admin, df_offense_offense, on='AGENCY_ID')
# print(df_agency_incidents.head())


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
