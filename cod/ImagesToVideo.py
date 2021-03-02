import cv2 as cv
import numpy as np
import os
from os.path import isfile, join

pathIn = '../data/output_images/linnaeus5x64/VA_frames/'
pathOut = 'video.mp4'
fps = 30
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
# for sorting the file names properly
files.sort(key=lambda x: x[5:-4])
for i in range(len(files)):
    filename = pathIn + files[i]
    # reading each files
    img = cv.imread(filename)
    test_image = cv.imread("../data/forest/test/bost102.jpg")
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)
video_extension_and_fourcc_dict = {'avi': cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                   'mp4': 0x7634706d}
out = cv.VideoWriter(pathOut, video_extension_and_fourcc_dict["mp4"], fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()