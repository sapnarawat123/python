# Import the os module
import os

# Get the current working directory
print("Current working directory:", os.getcwd())

# Check the environment variables
print("Environment variables:", os.environ)

# EXAMPLE---
# Import the string module
import string

# Print all ASCII lowercase characters
print(string.ascii_lowercase)

# Print all punctuation
print(string.punctuation)

# example-
# Import pandas as pd
import pandas as pd

# Convert sales to a pandas DataFrame
sales_df = pd.DataFrame(sales)

# Preview the first few rows
print(sales_df.head())