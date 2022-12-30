# File with helper function that help extract data from Image Reader 

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
            # change this later to .x when using real data
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
    gameMap = getGameMap(texts, gameMode)
    print(gameMode.description)
    print(gameMap)

def getGameMode(texts):
    top_left_word = None
    top_left_x = float('inf')
    top_left_y = float('inf')
    for text in texts:
        vertices = text.bounds.topLeft
        x1 = vertices['x']
        y1 = vertices['y']
        if y1 < top_left_y or (x1 == top_left_x and y1 < top_left_y):
            top_left_x = x1
            top_left_y = y1
            top_left_word = text

    return top_left_word

def getGameMap(texts, target):
    below_word = None
    below_bounds = None
    for text in texts:
        curBounds = text.bounds
        if (curBounds.topLeft['x'] >= target.bounds.topLeft['x'] and
            curBounds.bottomRight['x'] <= target.bounds.bottomRight['x'] and
            curBounds.topLeft['y'] > target.bounds.bottomRight['y']):
            below_word = text.description
            below_bounds = curBounds
            break

    # Print the word below the target word
    
    gameMapWords = []
    for text in texts:
        if (text.bounds.topLeft['y'] in range(below_bounds.topLeft['y'] - 7, below_bounds.topLeft['y'] + 7) 
            and not text.description.isdigit()):
            gameMapWords.append({
                "description": text.description,
                "position": text.bounds.topLeft['x']
            })
    
    print(gameMapWords)
    sortedWords = sorted(gameMapWords, key=lambda x: x['position'])
    wordList = list(map(lambda x:x['description'], sortedWords))

    return " ".join(wordList)