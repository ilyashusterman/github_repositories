from unittest import TestCase

from Repository import Repository


class TestRepository(TestCase):

	def setUp(self):
		self.repository = Repository(
			author='ilyashusterman', name='WordCount', load_data=False)

	def test_load_repository_data(self):
		self.repository.load()
		self.assertEqual(self.repository.contributors, 1)
		self.assertEqual(self.repository.commits, 46)
		self.assertEqual(self.repository.issues, 0)
