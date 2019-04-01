import os
import re
from setuptools import setup

base_path = os.path.dirname(__file__)

with open(os.path.join(base_path, 'cfscrape', '__init__.py')) as fp:
    VERSION = re.compile(r'.*__version__ = "(.*?)"',
                         re.S).match(fp.read()).group(1)

setup(
  name = 'cfscrape',
  packages = ['cfscrape'],
  version = VERSION,
  description = 'A simple Python module to bypass Cloudflare\'s anti-bot page. See https://github.com/venomous/cloudflare-scrape-js2py for more information.',
  author = 'VeNoMous',
  author_email = 'venom@gen-x.co.nz',
  url = 'https://github.com/venomous/cloudflare-scrape-js2py',
  keywords = ['cloudflare', 'scraping'],
  include_package_data = True,
  install_requires = ['requests >= 2.0.0']
)
