import unittest
import os
from unittest.mock import patch
from downloader.programm import UserInputHandler 

class TestUserInput(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handler = UserInputHandler()


    # test if the function returns correct user inputs
    @patch('builtins.input', side_effect=['com.unity.textmeshpro', '1.0.1', 'yes', ''])
    def test_prompt_user_for_input_correct(self, mock_input):
        package, version, use_unity_cache, custom_folder = self.handler.prompt_user_for_input()
        self.assertEqual(package, 'com.unity.textmeshpro')
        self.assertEqual(version, '1.0.1')
        self.assertEqual(use_unity_cache, True)
        self.assertEqual(custom_folder, None)

    # test if the function returns correct user inputs using a custom_folder
    @patch('builtins.input', side_effect=['com.unity.textmeshpro', '1.0.1', 'no', 'custom_folder'])
    def test_prompt_user_for_input_correct_custom_folder(self, mock_input):
        package, version, use_unity_cache, custom_folder = self.handler.prompt_user_for_input()
        self.assertEqual(package, 'com.unity.textmeshpro')
        self.assertEqual(version, '1.0.1')
        self.assertEqual(use_unity_cache, False)
        self.assertEqual(custom_folder, 'custom_folder')

    def test_valid_input(self):
        self.assertTrue(self.handler.check_user_input('com.unity.correct', '1.0.1', 'yes', ''))


    def test_invalid_input_empty_package_name(self):
        self.assertFalse(self.handler.check_user_input('', '1.0.1', 'yes', ''))


    def test_invalid_input_empty_version(self):
        self.assertFalse(self.handler.check_user_input('com.unity.sexy', '', 'yes', ''))


    @patch('os.path.exists', return_value=True)
    def test_valid_input_custom_folder(self, mock_exists):
        self.assertTrue(self.handler.check_user_input('com.unity.correct', '1.0.1', 'no', 'custom_folder'))

    @patch('os.path.exists', return_value=False)
    def test_invalid_input_custom_folder_not_exists(self, mock_exists):
        self.assertFalse(self.handler.check_user_input('com.unity.correct', '1.0.1', 'no', 'custom_folder'))


    def test_invalid_input_version(self):
        self.assertFalse(self.handler.check_user_input('com.unity.correct', '1ghsigeoh-0.1', 'yes', ''))

if __name__ == '__main__':
    unittest.main()
