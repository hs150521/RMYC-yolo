import cv2
import robomaster
from robomaster import robot
from ultralytics import YOLO

# 加载预训练的 YOLOv8 模型
model = YOLO('../runs/best.pt')

if __name__ == '__main__':
    ep_robot = robot.Robot()
    ep_robot.initialize(conn_type="rndis")

    ep_camera = ep_robot.camera
    ep_camera.start_video_stream(display=False)

    while True:
        img = ep_camera.read_cv2_image()
        # 在该帧上运行YOLOv8推理
        results = model(img)

        # 在帧上可视化结果
        annotated_frame = results[0].plot()

        # 显示带注释的帧
        cv2.imshow("YOLOv8", annotated_frame)
        # cv2.imshow("Robot", img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    ep_camera.stop_video_stream()
    ep_robot.close()
