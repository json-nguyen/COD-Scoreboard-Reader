import os
import imageText
import utils
import json

def detectText(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return transformText(response.text_annotations)
   

def transformText(texts):
    retVal = []
    for idx, text in enumerate(texts):
        # first index is the whole thing
        bounds = []

        for vertex in text.bounding_poly.vertices:
            bounds.append(vertex)

        vertices = imageText.Bounds(bounds[0], bounds[1], bounds[2], bounds[3])
        it = imageText.ImageText(text.description, vertices, idx)

        retVal.append(it)
    return retVal[1:]

# Takes in list of ImageText and extracts all scoreboard data and inputs into 2d array
def getScoreBoard(texts):
    # Grab all values with descriptions 1-8
    dict = {
        1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: []
    }
    playerNumbers = {}

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
    
    # Need to validate that these are the right numbers
    # TODO: handle case where validation fails
    # utils.hasOutliers(playerNumbers, 5)
    # TODO: loop through, grab everything on the same y and order by x

    

if __name__ == "__main__":
    #texts = detectText(r".\image.png")
    
    # utils.dumpJson(texts)

    f = open('testData.json')
    jsonData = json.load(f)
    texts = utils.convertJsonToImageTextList(jsonData)
    getScoreBoard(texts)
   
