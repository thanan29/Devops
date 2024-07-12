import pandas as pd
import numpy as np
import re
df=pd.read_csv("BL-Flickr-Images-Book.csv")
columns_to_drop=['Edition Statement','Corporate Author','Corporate Contributors','Former owner','Engraver','Contributors','Issuance type','Shelfmarks']
df.drop(columns=columns_to_drop,inplace=True)
df.set_index('Identifier',inplace=True)
df['Date of Publication']=df['Date of Publication'].str.extract(r'^(\d{4})',expand=False)
df['Place of Publication']=np.where(df['Place of Publication'].str.contains('London'),'London',df['Place of Publication'])
df['Place of Publication']=np.where(df['Place of Publication'].str.contains('Oxford'),'Oxford',df['Place of Publication'])
print(df.head())