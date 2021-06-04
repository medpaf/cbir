# USAGE
# python search.py --index index.csv --query queries/103100.png --result-path dataset

# import the necessary packages
# 导入必要的包
from methods.colordescriptor import ColorDescriptor
from methods.searcher import Searcher
import argparse
import cv2

# construct the argument parser and parse the arguments
# 构造参数解析器并分析参数
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# initialize the image descriptor
# 初始化图像描述符
cd = ColorDescriptor((8, 12, 3))

# load the query image and describe it
# 加载查询图像并对其进行描述
query = cv2.imread(args["query"])
features = cd.describe(query)

# perform the search
# 执行搜索
searcher = Searcher(args["index"])
results = searcher.search(features)

# display the query
# 显示查询
cv2.imshow("Query", query)

# loop over the results
# 循环查看结果
for (score, resultID) in results:
	# load the result image and display it
	# 加载结果图像并显示
	result = cv2.imread(args["result_path"] + "/" + resultID)
	cv2.imshow("Result", result)
	cv2.waitKey(0)
