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
# load input files
# look for relevant columns
# store data
# place data in file in appropriate location in new file

admin_file = proc_data_folder + "admin.csv"
# create dataframe
df1 = pandas.read_csv(fbi_data_folder + "agencies.csv", index_col = 'YEARLY_AGENCY_ID')

# grab state_id and ori
df.get (["STATE_ID", "ORI"])

# grab state_id and ori along with agency_id by index number
df1admin = df1.iloc[:, [14, 2]]


#print (df1admin)

#check type of newly created dataframe
print(type(df1admin))


df2 = pandas.read_csv(fbi_data_folder + "NIBRS_incident.csv", index_col = 'DATA_YEAR')

# select "AGENCY_ID", "INCIDENT_ID", "INCIDENT_DATE", "REPORT_DATE_FLAG", "INCIDENT_HOUR", "CLEARED_EXCEPT_ID", "CLEARED_EXCEPT_DATE", "CARGO_THEFT_FLAG"
df2admin = df2.iloc[:, [1, 5, 6, 7, 8, 9, 10, 3]]

# print (df2admin)

# check type of newly created dataframe
print(type(df2admin))

# sort dataframe by AGENCY_ID
df2admin.sort_values(["AGENCY_ID"], ascending=True)

# concatenate df1admin with df2admin
# Key variable is AGENCY_ID

dfadmin = pandas.merge(df1admin, df2admin, how='inner', on=['AGENCY_ID'])
print(dfadmin)
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
