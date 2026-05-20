"""
Test script to load and inspect survey data
"""

from data_ingestion import load_survey

# Load the sample survey
print("=" * 60)
print("TESTING CSV READER")
print("=" * 60)
print()

# Load the survey data
data = load_survey('data/raw/sample_survey.csv')

# If data loaded successfully, show some information
if data is not None:
 print()
 print("=" * 60)
 print("DATA INSPECTION")
 print("=" * 60)
 print()
 
 # Show the first 3 rows
 print(" First 3 responses:")
 print(data.head(3))
 print()
 
 # Show column names
 print(" Survey Questions (Column Names):")
 for i, column in enumerate(data.columns, 1):
 print(f" {i}. {column}")
 print()
 
 # Show data types
 print(" Data Types:")
 print(data.dtypes)
 print()
 
 # Show basic statistics for numerical columns
 print(" Quick Statistics:")
 print(data.describe())
 print()
 
 print(" Test completed successfully!")
else:
 print(" Failed to load data!")