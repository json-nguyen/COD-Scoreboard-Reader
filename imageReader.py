import os
import imageText

def detect_text(path):
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

    return transform_text(response.text_annotations)
   

def transform_text(texts):
    retVal = []
    for idx, text in enumerate(texts):
        
        # first index is the whole thing

        bounds = []
        for vertex in text.bounding_poly.vertices:
            bounds.append(vertex)

        vertices = imageText.Bounds(bounds[0], bounds[1], bounds[2], bounds[3])

        it = imageText.ImageText(text.description, vertices)


        retVal.append(it)
    return retVal[1:]

if __name__ == "__main__":
  texts = detect_text(r".\image.png")
  for text in texts:
    text.printTextData()

""", description: "195.88"
bounding_poly {
  vertices {
    x: 1156
    y: 582
  }
  vertices {
    x: 1206
    y: 582
  }
  vertices {
    x: 1206
    y: 595
  }
  vertices {
    x: 1156
    y: 595
  }
}
"""