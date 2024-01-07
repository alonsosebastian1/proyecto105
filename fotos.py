import os
import cv2

path = "Images/"
images = []
for files in os.listdir(path):
    name,extencion = os.path.splitext(files)
    if extencion in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+files
        #print(file_name)
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[0])
height,width,layers = frame.shape
size = (width,height)
print(size)
out = cv2.VideoWriter("Project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0, count-1):
    print(images[i])
    frame = cv2.imread(images[1])
    out.write(frame)
out.release()
print("listo")