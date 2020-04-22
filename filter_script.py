#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# specify paramter values -- this will be done in UI, and these will become empty lists or default args
COMPANIES = ['Bosch']
COUNTRIES = ['DE', 'NL']
POSITION_RANKS = ['Chief', 'Leader']


def get_latest_data():
    ''' Takes excel file with all linkedin contacts and returns a pandas dataframe
    '''
    
    # i leave this hardcoded for now, but should be fixed moving on
    df = pd.read_excel('200415 21h30 Pack 1 request on SO connections.xlsx', header=[1], index_col=[0]).reset_index(drop=True)
    
    # clean column names
    df.columns = df.columns.str.replace(' ', '')
    
    # extract country
    df['Country'] = df.Category.str[:2]

    # drop Category - as it contains no info anymore
    df = df.drop('Category', axis=1)

    # extract keywords from positions
    pos_ranks = ['Head', 'Director', 'Manager', 'Lead', 'Leader', 'Chief', 'MT', 'Expert', 'Consultant', 'Partner', 'President']

    # take only first element -- due to all "Head Directors"
    df['PositionRank'] = df.Position.str.split().map(lambda x: list(set(x) & set(pos_ranks)))
    df['PositionRank'] = df.PositionRank.map(lambda x: x[0] if x else 'Unknown')

    # TODO:
    # 1. Dutch titles (eg. Directeur)
    # 2. upper/lowercase
    # 3. NLP preprocess, remove brackets 

    return df


def filter_all_contacts():
    ''' This function ...
    
        Arguments ...
        
        Returns pandas dataframe (alt csv file)
    '''
    df = get_latest_data()

    return df[df.Company.isin(COMPANIES) & df.Country.isin(COUNTRIES) & df.PositionRank.isin(POSITION_RANKS)]



filter_all_contacts()


# In[ ]:




