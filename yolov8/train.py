from ultralytics import YOLO
# 加载模型
model = YOLO('yolov8n.pt')  # 加载预训练模型或需要恢复训练的模型

# 使用2个GPU训练模型
results = model.train(data='coco128.yaml', epochs=100, imgsz=640, device='mps')