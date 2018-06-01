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

import os
import re
import subprocess
import sys
import tempfile
from collections import namedtuple
from contextlib import contextmanager
from hamcrest import assert_that, contains
from textwrap import dedent


FLAKE8_ERROR_REGEX = re.compile(
  r'^.*:(?P<line>\d+):(?P<column>\d+): (?P<code>YCM\d+) (?P<message>.*)$' )

Error = namedtuple( 'Error', [ 'line', 'column', 'code', 'message' ] )


@contextmanager
def TemporaryFile( content ):
  content = dedent( content ).strip()
  try:
    with tempfile.NamedTemporaryFile( delete = False ) as f:
      f.write( content.encode( 'utf8' ) )
    yield f.name
  finally:
    os.remove( f.name )


def RunTest( content, expected_errors ):
  # Define environment variable to enable subprocesses coverage. See:
  # http://coverage.readthedocs.io/en/latest/subprocess.html
  env = os.environ.copy()
  env[ 'COVERAGE_PROCESS_START' ] = '.coveragerc'

  try:
    with TemporaryFile( content ) as filename:
      # Force Flake8 to only use one subprocess to avoid messing up coverage.
      output = subprocess.check_output( [ sys.executable,
                                          '-m', 'flake8',
                                          '--jobs=1',
                                          '--select=YCM',
                                          '--exit-zero',
                                          filename ], env = env )
  except subprocess.CalledProcessError as exception:
    print( exception.output.decode( 'utf8' ) )
    raise

  output = output.decode( 'utf8' )
  actual_errors = []
  for line in output.splitlines():
    match = FLAKE8_ERROR_REGEX.search( line )
    if match:
      actual_errors.append( Error( int( match.group( 'line' ) ),
                                   int( match.group( 'column' ) ),
                                   match.group( 'code' ),
                                   match.group( 'message' ) ) )
  assert_that( actual_errors, contains( *expected_errors ), '\n' + output )
