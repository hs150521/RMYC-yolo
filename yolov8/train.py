from ultralytics import YOLO


if __name__ == '__main__':
    # 加载模型
    model = YOLO('runs/detect/3.407epoch\\weights\\best.pt')  # 加载预训练模型或需要恢复训练的模型(yaml格式或者pt格式)
    # model = YOLO('yolov8n.yaml')

    # 训练模型
    results = model.train(data='dataset\\red_armo\\detect.yaml', epochs=2500, imgsz=640, device=0, patience=100)
