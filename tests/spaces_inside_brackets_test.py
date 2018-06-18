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


def YCM201_test():
  RunTest(
    """
    def test( param ):
      my_list = [ 1, 2, 3 ]
      my_dict = { 'key': 'value' }
    """,
    []
  )

  RunTest(
    """
    def test(
      param
    ):
      my_list = [
        1, 2, 3
      ]
      my_dict = {
        'key': 'value'
      }
    """,
    []
  )

  RunTest(
    """
    def test(param ):
      my_list = [1, 2, 3 ]
      my_dict = {'key': 'value' }
    """,
    [ Error( 1, 10, 'YCM201', 'exactly one space required after (' ),
      Error( 2, 14, 'YCM201', 'exactly one space required after [' ),
      Error( 3, 14, 'YCM201', 'exactly one space required after {' ) ]
  )


def YCM202_test():
  RunTest(
    """
    def test( param):
      my_list = [ 1, 2, 3]
      my_dict = { 'key': 'value'}
    """,
    [ Error( 1, 16, 'YCM202', 'exactly one space required before )' ),
      Error( 2, 22, 'YCM202', 'exactly one space required before ]' ),
      Error( 3, 29, 'YCM202', 'exactly one space required before }' ) ]
  )


def YCM204_test():
  RunTest(
    """
    def test():
      my_list = []
      my_dict = {}
    """,
    []
  )

  RunTest(
    """
    def test( ):
      my_list = [    ]
      my_dict = {  }
    """,
    [ Error( 1, 10, 'YCM204', 'no spaces between ( and ) for empty content' ),
      Error( 2, 14, 'YCM204', 'no spaces between [ and ] for empty content' ),
      Error( 3, 14, 'YCM204', 'no spaces between { and } for empty content' ) ]
  )


def InvalidSyntax_test():
  RunTest(
    """
    {
      'key': 'value' )
    }

    {
    """,
    []
  )
