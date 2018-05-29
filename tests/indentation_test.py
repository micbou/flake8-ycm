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

from test_utils import Error, RunTest


def YCM111_test():
  RunTest(
    """
      a = 1
      b = 1
    """,
    []
  )

  RunTest(
    """
      a = 1
       b = 1
    """,
    [ Error( 2, 2, 'YCM111', 'indentation is not a multiple of two spaces' ) ]
  )


def YCM112_test():
  RunTest(
    """
      if True:
        pass
    """,
    []
  )

  RunTest(
    """
      if True:
          pass
    """,
    [ Error( 2, 5, 'YCM112', 'expected an indented block of 2 spaces' ) ]
  )

  RunTest(
    """
      if True:
        if False:
            pass
    """,
    [ Error( 3, 7, 'YCM112', 'expected an indented block of 4 spaces' ) ]
  )


def YCM114_test():
  RunTest(
    """
    # A comment
    # Another one
    """,
    []
  )

  RunTest(
    """
    # A comment
     # Another one
    """,
    [ Error( 2,
             2,
             'YCM114',
             'indentation is not a multiple of two spaces (comment)' ) ]
  )


def YCM115_test():
  RunTest(
    """
    if True:
        # A comment
    """,
    [ Error( 2,
             5,
             'YCM115',
             'expected an indented block of 2 spaces (comment)' ) ]
  )
