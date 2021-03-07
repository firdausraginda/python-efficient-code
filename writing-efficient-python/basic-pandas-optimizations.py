import pandas as pd
import numpy as np

baseball_df = pd.read_csv('./baseball_stats.csv')

def calc_win_perc(wins, games_played):
    """ To Calculate Win Percentage Using Win & Games_Played Numbers """
    win_perc = wins/games_played
    
    return np.round(win_perc,2)

# pandas looping using iloc ----------------------------------------
win_perc_list_iloc = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_perc_list_iloc.append(win_perc)

baseball_df['WP'] = win_perc_list_iloc

print(baseball_df.head())

# pandas looping using .iterrows() ----------------------------------------
win_perc_list_iterrows = []

for i, row in baseball_df.iterrows():
    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)
    win_perc_list_iterrows.append(win_perc)

baseball_df['WP'] = win_perc_list_iterrows

print(baseball_df.head())

# pandas looping using .itertuples() ----------------------------------------
win_perc_list_itertuples = []

for row_tuple in baseball_df.itertuples():
    wins = row_tuple.W
    games_played = row_tuple.G
    win_perc = calc_win_perc(wins, games_played)
    win_perc_list_itertuples.append(win_perc)

baseball_df['WP'] = win_perc_list_itertuples

print(baseball_df.head())

# pandas using .apply() to avoid looping ----------------------------------------
# .apply() is like map() function

win_perc_list_apply = baseball_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
baseball_df['WP'] = win_perc_list_apply
print(baseball_df.head())

# broadcasting (vectorizing) in pandas to avoid looping ----------------------------------------
win_perc_list_broadcast = np.round(baseball_df['W'].values / baseball_df['G'].values, 2)
baseball_df['WP'] = win_perc_list_broadcast
print(baseball_df.head())