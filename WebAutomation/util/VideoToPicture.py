# -*- coding: utf-8 -*-
# 开发人员   ：Rocklee
# 开发时间   ：2019/5/20  15:25 
# 文件名称   ：VideoToPicture.PY
# 开发工具   ：PyCharm

# 运行起来仍有点小问题
import cv2
import os
def save_img():
    video_path = r'D:/cxli/api/onevideo/'
    videos = os.listdir(video_path)
    print(videos)
    for video_name in videos:
        print(video_name)
        file_name = video_name.split('.')[0]
        folder_name = video_path + file_name
        os.makedirs(folder_name,exist_ok=True)
        vc = cv2.VideoCapture(video_path+video_name) #读入视频文件
        c=0
        rval=vc.isOpened()

        print(vc.isOpened())
        print("------")

        while rval:   #循环读取视频帧
            c = c + 1
            rval, frame = vc.read()
            pic_path = folder_name+'/'
            if rval:
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame) #存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                #cv2.waitKey(1)
            else:
                break
        vc.release()
        print('save_success')
        print(folder_name)

save_img()
