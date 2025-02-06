import pandas as pd
# Paths to the Parquet files
test_file_path = 'test-0000-of-00001.parquet'
validation_file_path = 'validation-0000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Paths to the JSON files you want to create
output_test_json_path = 'test_data.json'
output_validation_json_path = 'validation_data.json'
# Convert DataFrames to JSON files
test_df.to_json(output_test_json_path, orient='records', lines=True)
validation_df.to_json(output_validation_json_path, orient='records', lines=True)
print(f"Test data has been exported to {output_test_json_path}")
print(f"Validation data has been exported to {output_validation_json_path}")