# RMYC-yolo

基于yolo的RMYC自瞄系统（开发中）

## 文件结构

- yolov5: yolov5代码(v7.0)
  - data: 所有训练数据
    - pt: 所有权重文件
      - yolov5s.pt: 官方权重
- yolov8: yolov8代码(v8.1.0)
  - docs: yolov8官方文档（多语言版）
  - dataset: 数据集存放位置

## 使用教程

### 配置环境

#### yolov8环境配置

参阅[官方文档](https://docs.ultralytics.com/zh/quickstart/#__tabbed_1_2)，注意把pytorch-cuda=11.8替换成自己的版本，cuda版本支持查看[PyTorch官网](https://pytorch.org/get-started/previous-versions/)，cuda版本切换参考[这篇文章](https://blog.csdn.net/qq_50677040/article/details/132131346)，其他环境要求在 */yolov8/pyproject.toml* 中

#### 安装RMSDK

过程请参阅[这篇博客](https://blog.csdn.net/C___programmer/article/details/135486406?spm=1001.2014.3001.5502)，安装完成后运行 *\RMSDK\00_SDK_test.py*

### 模型相关

#### 训练模型

##### 标注数据

首先准备训练的图片，然后下载[labelme最新版](https://github.com/labelmeai/labelme/releases/latest)标注数据

##### 转化txt

把标注好的数据的json文件放到 *\jso2txt\json_here* ，打开 *\json2txt\transfer.py* ，**在第5行把name2id更改为自己数据集的类别名**并运行程序，txt文件会在 *\json2txt\txt_here* 生成

##### 生成训练数据

训练数据放在 *\yolov8\dataset* 下，文件结构参考example文件夹，三个文件夹的作用参考[这篇文章](https://blog.csdn.net/kupepoem/article/details/101055179)，**注意修改detect.yaml的names为自己数据集的类别名**

##### 开始训练

运行 *\yolov8\train.py* ，第9行的参数详见[官方文档](https://docs.ultralytics.com/zh/modes/train/#_4)

#### 使用模型进行推理

- 若想保存推理结果，运行 *\yolov8\detect.py*
- 若想实时显示推理结果，运行 *\yolov8\detect_video.py*

参数详见[官方文档](https://docs.ultralytics.com/zh/modes/predict/#_4)

#### 导出模型

运行 *\yolov8\onnx_export.py*

### UART通信相关

#### 接口连接

使用UART接口与香橙派通信，（[引脚定义](Picture/README/OPI5_PLUS_V11_20230519-GK_加水印.pdf)P11），RM的RX端链接香橙派的8号引脚，TX端连接10号引脚，接地连接14号引脚

#### 启用UART

连接好之后需要在香橙派上打开串口，详见香橙派[用户手册](Picture/README/OrangePi_5_Plus_RK3588_用户手册_v1.6.pdf)（P213-P214）如果运行orangepi-config报错，请参考这篇[issue](https://github.com/Joshua-Riek/ubuntu-rockchip/issues/41)和[启用UART教程](https://blog.csdn.net/C___programmer/article/details/135604913?csdn_share_tail={"type"%3A"blog"%2C"rType"%3A"article"%2C"rId"%3A"135604913"%2C"source"%3A"C___programmer"})

#### 测试通讯

连接之后参考[2.3.4UART链接](https://robomaster-dev.readthedocs.io/zh-cn/latest/text_sdk/connection.html#uart-conn)进行测试，代码在 *\RMSDK\00_SDK_test.py* ，注意修改ser.port为自己的串口，运行代码后输入command或者command;，如果返回Already in SDK mode;则成功，无返回请检查UART连接

## 参考资料

### yolo代码

- [yolov5](https://github.com/ultralytics/yolov5)
- [yolov8](https://github.com/ultralytics/ultralytics)

### NPU部署

- https://blog.csdn.net/weixin_51651698/article/details/130187558
- [rknn模型](https://github.com/airockchip/yolov5/blob/master/README_rkopt_manual.md)

### RMSDK

- [RMSDK官方文档](https://robomaster-dev.readthedocs.io/zh-cn/latest/python_sdk/installs.html)
