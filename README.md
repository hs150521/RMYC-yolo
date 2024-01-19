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

#### 安装RMSDK（可选）

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

### Rndis通信

该标题下所有代码**默认位于RMSDK文件夹下**

首先配置香橙派网络

```bash
sudo vim /etc/network/
```

文件最下方加入（usb0请改为自己网卡）

```bash
auto usb0
iface usb0 inet static
address 192.168.42.3
netmask 255.255.255.0
gateway 192.168.1.1
```

随后运行 *01_rndis_test.py* 检查rndis是否可用，运行 *02_SDK_code.py* 输入command，若返回ok;则成功使用sdk在rndis模式下与RMEP通讯

### 视频流解码

#### 安装解码器

进入 *03_decoder_install* 先给脚本加权并安装依赖

```bash
sudo apt-get install aptitude libopus-dev cmake
sudo aptitude install libavcodec-dev=7:4.4.1-3ubuntu5
sudo aptitude install libswscale-dev=7:4.4.1-3ubuntu5
pip install "pybind11[global]"
chmod +x ./build.sh
./build.sh
```



## 参考资料

### yolo代码

- [yolov5](https://github.com/ultralytics/yolov5)
- [yolov8](https://github.com/ultralytics/ultralytics)

### NPU部署

- https://blog.csdn.net/weixin_51651698/article/details/130187558
- [rknn模型](https://github.com/airockchip/yolov5/blob/master/README_rkopt_manual.md)

### RMSDK

- [RMSDK官方文档](https://robomaster-dev.readthedocs.io/zh-cn/latest/python_sdk/installs.html)
