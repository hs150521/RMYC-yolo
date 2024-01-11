from ultralytics import YOLO
from PIL import Image
import cv2

# 加载预训练的 YOLOv8 模型
model = YOLO('runs\\detect\\2.125epoch\\weights\\best.pt')

# 定义包含图像文件用于推理的目录路径, 0表示网络摄像头
# source = 0
source = '..\\detect_sources\\1.mp4'

# 对来源进行推理
results = model(source, save=True, device=0)  # Results 对象的生成器
