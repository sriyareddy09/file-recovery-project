import pandas as pd

# Load CSV
df = pd.read_csv("testfolder_report.csv")

# Preview columns and sample data to confirm
print(df.columns)
print(df['Flags(Dir)'].head(10))

# Filter rows where 'Flags(Dir)' contains any of the keywords
filter_pattern = "unallocated|orphan|deleted"
deleted_files = df[df['Flags(Dir)'].str.contains(filter_pattern, case=False, na=False)]

# Optional: further filter by file extension, e.g., only files with extension 'txt'
# deleted_files = deleted_files[deleted_files['Extension'] == 'txt']

# Save filtered rows
deleted_files.to_csv("deleted_files_filtered.csv", index=False)

print(f"Filtered {len(deleted_files)} rows saved to 'deleted_files_filtered.csv'")
