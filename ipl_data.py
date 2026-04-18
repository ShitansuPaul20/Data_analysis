# -*- coding: utf-8 -*-
"""
IPL_data.ipynb
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print(matches.shape)
print(deliveries.shape)
matches.head()

print(deliveries.columns.tolist())

print(matches.isnull().sum())

matches = matches.dropna(subset=['winner'])
matches['city'] = matches['city'].fillna('Unknown')
matches['player_of_match'] = matches['player_of_match'].fillna('Unknown')
print(matches.shape)

plt.figure(figsize=(12,6))
win_counts = matches['winner'].value_counts()
sns.barplot(x=win_counts.values, y=win_counts.index, palette='rocket')
plt.title('Most Matches Won by Each Team')
plt.xlabel('Number of Wins')
plt.ylabel('Team')
plt.tight_layout()
plt.show()

tosswin = matches[matches['toss_winner'] == matches['winner']]
tossloss = matches[matches['toss_winner'] != matches['winner']]

labels = ['Toss Winner Won Match', 'Toss Winner Lost Match']
sizes = [len(tosswin), len(tossloss)]

plt.figure(figsize=(5,5))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Toss Winner vs Match Winner')
plt.show()

top_scorers = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_scorers.values, y=top_scorers.index, palette='magma', legend="false" )
plt.title('Top 10 Run Scorers in IPL History')
plt.xlabel('Total Runs')
plt.ylabel('Batsman')
plt.tight_layout()
plt.show()

wickets = deliveries[deliveries['dismissal_kind'].notna()]
top_bowlers = wickets.groupby('bowler')['dismissal_kind'].count().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette='coolwarm')
plt.title('Top 10 Wicket Takers in IPL History')
plt.xlabel('Total Wickets')
plt.ylabel('Bowler')
plt.tight_layout()
plt.show()

season_runs = deliveries.groupby('match_id')['total_runs'].sum().reset_index()
season_runs = season_runs.merge(matches[['id','season']], left_on='match_id', right_on='id')
season_total = season_runs.groupby('season')['total_runs'].sum()

plt.plot(season_total.index, season_total.values, marker='o', color='orange', linewidth=2)
plt.title('Season-wise Total Runs Scored in IPL')
plt.xlabel('Season')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_players = matches['player_of_match'].value_counts().head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_players.values, y=top_players.index, hue=top_players.index, palette='viridis', legend=False)
plt.title('Most Player of the Match Awards')
plt.xlabel('Number of Awards')
plt.ylabel('Player')
plt.tight_layout()
plt.show()

fours = deliveries[deliveries['batsman_runs']==4].groupby('match_id')['batsman_runs'].count().reset_index()
sixes = deliveries[deliveries['batsman_runs']==6].groupby('match_id')['batsman_runs'].count().reset_index()

fours = fours.merge(matches[['id','season']], left_on='match_id', right_on='id')
sixes = sixes.merge(matches[['id','season']], left_on='match_id', right_on='id')

season_fours = fours.groupby('season')['batsman_runs'].count()
season_sixes = sixes.groupby('season')['batsman_runs'].count()

plt.figure(figsize=(12,6))
plt.bar(season_fours.index, season_fours.values, label='Fours', color='blue', alpha=0.7)
plt.bar(season_sixes.index, season_sixes.values, label='Sixes', color='red', alpha=0.7, bottom=season_fours.values)
plt.title('Season-wise Fours and Sixes')
plt.xlabel('Season')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

win_by_runs = matches[matches['result'] == 'runs']['result'].count()
win_by_wickets = matches[matches['result'] == 'wickets']['result'].count()

labels = ['Won by Runs', 'Won by Wickets']
sizes = [win_by_runs, win_by_wickets]

plt.figure(figsize=(7,7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        colors=['#3498DB','#E74C3C'], startangle=140,
        explode=(0.05, 0.05))
plt.title('Winning by Runs vs Wickets')
plt.show()

top_venues = matches['venue'].value_counts().head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_venues.values, y=top_venues.index,
            hue=top_venues.index, palette='Set2', legend=False)
plt.title('Top 10 Venues by Number of Matches')
plt.xlabel('Number of Matches')
plt.ylabel('Venue')
plt.tight_layout()
plt.show()

avg_runs = deliveries.groupby('batter')['batsman_runs'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=avg_runs.values, y=avg_runs.index,
            hue=avg_runs.index, palette='cubehelix', legend=False)
plt.title('Top 10 Batsmen by Average Runs per Ball')
plt.xlabel('Average Runs')
plt.ylabel('Batsman')
plt.tight_layout()
plt.show()



