import sys
import models.ImageText as ImageText
import models.Bounds as Bounds
import utils.debuggingUtils as debuggingUtils
import utils.dataExtractorUtils as dataExtractorUtils
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

        vertices = Bounds.Bounds(bounds[0], bounds[1], bounds[2], bounds[3])
        it = ImageText.ImageText(text.description, vertices, idx)

        retVal.append(it)
    return retVal[1:]


if __name__ == "__main__":

    """ Detect Image through API """
    texts = detectText(r"images\image2.png")
    print(texts)
    # debuggingUtils.dumpJson(texts)

    """ Read in existing json file so we dont need to call API while testing """
    # f = open('testData/testData2.json')
    # jsonData = json.load(f)
    # texts = debuggingUtils.convertJsonToImageTextList(jsonData) 
    # gameMode = dataExtractorUtils.getTopLeftCorner(texts)
    # scoreboard = dataExtractorUtils.getScoreBoard(texts)
    # print(scoreboard)


[
  ['1', 'DENZA', '26/29', '6', '16', '4', '3046', '4', '3', '12', '14', '6.50', '761.50'],
  ['2', 'VORTEX', '17/25', '5', '12', '2', '1861', '3', '2', '8', '9', '4.25', '465.25'],
  ['3', 'HARRY', '22/19', '6', '16', '3', '2434', '4', '6', '12', '10', '5.50', '608.50'],
  ['4', 'GISMO', '12/23', '8', '10', '3', '2227', '5', '3', '7', '5', '3.00', '556.75'],
  ['5', 'MOCK', '25/22', '11', '16', '3', '2934', '8', '5', '9', '16', '6.25', '733.50'],
  ['6', 'HOLLOW', '22/19', '9', '16', '5', '2807', '0', '3', '6', 'CO', '16', '5.50', '701.75'],
  ['7', 'ULI', '25/17', '10', '22', '7', '3032', '8', 'co', '17', '6.25', '758.00'],
  ['8', '2REAL', '24/19', '9', '17', '5', '2554', '1', '3', '15', '9', '5.75', '638.50']
]