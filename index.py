# USAGE
# python index.py --dataset dataset --index index.csv

# import the necessary packages
# 导入必要的包
from methods.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
# 构造参数解析器并分析参数
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())

# initialize the color descriptor
# 初始化颜色描述符
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
# 打开输出索引文件进行写入
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
# 使用glob获取图像路径并在其上循环
for imagePath in glob.glob(args["dataset"] + "/*.png"):

	# extract the image ID (i.e. the unique filename) from the image path and load the image itself
	# 从图像路径中提取图像ID（即唯一的文件名）并加载图像本身
	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe the image
	# 描述图像
	features = cd.describe(image)

	# write the features to file
	# 将功能写入文件
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
# 关闭索引文件
output.close()
