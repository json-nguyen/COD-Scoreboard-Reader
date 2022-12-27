import os
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

        vertices = ImageText.Bounds(bounds[0], bounds[1], bounds[2], bounds[3])
        it = ImageText.ImageText(text.description, vertices, idx)

        retVal.append(it)
    return retVal[1:]


if __name__ == "__main__":
    #texts = detectText(r".\image.png")
    
    # utils.dumpJson(texts)

    f = open('testData.json')
    jsonData = json.load(f)
    texts = debuggingUtils.convertJsonToImageTextList(jsonData)
    dataExtractorUtils.getScoreBoard(texts)
   
