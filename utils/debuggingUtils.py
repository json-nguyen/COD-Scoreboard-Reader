""" File consisting mostly of functions used for testing and debugging """

import json
import models.ImageText as ImageText
import models.Bounds as Bounds

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
    vertices = Bounds.Bounds(
      text['bounds']['topLeft'],
      text['bounds']['topRight'],
      text['bounds']['bottomRight'],
      text['bounds']['bottomLeft']
    )

    it = ImageText.ImageText(text['description'], vertices, text['id'])
    retVal.append(it)
  return retVal

