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

