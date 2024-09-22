import requests


class UnityPackage:

    def __init__(self, package_name, version):
        self.package_name = package_name
        self.version = version
        self.unity_url = f'https://packages.unity.com/{self.package_name}'

    def fetch_package_data(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
