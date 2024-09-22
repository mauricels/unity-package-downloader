import requests


class UnityPackage:

    def __init__(self, package_name, version):
        self.package_name = package_name
        self.version = version
        self.combined = self.package_name + '@' + self.version
        self.current_url = f'https://packages.unity.com/{self.package_name}'

    def fetch_package_data(self, url):
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def download_tgz(self, url, destination):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(chunksize=128):
                    file.write(chunk)
            return destination
        else:
            raise Exception(f'Failed to downloade package {self.combined}: {response.status_code}')

    def download_package(self):
        return self.download_tgz(self.current_url, self.combined)

