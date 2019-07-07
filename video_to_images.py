import cv2
import os
print(cv2.__version__)
folder_name = 'Downloads/cotton'
video_name = 'Downloads/60m.MP4'
numer_sec = 1


def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
      vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*numer_sec*1000))    # added this line 
      success,image = vidcap.read()
      
      image_name = os.path.join(folder_name,  "framme_%d.jpg" % count)
      print ('Save a new frame: '+"framme_%d.jpg" % count)
      cv2.imwrite( image_name, image)     # save frame as JPEG file
      count = count + 1

if __name__=="__main__":
    # a = argparse.ArgumentParser()
    # a.add_argument("--pathIn", help="path to video")
    # a.add_argument("--pathOut", help="path to images")
    # args = a.parse_args()
    # print(args)
    
    extractImages(video_name, folder_name)
