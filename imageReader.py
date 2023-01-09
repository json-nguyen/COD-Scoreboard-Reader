import sys
import models.ImageText as ImageText
import models.Bounds as Bounds
import utils.debuggingUtils as debuggingUtils
import utils.dataExtractorUtils as dataExtractorUtils
import utils.excelUtils as excelUtils
import json
import os 
from google.cloud import vision
from pprint import pprint

# GOOGLE_CREDENTIALS = os.environ.get("united-monument-371102-ca96322d50e8.json")
def detectText(path):
    """Detects text in the file."""
    import io
    # Load the credentials from the JSON file
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

        vertices = Bounds.Bounds(bounds[0], bounds[1], bounds[2], bounds[3])
        it = ImageText.ImageText(text.description, vertices, idx)

        retVal.append(it)
    return retVal[1:]


if __name__ == "__main__":

    """ Detect Image through API """
    # debuggingUtils.dumpJson(texts)

    """ Read in existing json file so we dont need to call API while testing """
    # f = open('testData/testData.json')
    # jsonData = json.load(f)
    #initialTexts = debuggingUtils.convertJsonToImageTextList(jsonData) 
    
    images = os.listdir('./images')
    for image in images:
        initialTexts = detectText("./images/" + image)

        print("READING IMAGE", image)
        texts = dataExtractorUtils.removeBestOfFiveText(initialTexts)
        gameMode, gameMap, totalGameTime = dataExtractorUtils.getTopLeftCorner(texts)
        scoreboard = dataExtractorUtils.getScoreBoard(texts)
        teamNames = dataExtractorUtils.getTeamNames(texts)
        gameScore = dataExtractorUtils.getGameScore(texts, gameMode, teamNames)
        # print("GAMEMODE: ", gameMode)
        # print("MAP: ", gameMap)
        # print("TOTAL GAME TIME", totalGameTime)
        # print("SCORE: ", gameScore[0], gameScore[1])

        # print("\n", teamNames[0])
        # pprint(scoreboard[:len(scoreboard)//2], compact=True)
        # print("\n", teamNames[1])
        # pprint(scoreboard[len(scoreboard)//2:], compact=True)
        exportExcel = excelUtils.exportToExcel(gameMode, gameMap, gameScore, totalGameTime, scoreboard, teamNames)
      


