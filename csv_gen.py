import pandas as pd
import numpy as np


df_1 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_BMW.csv")
df_2 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_Daimler.csv")
df_3 = pd.read_csv(r"C:\Users\kroherl\OneDrive - Haufe Group\Documents\3_Mine\20_Code\Twitter_API_NLP\data\translated_ev\done\sentiment_Tesla.csv")

df_new = pd.concat([df_1, df_2, df_3])

df_new['topics'] = np.random.choice(['power plant', 'esg', 'car', 'germany', 'green future'], len(df_new))


df_new.to_csv(r"C:\Users\kroherl\Documents\EV-Data\test_all_data_sentiment.csv")
