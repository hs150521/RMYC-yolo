from ultralytics import YOLO

# 加载模型
model = YOLO('runs\\detect\\2.125epoch\\weights\\best.pt')

# 导出模型
model.export(format='onnx')