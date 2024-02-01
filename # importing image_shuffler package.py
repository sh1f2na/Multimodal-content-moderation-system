# importing image_shuffler package
from image_shuffler import Shuffler

# Reading the image from local directory
# to python environment
img = Shuffler("image_98.jpg")

# specifying the matrix to shuffle
img.shuffle(matrix=(300, 73))

# displaying & saving the shuffled
# image
img.show()
img.save()
