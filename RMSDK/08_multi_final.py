import cv2
import queue
from threading import Thread
import robomaster
from robomaster import robot
from ultralytics import YOLO
import re
import time

# 加载预训练的 YOLOv8 模型
model = YOLO('../runs/best.pt')
q=queue.Queue()
cnt=0
if __name__ == '__main__':

    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_gimbal = ep_robot.gimbal
    ep_blaster = ep_robot.blaster
    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False, resolution='360p')

    def refer(name):
        global cnt
        while True:
            if(~q.empty()):
                cnt+=1
                results = model(q.get())

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

                posx = float(pos_arr[0])+40
                posy = float(pos_arr[1])-20

                if float(pos_arr[0]) != 0:
                    yaw = int((posx/360-1)*55)
                    pitch = -int((posy/180-1)*55)
                    print(yaw,pitch)
                    ep_gimbal.move(yaw=yaw, pitch=pitch, pitch_speed=20, yaw_speed=20)
                    time.sleep(1)
                    ep_blaster.fire()

                cv2.waitKey(1)
            
    t1 = Thread(target=refer,args="1")
    t2 = Thread(target=refer,args="2")
    t3 = Thread(target=refer,args="3")
    t4 = Thread(target=refer,args="4")
    t5 = Thread(target=refer,args="5")
    t6 = Thread(target=refer,args="6")
    
    q.put(ep_camera.read_cv2_image(strategy='newest'))
    q.put(ep_camera.read_cv2_image(strategy='newest'))
    q.put(ep_camera.read_cv2_image(strategy='newest'))
    q.put(ep_camera.read_cv2_image(strategy='newest'))
    q.put(ep_camera.read_cv2_image(strategy='newest'))
    #q.put(ep_camera.read_cv2_image(strategy='newest'))
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    #t6.start()

    while True:
        if(cnt>0):
            q.put(ep_camera.read_cv2_image(strategy='newest'))
            cnt-=1
    
    t1.join()
    t2.join()

    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()

