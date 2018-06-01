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


def YCM251_test():
  RunTest(
    """
    def test( a = 1, b = 2 ): c =3
    """,
    []
  )

  RunTest(
    """
    def test( a= 1, b =2, c=3 )
    """,
    [ Error( 1,
             12,
             'YCM251',
             'exactly one space required around = for named parameter' ),
      Error( 1,
             19,
             'YCM251',
             'exactly one space required around = for named parameter' ),
      Error( 1,
             24,
             'YCM251',
             'exactly one space required around = for named parameter' ) ]
  )

  RunTest(
    """
    def foo( a =bar( b= 2 ), c  =3 )
    """,
    [ Error( 1,
             12,
             'YCM251',
             'exactly one space required around = for named parameter' ),
      Error( 1,
             19,
             'YCM251',
             'exactly one space required around = for named parameter' ),
      Error( 1,
             29,
             'YCM251',
             'exactly one space required around = for named parameter' ) ]
  )
