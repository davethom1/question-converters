# Qualtrics Converter

The code in this repo converts a Qualtrics survey export file (*.qsf) to an ICPSR question text file (*.txt*).

# Motivation

Including question text in the documentation for studies helps users understand the data and make decisions about whether to reuse it, but generating question text is time-consuming. This code should help reduce the labor required to generate question text for surveys originally depoloyed on Qualtrics.

# Examples

## Qualtrics Export

See [Open_Data_Flint_Revised_Pilot.qsf](Open_Data_Flint_Revised_Pilot.qsf) for an example Qualtrics export file. It's JSON though they use a different file extension--`.qsf`. Here's an example section from one question:

```
{
      "SurveyID": "SV_8v79iA9BlgTnAnH",
      "Element": "SQ",
      "PrimaryAttribute": "QID7",
      "SecondaryAttribute": "Do you use similar websites or resources to accomplish the objectives you have in using Open Data...",
      "TertiaryAttribute": null,
      "Payload": {
        "QuestionText": "Do you use similar websites or resources to accomplish the objectives you have in using Open Data Flint?",
        "DefaultChoices": false,
        "DataExportTag": "Similar",
        "QuestionID": "QID7",
        "QuestionType": "MC",
        "Selector": "SAVR",
        "SubSelector": "TX",
        "DataVisibility": {
          "Private": false,
          "Hidden": false
        },
        "Configuration": {
          "QuestionDescriptionOption": "UseText"
        },
        "QuestionDescription": "Do you use similar websites or resources to accomplish the objectives you have in using Open Data...",
        "Choices": {
          "1": {
            "Display": "Yes"
          },
          "2": {
            "Display": "No"
          }
        },
        "ChoiceOrder": [
          1,
          2
        ],
        "Validation": {
          "Settings": {
            "ForceResponse": "ON",
            "ForceResponseType": "ON",
            "Type": "None"
          }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 3,
        "NextAnswerId": 1
      }
    },
```

## ICPSR Question Text

Here's an exerpt from the [Longitudinal Study of the Second Generation in Spain (ILSEG)](https://www.icpsr.umich.edu/icpsrweb/ICPSR/studies/36286):

```
path         = .
title        = Longitudinal Study of the Second Generation in Spain (ILSEG), Public Use Data
charset      = Windows-1252
records/case = 1
*
name = V4
text = 
What is the name of your school?                            
*
name = V5
text = 
What grade are you in?                              
*
name = V6
text = 
What is your sex?
```
# Credits

## Author

David Thomas (davethom@umich.edu)