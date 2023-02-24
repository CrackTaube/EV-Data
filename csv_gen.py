import pandas as pd
import numpy as np


df = pd.read_csv(r"C:\Users\kroherl\Documents\EV-Data\small_daimler.csv")

df['topics'] = np.random.choice(['power plant', 'esg', 'car', 'germany', 'green future'], len(df))


df.to_csv(r"C:\Users\kroherl\Documents\EV-Data\small_test_data_sentiment.csv")
