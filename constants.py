# declare constants
__genericHeaders = ['KILLS/DEATH', 'ASSISTS', 'NON-TRADED KILLS', 'HIGHEST STREAK', 'DAMAGE']
__hardpointHeaders = ['HILL TIME', 'AVG HILL TIME', 'OBJECTIVE KILLS', 'CONTESTED HILL TIME', 'KILLS/HILL', 'DMG/HILL' ]
__controlHeaders = ['TIERS CAPTURED', 'OBJECTIVE KILLS', 'OFFENSIVE KILLS', 'DEFENSIVE KILLS', 'KILLS/ROUND', 'DMG/ROUND']
__searchAndDestroyHeaders = ['BOMBS PLANTED', 'BOMBS DEFUSED', 'FIRST BLOODS', 'FIRST DEATHS', 'KILLS/ROUND', 'DMG/ROUND']

GAMEMODE_HEADERS = {
  'HARDPOINT': __genericHeaders + __hardpointHeaders,
  'CONTROL': __genericHeaders + __controlHeaders,
  'SEARCH AND DESTROY': __genericHeaders + __searchAndDestroyHeaders
}

print(GAMEMODE_HEADERS)