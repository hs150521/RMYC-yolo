import cv2
from multiprocessing import  Process, Queue
import robomaster
from robomaster import robot
from ultralytics import YOLO
import re
import time

# 加载预训练的 YOLOv8 模型
model = YOLO('../runs/best.pt')
q=Queue()
q_cnt=Queue()
#cnt=0
if __name__ == '__main__':

    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_gimbal = ep_robot.gimbal
    ep_blaster = ep_robot.blaster
    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False, resolution='360p')

    def refer(name,q,q_cnt,model):
        #global cnt
        #from ultralytics import YOLO
        #print("getting1")
        #model = YOLO('../runs/best.pt')
        #model = YOLO('/home/yuanzl/RM-yolo/runs/best.pt')
        #print("getting2")
        while True:
            if(~q.empty()):
                #cnt+=1
                q_cnt.put(name)
                print("getting3")
                results = model(q.get())
                print("getting4")
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
                
                '''
                posx = float(pos_arr[0])+40
                posy = float(pos_arr[1])-20

                if float(pos_arr[0]) != 0:
                    yaw = int((posx/360-1)*55)
                    pitch = -int((posy/180-1)*55)
                    print(yaw,pitch)
                    ep_gimbal.move(yaw=yaw, pitch=pitch, pitch_speed=20, yaw_speed=20)
                    time.sleep(1)
                    ep_blaster.fire()
                '''
                
                cv2.waitKey(1)
    
    process_list = []
    for i in range(5):  #开启子进程执行函数
        q.put(ep_camera.read_cv2_image(strategy='newest'))
        p = Process(target=refer,args=(str(i),q,q_cnt,model,)) #实例化进程对象
        p.start()
        process_list.append(p)
 

    while True:
        if(~q_cnt.empty()):
            q.put(ep_camera.read_cv2_image(strategy='newest'))
            print(q_cnt.get())
    
    for i in process_list:
        p.join()       

    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()

