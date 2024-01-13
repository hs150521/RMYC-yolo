from ultralytics import YOLO
from PIL import Image
import cv2

# 加载预训练的 YOLOv8 模型
model = YOLO('runs\\detect\\train\\weights\\best.pt') # windows
# model = YOLO('runs/detect/2.125epoch/weights/best.pt') # linux

# 定义包含图像文件用于推理的目录路径, 0表示网络摄像头
# source = 0
source = '..\\detect_sources\\3.mp4' # windows
# source = '../detect_sources/1.mp4' #linux

# 对来源进行推理
results = model(source, save=True, device=0)  # Results 对象的生成器, device=0(CUDA)/'cpu'(CPU)
