import pandas as pd

# Step 1: Read the Excel file
# Replace 'your_file.xlsx' with your actual file path
df = pd.read_excel('your_file.xlsx')

# Step 2: Create a mapping dictionary for each relationship
# For Pincode to District mapping
pincode_to_district = {}
# For District to Pincode mapping
district_to_pincode = {}

# Fill the dictionaries with valid pairs (where both pincode and district exist)
for index, row in df.dropna(subset=['Pincode', 'District']).iterrows():
    pincode = row['Pincode']
    district = row['District']
    pincode_to_district[pincode] = district
    district_to_pincode[district] = pincode

# Step 3: Fill in missing values
# Fill missing districts based on pincode
for index, row in df.iterrows():
    # If pincode exists but district is missing
    if pd.notna(row['Pincode']) and pd.isna(row['District']):
        if row['Pincode'] in pincode_to_district:
            df.at[index, 'District'] = pincode_to_district[row['Pincode']]
    
    # If district exists but pincode is missing
    elif pd.isna(row['Pincode']) and pd.notna(row['District']):
        if row['District'] in district_to_pincode:
            df.at[index, 'District'] = district_to_pincode[row['District']]

# Step 4: Save the updated dataframe to a new Excel file
df.to_excel('updated_data.xlsx', index=False)

print("Missing values have been filled successfully!")
