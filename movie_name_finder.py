from similarity_finder import SimilarityFinder
import MySQLdb, json

class MovieNameFinder():
	def __init__(self):
		self.movie_list = self.get_movie_list()
		self.sf = SimilarityFinder(self.movie_list)

	def get_movie_list(self):
		with open('dummy.json') as data_file:
			data = json.load(data_file)
		return data["movies"]

	def get_movie_name(self, text):
		return self.sf.findMostSimilarItem(text)

if __name__ == '__main__':
	mf = MovieNameFinder()
	print mf.get_movie_name("mau nonton beauty and the beast")