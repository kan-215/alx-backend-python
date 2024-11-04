#!/usr/bin/env python3
"""The Module tests for client """

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ tests for Github Org Client """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Ensures GithubOrgClient.org returns the correct output"""
        test_class = GithubOrgClient(input)
        test_class.org
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """ensures public_repos_url returns the expected URL"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
            mock_org.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Ensures public_repos returns expected repo list"""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "https://api.github.com/orgs/test/repos"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected_repo_names = [repo["name"] for repo in json_payload]
            self.assertEqual(result, expected_repo_names)
            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Tests for_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integrates Testing with fixtures"""

    @classmethod
    def setUpClass(cls):
        """Sets up mocks for requests.get for integration tests"""
        config = {'return_value.json.side_effect': [cls.org_payload, cls.repos_payload]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock_get = cls.get_patcher.start()

    def test_public_repos(self):
        """tests public_repos integration"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.mock_get.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for public_repos with specific license"""
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos("apache-2.0"), self.apache2_repos)
        self.mock_get.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Stops the patcher after tests"""
        cls.get_patcher.stop()
