import requests
from bs4 import BeautifulSoup
import re

GITHUB_URL = 'https://github.com'

class Repository(object):

	@classmethod
	def get_repository_url(cls, author, repository_name):
		return '{github_url}/{author}/{repository_name}'.format(
			github_url=GITHUB_URL, author=author,
			repository_name=repository_name
		)

	def __init__(self, author, name, load_data=True):
		self.contributors = None
		self.author = author
		self.name = name
		self.url = self.get_repository_url(self.author, self.name)
		self.raw_text = None
		self.commits = None
		if load_data:
			self.load()

	def load(self):
		response = requests.get(self.url)
		soup = BeautifulSoup(response.content, 'html.parser')
		raw_text = ''.join(soup.get_text())
		self.raw_text = re.sub('\s+', ' ', raw_text)
		self.contributors = int(self.find_value('contributor'))
		self.commits = int(self.find_value('commits'))

	def find_value(self, value, margin=2):
		start_margin = 1
		value_index = self.raw_text.find(value)
		while self.raw_text[value_index-margin] is not ' ':
			margin += 1
		return self.raw_text[value_index-margin : value_index-start_margin]
