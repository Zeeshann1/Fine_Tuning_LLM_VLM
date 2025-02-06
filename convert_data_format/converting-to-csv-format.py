import pandas as pd
# Paths to the Parquet files
test_file_path = 'test-00000-of-00001.parquet'
validation_file_path = 'validation-00000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Paths to the CSV files you want to create
output_test_csv_path = 'test_data.csv'
output_validation_csv_path = 'validation_data.csv'
# Convert DataFrames to CSV files
test_df.to_csv(output_test_csv_path, index=False)
validation_df.to_csv(output_validation_csv_path, index=False)
print(f"Test data has been exported to {output_test_csv_path}")
print(f"Validation data has been exported to {output_validation_csv_path}")