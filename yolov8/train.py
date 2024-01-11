from ultralytics import YOLO


if __name__ == '__main__':
    # 加载模型
    model = YOLO('yolov8n.yaml')  # 加载预训练模型或需要恢复训练的模型(yaml格式或者pt格式)

    # 训练模型
    results = model.train(data='dataset\\red_armo\\detect.yaml', epochs=100, imgsz=640, device=0)
