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
    
    # 
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
    
    # TODO: loop through, grab everything on the same y and order by x

    for key in playerNumbers:
      print(playerNumbers[key].printTextWhenJson())