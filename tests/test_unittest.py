import unittest
from github_repo_manager.github import create_github_repo, list_github_repos

class TestGithubRepoManager(unittest.TestCase):
    
    def test_create_github_repo(self):
        result = create_github_repo("test-repo", "This is a test repository")
        self.assertIn('id', result)

    def test_list_github_repos(self):
        result = list_github_repos()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
