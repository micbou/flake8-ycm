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

import tokenize


__author__ = 'Michel Bouard'
__email__ = 'contact@micbou.com'
__version__ = '0.1.0'


LEFT_BRACKETS = [ '(', '[', '{' ]
RIGHT_BRACKETS = [ ')', ']', '}' ]
CORRESPONDING_BRACKET = {
  '(': ')',
  '[': ']',
  '{': '}',
  ')': '(',
  ']': '[',
  '}': '{'
}


def Indentation( logical_line,
                 previous_logical,
                 indent_level,
                 previous_indent_level ):
  """Use two spaces per indentation level."""
  comment = '' if logical_line else ' (comment)'
  if indent_level % 2:
    code = 'YCM111' if logical_line else 'YCM114'
    message = ' indentation is not a multiple of two spaces' + comment
    yield 0, code + message
  if ( previous_logical.endswith( ':' ) and
       ( indent_level - previous_indent_level != 2 ) ):
    code = 'YCM112' if logical_line else 'YCM115'
    message = ' expected an indented block of {} spaces{}'.format(
      previous_indent_level + 2, comment )
    yield 0, code + message


Indentation.name = 'flake8-ycm'
Indentation.version = __version__


def SpacesInsideBrackets( logical_line, tokens ):
  """Require spaces inside parentheses, square brackets, and braces for
  non-empty content."""
  for index in range( len( tokens ) ):
    _, prev_text, _, prev_end, _ = ( tokens[ index - 1 ] if index - 1 >= 0 else
                                     ( None, None, None, None, None ) )
    token_type, text, start, end, _ = tokens[ index ]
    next_token_type, next_text, next_start, _, _ = (
      tokens[ index + 1 ] if index + 1 < len( tokens ) else
      ( None, None, None, None, None ) )
    if text in LEFT_BRACKETS:
      if ( next_text == CORRESPONDING_BRACKET[ text ] and
           next_start != end ):
        code = 'YCM204'
        message = ( ' no spaces between {} and {}'
                    ' for empty content'.format( text, next_text ) )
        yield end, code + message
      if ( next_token_type not in [ tokenize.NL, tokenize.NEWLINE ] and
           next_text != CORRESPONDING_BRACKET[ text ] and
           next_start[ 0 ] == start[ 0 ] and
           next_start[ 1 ] - start[ 1 ] != 2 ):
        code = 'YCM201'
        message = ' exactly one space required after {}'.format( text )
        yield end, code + message
    if text in RIGHT_BRACKETS:
      if ( prev_text != CORRESPONDING_BRACKET[ text ] and
           prev_end[ 0 ] == end[ 0 ] and
           end[ 1 ] - prev_end[ 1 ] != 2 ):
        code = 'YCM202'
        message = ' exactly one space required before {}'.format( text )
        yield start, code + message


SpacesInsideBrackets.name = 'flake8-ycm'
SpacesInsideBrackets.version = __version__
