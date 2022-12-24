""" File consisting mostly of functions used for testing and debugging """

import json
import imageText

def dumpJson(texts): 
    x = []
    for text in texts: 
        dict = {
            'id': text.id,
            'description': text.description, 
            'bounds': {
                'topLeft': {
                    'x': text.bounds.topLeft.x,
                    'y': text.bounds.topLeft.y
                },
                'topRight': {
                    'x': text.bounds.topRight.x,
                    'y': text.bounds.topRight.y
                },
                'bottomRight': {
                    'x': text.bounds.bottomRight.x,
                    'y': text.bounds.bottomRight.y
                },
                'bottomLeft': {
                    'x': text.bounds.bottomLeft.x,
                    'y': text.bounds.bottomLeft.y
                },
            }
        }
        x.append(dict)
    print(json.dumps(x))

def convertJsonToImageTextList(data):
  retVal = []
  for text in data:
    vertices = imageText.Bounds(
      text['bounds']['topLeft'],
      text['bounds']['topRight'],
      text['bounds']['bottomRight'],
      text['bounds']['bottomLeft']
    )

    it = imageText.ImageText(text['description'], vertices, text['id'])
    retVal.append(it)
  return retVal
#[1, 5, 7, 2, 3, 6, 0, 4]
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
