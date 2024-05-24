import cv2
import thread
from multiprocessing import  Process, Queue
import robomaster
from robomaster import robot
from robomaster import camera
import time
import re

# 加载预训练的 YOLOv8 模型
q=Queue()
q_cnt=Queue()
q_ans=Queue()
#cnt=0
if __name__ == '__main__':

    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_gimbal = ep_robot.gimbal
    ep_blaster = ep_robot.blaster
    ep_camera = ep_robot.camera
    #ep_camera.start_video_stream(display=False, resolution=camera.STREAM_360P)
    #time.sleep(10)
    #ep_camera.stop_video_stream()
    ep_camera.start_video_stream(display=False, resolution=camera.STREAM_360P)

    process_list = []
    for i in range(5):  #开启子进程执行函数
        put_img=ep_camera.read_cv2_image(strategy='newest')
        #cv2.imwrite("img", put_img)
        #print(put_img)
        #cv2.imshow("img_show", put_img)
        q.put(put_img)
        p = Process(target=thread.refer,args=(str(i),q,q_cnt,q_ans,)) #实例化进程对象
        p.start()
        process_list.append(p)
 

    while True:
        if(~q_cnt.empty()):
            q.put(ep_camera.read_cv2_image(strategy='newest'))
            print(q_cnt.get())
        if(~q_ans.empty()):
            results=q_ans.get()
            for r in results:
                boxes = r.boxes

            pos = boxes.xywh
            pos = str(pos)

            pos_arr = []
            pos_arr = re.findall("\d+\.?\d*", pos)

            print("↓\n")
            print(pos_arr)
            print("↑\n")
            annotated_frame = results[0].plot()
            cv2.imshow("YOLOv8", annotated_frame)
            cv2.waitKey(1)
    
    for i in process_list:
        p.join()       

    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()

