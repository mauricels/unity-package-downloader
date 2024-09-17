import unittest
from unittest.mock import patch
from downloader.programm import prompt_user_for_package

class TestUserInput(unittest.TestCase):
    @patch('builtins.input', side_effect=['com.unity.textmeshpro', 'cache'])
    def test_prompt_user_for_package(self, mock_input):
        # Testet, ob die Funktion korrekt nach Paketnamen und Installationsort fragt
        package, location = prompt_user_for_package()
        self.assertEqual(package, 'com.unity.textmeshpro')
        self.assertEqual(location, 'cache')

    @patch('builtins.input', side_effect=['com.unity.package', '/custom/path'])
    def test_prompt_user_for_package_custom_path(self, mock_input):
        # Testet, ob ein benutzerdefinierter Pfad korrekt abgefragt wird
        package, location = prompt_user_for_package()
        self.assertEqual(package, 'com.unity.package')
        self.assertEqual(location, '/custom/path')

if __name__ == '__main__':
    unittest.main()
