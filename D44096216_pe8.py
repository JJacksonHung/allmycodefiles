import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def highest_win_loss_pct(data):
    highest_pct_teams = data.loc[data.groupby('Conference')['PCT'].idxmax()]
    return highest_pct_teams[['Conference', 'Team', 'PCT']]

def average_points_scored(data):
    average_pf = data.groupby('Conference')['PF'].mean()
    return average_pf

def better_away_than_home(data):
    better_away = data[data['Away'].str.split('-').apply(lambda x: int(x[0]) > int(x[1])) & 
                       data['Home'].str.split('-').apply(lambda x: int(x[0]) < int(x[1]))]
    count_better_away = better_away.groupby('Conference').size()
    return count_better_away

def main():
    file_path = 'pe8_data.csv'
    data = load_data(file_path)
    
    if data is not None:
        # Convert percentage string to float
        data['PCT'] = data['PCT'].str.rstrip('%').astype('float') / 100.0
        
        # Answer question 1
        highest_pct_teams = highest_win_loss_pct(data)
        print("Teams with the highest win-loss percentage in each conference:")
        print(highest_pct_teams)
        print()
        
        # Answer question 2
        average_pf = average_points_scored(data)
        print("Average points scored (PF) by the teams in each conference:")
        print(average_pf)
        print()
        
        # Answer question 3
        count_better_away = better_away_than_home(data)
        print("Number of teams with a better away record than home record in each conference:")
        print(count_better_away)
    else:
        print("Data loading failed.")

if __name__ == "__main__":
    main()

