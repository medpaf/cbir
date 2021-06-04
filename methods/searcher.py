# import the necessary packages
# 导入必要的包
import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath):
		# store the index path
		# 存储索引路径
		self.indexPath = indexPath

	def search(self, queryFeatures, limit = 10):
		# initialize the dictionary of results
		# 初始化结果字典
		results = {}

		# open the index file for reading
		# 打开索引文件进行读取
		with open(self.indexPath) as f:
			# initialize the CSV reader
			# 初始化CSV读取器
			reader = csv.reader(f)

			# loop over the rows in the index
			# 循环索引中的行
			for row in reader:
				# parse out the image ID and features, then compute the chi-squared distance between the features in our index and our query features
				# 解析图像ID和特征，然后计算索引中的特征和查询特征之间的卡方距离
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)

				# now that we have the distance between the two feature vectors, we can udpate the results dictionary -- the key is the current image ID in the index and the value is the distance we just computed, representing how 'similar' the image in the index is to our query
				# 现在我们已经得到了两个特征向量之间的距离，我们可以创建结果字典——关键是索引中的当前图像ID，值是我们刚刚计算的距离，表示索引中的图像与查询的“相似”程度
				results[row[0]] = d

			# close the reader
			# 关闭读卡器
			f.close()

		# sort our results, so that the smaller distances (i.e. the more relevant images are at the front of the list)
		# 对结果进行排序，以便距离越小（即列表前面的相关图像越多）
		results = sorted([(v, k) for (k, v) in results.items()])

		# return our (limited) results
		# 返回我们（有限）的结果
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		# 计算卡方距离
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# return the chi-squared distance
		# 返回卡方距离
		return d