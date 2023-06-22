import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

html_url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"

nba_table = pd.read_html(html_url)
nba = nba_table[0]

nba['3P'] = pd.to_numeric(nba['3P'], errors='coerce')
nba['G'] = pd.to_numeric(nba['G'], errors='coerce')
nba['AST'] = pd.to_numeric(nba['AST'],errors='coerce')
nba['STL'] = pd.to_numeric(nba['STL'],errors='coerce')
nba['BLK'] = pd.to_numeric(nba['BLK'],errors='coerce')

top_10_players_3P = nba.sort_values(by='3P', ascending=False).head(10)
top_10_players_AST = nba.sort_values(by='AST',ascending=False).head(10)
top_10_players_STL = nba.sort_values(by='STL',ascending=False).head(10)
top_10_players_BLK = nba.sort_values(by='BLK',ascending=False).head(10)


xPlayers3P = top_10_players_3P['Player']
y3Point = top_10_players_3P['3P']

xPlayersAST = top_10_players_AST['Player']
yAssist = top_10_players_AST['AST']

xPlayersSTL = top_10_players_STL['Player']
ySTL = top_10_players_STL['STL']

xPlayersBLK = top_10_players_BLK['Player']
yBLK = top_10_players_BLK['BLK']

games_played_AST = top_10_players_AST['G']
games_played_3P = top_10_players_3P['G']
games_played_STL = top_10_players_STL['G']
games_played_BLK = top_10_players_BLK['G']


fig, axs = plt.subplots(2,2,figsize=(18,12))

scatter_3P=axs[0,0].scatter(xPlayers3P,y3Point,s=100,c=games_played_3P,cmap='viridis',alpha=0.7)
axs[0,0].set_ylabel('3P')
axs[0,0].set_title('Top 10 Players by 3-Point Field Goal Per Game - 2023 Season')
cbar_3P = plt.colorbar(scatter_3P,ax = axs[0,0])
cbar_3P.set_label('Games Played')
axs[0, 0].tick_params(axis='x', rotation=30, labelsize=7)

scatter_AST=axs[1,0].scatter(xPlayersAST,yAssist,s=100,c=games_played_AST,cmap='viridis',alpha=0.7)
axs[1,0].set_ylabel('AST')
axs[1,0].set_title('Top 10 Players by Assist Per Game - 2023 Season')
cbar_AST = plt.colorbar(scatter_AST,ax=axs[1,0])
cbar_AST.set_label('Games Played')
axs[1, 0].tick_params(axis='x', rotation=30, labelsize=7)

scatter_STL = axs[0,1].scatter(xPlayersSTL,ySTL,s=100,c=games_played_STL,cmap='viridis',alpha=0.7)
axs[0,1].set_ylabel('STL')
axs[0,1].set_title('Top 10 Players by Steal Per Game - 2023 Season')
cbar_STL = plt.colorbar(scatter_STL,ax=axs[0,1])
cbar_STL.set_label('Games Played')
axs[0, 1].tick_params(axis='x', rotation=30, labelsize=7)

scatter_BLK = axs[1,1].scatter(xPlayersBLK,yBLK,s=100,c=games_played_BLK,cmap='viridis',alpha=0.7)
axs[1,1].set_ylabel('BLK')
axs[1,1].set_title('Top 10 Players by Blok Per Games - 2023 Season')
cbar_BLK = plt.colorbar(scatter_BLK,ax=axs[1,1])
cbar_BLK.set_label('Games Played')
axs[1, 1].tick_params(axis='x', rotation=30, labelsize=7)

plt.tight_layout()
plt.show()