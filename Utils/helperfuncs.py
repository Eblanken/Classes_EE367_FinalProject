from skimage.transform import rescale
import numpy as np

# Resizes images so that they fit within the specified bounding box
def standardizedResize(highResImage, maximumDimensions):
    imageSize = highResImage.shape
    imageRowsRescale =  maximumDimensions[0] / imageSize[0]
    imageColsRescale = maximumDimensions[1] / imageSize[1]
    scaleFactor = min(imageRowsRescale, imageColsRescale)
    out0 = rescale(highResImage[:, :, 0], scaleFactor)
    out1 = rescale(highResImage[:, :, 1], scaleFactor)
    out2 = rescale(highResImage[:, :, 2], scaleFactor)
    return np.stack((out0, out1, out2), 2)
