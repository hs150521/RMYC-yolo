def refer(name,q,q_cnt,q_ans):
    
    import cv2
    from multiprocessing import  Process, Queue
    from ultralytics import YOLO
    import re
    import time

    # 加载预训练的 YOLOv8 模型
    #q=Queue()
    #q_cnt=Queue()
    #cnt=0
    #global cnt
    #from ultralytics import YOLO
    #print("getting1")
    #model = YOLO('../runs/best.pt')
    model1 = YOLO('/home/yuanzl/RM-yolo/runs/best.pt')
    #print("getting2")
    while True:
        if(~q.empty()):
            #cnt+=1
            
            #print("getting3")
            tmp_img=q.get()
            #cv2.imshow("img_shpw", tmp_img)
            #print("getting3.5")
            results = model1.predict(tmp_img)
            q_ans.put(results)
            '''
            #print("getting4")
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
            '''
            q_cnt.put(name)


    cv2.destroyAllWindows()
