'''
	users with > 20 visits
	run: python top_users.py user_visits-msweb.data > top_users.out
'''

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopUsers(MRJob):

	def mapper(self, line_no, line):
		'''Extracts the user that visited'''
		cell = csv_readline(line)
		if cell[0] == 'V':
			yield cell[3], 1

	def reducer(self, user, visit_counts):
		'''sums the counts for each user, and prints if > 20'''
		total = sum(visit_counts)
		if total > 20:
			yield user, total

if __name__ == '__main__':
	TopUsers.run()
