import pandas as pd


# Loading the CSV files
package_delivery_info = pd.read_csv('cleaned_package_delivery_info.csv')
transaction_info = pd.read_csv('cleaned_transaction_info.csv')
user_info = pd.read_csv('cleaned_user_info.csv')

# Get user_id values from each dataset
user_ids_user_info = set(user_info['user_id'])
user_ids_transaction_info = set(transaction_info['user_id'])
user_ids_package_info = set(package_delivery_info['user_id'])

# Check if all user_id values are the same across the three datasets
same_user_ids = user_ids_user_info == user_ids_transaction_info == user_ids_package_info

# Displaying the result
if same_user_ids:
    print("The user_id values are identical across all three datasets.")
else:
    print("There are differences in the user_id values across the datasets.")
    

#The user_id values are identical across all three datasets. So we can merge the datasets using the user_id column as the key (outer and inner joint in this case is equivalent).
# Loading the CSV files
package_delivery_info = pd.read_csv('cleaned_package_delivery_info.csv')
transaction_info = pd.read_csv('cleaned_transaction_info.csv')
user_info = pd.read_csv('cleaned_user_info.csv')

# First, merge user_info with transaction_info on 'user_id' using an outer join
merged_user_transaction = pd.merge(user_info, transaction_info, on='user_id', how='outer')

# Next, merge the resulting data with package_delivery_info using an outer join
merged_data_final = pd.merge(merged_user_transaction, package_delivery_info, on='user_id', how='outer')

# Display the final merged data
print(merged_data_final)

# Save the merged data to a new CSV file (optional)
merged_data_final.to_csv('merged_data_final.csv', index=False)


#This is the dataset (csv file) we will upload to the SQL database (representing its "release" to production).