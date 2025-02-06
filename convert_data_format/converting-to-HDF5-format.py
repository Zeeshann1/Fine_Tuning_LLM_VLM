import pandas as pd
# Paths to the Parquet files
test_file_path = 'test-0000-of-00001.parquet'
validation_file_path = 'validation-0000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Paths to the HDF5 files you want to create
output_test_hdf5_path = 'test_data.h5'
output_validation_hdf5_path = 'validation_data.h5'
# Convert DataFrames to HDF5 files
test_df.to_hdf(output_test_hdf5_path, key='test', mode='w')
validation_df.to_hdf(output_validation_hdf5_path, key='validation', mode='w')
print(f"Test data has been exported to {output_test_hdf5_path}")
print(f"Validation data has been exported to {output_validation_hdf5_path}")