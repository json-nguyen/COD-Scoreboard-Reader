class ImageText:

  def __init__(self, description, bounds):
    self.description = description
    self.bounds = Bounds(bounds.topLeft, bounds.topRight, bounds.bottomRight, bounds.bottomLeft)
  
  def printTextData(self):
      print('\n"{}"'.format(self.description))
      print('Top Left: ({},{})'.format(self.bounds.topLeft.x, self.bounds.topLeft.y))
      print('Top Right: ({},{})'.format(self.bounds.topRight.x, self.bounds.topRight.y))
      print('Bottom Right: ({},{})'.format(self.bounds.bottomRight.x, self.bounds.bottomRight.y))
      print('Bottom Left: ({},{})'.format(self.bounds.bottomLeft.x, self.bounds.bottomLeft.y))


class Bounds:
  def __init__(self, topLeft, topRight, bottomRight, bottomLeft):
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomRight = bottomRight
    self.bottomLeft = bottomLeft