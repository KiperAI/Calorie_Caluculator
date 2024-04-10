from selectorlib import Extractor
import requests


class Temperature:
    """
    A scraper that uses a yml file to read the xpath of a value it needs to extract
    form the timeanddate.com/weather/ url webpage.
    """
    base_url = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(' ', '-')
        self.city = city.replace(' ', '-')

    def _build_url(self):
        """builds the url string adding country and city
        """

        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        """Extract a value as instructed by the yml file and return a dictionary"""

        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape
        """

        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('°C', '').strip())


if __name__ == '__main__':
    temperature = Temperature(country='poland', city='lublin')
    print(temperature.get())

