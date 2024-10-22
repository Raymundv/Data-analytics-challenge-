#Data exploration for the user_info.csv file
#------------------------------
# Importing the necessary libraries
import pandas as pd

# Loading the CSV file into a pandas DataFrame
df = pd.read_csv('user_info.csv')

# Creating a new column with the length of each user_id
df['user_id_length'] = df['user_id'].apply(len)

# The maximum and minimum lengths
max_length = df['user_id_length'].max()
min_length = df['user_id_length'].min()

# Print the results
print(f"Maximum length of user_id: {max_length}")
print(f"Minimum length of user_id: {min_length}")

#So the entries in the user_id column have a maximum length of 36 characters and a minimum length of 36 characters. This suggests that the user_id field may contain UUIDs (Universally Unique Identifiers) which are typically 36 characters long or CHAR(36) in SQL.

#Exploring the name field


# Creating a new column with the length of each name
df['name_length'] = df['name'].apply(len)

# the maximum and minimum lengths of the name column
max_length = df['name_length'].max()
min_length = df['name_length'].min()

# Print the results
print(f"Maximum length of name: {max_length}")
print(f"Minimum length of name: {min_length}")

#The entries in the name column have a maximum length of 26 characters and a minimum length of 3 characters. This suggests that the name field may be a VARCHAR(26) in SQL, as VARCHAR is used for variable-length strings. However, it will be set to a higher value to accommodate longer names.

#Exploring the email field


# Create a new column with the length of each email
df['email_length'] = df['email'].apply(len)

# Find the maximum and minimum lengths of the email column
max_length = df['email_length'].max()
min_length = df['email_length'].min()

# Print the results
print(f"Maximum length of email: {max_length}")
print(f"Minimum length of email: {min_length}")

print(df)
#The entries in the email column have a maximum length of 40 characters and a minimum length of 12 characters. This suggests that the email field may be a VARCHAR(40) in SQL, as VARCHAR is commonly used for email addresses.

#Exploring the join_date field

# Function to apply formatting only where necessary
def convert_date(date_str):
    try:
        # Try to parse the date using different formats
        return pd.to_datetime(date_str).strftime('%Y-%m-%d')
    except:
        return date_str  # Return the original if already in the correct format or if there's an error

# Apply the conversion function to the 'join_date' column
df['join_date'] = df['join_date'].apply(convert_date)

print(df['join_date'].head(25))



# Read the data from the CSV file

# Check for repeated values in the user_id column
repeated_user_ids = df[df.duplicated('user_id', keep=False)]

if not repeated_user_ids.empty:
    print("Repeated user_id values found:")
    print(repeated_user_ids[['user_id']])
else:
    print("No repeated user_id values found.")



#There are four rows with repeated user_id values: 
#The value for the user_id in row 0 matches with the one in row 10000, and the value in row 1 matches with the one in row 10001. 



#Let's explore further the rows with repeated user_id values to determine if they are exact duplicates or if there are differences in other columns.


# Set pandas display options to show all columns
pd.set_option('display.max_columns', None)

# Check for repeated rows across all columns
repeated_rows = df[df.duplicated(keep=False)]

if not repeated_rows.empty:
    print("Rows with repeated values across all columns found:")
    print(repeated_rows)
else:
    print("No repeated rows found.")

#The full rows mentioned above are exact duplicates (same value in all columns). This suggests that these rows can be removed from the dataset to ensure data integrity. 

# A last validation step is to check for any missing values in the dataset. This can be done by counting the number of missing values in each column.
df = pd.read_csv('user_info.csv')
missing_values = df.isnull().sum()

# Display the missing values for each column 
missing_values
#There are no missing values in the user_info.csv dataset.


# Now with all this information, I will clean the data in the user_info.csv file by standardizing the date format, removing duplicate rows, and writing the cleaned data to a new CSV file.


# Read the data from the CSV file (starting fresh)
df = pd.read_csv('user_info.csv')

# Function to standardize date formats
def convert_date(date_str):
    try:
        # Try to parse the date using different formats
        return pd.to_datetime(date_str).strftime('%Y-%m-%d')
    except:
        return date_str  # Return the original if already in the correct format or if there's an error

# Apply the conversion function to the 'join_date' column
df['join_date'] = df['join_date'].apply(convert_date)
# Apply the date standardization function


# Removing duplicate rows
df = df.drop_duplicates()

# Write the formatted and cleaned data to a new CSV file
df.to_csv('cleaned_user_info.csv', index=False, header=True)

print("Formatted and cleaned data has been written to 'cleaned_user_info.csv'")

# Check for repeated values in the user_id column
df_cleaned = pd.read_csv('cleaned_user_info.csv')

repeated_user_ids = df_cleaned[df_cleaned.duplicated('user_id', keep=False)]

if not repeated_user_ids.empty:
    print("Rows with repeated user_id values found:")
    print(repeated_user_ids)
else:
    print("No repeated user_id values found.")



#The cleaned data in the cleaned_user_info.csv file no longer contains repeated user_id values. This cleaned data can now be used for further analysis or merging with the other datasets.

