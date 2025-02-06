import pandas as pd
# Paths to the Parquet files
test_file_path = 'test-0000-of-00001.parquet'
validation_file_path = 'validation-0000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Paths to the Excel files you want to create
output_test_excel_path = 'test_data.xlsx'
output_validation_excel_path = 'validation_data.xlsx'
# Convert DataFrames to Excel files
test_df.to_excel(output_test_excel_path, index=False)
validation_df.to_excel(output_validation_excel_path, index=False)
print(f"Test data has been exported to {output_test_excel_path}")
print(f"Validation data has been exported to {output_validation_excel_path}")