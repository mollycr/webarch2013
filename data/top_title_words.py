'''
	finds and prints the top 10 words in titles
	run: 
 '''

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopTitleWords(MRJob):

	def mapper(self, line_no, line):
		'''emits words in the title'''
		cell = csv_readline(line)
		if cell[0] == 'A':
			title = cell[3]
			for word in string.split(title):
				yield word, 1

	def reducer(self, word, word_counts):
		'''sums the counts for each word, and finds top 10'''
		total = sum(word_counts)
		if "INSERT_CONDITION_HERE":
			yield word, total

if __name__ == '__main__':
	TopUsers.run()
