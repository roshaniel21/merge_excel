import pandas as pd
import os

# Define the folder path where the Excel files are located
folder_path = r'C:\Users\DanielRP\Desktop\Erbil Logs'

# Prompt the user to input the file names
file1 = input("Enter the name of the first Excel file (with extension): ")
file2 = input("Enter the name of the second Excel file (with extension): ")

# Construct full file paths
file_path1 = os.path.join(folder_path, file1)
file_path2 = os.path.join(folder_path, file2)

# Load the Excel files
df1 = pd.read_excel(file_path1)
df2 = pd.read_excel(file_path2)

# Merge the two DataFrames
merged_df = pd.concat([df1, df2])

# Save the merged DataFrame to a new Excel file
output_file_path = os.path.join(folder_path, 'merged_file.xlsx')
merged_df.to_excel(output_file_path, index=False)

print("Files merged successfully! Merged file saved as 'merged_file.xlsx'")

