import os
import re

YES_RESP = ['Y', 'y', 'yes']
VERSION_RE = r'^\d+(\.\d+)*$'


class UserInputHandler:

    def prompt_user_for_input(self):
        # asks the user which package he wants to install
        package = input("Which package do you want to install? Example: com.unity.textmeshpro")
        
        # asks the user which version of the package he wants to install
        version = input('Which version do you want to install? Example: 1.0.1')

        # asks the user if he wants if he wants to install it into a custom folder or use the unity cache 
        use_unity_cache = input('Do you want to use the default win unity cache folder? (Y)es or (N)o?')

        if use_unity_cache in YES_RESP:
            return package, version, True, None 
        
        # asks the user to enter a custom folder 
        custom_folder = input('Please enter a custom folder...')
        
        return package, version, False, custom_folder

    def check_user_input(self, package, version, use_unity_cache, custom_folder):
        correct = True 

        if not package.strip():
            print('The package name is empty')
            correct = False 

        if not version.strip():
            print('The version is empty')
            correct = False 

        if not re.match(VERSION_RE, version):
            print('The version is invalid')
            correct = False

        if use_unity_cache in YES_RESP: 
            return correct 

        if not custom_folder.strip():
            print('The version is empty')
            correct = False
        elif not os.path.exists(custom_folder):
            print('The custom folder does not exist')
            correct = False

        return correct 

