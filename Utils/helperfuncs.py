from   skimage.transform import rescale
import numpy as np
import os
import glob
from   parse import parse

# Resizes images so that all dimensions match the bounding box when possible
def standardizedResize(highResImage, maximumDimensions):
    imageSize = highResImage.shape
    imageRowsRescale =  maximumDimensions[0] / imageSize[0]
    imageColsRescale = maximumDimensions[1] / imageSize[1]
    scaleFactor = min(imageRowsRescale, imageColsRescale)
    out0 = rescale(highResImage[:, :, 0], scaleFactor)
    out1 = rescale(highResImage[:, :, 1], scaleFactor)
    out2 = rescale(highResImage[:, :, 2], scaleFactor)
    return [np.stack((out0, out1, out2), 2), scaleFactor]

def standardizedResize1D(highResImage, maximumDimensions):
    imageSize = highResImage.shape
    imageRowsRescale =  maximumDimensions[0] / imageSize[0]
    imageColsRescale = maximumDimensions[1] / imageSize[1]
    scaleFactor = min(imageRowsRescale, imageColsRescale)
    out = rescale(highResImage[:, :], scaleFactor)
    return (out, scaleFactor)

# Verifies that the outpath is ready. Returns path string if ready and None
# if a disparity output already exists there.
def verifyOutPath(currentImageName, algorithmName):
    outPath   = "Output/%s/%s" % (currentImageName, algorithmName)
    if not os.path.isdir(outPath):
        if not os.path.isdir("Output"):
            print("No Output folder, creating empty folder.")
            os.mkdir("Output")
        if not os.path.isdir("Output/%s" % currentImageName):
            os.mkdir("Output/%s" % currentImageName)
        os.mkdir(outPath)
    elif os.path.isfile(outPath + "/OutDisparity.ppm"):
        return True
    
    return False

def getResourcePaths(currentImageName):
    leftPathList          = glob.glob("Data/%s/Left.*" % currentImageName)
    leftPath = None
    if(len(leftPathList) > 0):
        leftPath = leftPathList[0]
        
    rightPathList         = glob.glob("Data/%s/Right.*" % currentImageName)
    rightPath = None
    if(len(rightPathList) > 0):
        rightPath = rightPathList[0]

    disparityLeftList     = glob.glob("Data/%s/disparityGTLeft.*" % currentImageName)
    disparityLeftPath = None
    if(len(disparityLeftList) > 0):
        disparityLeftPath = disparityLeftList[0]

    disparityRightList    = glob.glob("Data/%s/disparityGTRight.*" % currentImageName)
    disparityRightPath = None
    if(len(disparityRightList) > 0):
        disparityRightPath = disparityRightList[0]

    cameraCalibrationList = glob.glob("Data/%s/calib.txt" % currentImageName)
    cameraCalibrationPath = None
    if(len(cameraCalibrationList) > 0):
        cameraCalibrationPath = cameraCalibrationList[0]

    occlusionMapLeftList  = glob.glob("Data/%s/occlusionLeft.*" % currentImageName)
    occlusionMapLeftPath = None
    if(len(occlusionMapLeftList) > 0):
        occlusionMapLeftPath = occlusionMapLeftList[0]

    occlusionMapRightList = glob.glob("Data/%s/occlusionRight.*" % currentImageName)
    occlusionMapRightPath = None
    if(len(occlusionMapRightList) > 0):
        occlusionMapRightPath = occlusionMapRightList[0]
    
    return [leftPath, rightPath, disparityLeftPath, disparityRightPath, cameraCalibrationPath, occlusionMapLeftPath, occlusionMapRightPath]    

def getCalibrationMatrices(cameraCalibrationPath):
    file = open(cameraCalibrationPath, "r")

    # Camera calibration 0
    calibMatrix0 = np.zeros((3, 3))
    coefficients0 = parse("cam0=[{:f} 0 {:f}; 0 {:f} {:f}; 0 0 1]\n", file.readline())
    calibMatrix0[0, 0] = coefficients0[0]
    calibMatrix0[0, 2] = coefficients0[1]
    calibMatrix0[1, 1] = coefficients0[2]
    calibMatrix0[1, 2] = coefficients0[3]
    calibMatrix0[2, 2] = 1

    # Camera calibration 1
    calibMatrix1 = np.zeros((3, 3))
    coefficients1 = parse("cam1=[{:f} 0 {:f}; 0 {:f} {:f}; 0 0 1]\n", file.readline())
    calibMatrix1[0, 0] = coefficients1[0]
    calibMatrix1[0, 2] = coefficients1[1]
    calibMatrix1[1, 1] = coefficients1[2]
    calibMatrix1[1, 2] = coefficients1[3]
    calibMatrix1[2, 2] = 1

    # Done
    return calibMatrix0, calibMatrix1
    

