# File with helper function that help extract data from Image Reader 
import heapq

def removeBestOfFiveText(texts): 
    print("initial length", len(texts))
    best = None
    idsToRemove = []
    for text in texts:
        if text.description.upper() == "BEST":
            best = text
    if best is None:
        return texts

    idsToRemove.append(best.id)

    for text in texts:
        if (text.bounds.topLeft['y'] in range(best.bounds.topLeft['y'] - 3, best.bounds.topLeft['y'] + 3)
            and best.id != text.id):
            idsToRemove.append(text.id)
    
    return list(filter(lambda x: x.id not in idsToRemove, texts))

def hasOutliers(data, deviation):
    sortedListIndexs = sorted(data, key=lambda x: data[x].bounds.topLeft['x'])
    sortedList = []
    for x in sortedListIndexs:
        sortedList.append(data[x])
    median = (sortedList[3].bounds.topLeft['x'] + sortedList[4].bounds.topLeft['x'])/2
    for x in sortedList:
        if x.bounds.topLeft['x'] > median + deviation or  x.bounds.topLeft['x'] < median - deviation:
            return True
    return False

# Takes in list of ImageText and extracts all scoreboard data and inputs into 2d array
def getScoreBoard(texts):
    dict = {
        1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []
    }
    playerNumbers = {}

    # Grab all values with descriptions 1-8
    for x in range(1, 9):
        for text in texts:
            if(text.description == str(x)):
                dict[x].append(text)
    
    for idx1, key in enumerate(dict):
        for idx2, value in enumerate(dict[key]):
            if idx2 == 0:
                playerNumbers[idx1] = value
                continue
            # change this later to ['x'] when using real data
            if playerNumbers[idx1].bounds.topLeft['x'] > value.bounds.topLeft['x']:
                playerNumbers[idx1] = value

    if hasOutliers(playerNumbers, 5):
      # TODO: handle case where validation fails
        print("HAS OUTLIERS, FIX THESE")
        return
    
    scoreboard = []

    for key in playerNumbers:
        unsortedScoreboard = []
        for test in texts:
            if test.bounds.bottomLeft['y'] in range(playerNumbers[key].bounds.bottomLeft['y'] - 5, playerNumbers[key].bounds.bottomLeft['y'] + 5):
                unsortedScoreboard.append({
                    "description": test.description,
                    "position": test.bounds.bottomLeft['x']
                })
        sortedRow = sorted(unsortedScoreboard, key=lambda x: x['position'])
        scoreboard.append(list(map(lambda x:x['description'], sortedRow)))
    return scoreboard


def getTopLeftCorner(texts): 
    gameMode = getGameMode(texts)
    print("GAMEMODE: ", gameMode.description)
    gameMap, gameMapText = getWordsBelow(texts, gameMode)

    totalGameTime, _ = getWordsBelow(texts, gameMapText)
    return (gameMode.description, gameMap, totalGameTime.split()[-1])

def getGameMode(texts):
    top_left_word = None
    top_left_x = float('inf')
    top_left_y = float('inf')
    # game mode is always top left, so we grab the top left most word
    for text in texts:
        vertices = text.bounds.topLeft
        x1 = vertices['x']
        y1 = vertices['y']
        if y1 < top_left_y or (x1 <= top_left_x and y1 < top_left_y):
            top_left_x = x1
            top_left_y = y1
            top_left_word = text

    return top_left_word

def getWordsBelow(texts, target):
    belowText = None
    for text in texts:
        curBounds = text.bounds
        # under 
        # if top left ['x'] in range 5
        if (curBounds.topLeft['x'] in range(target.bounds.topLeft['x'] - 3, target.bounds.topLeft['x'] + 3) and
            curBounds.topLeft['y'] < target.bounds.bottomLeft['y'] + 20 and
            target.description is not text.description 
            ):
            print('here')
            belowText = text
    
    gameMapWords = []
    for text in texts:
        if (text.bounds.topLeft['y'] in range(belowText.bounds.topLeft['y'] - 7, belowText.bounds.topLeft['y'] + 7) 
            and not text.description.isdigit()):
            gameMapWords.append({
                "description": text.description,
                "position": text.bounds.topLeft['x']
            })
    
    sortedWords = sorted(gameMapWords, key=lambda x: x['position'])
    wordList = list(map(lambda x:x['description'], sortedWords))

    return " ".join(wordList), belowText

def getTeamNames(texts): 
    # Get team names, they are the left furthest texts
    teamNames = heapq.nsmallest(2, texts, key=lambda x: x.bounds.topLeft['x'])

    # Make sure they are ordered from top to bottom
    teamNames.sort(key=lambda y: y.bounds.topLeft['y'])

    # Team Names consist of more than one word so fetch them
    def findWordsToRight(initial, texts):
        done = False
        boundsX = initial.bounds.topRight['x']
        boundsY = initial.bounds.topRight['y']
        teamName = initial.description
        while not done:
            done = True
            for text in texts:
                if (text.bounds.topLeft['x'] in range(boundsX, boundsX + 15) and 
                    text.bounds.topLeft['y'] in range(boundsY - 3, boundsY + 3) and
                    text.description not in teamName):
                    boundsX = text.bounds.topRight['x']
                    teamName = teamName + " " + text.description
                    done = False
        return teamName

    team1 = findWordsToRight(teamNames[0], texts)
    team2 = findWordsToRight(teamNames[1], texts)

    return [team1, team2]

def getGameScore(texts, gameMode, teamNames): 
    rightScore = None
    top_right_x = float('inf')
    top_right_y = float('inf')
    # score is top right most exluding game mode
    for text in texts:
        vertices = text.bounds.topRight
        x1 = vertices['x']
        y1 = vertices['y']
        if ((y1 < top_right_y or (x1 >= top_right_x and y1 < top_right_y)) and 
            text.description is not gameMode and
            text.description in teamNames != -1):
            top_right_x = x1
            top_right_y = y1
            rightScore = text
    
    # now get the other score which is left of the score we just found
    leftScore = None
    boundsY = rightScore.bounds.topLeft['y']
    for text in texts:
        if leftScore is None:
            leftScore = text
            continue

        if (text.bounds.topLeft['y'] in range(boundsY - 3, boundsY + 3) and 
            text.bounds.topRight['x'] > leftScore.bounds.topRight['x'] and
            text.description is not rightScore.description):
            leftScore = text

    return [leftScore.description, rightScore.description]