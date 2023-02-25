import pandas as pd
import numpy as np


df_1 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_BMW.csv")
df_2 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_Daimler.csv")
df_3 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_Tesla.csv")

df_1 = df_1.head(1000)
df_2 = df_2.head(1000)
df_3 = df_3.head(1000)

df =  pd.concat([df_1, df_2, df_3])

df['topics'] = np.random.choice(['power plant', 'esg', 'car', 'germany', 'green future'], len(df))

for index, row in df.iterrows():
    if row.Company == 'BMW':
        row["Company"] = "BMW.DE"
    elif row.Company == 'Daimler':
        row["Company"] = "MBG.DE"
    else:
        row["Company"] = "TSLA"
df.info()

df.to_csv(r"C:\Users\kroherl\Documents\EV-Data\small_test_data.csv")
