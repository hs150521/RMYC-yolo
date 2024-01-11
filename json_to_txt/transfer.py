import json
import os
import glob
import os.path as osp


def labelme2yolov2Seg(jsonfilePath, resultDirPath, classList):

    # 0.创建保存转换结果的文件夹
    if not os.path.exists(resultDirPath):
        os.mkdir(resultDirPath)

    # 1.获取目录下所有的labelme标注好的Json文件，存入列表中
    jsonfileList = glob.glob(osp.join(jsonfilePath, "*.json"))
    print(jsonfileList)  # 打印文件夹下的文件名称

    # 2.遍历json文件，进行转换
    for jsonfile in jsonfileList:
        # 3. 打开json文件
        with open(jsonfile, "r", encoding='UTF-8') as f:
            file_in = json.load(f)

            # 4. 读取文件中记录的所有标注目标
            shapes = file_in["shapes"]

            # 5. 使用图像名称创建一个txt文件，用来保存数据
            with open(resultDirPath + "\\" + jsonfile.split("\\")[-1].replace(".json", ".txt"), "w") as file_handle:
                # 6. 遍历shapes中的每个目标的轮廓
                for shape in shapes:
                    # 7.根据json中目标的类别标签，从classList中寻找类别的ID，然后写入txt文件中
                    file_handle.writelines(str(classList.index(shape["label"])) + " ")

                    # 8. 遍历shape轮廓中的每个点，每个点要进行图像尺寸的缩放，即x/width, y/height
                    for point in shape["points"]:
                        x = point[0] / file_in["imageWidth"]  # mask轮廓中一点的X坐标
                        y = point[1] / file_in["imageHeight"]  # mask轮廓中一点的Y坐标
                        file_handle.writelines(str(x) + " " + str(y) + " ")  # 写入mask轮廓点

                    # 9.每个物体一行数据，一个物体遍历完成后需要换行
                    file_handle.writelines("\n")
            # 10.所有物体都遍历完，需要关闭文件
            file_handle.close()
        # 10.所有物体都遍历完，需要关闭文件
        f.close()


if __name__ == "__main__":
    jsonfilePath = r"json_here"  # 要转换的json文件所在目录
    resultDirPath = r"txt_here"  # 要生成的txt文件夹
    labelme2yolov2Seg(jsonfilePath=jsonfilePath, resultDirPath=resultDirPath,
                      classList=['red'])  # 更改为自己的类别名
