# Copyright 2018 Michel Bouard <contact@micbou.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup
import os
import re


DIR_OF_THIS_SCRIPT = os.path.abspath( os.path.dirname( __file__ ) )
VERSION_REGEX = re.compile( r'__version__ = \'(?P<version>.*)\'' )


def ReadFile( *args ):
  with open( os.path.join( DIR_OF_THIS_SCRIPT, *args ), 'r' ) as f:
    return f.read()


version = VERSION_REGEX.search( ReadFile( 'flake8_ycm.py' ) ).group( 'version' )
long_description = ReadFile( 'README.rst' ) + '\n\n' + ReadFile( 'HISTORY.rst' )

setup(
  name = 'flake8-ycm',
  version = version,
  description = 'A Flake8 plugin that enforces YouCompleteMe '
                'and ycmd coding style',
  long_description = long_description,
  license = 'Apache License 2.0',
  author = 'Michel Bouard',
  author_email = 'contact@micbou.com',
  url = 'https://github.com/micbou/flake8-ycm',
  py_modules = [ 'flake8_ycm' ],
  entry_points = {
    'flake8.extension': [
      'YCM11 = flake8_ycm:Indentation',
      'YCM20 = flake8_ycm:SpacesInsideBrackets',
    ]
  },
  install_requires = [
    'flake8 >= 3.0.0'
  ],
  python_requires = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
  zip_safe = False,
  keywords = 'flake8, YouCompleteMe, ycmd, coding style',
  classifiers=[
    'Development Status :: 1 - Planning',
    'Framework :: Flake8',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Natural Language :: English',
    "Programming Language :: Python :: 2",
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ]
)
