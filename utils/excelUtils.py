import pandas as pd

def exportToExcel(gameMode, gameMap, gameScore, scoreboard, teamNames):
  # Create a DataFrame
  dataframe = {
      'map': [],
      'gamemode': [],
      'winning_team': [],
      'losing_team': [],
      'winning_team_score': [],
      'losing_team_score': [],
      'team': [],
      'player': [],
      'player_kills': [],
      'player_deaths': [],
      'player_assists': [],
      'player_non_traded_kills': [],
      'player_dmg': [],
      'player_hill_time': []
    }

  winningTeam = teamNames[0] if gameScore[0] > gameScore[1] else teamNames[1]
  losingTeam = teamNames[1] if gameScore[0] > gameScore[1] else teamNames[0]
  winningScore = gameScore[0] if gameScore[0] > gameScore[1] else gameScore[1]
  losingScore = gameScore[1] if gameScore[0] > gameScore[1] else gameScore[0]
  winningScoreboard = scoreboard[:len(scoreboard)//2] if gameScore[0] > gameScore[1] else scoreboard[len(scoreboard)//2:]
  losingScoreboard = scoreboard[len(scoreboard)//2:] if gameScore[0] > gameScore[1] else scoreboard[:len(scoreboard)//2]
 
  for row in winningScoreboard:
    dataframe['map'].append(gameMap.lower())
    dataframe['gamemode'].append(gameMode.lower())
    dataframe['winning_team'].append(winningTeam)
    dataframe['losing_team'].append(losingTeam)
    dataframe['winning_team_score'].append(winningScore)
    dataframe['losing_team_score'].append(losingScore)
    dataframe['team'].append(winningTeam)
    dataframe['player'].append(row[1].lower())
    dataframe['player_kills'].append(row[2].split('/')[0])
    dataframe['player_deaths'].append(row[2].split('/')[1])
    dataframe['player_assists'].append(row[3])
    dataframe['player_non_traded_kills'].append(row[4])
    dataframe['player_dmg'].append(row[6])
    dataframe['player_hill_time'].append(row[7] if gameMode == 'HARDPOINT' else 'N/A')
 
  for row in losingScoreboard:
    dataframe['map'].append(gameMap.lower())
    dataframe['gamemode'].append(gameMode.lower())
    dataframe['winning_team'].append(winningTeam)
    dataframe['losing_team'].append(losingTeam)
    dataframe['winning_team_score'].append(winningScore)
    dataframe['losing_team_score'].append(losingScore)
    dataframe['team'].append(losingTeam)
    dataframe['player'].append(row[1].lower())
    dataframe['player_kills'].append(row[2].split('/')[0])
    dataframe['player_deaths'].append(row[2].split('/')[1])
    dataframe['player_assists'].append(row[3])
    dataframe['player_non_traded_kills'].append(row[4])
    dataframe['player_dmg'].append(row[6])
    dataframe['player_hill_time'].append(row[7] if gameMode == 'HARDPOINT' else 'N/A')

  df = pd.DataFrame(dataframe)
  df.to_excel('data.xlsx', index=False)

