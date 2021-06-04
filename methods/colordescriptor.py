# import the necessary packages
# 导入必要的包
import numpy as np
import cv2
import imutils

class ColorDescriptor:
	def __init__(self, bins):
		# store the number of bins for the 3D histogram
		# 存储三维直方图的箱子数量
		self.bins = bins

	def describe(self, image):
		# convert the image to the HSV color space and initialize the features used to quantify the image
		# 将图像转换为HSV颜色空间并初始化用于量化图像的特征
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# grab the dimensions and compute the center of the image
		# 获取尺寸并计算图像的中心
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# divide the image into four rectangles/segments (top-left,top-right, bottom-right, bottom-left)
		# 将图像分成四个矩形/段（左上，右上，右下，左下）

		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]

		# construct an elliptical mask representing the center of the image
		# 构造一个椭圆遮罩，表示形象
		(axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.75) // 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# loop over the segments
		# 在分段上循环
		for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image, subtracting the elliptical center from it
			# 为图像的每个角构造一个遮罩，从中减去椭圆中心
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)

			# extract a color histogram from the image, then update the feature vector
			# 从图像中提取颜色直方图，然后更新特征向量
			hist = self.histogram(image, cornerMask)
			features.extend(hist)

		# extract a color histogram from the elliptical region and update the feature vector
		# 从椭圆区域提取颜色直方图并更新特征向量
		hist = self.histogram(image, ellipMask)
		features.extend(hist)

		# return the feature vector
		# 返回特征向量
		return features

	def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region of the image, using the supplied number of bins per channel
		# 使用每个通道提供的存储箱数，从图像的遮罩区域提取三维颜色直方图
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 180, 0, 256, 0, 256])

		# normalize the histogram if we are using OpenCV 2.4
		# 如果我们使用OpenCV 2.4，则对直方图进行标准化
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()

		# otherwise handle for OpenCV 3+
		# 否则处理OpenCV 3+
		else:
			hist = cv2.normalize(hist, hist).flatten()

		# return the histogram
		# 返回直方图
		return hist