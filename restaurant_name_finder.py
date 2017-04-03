import requests, os

class RestaurantNameFinder():
	def __init__(self):
		self.my_dir = os.path.dirname(__file__)
		self.verbs = [line.rstrip() for line in open(os.path.join(self.my_dir, 'verb_list.txt'))]
		self.prepositions = [" di ", " ke ", " d ", " k "]

	def find_between(self, s, first, last):
		try:
			start = s.index( first ) + len( first )
			end = s.index( last, start )
			return s[start:end]
		except ValueError:
			return ""

	def get_restaurant_name(self, text, location):
		restaurant_name = ""
		if any(verb in text for verb in self.verbs):
			for preposition in self.prepositions:
				if preposition in text:
					if not location:
						restaurant_name = text.split(preposition, 1)[1]
					else:
						restaurant_name = self.find_between(text, preposition, location)
		return restaurant_name
