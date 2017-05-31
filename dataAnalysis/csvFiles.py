import pandas as pd

df = pd.read_csv('../../../Rodolfo/Desktop/csvFiles/FRED-NROU.csv')

print(df.VALUE.mean())
