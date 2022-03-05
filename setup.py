from distutils.core import setup
setup(
  name = 'pangoro',
  packages = ['pangoro'],
  version = '0.12',
  license='MIT',
  description = 'Scraping in python made easy - receive the content you like in just one line of code!',
  author = 'GRoup D',
  author_email = 'ie.sambd.group.d@gmail.com',
  url = 'https://github.com/GroupD-IE/pangoro',
  download_url = 'https://github.com/joelbarmettlerUZH/Scrapeasy/archive/pypi-0_1_3.tar.gz',
  keywords = ['scraping', 'cleaning', 'numerical', 'categorical', 'dataframe', 'wrangling', 'cleaning', 'dataframe'],
  install_requires=[
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License ::= MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)