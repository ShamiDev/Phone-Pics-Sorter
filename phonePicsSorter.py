import os
import cv2
import shutil

ogpath = "D:/Pictures/My_Phone"

cwd = os.getcwd()
print(cwd)
os.chdir(ogpath)
print(os.getcwd())
print(os.listdir(ogpath))

animePath = ogpath + "/Anime art"
animePics = os.listdir(animePath)

gamingPath = ogpath + "/Gaming art"
gamingPics = os.listdir(gamingPath)

miscPath = ogpath + "/Other Favourite Art"
miscPics = os.listdir(miscPath)

# img = cv2.imread("D:/Pictures/My_Phone/Anime art/2c4825b.jpg")

paths = [animePath, gamingPath, miscPath]
pics = [animePics, gamingPics, miscPics]

for i in range(3):
    print(paths[i])
    for file_ in pics[i]:
        try:
            name, ext = os.path.splitext(file_)
            if ext == '' or ext == '.gif':
                continue

            imgPath = paths[i] + '/' + file_
            img = cv2.imread(imgPath)
            # "D:\Pictures\My_Phone\Other Favourite Art\sendToPhone"
            destPath = paths[i] + '/sendToPhone'
            # print(img.shape, end=' ___ ')
            ext = ext[1:]  # extension without the .
            print(name, ext, end=' _-^-_ ')
            imgShape = img.shape
            imgHeight = float(imgShape[0])
            imgWidth = float(imgShape[1]) * 1.2
            if imgHeight > imgWidth:
                print("Move to sendToPhone folder")
                shutil.move(imgPath, destPath)
            else:
                print("Don't move")
        except:
            continue
        # if it is the directory, go to next iteration
    print('\n' * 2)
