import pandas as pd

# Load Excel file
df = pd.read_excel("your_file.xlsx")

# Create a reference mapping of known pincode-district pairs
mapping = df.dropna().drop_duplicates(subset=["pincode", "district"]).set_index("pincode")["district"].to_dict()

# Fill missing district using pincode
df["district"] = df.apply(
    lambda row: mapping.get(row["pincode"], row["district"]) if pd.isna(row["district"]) else row["district"],
    axis=1
)

# Also, create reverse mapping to fill missing pincode using district
reverse_mapping = df.dropna().drop_duplicates(subset=["district", "pincode"]).set_index("district")["pincode"].to_dict()

# Fill missing pincode using district
df["pincode"] = df.apply(
    lambda row: reverse_mapping.get(row["district"], row["pincode"]) if pd.isna(row["pincode"]) else row["pincode"],
    axis=1
)

# Save back to Excel
df.to_excel("cleaned_file.xlsx", index=False)
