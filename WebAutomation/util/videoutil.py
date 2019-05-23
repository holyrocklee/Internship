import cv2


def save_image(video,output):
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 1
    while success:
        success, image = vidcap.read()
        cv2.imwrite(pathOut+str(count)+".jpg", image)  # save frame as JPEG file
        print(count)
        count += 1


if __name__ == '__main__':
    pathIn = 'D:\\cxli\\api\\汽车相关素材\\捷豹.mp4'
    pathOut = 'C:\\api_iscar\\04jiebao\\'
    save_image(pathIn,pathOut)
