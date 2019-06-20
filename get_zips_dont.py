import pandas as pd

zipcode_df = pd.read_csv('data/free-zipcode-database.csv')
#print(zipcode_df.columns)

zips_IL = zipcode_df[zipcode_df['State'] == 'IL']['Zipcode']

zips_IL = zips_IL.drop_duplicates()

zips_IL.columns = ['zipcode']

zips_IL.to_csv('data/zips.csv', index=False)








