import pandas as pd
# Paths to the Parquet files
test_file_path = 'test-0000-of-00001.parquet'
validation_file_path = 'validation-0000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Paths to the Feather files you want to create
output_test_feather_path = 'test_data.feather'
output_validation_feather_path = 'validation_data.feather'
# Convert DataFrames to Feather files
test_df.to_feather(output_test_feather_path)
validation_df.to_feather(output_validation_feather_path)
print(f"Test data has been exported to {output_test_feather_path}")
print(f"Validation data has been exported to {output_validation_feather_path}")