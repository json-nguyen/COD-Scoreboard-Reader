import models.Bounds as Bounds

class ImageText:

  def __init__(self, description, bounds, id):
    self.id = id
    self.description = description
    self.bounds = Bounds.Bounds(bounds.topLeft, bounds.topRight, bounds.bottomRight, bounds.bottomLeft)
  
  def printTextData(self):
      print('\n"{}"'.format(self.description))
      print('Top Left: ({},{})'.format(self.bounds.topLeft.x, self.bounds.topLeft.y))
      print('Top Right: ({},{})'.format(self.bounds.topRight.x, self.bounds.topRight.y))
      print('Bottom Right: ({},{})'.format(self.bounds.bottomRight.x, self.bounds.bottomRight.y))
      print('Bottom Left: ({},{})'.format(self.bounds.bottomLeft.x, self.bounds.bottomLeft.y))

  def printTextWhenJson(self):
      print('\n"{}"'.format(self.description))
      print('id: {}'.format(self.id))
      print('Top Left: ({},{})'.format(self.bounds.topLeft['x'], self.bounds.topLeft['y']))
      print('Top Right: ({},{})'.format(self.bounds.topRight['x'], self.bounds.topRight['y']))
      print('Bottom Right: ({},{})'.format(self.bounds.bottomRight['x'], self.bounds.bottomRight['y']))
      print('Bottom Left: ({},{})'.format(self.bounds.bottomLeft['x'], self.bounds.bottomLeft['y']))



#  {
#     "id": 6,
#     "description": "1",
#     "bounds": {
#       "topLeft": {
#         "x": 190,
#         "y": 222
#       },
#       "topRight": {
#         "x": 196,
#         "y": 222
#       },
#       "bottomRight": {
#         "x": 196,
#         "y": 234
#       },
#       "bottomLeft": {
#         "x": 190,
#         "y": 234
#       }
#     }
#   },
#   {
#     "id": 7,
#     "description": "CoutiSZN",
#     "bounds": {
#       "topLeft": {
#         "x": 214,
#         "y": 222
#       },
#       "topRight": {
#         "x": 281,
#         "y": 222
#       },
#       "bottomRight": {
#         "x": 281,
#         "y": 234
#       },
#       "bottomLeft": {
#         "x": 214,
#         "y": 234
#       }
#     }
#   },