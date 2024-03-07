import cv2
import robomaster
from robomaster import robot
from ultralytics import YOLO
import time

# 加载预训练的 YOLOv8 模型
model = YOLO('../runs/best.pt')

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False,resolution='480p')

    while True:

        img = ep_camera.read_cv2_image(strategy='newest')

        results = model(img)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLOv8", annotated_frame)

        cv2.waitKey(1)

    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()

