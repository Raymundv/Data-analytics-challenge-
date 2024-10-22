import pandas as pd
#transaction_id,user_id,amount,timestamp,transaction_type
# Reading the transaction_info.csv file
df = pd.read_csv('transaction_info.csv')

# Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Check maximum and minimum user_id lenght
df['transaction_id_length'] = df['transaction_id'].apply(len)

#the maximum and minimum lengths
max_length = df['transaction_id_length'].max()
min_length = df['transaction_id_length'].min()

# Print the results
print(f"Maximum length of transaction_id: {max_length}")
print(f"Minimum length of transaction_id: {min_length}")
 
#The maximum and minimum lengths of the transaction_id column are 36 characters each. This suggests that the transaction_id field can be regarded as UUIDs (Universally Unique Identifiers) which are typically 36 characters long or VARCHAR(36)/CHAR(36) in SQL.

#Now for the user_id column
df['user_id_length'] = df['user_id'].apply(len)

# Find the maximum and minimum lengths for user_id
max_user_id_length = df['user_id_length'].max()
min_user_id_length = df['user_id_length'].min()

# Print the results for user_id
print(f"Maximum length of user_id: {max_user_id_length}")
print(f"Minimum length of user_id: {min_user_id_length}")

#Same results as for the transaction_id column. The user_id field can also be regarded as UUIDs (Universally Unique Identifiers) which are typically 36 characters long or VARCHAR(36) in SQL.

# Check for amount field
amount_dtype = df['amount'].dtype
print(f"Data type of the amount field: {amount_dtype}")


# Calculate the maximum number of characters before the period in the amount field
df['amount_before_period'] = df['amount'].astype(str).apply(lambda x: len(x.split('.')[0]))
max_chars_before_period = df['amount_before_period'].max()

# Print the result
print(f"Maximum number of characters before the period in the amount field: {max_chars_before_period}")
# Maximum number of characters before the period in the amount field: 3. Still, the amount field can be considered as DECIMAL(10,2) in SQL.


# Working with the timestamp field


# Convert the timestamp field to datetime format

from dateutil import parser
def convert_timestamp(ts):
    try:
        # Attempt to parse the timestamp using the flexible dateutil parser
        parsed_date = parser.parse(ts)
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')  # Uniform output format
    except (ValueError, TypeError):
        # Return NaT if parsing fails
        return pd.NaT
df = pd.read_csv('transaction_info.csv')

# Apply the conversion function to the 'timestamp' column
df['timestamp'] = df['timestamp'].apply(convert_timestamp)

print(df['timestamp'].head(15))



#Validating the timestamp format
import re

# Regex pattern for YYYY-MM-DD HH:MM:SS format
pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'

# Function to check if a timestamp matches the desired format
def check_format(ts):
    if pd.isna(ts):  # Ignore NaT or NaN values
        return False
    return bool(re.match(pattern, ts))

# Check which timestamps do not match the pattern
invalid_timestamps = df[~df['timestamp'].apply(check_format)]

# Optionally, count how many invalid timestamps there are
print(f"Number of invalid timestamps: {len(invalid_timestamps)}")


#Printing distinct values in the transaction_type column
distinct_transaction_types = df['transaction_type'].unique()
print(distinct_transaction_types)


#Printing duplicate values in the transaction_id column
df = pd.read_csv('transaction_info.csv')

# Find duplicate transaction_ids
duplicate_transaction_ids = df[df.duplicated('transaction_id', keep=False)]

# Print the duplicate transaction_ids
print("Duplicate transaction_ids found:")
print(duplicate_transaction_ids)

#The same issue as for the user_info.csv file: The same rows has duplicate keys.

#Check for duplicates in the user_id column

duplicate_user_ids = df[df.duplicated(subset='user_id', keep=False)]

# Display the rows with duplicate user_id
duplicate_user_ids

#Validating if these are full duplicate rows. 

# Read the data from the CSV file
df = pd.read_csv('transaction_info.csv')

# Find duplicate rows
duplicate_rows = df[df.duplicated(keep=False)]

# Print the duplicate rows
if not duplicate_rows.empty:
    print("Duplicate rows found:")
    print(duplicate_rows)
else:
    print("No duplicate rows found.")
#Same as in the user_info.csv file, the same rows are fully identical.

#With this information, I will drop the duplicate rows, work the timestamp column and save the cleaned data to a new CSV file.
# Drop duplicate rows and converting timestamp to datetime format

from dateutil import parser

# Function to convert timestamps to a uniform format
def convert_timestamp(ts):
    try:
        # Attempt to parse the timestamp using the flexible dateutil parser
        parsed_date = parser.parse(ts)
        return parsed_date.strftime('%Y-%m-%d %H:%M:%S')  # Uniform output format
    except (ValueError, TypeError):
        # Return NaT if parsing fails
        return pd.NaT

# Read the data from the CSV file
df = pd.read_csv('transaction_info.csv')

# Apply the conversion function to the 'timestamp' column
df['timestamp'] = df['timestamp'].apply(convert_timestamp)

# Print the first 15 converted timestamps
print(df['timestamp'].head(15))

# Drop duplicate rows (keeping the first occurrence)
df_cleaned = df.drop_duplicates()

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_transaction_info.csv', index=False)

print("Duplicate rows have been dropped and the cleaned data has been saved to 'cleaned_transaction_info.csv'")


