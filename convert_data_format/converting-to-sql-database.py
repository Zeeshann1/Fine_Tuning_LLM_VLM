import pandas as pd
from sqlalchemy import create_engine
# Paths to the Parquet files
test_file_path = 'test-0000-of-00001.parquet'
validation_file_path = 'validation-0000-of-00001.parquet'
# Read the Parquet files into DataFrames
test_df = pd.read_parquet(test_file_path)
validation_df = pd.read_parquet(validation_file_path)
# Create an SQLite engine
engine = create_engine('sqlite:///my_database.db')
# Write DataFrames to SQL tables
test_df.to_sql('test_table', con=engine, if_exists='replace', index=False)
validation_df.to_sql('validation_table', con=engine, if_exists='replace', index=False)
print("Data has been exported to the SQL database")