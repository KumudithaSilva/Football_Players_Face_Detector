import numpy as np
import cv2
import pywt

def w2d(image, model='haar', level=1):
    imArray = image
    
    # Convert to grayscale
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    # Convert to float
    imArray = np.float32(imArray)
    # Scales the pixel values of the image to the range [0, 1] by dividing each pixel value by 255
    imArray /= 255;
    # Compute cofficinets
    coeffs = pywt.wavedec2(imArray, model, level=level)
    
    # Process Coefficinets
    coeffs_H = list(coeffs)
    # Remove low-frequency information
    coeffs_H[0] *= 0;
    
    # Reconstruction
    imArray_H = pywt.waverec2(coeffs_H, model);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)
    return imArray_H
    