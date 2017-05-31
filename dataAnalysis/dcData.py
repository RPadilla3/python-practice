import pandas as pd

dcData = pd.read_csv('../../../Rodolfo/Desktop/dc-parking-data-node/data/moving_april_2016.csv')

dcData.drop([33, 34], axis=0, inplace=True)

print(dcData.head(50))
