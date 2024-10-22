import pandas as pd
from dateutil import parser

# Reading the data from the CSV file
df = pd.read_csv('package_delivery_info.csv')

# Calculate the length of each package_id
df['package_id_length'] = df['package_id'].apply(len)

# Finding the maximum and minimum length of the package_id column
max_length = df['package_id_length'].max()
min_length = df['package_id_length'].min()

print(f"Maximum length of package_id: {max_length}")
print(f"Minimum length of package_id: {min_length}")
#REsult is 36 and 36 for the maximum and minimum length values in the package_id column. This suggest that the package_id field can be regarded as UUIDs (Universally Unique Identifiers) which are typically 36 characters long or VARCHAR(36)/CHAR(36) in SQL.

#For the courier column


# Read the data from the CSV file
df = pd.read_csv('package_delivery_info.csv')

# Find the distinct values in the courier field
distinct_couriers = df['courier'].unique()

print("Distinct values in the courier field:")
for courier in distinct_couriers:
    print(courier)


#the entries are case sensitive, but represent the same carrier. We can clean this up by converting all entries to uppercase and removing any leading/trailing spaces.
#Cleaning and homologating the carriers. 


# Read the data from the CSV file
df = pd.read_csv('package_delivery_info.csv')

# Transform the courier column to uppercase and remove leading/trailing spaces
df['courier'] = df['courier'].str.upper().str.strip()

# Print the transformed DataFrame to verify the changes
print(df[['courier']].head())




#delivery date homologation 
def convert_timestamp(ts):
    try:
        # Attempt to parse the time using the flexible dateutil parser
        parsed_date = parser.parse(ts)
        return parsed_date.strftime('%Y-%m-%d')  # Only output the date part
    except (ValueError, TypeError):
        # Return NaT if parsing fails
        return pd.NaT

df = pd.read_csv('package_delivery_info.csv')
# Apply the conversion function to the 'delivery_date' column
df['delivery_date'] = df['delivery_date'].apply(convert_timestamp)

print(df['delivery_date'])

#for the delivery status identifying the distinct values in the delivery_status field

distinct_delivery_status = df['delivery_status'].unique()
print("Distinct values in the delivery_status field:")
for status in distinct_delivery_status:
    print(status)
#results Delivered
#In Transit
#Pending
#Lost

#Finally for the user_id field

# Read the data from the CSV file
df = pd.read_csv('package_delivery_info.csv')

# Calculate the length of each user_id
df['user_id_length'] = df['user_id'].apply(len)

# Find the maximum and minimum length of the user_id column
max_length = df['user_id_length'].max()
min_length = df['user_id_length'].min()

print(f"Maximum length of user_id: {max_length}")
print(f"Minimum length of user_id: {min_length}")

#The same result as for the package_id. The user_id field can also be regarded as UUIDs (Universally Unique Identifiers) which are typically 36 characters long or VARCHAR(36) in SQL.
#I will test if there 
#producing a csv file with the cleaned data. 



# Function to convert timestamps to a uniform date format
def convert_timestamp(ts):
    try:
        # Attempt to parse the time using the flexible dateutil parser
        parsed_date = parser.parse(ts)
        return parsed_date.strftime('%Y-%m-%d')  # Only output the date part
    except (ValueError, TypeError):
        # Return NaT if parsing fails
        return pd.NaT

# Read the data from the CSV file
df = pd.read_csv('package_delivery_info.csv')

# Transform the courier column to uppercase and remove leading/trailing spaces
df['courier'] = df['courier'].str.upper().str.strip()

# Print the transformed DataFrame to verify the changes
print(df[['courier']].head())

# Apply the conversion function to the 'delivery_date' column
df['delivery_date'] = df['delivery_date'].apply(convert_timestamp)

# Print the transformed delivery_date column to verify the changes
print(df['delivery_date'].head())

# Find duplicate rows
duplicate_rows = df[df.duplicated(keep=False)]

# Print the duplicate rows
if not duplicate_rows.empty:
    print("Duplicate rows found:")
    print(duplicate_rows)
else:
    print("No duplicate rows found.")

# Drop duplicate rows (keeping the first occurrence)
df_cleaned = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_package_delivery_info.csv', index=False)

print("Duplicate rows have been dropped and the cleaned data has been saved to 'cleaned_package_delivery_info.csv'")

#Validating if the cleaned data has repited values for the keys user_id, and package_id)

package_delivery_df = pd.read_csv('cleaned_package_delivery_info.csv')

# Check for duplicates based on both user_id and package_id
duplicate_user_id = package_delivery_df[package_delivery_df.duplicated(subset=['user_id'], keep=False)]

# Display the rows with duplicated user_id and package_id combinations
duplicate_user_id

duplicate_package_id = package_delivery_df[package_delivery_df.duplicated(subset=['package_id'], keep=False)]
duplicate_package_id

#So there are not duplicates in the keys. The data is cleaned and ready for further analysis. 







