import cv2
import rkmedia
import rkmedia.rkmedia as rkmedia
import rkmedia.rkmedia_vdec as rkmedia_vdec
import rkmedia.rkmedia_venc as rkmedia_venc
import rkmedia.rkmedia_vi as rkmedia_vi
import rkmedia.rkmedia_vo as rkmedia_vo

# 定义摄像头的参数
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
CAMERA_FPS = 30
CAMERA_FORMAT = rkmedia.VIDEO_FMT_H264

# 定义显示的参数
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_FORMAT = rkmedia.VIDEO_FMT_RGB888

# 创建一个摄像头对象
camera = rkmedia_vi.VI(CAMERA_WIDTH, CAMERA_HEIGHT, CAMERA_FPS, CAMERA_FORMAT)

# 创建一个解码器对象
decoder = rkmedia_vdec.VDEC(CAMERA_WIDTH, CAMERA_HEIGHT, CAMERA_FORMAT, DISPLAY_FORMAT)

# 创建一个显示对象
display = rkmedia_vo.VO(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_FORMAT)

# 循环从摄像头读取数据并解码显示
while True:
    # 从摄像头读取一帧数据
    frame = camera.read()
    if frame is None:
        break

    # 使用解码器解码数据
    decoded_frame = decoder.decode(frame)
    if decoded_frame is None:
        continue

    # 使用显示对象显示数据
    display.show(decoded_frame)

# 释放资源
camera.release()
decoder.release()
display.release()