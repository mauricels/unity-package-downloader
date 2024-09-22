import unittest
import requests
from unittest.mock import patch, MagicMock
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
        fetch_result = UnityPackage('com.unity.burst', '1.8.9').fetch_package_data('https://packages.unity.org/just_a_mock')

        # Verify that the metadata is correct
        self.assertEqual(fetch_result['_id'], 'com.unity.burst')
        self.assertEqual(fetch_result['versions']['1.8.9']['dist']['tarball'],
                         'https://download.packages.unity.com/com.unity.burst/-/com.unity.burst-1.8.9.tgz')

    @patch('requests.get')
    def test_download_tgz(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.iter_content = MagicMock(return_value=[b'chunk1', b'chunk2'])
        mock_get.return_value = mock_response


        package = UnityPackage('com.unity.burst', '1.8.9')

        result = package.download_tgz('https://download.packages.unity.com/com.unity.burst/-/com.unity.burst-1.8.9.tgz', 'com.unity.burst-1.8.9.tgz')

        self.assertEqual(result, 'com.unity.burst-1.8.9.tgz')

        mock_get.assert_called_with('https://download.packages.unity.com/com.unity.burst/-/com.unity.burst-1.8.9.tgz', stream=True)


        with open('com.unity.burst-1.8.9.tgz', 'rb') as file:
            file_content = file.read()
            self.assertEqual(file_content, b'chunk1chunk2')

    @patch('downloader.downloader.UnityPackage.download_tgz')
    def test_download_package(self, mock_download_tgz):
        package_name = 'com.unity.burst'
        version = '1.8.9'
        package = UnityPackage(package_name, version)

        package.download_package()

        mock_download_tgz.assert_called_once_with(package.current_url, package.combined)
         

    def test_get_combinded_package_name(self):
        package = UnityPackage('hello', '1.0')
        self.assertEqual(package.combined, 'hello@1.0')

if __name__ == '__main__':
    unittest.main()

