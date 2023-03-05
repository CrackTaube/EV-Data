import pandas as pd

df = pd.read_csv(r'C:\Users\kroherl\Documents\Data - Folder not Git\label_all.csv')

def split_df_by_company(df, company_column_name):
    # Get the unique company names from the specified column
    unique_companies = df[company_column_name].unique()
    
    # Initialize an empty dictionary to store the split DataFrames
    split_dfs = {}
    
    # Loop through the unique company names
    for company in unique_companies:
        # Get the DataFrame for the current company
        company_df = df[df[company_column_name] == company]
        
        # Save the DataFrame as a CSV file in the output directory
        filename = f'{company}.csv'
        filepath = f'C:/Users/kroherl/Documents/Data/EV-Data/{filename}'
        company_df.to_csv(filepath, index=False)
        
        # Add the DataFrame to the dictionary of split DataFrames
        split_dfs[company] = company_df
    
    return split_dfs

if __name__ == '__main__':
    split_df_by_company(df, 'Company')