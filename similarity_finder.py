from difflib import SequenceMatcher

class SimilarityFinder:
	"""docstring for SimilarityFinder"""
	def __init__(self, items):
		self.items = items

	def similar(self, a,b):
		return SequenceMatcher(None, a, b).ratio()

	def findMostSimilarItem(self, str):
		max_idx = 0
		maximum = 0
		found = 0
		res = ""
		for item in self.items:
			item = item.replace("\n","")
			if str.find(item) != -1:
				res = item
				found = 1
				break
			elif str.find(item.split(":")[0]) != -1:
				res = item
				found = 1
				break

		if found == 0:
			for i, item in enumerate(self.items):
				if maximum < self.similar(str, item):
					maximum = self.similar(str, item)
					max_idx = i

				if item.find(":") != -1:
					firstWord = item.split(":")[0]
					if maximum < self.similar(str, firstWord):
						maximum = self.similar(str, firstWord)
						max_idx = i
						
			if maximum > 0.45:
				res = self.items[max_idx]

		return res

if __name__ == '__main__':
	file = open("movies_list.txt",'r')
	titles = file.readlines()

	sf = SimilarityFinder(titles)

	print sf.findMostSimilarItem("mau makan nih")