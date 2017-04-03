from similarity_finder import SimilarityFinder
from nltk.util import skipgrams
import json, re

class MovieNameFinder():
	def __init__(self):
		self.movie_list = self.get_movie_list()
		self.sf = SimilarityFinder(self.movie_list)

	def get_movie_list(self):
		with open('dummy.json') as data_file:
			data = json.load(data_file)
		return data["movies"]

	def generate_skip_n_grams(self, text):
		result = []
		tokens = text.split(":")
		if (len(tokens) > 1):
			result.append(tokens[0])
			
		regex = re.compile('[^a-zA-Z0-9]')
		text = regex.sub(' ', text)

		if (len(text.split()) == 1):
			result.append(text)
		else:
			for n in range(2, len(text.split())+1):
				for k in range(1, len(text.split())):
					tuples = list(skipgrams(text.split(), n, k))
					for item in tuples:
						substring = ""
						for i in range(len(item)):
							substring += item[i] + " "
						if substring[:-1] not in result:
							result.append(substring[:-1])
		return result

	def get_movie_name(self, text):
		return self.sf.findMostSimilarItem(text)
		# regex = re.compile('[^a-zA-Z0-9]')
		# text = regex.sub(' ', text.lower())

		# movie_name = ""
		# for movie in self.movie_list:
		# 	substrings = self.generate_skip_n_grams(movie.lower())
		# 	if any(substring in text for substring in substrings):
		# 		movie_name = movie
					
		# return movie_name


if __name__ == '__main__':
	mf = MovieNameFinder()
	print mf.get_movie_name("mau nonton smurfs")