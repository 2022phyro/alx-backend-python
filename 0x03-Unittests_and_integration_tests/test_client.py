#!/usr/bin/env python3
"""Testing the GithubOrg file client.py"""
from unittest import TestCase, main
from unittest.mock import Mock, patch, PropertyMock
from parameterized import parameterized_class, parameterized
from typing import Mapping, Sequence, Any, Dict, List
from client import GithubOrgClient, get_json
import client


class TestGithubOrgClient(TestCase):
    """Tests the githuborgclient and its methods amd properties

    Args:
        TestCase (unittest): The base unittest
    """

    @parameterized.expand([
        ('google', {'res': 'https://github/google.com'}),
        ('abc', {'res': 'https//github/abc.com'}),
    ])
    @patch('client.get_json')
    def test_org(self, name: str,
                 payload: Dict[str, str], mock_get: Mock) -> None:
        """tests the org method

        Args:
            name (str): the name of the instance
            payload (Dict[str, str]): expected result
            mock_get (Mock): our mock object for controlling the test
        """
        mock_get.return_value = payload
        inst = GithubOrgClient(name)
        x = inst.org
        y = inst.org
        mock_get.assert_called_once()
        self.assertEqual(x, mock_get())
        self.assertEqual(y, mock_get())

    def test_public_repos_url(self) -> None:
        """tests the _public_repos_url property
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as url:
            url.return_value = 'https://github/google.com'
            inst = GithubOrgClient('google')
            self.assertEqual(inst._public_repos_url,
                             "https://github/google.com")

    @parameterized.expand([
        ('google', "https://api/google.com",
         [{'name': 'Dart'}, {'name': 'Jest'}], ['Dart', 'Jest']),
        ('abc', "https://api/abc.com",
         [{'name': 'Reword'}, {'name': 'AI'}, {"name": 'TS'}],
         ['Reword', 'AI', 'TS']),
        ('redis', "https://api/redis.com", [{'name': 'C'}], ['C']),
        ('marksman', "https://api/marksman.com", [], []),
    ])
    @patch('client.get_json')
    def test_public_repos(self, name: str,
                          url: str, res: List,
                          final: List, mock_get: Mock) -> None:
        """tests the public_repos methods

        Args:
            name (str): the instance name
            url (str): the expected _public_repos_url
            res (List): the expected result of get_json()
            final (List): the expected final result of public_repos
            mock_get (Mock): our mock object for controlling the tests
        """
        mock_get.return_value = res
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as url:
            url.return_value = url
            inst = GithubOrgClient(name)
            x = inst.public_repos()
            y = inst.public_repos()
            self.assertEqual(inst._public_repos_url, url)
            mock_get.assert_called_once()
            self.assertEqual(x, final)
            self.assertEqual(y, final)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict,
                         license_key: str, res: bool) -> None:
        """Tests the has_license method

        Args:
            repo (Dict): the repo to check
            license_key (str): the expected key to get
            res (bool): the expected result of the has_license()
        """
        x = GithubOrgClient('hello')
        self.assertEqual(x.has_license(repo, license_key), res)


if __name__ == '__main__':
    main()
