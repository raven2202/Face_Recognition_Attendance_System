import cv2
import face_recognition
import pickle
import os

#importing student images into a list
folderPath = 'Images'
pathList=os.listdir(folderPath)
print(pathList)
imgList=[]
studentIds=[]
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    #removing .jpg from images
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)

def findencodings(imageslist):
    encodelist=[]
    for img in imageslist:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

    return encodelist

print("Encoding started......")
encodeListKnown=findencodings(imgList)
encodeListKnownWithIds=[encodeListKnown,studentIds]
print("Encoding ended")

file=open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownWithIds,file)
file.close()
print("File Saved")