import numpy as np
import pandas as pd

excel_file_1 = pd.ExcelFile('sample.xlsx')

print(excel_file_1.sheet_names)

dataframe1 = excel_file_1.parse('Sheet1')
print(dataframe1)