import pandas as pd
import os


import logging
# Initializing a logger
logger = logging.getLogger(__name__)

# read in the dataset
def get_data_dir():
    '''
    Quick function to leverage os functions to identify the base 'data'
    directory, for use in the subsequent explicit directory pulls
    '''
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(CURRENT_DIR, 'data'))

def get_mojo_dir():
    ''' Grab the directory path containing the mojo data json stuff
    '''
    return os.path.join(get_data_dir(), 'boxofficemojo')

def get_metacritic_dir():
    ''' Grab the directory path containing the metacritic data json stuff
    '''
    return os.path.join(get_data_dir(), 'metacritic')

def get_movies(aDir):
    import os, json
    file_contents = os.listdir(aDir)

    movie_list = []

    for filename in file_contents:
        filepath = os.path.join(aDir, filename)

        with open(filepath, 'r') as movie_file:
            movie_data = json.load(movie_file)
        if hasattr(movie_data, "keys"): # type(movie_data) == dict:
            movie_list.append(movie_data)
    logger.info("Pulled", str(len(movie_list)), " items from", filepath)

    return movie_list

def load_mojo_data():
    return pd.DataFrame(get_movies(get_mojo_dir()))

def load_metacritic_data():
    return pd.DataFrame(get_movies(get_metacritic_dir()))

def clean_mojo_data(input_df):
    input_df.loc[:,'box_flag'] = 1
    input_df['year']=input_df['year'].fillna(0)
    input_df['year']=input_df['year'].astype(int)
    input_df['key'] = input_df['mojo_slug'].str.cat(input_df['year'].values.astype(str))
    return input_df

def clean_metacritic_data(input_df):
    input_df['title1']=input_df['title'].fillna('z')
    input_df['title1'] = map(lambda x: x.lower(), input_df['title1'])
    input_df.loc[:,'mojo_slug']=input_df['title1'].str.replace(' ', '')
    input_df['mojo_slug']=input_df['mojo_slug'].str.replace('.', '')
    input_df['mojo_slug']=input_df['mojo_slug'].str.replace(',', '')
    input_df=input_df.drop('title1', axis=1)

    input_df['year']=input_df['year'].fillna(0)

    input_df['key'] = input_df['mojo_slug'].str.cat(input_df['year'].values.astype(str))

    return input_df

def get_combined_movie_data():
    mojo = load_mojo_data()
    mojo_clean = clean_mojo_data(mojo)
    critic = load_metacritic_data()
    critic_clean = clean_metacritic_data(critic)
    comb_data = movies_crictics_df=pd.merge(mojo_clean, critic_clean, on=('key'), how='outer')
    return comb_data
