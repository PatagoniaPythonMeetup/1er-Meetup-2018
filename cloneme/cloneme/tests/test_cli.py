import unittest
import argparse
from cloneme import parser

class TestSomething(unittest.TestCase):

    """Testing something"""

    @classmethod
    def setUpClass(cls):
        cls.parser = parser.create_parser()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parses_repo_correctly(self):
        repo = "LucianoFromTrelew/chestella"
        args = self.parser.parse_args(repo.split())
        self.assertEqual(args.repo, repo)

    def test_does_not_parses_wrong_repo(self):
        wrong_repos = ["LucianoFromTrelew", "LucianoFromTrelew/", "", "/", " / ", "_/_", "12/123"]
        for repo in wrong_repos:
            with self.subTest(repo=repo):
                with self.assertRaises(SystemExit):
                    self.parser.parse_args(repo.split())
