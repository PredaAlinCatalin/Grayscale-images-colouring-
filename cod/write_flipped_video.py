
# coding: utf-8

# In[4]:


import numpy as np
import cv2 as cv


# In[14]:


def flip_frames(video_filename):
    flipped_frames = []
    cap = cv.VideoCapture(video_filename)
    if cap.isOpened() is False:
        print("Error opening video stream or file")
        return flipped_frames
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()  # Read the frame
        if ret is True:
            if 0 <= count <= 9:
                cv.imwrite("D:\\VedereArtificiala\\VATema4\\VA_frames\\frame00%d.jpg" % count, frame)
            elif 10 <= count <= 99:
                cv.imwrite("D:\\VedereArtificiala\\VATema4\\VA_frames\\frame0%d.jpg" % count, frame)
            elif 100 <= count <= 999:
                cv.imwrite("D:\\VedereArtificiala\\VATema4\\VA_frames\\frame%d.jpg" % count, frame)
            flipped_frame = np.fliplr(frame)
            flipped_frames.append(flipped_frame)
        else:
            break
        count += 1
    cap.release()
    return flipped_frames


# In[16]:


#change this on your machine
video_filename = "D:\\VedereArtificiala\\VATema4\\VA.mp4"


flipped_frames = flip_frames(video_filename)
video_output_name = "%s_flipped.mp4" % video_filename[:-4]
video_extension_and_fourcc_dict = {'avi': cv.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                   'mp4': 0x7634706d}
output_video = cv.VideoWriter(video_output_name, video_extension_and_fourcc_dict["mp4"], 30,
                              (flipped_frames[0].shape[1], flipped_frames[0].shape[0]))

num_frames = len(flipped_frames)
for i in range(0, num_frames):
    output_video.write(flipped_frames[i])

output_video.release()

