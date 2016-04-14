import pandas as pd
import os

def get_award_data_dir():
    '''
    Quick function to leverage os functions to identify the base 'data'
    directory, for use in the subsequent explicit directory pulls
    '''
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    DATA_DIR = os.path.abspath(os.path.join(CURRENT_DIR, 'data'))
    return os.path.join(DATA_DIR, 'awards')

def load_award_data():
    award_file = os.path.abspath(os.path.join(get_award_data_dir(),'academy_awards.csv'))
    with open(award_file, 'r') as csv_file:
        award_data = pd.read_csv(csv_file)

    return award_data

def award_categories():
    major_award_categories = ['Directing',
                          'Best Picture',
                          'Actress -- Leading Role',
                          'Actor -- Leading Role',
                         'Cinematography']
    return major_award_categories

def clean_raw_award_data(award_df):
    return award_df[['Year','Category','Nominee','Additional Info','Won?']]

def clean_updated_award_df(award_df):
    new_df = award_df[['Film','Year_Num','Category','NO','YES','Nominee']]
    new_df.rename(columns={'Year_Num' : 'Year'}, inplace=True )
    return new_df

def restrict_to_major_awards(award_df):
    return award_df[award_df['Category'].isin(award_categories())].reset_index()

def add_result_flags(award_df):
    winners = pd.get_dummies(award_df['Won?'])
    return pd.concat([award_df,winners],axis=1)

def film_from_additional(row):
     # add a "Film" column to df
    additional_info_txt = row['Additional Info']
    text_info = str(additional_info_txt)
    film = text_info.split('{')
    film_txt = film[0].strip()
    return film_txt

def nominee_is_film(row):
    nominee_txt = row['Nominee']
    return nominee_txt.strip()

def get_category_functions():
    '''
    Each of the functions that are the values must be defined above this!
    '''
    return {'Actor -- Leading Role':film_from_additional,
                 'Actress -- Leading Role':film_from_additional,
                 'Cinematography':nominee_is_film,
                 'Directing':nominee_is_film,
                 'Best Picture':nominee_is_film}

def get_film(df_row):
    cat_functions = get_category_functions()
    return cat_functions[df_row.Category](df_row)

def add_film_name_to_df(award_df):
    award_df['Film'] = award_df.apply(get_film, axis=1)
    return award_df

def get_year_num(df_row):
    if ' ' in df_row['Year']:
        year_txt = df_row['Year'].split(' ')
    else:
        year_txt = None
    return year_txt[0]

def add_clean_year_to_df(award_df):
    award_df['Year_Num'] = award_df.apply(get_year_num, axis=1)
    return award_df



def get_awards_data():
     raw_data = load_award_data()
     clean_raw_data = clean_raw_award_data(raw_data)
     major_award_data = restrict_to_major_awards(clean_raw_data)
     major_awards_with_results = add_result_flags(major_award_data)
     major_with_film = add_film_name_to_df(major_awards_with_results)
     major_with_film_and_year = add_clean_year_to_df(major_with_film)
     final_award_data = clean_updated_award_df(major_with_film_and_year)
     print "Award data contains " + str(len(final_award_data))
     return final_award_data
