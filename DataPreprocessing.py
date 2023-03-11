
import pandas as pd
import numpy as np




df_seed = pd.read_csv('Data/MNCAATourneySeeds.csv')
df_teams = pd.read_csv('Data/MTeams.csv')
df_teams['tm_join'] = df_teams.TeamName.apply(lambda x: x.replace('St','State'))

#get 2023 data & join seed w/ team names
df_s_2023 = df_seed[df_seed['Season'] == 2023]
seed_tms = pd.merge(df_s_2023, df_teams.loc[:,['TeamID','TeamName','tm_join']], on='TeamID')



df_elo = pd.read_html('https://www.warrennolan.com/basketball/2023/elo')[0]

df_elo_final = df_elo.loc[:,['Team','ELO']]
df_elo_final.head()

seed_elos = pd.merge(seed_tms,df_elo_final, left_on = 'tm_join',right_on = 'Team', how='left')

seed_elos.isnull().any()


#simple formula to get win probability from elo rating differential
def win_prob_t1(team1_elo,team2_elo):
    elo_diff_m = (team2_elo-team1_elo)/400
    t1_win_prob = 1/(1+10**elo_diff_m)
    return t1_win_prob


# build team class for simulation
class Team:
    def __init__(self, teamid, data, season):
        self.teamid = teamid
        self.data = data[(data['TeamID'] == self.teamid) &
                         (data['Season'] == season)].copy()
        self.team_name = self.data['TeamName'].unique()[0]

    def getPointsScored(self):
        return self.data['PtScored'].values

    def getPointsAllowed(self):
        return self.data['PtAllowed'].values

    def getAttributes(self):
        self.attributes = dict()
        for col in self.data.columns:
            self.attributes[col] = self.data[col].values
        return self.attributes


import random as rd


def sim_once(team1, team2):
    score_team1 = rd.gauss(team1.getPointsScored().mean(), team1.getPointsScored().std())
    score_team2 = rd.gauss(team2.getPointsScored().mean(), team2.getPointsScored().std())
    score_against_team1 = rd.gauss(team1.getPointsAllowed().mean(), team1.getPointsAllowed().std())
    score_against_team2 = rd.gauss(team2.getPointsAllowed().mean(), team2.getPointsAllowed().std())
    final_score_t1 = (score_team1 + score_against_team2) / 2
    final_score_t2 = (score_team2 + score_against_team1) / 2
    if final_score_t1 == final_score_t2:
        sim_once(team1, team2)
    return (final_score_t1, final_score_t2, final_score_t1 > final_score_t2)


def sim_multiple(team1, team2, n):
    """Takes two teams in and returns win % of t1, t1 point dist, t2 point dist, win loss binary"""
    t1_points = []
    t2_points = []
    w_l = []
    for i in range(n):
        sim = sim_once(team1, team2)
        t1_points.append(sim[0])
        t2_points.append(sim[1])
        w_l.append(sim[2])
    return (sum(w_l) / n)

df = pd.read_csv('Data/MRegularSeasonDetailedResults.csv')




df_winners = df.loc[:,['Season','DayNum','WTeamID','WScore','LScore']]
df_losers = df.loc[:,['Season','DayNum','LTeamID','LScore','WScore']]

#rename columns
df_winners.columns = ['Season','DayNum','TeamID','PtScored','PtAllowed']
df_losers.columns = ['Season','DayNum','TeamID','PtScored','PtAllowed']

df_tm = pd.concat([df_winners,df_losers])

print(df_tm)

df_tm_names = pd.merge(df_tm,df_teams.loc[:,['TeamID','TeamName']], on ='TeamID')
#df_tm_names[df_tm_names.TeamID == 1216]
'''
#Example of how to team objects
alabama = Team(1104,df_tm_names,2023)
hartford = Team(1216,df_tm_names,2023)
#run simulation of two teams
sim_out = sim_multiple(alabama,hartford,1000)
#results of simulation (win probability, t1 scors, t2 scores, win / loss binary)
print(sim_out)
'''
def predict(id1,id2,n):
    team1 = Team(id1,df_tm_names,2023)
    team2 = Team(id2, df_tm_names, 2023)
    ans =  sim_multiple(team1,team2,n)
    return str(ans)

print(predict(1104,1216,100))



