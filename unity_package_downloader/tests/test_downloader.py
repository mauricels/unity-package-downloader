import unittest
from unittest.mock import patch
from downloader.downloader import UnityPackage

# Assuming UnityPackage is implemented elsewhere
class TestUserInput(unittest.TestCase):

    @patch('requests.get')  # Correctly patch 'requests.get'
    def test_fetch_package_data(self, mock_get):
        # Fake API response
        mock_response = {
                "_id": "com.unity.burst",
                "name": "com.unity.burst",
                "description": "Burst is a compiler...",
                "versions": {
                    "1.8.9": {
                        "dist": {
                            "tarball": "https://download.packages.unity.com/com.unity.burst/-/com.unity.burst-1.8.9.tgz",
                            "shasum": "d6b95a30a032b6a5a247f455d2d5b74e45061777"
                            }
                        }
                    }
                }

        # Inject fake API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Assuming UnityPackage is implemented elsewhere with fetch_package_data method
        fetch_result = UnityPackage("com.unity.burst", "1.8.9").fetch_package_data("https://packages.unity.org/just_a_mock")

        # Verify that the metadata is correct
        self.assertEqual(fetch_result['_id'], 'com.unity.burst')
        self.assertEqual(fetch_result['versions']['1.8.9']['dist']['tarball'],
                         'https://download.packages.unity.com/com.unity.burst/-/com.unity.burst-1.8.9.tgz')


if __name__ == '__main__':
    unittest.main()

